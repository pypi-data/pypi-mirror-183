import commandhooker
import interpreter as inter
import arduinohooker as ah
import op
import struct
import sys
from multiprocessing import Process,Pipe
from ctypes import *
from commandhooker import Colored
color = Colored()
size_dict = {
    'int':2,
    'float':4,
    'double':4,
    'char':1
}
short_list = {
    'int':'h',
    'float':'f',
    'double':'d',
    'char':'c'   
}
temp = []
no_variable = 0  
db = 0 # if db == 1, then addr of function_list.variable_list[no_variable]
       # need to be refreshed
       # if db == 2 then current line need to be refreshed
source = []
#-----those three should be given by command------


#-------------------------------------------------
class debuger:

    def __init__(self,port,baud_rate,folder,file) -> None:
        self.arduino = ah.hooker(folder_name=folder,file_name=file,baudRate=baud_rate,port=port)
        self.programmer = commandhooker.user()
        self.temp_folder = ""
        self.arduino_current_func = ""
        self.arduino_current_line = 0
        self.arduino_current_variable = inter.default_variable #the variable is under checking
        self.function_list = []
        self.state = "p"
        self.source = inter.read_source(self.arduino.ab_file_path())
        # state:
        # 1/ w state information from arduino will be interpret as value of variable
        # 2/ b state ....... interpreted as breakpoint information
        # 3/ p state next message will be line of the pause 
        # 4/ c state Serial.print already had in source code
    def check(self):
        global source
        if(self.arduino.compile(self.arduino.ab_file_path())):
            # if compile return 1, then the source file is wrong
            raise Exception("Source file wrong.")
        else:
            # else the compile is alright
            new_folder_path = self.arduino.folder_name+'//temp'
            self.temp_folder = new_folder_path
            op.mkdir(new_folder_path)
            new_file_path = new_folder_path+'//'+'temp.ino'
            op.copy('debuger.cpp',self.temp_folder+'//debuger.cpp')
            op.copy('debuger.hpp',self.temp_folder+'//debuger.hpp')
            self.function_list = inter.interpret(self.arduino.ab_file_path(),new_file_path)
            op.save(self.function_list,'func.pkl')
            self.arduino_current_func = self.function_list[1]#current function intialized as setup()
            self.programmer.write_once("debug file has been generated at " + new_file_path)
            if(self.arduino.compile(new_file_path) | self.arduino.burn(new_file_path)):
                raise Exception("Uploading error")
            else:
                self.programmer.write_once(self.programmer.colors.green("Uploading successfully"))
    def run(self):
        receive,send = Pipe(True)
        programmer_process = Process(target=self.handle,args=((receive,send),100))
        programmer_process.start()
        receive.close()
        while(1):
            message = input()
            send.send(message)
            #self.programmer.write_once("programmer type: " + message)
            

    def handle(self,pipe,x):
        self.arduino.open_ser()
        print('\n>>>',end='')
        receive,send = pipe
        send.close()
        
        while(1):
            self.arduino.read_once()
            if(self.arduino.receive_message != ""):
                self.handle_message_from_arduino()
                self.arduino.receive_message = ""
            if(receive.poll()):
                self.programmer.receive_message = receive.recv()
                self.handle_message_from_programmer()
                self.programmer.receive_message = ""
    
    def handle_message_from_arduino(self):
        global db
        global no_variable
        global temp
        message = self.arduino.receive_message
        #print(color.blue(message))
        if self.state == 'c' or self.state == 'p' or self.state == 'w':
            # it means the program is running

            if message == "DEADBEEFfunc":
                # if message = deadbeeffunc, then next message 
                # should be name of current running function
                self.arduino_current_func = -1
                no_variable = 0
                db = 0
            elif message == "DEADBEEF":
                # in this situation, next message should be addr
                # of next variable in current function
                db = 1
                no_variable += 1
            elif message == "DEADBEEFline":
                db = 2
            
            else:
                if(db == 1):
                    # which means this message must be addr of a variable
                    if no_variable > len(self.arduino_current_func.variable_list):
                        # then this addr must be global variables
                        self.function_list[0].\
                            variable_list[no_variable-len(self.arduino_current_func.variable_list)-1].addr\
                                = int(message)
                    else:
                        self.arduino_current_func.variable_list[no_variable-1].addr = int(message)
                    db = 0

                elif(self.arduino_current_func == -1):
                    # which means this message must be name of a function
                    self.arduino_current_func = self.find_function(message)
                elif(db == 2):
                    # which means now the program jumps another line, current line need to be refreshed
                    self.arduino_current_line = int(message)
                    #print(self.arduino_current_line)
                    db = 0
                else:
                    # it's must be Serial.print of origin source code,but we don't allow.
                    # self.programmer.write_once(message)
                    pass
        elif self.state == 'b':
            if message == '0':
                self.programmer.write_once("No breakpoint Yet" + '\n ')
                print('>>>',end='')
            elif message.isdigit():
                self.programmer.write_once("breakpoint at line " + message + '\n ')
                print('>>>',end='')
            else:
                pass
        else:
            if message == "W":
                db = 3
            elif message == 'w':
                result = self.turn(self.arduino_current_variable.type)
                self.programmer.write_once(result)
                print('>>>',end='')
                self.arduino_current_variable = inter.default_variable
                temp = []
                db = 0
                
            elif(db == 3):
                # which means the programmer now wants to watch value of a variable
                temp.append(message) 
        
    def handle_message_from_programmer(self):
        global temp
        message = self.programmer.receive_message
        message.strip()
        
        if message == '':
            print('>>>',end='')
            return
        if(message[0] == 'b'):
            # below code seems to be a little tedious,
            # but it can check whether the command is valid.
            self.state = 'b'
            if ('+' in message):
                message = message.replace(' ','')
                number = message[message.index('+')+1:]
                if number.isdigit():
                    self.arduino.write_once('b+'+ number + '\n')
                else:
                    self.programmer.write_once("Invalid command!")
                print('>>>',end='')
            elif ('-' in message):
                message = message.replace(' ','')
                number = message[message.index('-')+1:]
                if number.isdigit():
                    self.arduino.write_once('b-'+ number + '\n')
                else:
                    self.programmer.write_once("Invalid command!")
                print('>>>',end='')
            elif ('info' in message):
                self.arduino.write_once("b info\n")
            else:
                self.programmer.write_once("Invalid command!")
                print('>>>',end='')
        elif(message == 'c'):
            self.state = 'c'
            self.arduino.write_once(message + '\n')
            self.programmer.write_once('program running...\n')
            print('>>>',end='')
        elif(message == 's'):
            self.arduino.write_once(message + '\n')
            print(color.red(str(self.arduino_current_line)))
            self.programmer.write_once(str(self.arduino_current_line) + '-->' + self.source[self.arduino_current_line-1].content)
            print('>>>',end='')
        elif(message == 'p'):
            if self.state == 'p':
                self.programmer.write_once('program has been paused!')
                print('>>>',end='')
                return
            self.state = 'p'
            self.arduino.write_once('p')
            times = 15
            while(times>0):
                #print(color.red(self.arduino.read_once()))
                self.arduino.read_once()
                if(self.arduino.receive_message!=''):
                    self.handle_message_from_arduino()
                    
                    self.arduino.receive_message = ''
                times-=1
            self.programmer.write_once("pause at " + self.arduino.ab_file_path() + ", line " + str(self.arduino_current_line)\
                    + '\n' + self.find_line(self.arduino_current_line).content)
            print('>>>',end='')
        elif(message[0] == 'n'):
            if self.is_func_declaration(self.arduino_current_line):    
                # when the line is in a certain function, then we write 's' until stepping out of the function
                l = self.arduino_current_line
                func = self.arduino_current_func
                self.arduino.write_once('s\n')
                threshold = 3
                while(threshold>0):
                    if(self.arduino.read_once() == ''):
                        threshold-=1
                    else:
                        self.handle_message_from_arduino()
                while(self.arduino_current_line >= func.difination[0].line and \
                    self.arduino_current_line <= func.difination[1].line):
                    self.arduino.write_once('s\n')
                    threshold = 1
                    while(threshold>0):
                        if(self.arduino.read_once() == ''):
                            threshold-=1
                        else:
                            self.handle_message_from_arduino()
                self.programmer.write_once(str(l) + '-->' + self.source[l-1].content)
                print('>>>',end='')
            else:
                self.arduino.write_once("s\n")
                self.programmer.write_once(str(self.arduino_current_line) + '-->' + self.source[self.arduino_current_line-1].content)
                print('>>>',end='')
        elif(message[0] == 'w'):
            if message.find('-') == -1:
                self.programmer.write_once("Invalid command!")
                print('>>>',end='')
                return
            flag = 0
            for m in message.split('-')[1:]:
                if not m.isdigit():
                    self.programmer.write_once("Invalid command!")
                    print('>>>',end='')
                    flag = 1
                    break
            if(not flag):
                self.arduino.write_once(message + '\n')
                while( (message:=self.arduino.read_once()) != 'w' ):
                    if message.isdigit():
                        self.programmer.write_once(message)
                    
            else:    
                flag = 0           
        elif(message[0] == 'm'):
            if message.find('-') == -1:
                self.programmer.write_once("Invalid command!")
                print('>>>',end='')
                return
            flag = 0
            for m in message.split('-')[1:]:
                if not m.isdigit():
                    self.programmer.write_once("Invalid command!")
                    print('>>>',end='')
                    flag = 1
                    break
            if int(message.split('-')[2])>255:
                self.programmer.write_once("Target number is bigger than 255")
                print('>>>',end='')
                flag = 1

            if(not flag):
                self.arduino.write_once(message + '\n')
                    
            else:    
                flag = 0       
        elif(message[0] == 'd'):
            self.state = 'w'
            if message.find('-') == -1:
                self.programmer.write_once("Invalid command!")
                print('>>>',end='')
                return
            variable = message.split('-')[1]
            if((index:=variable.find('['))!=-1):
                #when the variable is certain element of a array, then we need get rid of '['
                #like d-a[12]:check value of a[12], the value name is a[12], but the true name should be a 
                variable = variable[:index]
            if (v:=self.find_variable_in_function(self.arduino_current_func,variable))!=-1\
                or (v:=self.find_variable_in_function(self.function_list[0],variable))!=-1:
                self.arduino_current_variable = v
                if type(v) == type(inter.default_variable):
                    # its a variable
                    addr = v.addr
                    if addr == 0:
                        self.programmer.write_once("Varaible has not been initialezed") 
                        print('>>>',end='')
                        return
                    size = size_dict[v.type]
                    command = "w-"+str(addr)+'-'+str(size)
                    self.arduino.write_once(command)
                    while(1):
                        value = self.arduino.read_once()
                        if(value == "w"):
                            break
                        elif (value == "W" or value == ''):
                            continue
                        else:
                            temp.append(value)
                    result = self.turn(v.type)
                    self.programmer.write_once(result)
                    print('>>>',end='')
                    
                else:
                    #its an array
                    # two kinds of input: say there is an array a[10]
                    # 1 programmer input: a
                    # then we need print every element of it.
                    # 2 programmer a[10]
                    # then we need print 10th element of it.
                    if (index:=message.find('['))!=-1:
                        index2 = message.find(']')
                        number = int(message[index+1:index2])
                        size = size_dict[v.type]
                        if number<v.length and number>-1:
                            addr = v.addr + size*number
                            command = "w-"+str(addr)+'-'+str(size)
                            self.arduino.write_once(command)
                            while(1):
                                value = self.arduino.read_once()
                                if(value == "w"):
                                    break
                                elif (value == "W" or value == ''):
                                    continue
                                else:
                                    temp.append(value)
                            result = self.turn(v.type)
                            self.programmer.write_once(result)
                            print('>>>',end='')
                        else:
                            self.programmer.write_once("length is out of range")
                            print('>>>',end='')
                    else:
                        size = size_dict[v.type]
                        for i in range(v.length):
                            addr = v.addr + i*size
                            command = "w-"+str(addr)+'-'+str(size)
                            self.arduino.write_once(command)
                            # when switch = 1, receive value from arduino and save it in temp
                            # when switch = 0, then next information will be "w" or "W"
                            while(1):
                                value = self.arduino.read_once()
                                if(value == "w"):
                                    break
                                elif (value == "W" or value == ''):
                                    continue
                                else:
                                    temp.append(value)
                            result = self.turn(v.type)
                            self.programmer.write_once(result)
                        print('>>>',end='')

            
            else:
                self.programmer.write_once("Variable not found")
                print('>>>',end='')
        elif(message[0] == 'g'):
            if message.find('-') == -1:
                self.programmer.write_once("Invalid command!")
                print('>>>',end='')
                return
            l = message.split('-')
            if len(l)<=2:
                self.programmer.write_once("Invalid command")
                print('>>>',end='')
                return 
            variable = l[1]
            if (index:=variable.find('['))!=-1:
                variable = variable[:index]
            value = eval(l[2])
            number = 0
            if (v:=self.find_variable_in_function(self.arduino_current_func,variable))!=-1\
                or (v:=self.find_variable_in_function(self.function_list[0],variable))!=-1:
                if message.find('[')!=-1:
                    #its an array
                    index1 = message.find('[')
                    index2 = message.find(']')
                    number = int(message[index1+1:index2])

                self.arduino_current_variable = v
                if str(type(value)).find(v.type)!= -1:
                    byte_list = bin(int.from_bytes(struct.pack(short_list[v.type],value),sys.byteorder))
                    byte_list = byte_list[2:]
                    byte_list = (size_dict[v.type]*8-len(byte_list))*'0' + byte_list # make up for 
                    # every time 8 bits, send the data
                    for i in range(0,size_dict[v.type]):
                        byte = int(byte_list[i*8:(i+1)*8],2) 
                        command = "m-"+str(v.addr+number*size_dict[v.type]+size_dict[v.type]-i-1)+'-'+str(byte)
                        self.arduino.write_once(command +'\n')
                        # time.sleep(0.1)
                    self.programmer.write_once('done')
                    print('>>>',end='')
                else:
                    self.programmer.write_once("value should be the same type as variable")
                    print('>>>',end='')
        elif(message[0] == 'l'):
            if message == 'lall':
                for content in self.source:
                    print_content = str(self.source.index(content)+1) + '-->' + content.content
                    self.programmer.write_once(print_content)
                return
            if message == 'lthis':
                print(color.red(str(self.arduino_current_line)))
                print_content = str(self.arduino_current_line) + '-->' + self.source[self.arduino_current_line-1].content
                self.programmer.write_once(print_content)
                print(">>>",end='')
                return
            if len(message) == 1:
                line_num = 7
            elif message[1:].isdigit():
                line_num = int(message[1:])
            else:
                self.programmer.write_once('lx x is number of lines you want to print out')
                print(">>>",end="")
                return
            for i in range(line_num):
                #print next seven lines
                try:
                    print_content = str(self.arduino_current_line+i) + '-->' + self.source[self.arduino_current_line+i].content
                    self.programmer.write_once(print_content)
                except:
                    # if current line is the last few lines of the program, then we can't print "next seven lines". 
                    break
            print('>>>',end='')
        else:
            try:
                try:
                    print(eval(message))
                except:
                    eval(message)
                print('>>>',end='')
            except:
                self.programmer.write_once("Invalid expression")
                print('>>>',end='')

    def debug(self):
        print('Debuger developed by fatdog xie')
        self.check()
        self.run()


