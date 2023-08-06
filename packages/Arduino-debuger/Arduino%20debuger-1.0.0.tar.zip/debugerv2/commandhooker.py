import sys
from colorama import init,Fore,Back,Style
class Colored(object):
    def __init__(self) -> None:
        pass
    def red(self,s):
        return Fore.RED + s + Fore.RESET
    def green(self,s):
        return Fore.GREEN + s + Fore.RESET
    def yellow(self,s):
        return Fore.YELLOW + s + Fore.RESET
    def blue(self,s):
        return Fore.BLUE + s + Fore.RESET
    def magenta(self,s):
        return Fore.MAGENTA + s + Fore.RESET
    def cyan(self,s):
        return Fore.CYAN + s + Fore.RESET
    def white(self,s):
        return Fore.WHITE + s + Fore.RESET
    def balck(self,s):
        return Fore.BLACK
    def white_green(self,s):
        return Fore.WHITE + Back.GREEN + s + Fore.RESET + Back.RESET

class user:
    def __init__(self) -> None:
        self.colors = Colored()
        self.receive_message = ""
        self.send_message = ""
        
    def read_once(self):
        self.receive_message = input()
        #print("receive from programmer: " + self.receive_message)
    def receive(self):
        while(1):
            self.read_once()

    def send(self):
        while(1):
            if self.send_message != "":
                self.write_once()
                #print("send to programmer: " + self.send_message)
                self.send_message = ""
    
    def write_once(self,command=''):
        if command == '':
            print(self.send_message)
        else:
            print(command)
        


if __name__ == '__main__':
    u = user()
    while(1):
        u.read_once()
        print(u.receive_message)


    # color = Colored()
    # print(color.red('I am red!'))
    # print(color.green('I am green!'))
    # print(color.yellow('I am yellow!'))
    # print(color.blue('I am blue!'))
    # print(color.magenta('I am magenta!'))
    # print(color.cyan('I am cyan!'))
    # print(color.white('I am white!'))
    # print(color.white_green('I am white green!'))