from copy import deepcopy
from commandhooker import Colored
from debuger import baudRate
b = Colored()
DEADBEEF = "DEADBEEF"
class one_line:
    def __init__(self,content='',line=0) -> None:
        #c is a string and l is the line where code is at
        self.content = content
        self.line = line
        self.before_line = []
        self.after_line = []

class variable:
    def __init__(self,name='',type='',value=0,addr=0,line=0) -> None:
        self.name = name
        self.value = value
        self.addr = addr
        self.type = type
        self.line = line

class array:
    def __init__(self,length=0,name='',type='',value=[],addr=0,line=0) -> None:
        self.length = length
        self.name = name
        self.type = type
        self.addr = addr
        self.value = value
        self.line = line

class function:
    def __init__(self,difination=[],name='',type=''):
        self.name = name
        self.type = type
        self.difination = difination# where it begins and where it ends
        self.declaration = []
        self.variable_list = []


type_list = ['int','char','double','float','void','String']
number_list = [str(i) for i in range(10)]
alpha_list = [chr(i) for i in range(97,97+26)]+[chr(i) for i in range(65,65+26)]


function_list = [function(name="global",type='void')]
default_variable = variable()
default_array = array()
# 0 read the source


def read_source(path):
    #read source code and return a list, an element is a line of code.
    if path[-3:]!="ino":
        raise Exception("ERROR! Only .ino file can be debugged.")
    with open(path,'r') as file:
        source = file.readlines()
        result = []
        for i in range(len(source)):
            result.append(one_line(source[i],i+1))
        return result

# 1 get rid of annotation/'\n'/ two ; in oneline
# make all '{' a single line 
def is_empty(line):
    content = line.content
    valid_character = [chr(i) for i in range(97,97+26)]+[chr(i) for i in range(65,65+26)]\
        + ['+','-','*','/','{','}','(',')']
    
    for c in valid_character:
        if c in content:
            return False
    return True

def remove_annotation(source):
    #remove empty line and notation.
    temp = deepcopy(source)
    result = []

    for line in temp:
        if((index:=line.content.find("//"))!=-1):
            #there is // in this line
            line.content = line.content[:index]
        result.append(line)
    temp = deepcopy(result)
    temp = one_line_one_sentence(temp)
    result = []
    flag = 0 # flag==0 means this line is not in annotation  
    for line in temp:
        line.content = line.content.strip()
        if((index:=line.content.find("/*"))!=-1):
            flag = 1
            line.content = line.content[:index]
        if((index:=line.content.find("*/"))!=-1):
            flag = 0
            line.content = line.content[index+2:]
        if(flag == 1):
            line.content = ''
        result.append(line)
    
    temp = []
    for line in result:
        if(is_empty(line)):
            continue
        else:
            temp.append(line)
    
    return temp

def one_line_one_sentence(source):
    #prevent two ';'s in one line
    #source is after annotation removing
    result = []
    for line in source:
        if line.content.count(';') > 1:
            line_list = line.content[:-1].split(';')
            for l in line_list:
                result.append(one_line(l+';',line.line))
        else:
            result.append(line)
    return result

def handle_spacein_line(source):
    is_in_string = 0
    temp = deepcopy(source)
    result = []
    for line in temp:
        new_line = ''
        if line.content[0] == '#':
            result.append(line)
            continue
        for index in range(len(line.content)):
            c = line.content[index]
            if ord(c) == 34:
                is_in_string = 1-is_in_string
                if is_in_string:
                    new_line += c
                    continue
            if c == ' ':
                a = line.content[index+1]
                b = line.content[index-1]
                if (a in number_list or a in alpha_list) and (b in number_list or b in alpha_list):
                    new_line += c
                else: 
                    pass
            else:
                new_line += c
        result.append(one_line(content=new_line,line=line.line))
    return result

def replace_macro(source):
    macro_list = []
    for line in source:
        if (index:=line.content.find("#define"))!=-1:
            temp = line.content[index+7:].split(' ')
            macro = []
            for c in temp:
                if(c!=' ' and c!=''):
                    macro.append(c)
            macro_list.append(macro)
    for line in source:
        if line.content.find('#')!=-1:
            continue
        for macro in macro_list:
            if line.content.find(macro[0])!=-1:
                line.content = line.content.replace(macro[0],macro[1])