# tool-functions
    def find_variable_in_function(self,func,var):
        for v in func.variable_list:
            if v.name == var:
                return v
        return -1

    def is_func_declaration(self,line):
        for func in self.function_list:
            for l in func.declaration:
                if l.line == line:
                    self.arduino_current_func = func
                    return True
        return False

    def find_function(self,name):
        for func in self.function_list:
            if func.name == name:
                return func
    
    def find_line(self,line):
        for l in self.source:
            if l.line == line:
                return l
        else:
            return 0
    
    def turn(self,type):
        global temp
        value = 0
        int_temp = [int(i) for i in temp]
        if type == 'int':
            value = int_temp[0] + 256*int_temp[1]
        elif type == 'float' or type == 'double':
            sum_ = 0
            for i in range(len(int_temp)):
                sum_ += 256**i*int_temp[i]
            value = struct.unpack('!f', bytes.fromhex(hex(sum_)[2:]))[0]
        temp = []
        return value
        
if __name__ == "__main__":
    port = 'COM3'
    baud_rate = 9600
    folder = "C:\\Users\\xingxing\\Documents\\Arduino\\test4"
    file = "test4.ino"
    debugerv2 = debuger(port=port,baud_rate=baud_rate,file=file,folder=folder)
    #debugerv2.turn()
    debugerv2.debug()