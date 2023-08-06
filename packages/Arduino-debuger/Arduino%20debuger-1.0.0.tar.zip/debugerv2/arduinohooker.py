import os
import serial

class hooker:

    
    def __init__(self,port="COM3",baudRate=9600,file_name='test.ino',folder_name = 'test') -> None:
        self.serialPort = port
        self.baudRate = baudRate
        self.file_name = file_name
        self.folder_name = folder_name
        self.receive_message = ""
        self.send_message = ""
        self.ser = ''

    # 0 basic operations
    def open_ser(self):
        self.ser = serial.Serial(self.serialPort,self.baudRate,timeout = 0.5)
        print("参数设置：串口=%s ，波特率=%d" % (self.serialPort, self.baudRate))
    def close_ser(self):
        self.ser.close()
    def ab_file_path(self):
        return self.folder_name + '//' + self.file_name
    def burn(self,file):
        #upload the code into arduino    
        command = r".\arduino-cli upload -b arduino:avr:uno -p" + self.serialPort + ' ' + file
        return os.system(command)
    def compile(self,file):
        #compile the code
        command = r'.\arduino-cli compile -b arduino:avr:uno ' + eval(repr(file))
        print(command)
        return os.system(command)

    # 1 receive the message from arduino
    def receive(self):
        while(1):
            self.read_once()

    def read_once(self):
        self.receive_message = self.ser.readline().strip().decode('utf-8','ignore')
        if self.receive_message!="":
            #print("receive from arduino: " + self.receive_message)
            pass
        return self.receive_message
    #2 write to arduino
    def write_once(self,command=''):
        if command =='':
            self.ser.write(self.send_message.encode())
        else:
            #print("send to arduino: " + command)
            self.ser.write(command.encode())
    def send(self):
        while(1):
            if self.send_message != "":
                self.write_once()
                print("send to arduino: " + self.send_message)
                self.send_message = ""

if __name__ == "__main__":
    import time
    h = hooker()
    h.open_ser()
    time.sleep(3)
    h.send_message = "c\n"
    h.write_once()
    h.send_message = "p\n"
    h.write_once()
    h.receive()