#2 find function in this code/local scope in this code

# in a certain line, there is alpha/digit/()/{}/space
def find_function_definition(source):
    scope = []
    for line in source:
        flag = 0
        if line.content.find('"') != -1:
            continue
        else:
            if " " in line.content and "(" in line.content:
                type = line.content.split(' ')[0]
                for c in type:
                    if not (c in number_list or c in alpha_list):
                        flag = 1
                if flag:
                    continue
                name = line.content[line.content.find(' ')+1:line.content.find('(')]
                scope.append([line,0])
                scope[-1][1] = find_end_scope(source,line)
                function_list.append(function(name=name,type=type,difination=scope[-1]))
    return scope

def find_function_declaration(source):
    global function_list
    for function in function_list:
        for line in source:
            if function.name in line.content:
                function.declaration.append(line)

def find_end_scope(source,line):
    # find '}' matched to '{' in line
    flag = 0
    for l in source[source.index(line)+1:]:
        flag = flag - l.content.count('{') + l.content.count('}')
        if flag>0:
            return l

# 3 find variable in one function/or in global

def find_variable_inoneline(temp_line):
    line = deepcopy(temp_line)
    flag = 0
    variable_list = []
    for type in type_list:
        if (index:=line.content.find(type)) != -1:
            #here comes a type in this line
            if(index == 0):
                # take int as example
                # index=0 means 'int' is the first word in the sentense. 
                flag = 1
            else:
                if(line.content[index+len(type)]!=' '):
                    continue
                for c in line.content[index+len(type):]:
                    if c == ' ':
                        continue
                    elif c == ')':
                        flag = 0
                        break
                    else:
                        flag = 1
                        break
            # flag = 0: 'int' just a part of other expression. 
            # just like: 'void breakpoint()'. it has 'int' in this line but it's not used in variable declaration.
            if(flag):
                name = []
                line.content = line.content[index+len(type)+1:].replace(' ','')
                for i in range(len(line.content)):
                    if line.content[i] not in ['=',';']:
                        continue
                    else:
                        is_in = 0
                        start = 0
                        for i in range(len(line.content)):
                            c = line.content[i]
                            if c == '{':
                                is_in = 1
                            elif c == '}':
                                is_in = 0
                            elif c == ',' or c == ';':
                                if is_in:
                                    continue
                                else:
                                    name.append(line.content[start:i])
                                    start = i+1

                        break
    
                for n in name:
                    index1 = n.find('=')
                    if index1 == -1:
                        temp_name = n
                    else:
                        temp_name = n[:index1]


                    if (index1:=temp_name.find('[')) != -1:
                        #it means this variable is a array
                        
                        index2 = n.find(']')
                        if index1+1==index2:
                            #int a[] = {1,2,3,4}
                            index1 = n.find('{')
                            index2 = n.find('}')
                            length = n[index1+1:index2].count(',')+1
                            n = n[:n.find('[')]
                        else:
                            #int a[5]
                            index2 = n.find(']')
                            length = int(n[index1+1:index2])
                            n = n[:index1]
                        variable_list.append(array(length=length,name=n,type=type,line=line))
                    else:
                        # an ordinary variable
                        variable_list.append(variable(name=temp_name,type=type,line=temp_line)); 
            break
    return variable_list

def find_variable_function(function,source):
    for line in source:
        if line.line > function.difination[0].line and \
            line.line < function.difination[1].line:
            function.variable_list += find_variable_inoneline(line)

def is_global_line(line):
    for function in function_list[1:]:
        if line.line > function.difination[0].line \
            and line.line < function.difination[1].line:
            return False
    return True

def find_variable_global(source):
    for line in source:
        if is_global_line(line):
            # print(line.content)
            function_list[0].variable_list += find_variable_inoneline(line)


        
# 4 change the source file according to the function list and variable_list


def add_source(source):
    # add "Serial.print((unsigned long) &variable)" after every variable
    # add function name at begin of any function
    for function in function_list[1:]:
        # for local variable, print address after its difination 
        find_line(source,function.difination[0]).after_line.append(
        "spl("+chr(34)+"DEADBEEFfunc"+chr(34)+");spl("+chr(34)+function.name+chr(34)+");\n")
        if function.name == 'setup':
            set_up = function
        for var in function.variable_list:
            if type(var) == type(default_array):
                # if var is a array
                find_line(source,var.line).after_line.append(
        "spl("+chr(34)+"DEADBEEF"+chr(34)+");spl((unsigned long) &"+var.name+"[0]);\n")
            else:
                # then var is a variable
                find_line(source,var.line).after_line.append(
        "spl("+chr(34)+"DEADBEEF"+chr(34)+");spl((unsigned long) &"+var.name+");\n")
    set_up.difination[0].after_line.insert(0,"Serial.begin("+str(baudRate)+");\n")
    for var in function_list[0].variable_list:
        # for global variable, print address at last of void setup()
        set_up.difination[0].before_line.append(var.line.content+'\n')
        
        # move all the global variables before setup function.
        if type(var) == type(default_array):
            # if var is a array
            find_line(source,set_up.difination[1]).before_line.append(
    "spl("+chr(34)+"DEADBEEF"+chr(34)+");spl((unsigned long) &"+var.name+"[0]);\n")
        else:
            # then var is a variable
            find_line(source,set_up.difination[1]).before_line.append(
    "spl("+chr(34)+"DEADBEEF"+chr(34)+");spl((unsigned long) &"+var.name+");\n")
            
    
    #add breakpoint() after every line
    for line in source:
        if(is_global_line(line)):
            continue
        else:
            line.before_line.append("breakpoint(" + str(line.line)+");\n")

def find_line(source,certain_line):
    for line in source:
        if line.line == certain_line.line:
            return line

# 5 generate the new source
def generate(source,path):
    source = get(source)
    file = open(path,'w')
    file.truncate(0)
    file.write(' #include "debuger.hpp" \n')
    for line in source:
        file.write(line)
    file.close()

def get(source):
    # global variables have been in the before lines of "void setup"
    # so if the line is a global variables, we just jump over it.
    result = []
    for line in source:
        flag = 0
        if line.content.find("Serial.begin")!=-1:
            continue
        for v in function_list[0].variable_list:
            if line.line == v.line.line:
                flag = 1
                break
        if flag:
            continue
        result += list(set(line.before_line))
        # print(line.before_line)
        result.append(line.content+'\n')
        result += line.after_line
        # print(line.after_line)
    return result

def get_simple(source):
    result = []
    for line in source:
        result.append(line.content)
    return result


# 6 display the result

def show_function_variable(function):
    for v in function.variable_list:
        
        content = "In function "+ b.magenta(function.name)\
            + ', debuger finds ' + b.white_green(v.name)\
            + ' at line ' + str(v.line.line)
        print(content)

def show():
    for v in function_list[0].variable_list:
        content = "In global "+ b.magenta(function_list[0].name)\
            + ', debuger finds ' + b.white_green(v.name)\
            + ' at line ' + str(v.line.line)
        print(content)
    for func in function_list[1:]:
        content = "debuger finds function " + b.magenta(func.name)\
            + " from line " + str(func.difination[0].line) + " to line " + str(func.difination[1].line)
        print(content)
        show_function_variable(func)


# 7 get it all.
def interpret(source_path,new_source_path):
    # source_path = new_source_path
    source = read_source(source_path)
    source_without_annatation = remove_annotation(source)
    source = handle_spacein_line(source_without_annatation)
    replace_macro(source)
    fix_bug1(source,new_source_path)
    find_function_definition(source)
    find_function_declaration(source)
    for function in function_list[1:]:
        find_variable_function(function,source)
    find_variable_global(source)
    # for func in function_list:
    #     get_function_variable(func)

    add_source(source)
    generate(source,new_source_path)
    show()
    return function_list

# bug fixing
def fix_bug1(source,new_source_path):
    # must make sure every end line of a function is a single '}'
    # {
    #   ....
    # }   this is alright
    #
    # {
    # .....; } this is what I want to remove.
    for line in source:
        if (index:= line.content.find(";}"))!=-1:
            if(index == len(line.content)-2):
                # then ';}' is at end of a line
                line.content = line.content[:-1]
                source.insert(source.index(line)+1,one_line('}',line.line))
            else:
                raise Exception(";} must at end of a line")
    generate(source,new_source_path)
    source = read_source(new_source_path)
    return source
if __name__ == "__main__":
    interpret('test/test.ino','test/debugertest.ino')

