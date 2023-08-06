#pragma once

#include "debuger.hpp"
#include<Arduino.h>
int index(int* array, int num);
int breaklist[max_num_breakpoint];
int flag = 0;
int temp_breakpoint = 0;
void breakpoint(int line){    

    //if below three conditions are met at the same time, 
    //then just get out of the loop and make this breakpoint be ignored
    //c1: flag == 1; c2:line is not in breaklist; c3:line is not tempbreakpoint
    spl("DEADBEEFline");spl(line);
    bool flag1,flag2,flag3;
    flag2 = index(breaklist,line) == -1;
    flag3 = line!= temp_breakpoint;    
    // check whether p is pressed to stop the program 
    int c=0;
    if(Serial.available()) c = Serial.read();
    if(c == 'p') {flag = 0;spl(line);}
    flag1 = flag;

        
    if(flag1&&flag2&&flag3){
        return;
      }
    
    //p_info(line);
    String command;
    while(1){
      
        command = Serial.readStringUntil(char(10));
        // if(command!="") {spl(command);sp(">>>");}
        if(command[0] == 'c'){
            //if continue, get out of this function and continue executing the program
            //until next breakpoint, which means 'pause' is cancled and flag is reset.
            //also the temp_breakpoint is reset
            // spl("C");
            flag = 1;
            temp_breakpoint = 0;
            break;
            }
        else if (command[0] == 'b'){
            //if set breakpoint, then manuplate the breaklist.
            //b + 12: add a breakpoint at line 12
            //b - 12: minus a breakpoint at line 12
            // command transferred to arduino won't contain any space
            // bound check and other exception check will be done by python.
            // exception check needed:
            // 1 command[1] == (+ or -):mbt(must be true)
            // 2 command[2:].toInt() in breaklist:mbt
            // spl("B");
            if(command[1] == '+'){
                int i = command.substring(2).toInt();
                int index_num = index(breaklist,0);
                breaklist[index_num] = i;
            }else if(command[1] == '-'){
                int i = command.substring(2).toInt();
                int index_num = index(breaklist,i);
                breaklist[index_num] = 0;
            } 
            else{
                //print b info
                int f = 0;
                for(int i=0;i<max_num_breakpoint;i++){
                    if(breaklist[i]!=0){
                        f = 1;
                        /*sp("breakpoint at line ");*/spl(breaklist[i]);
                    }
                }
                if(f == 0){
                        /*spl("No breakpoint yet");*/
                        spl(0);
                    }
            }
            continue;
        }   
        else if (command[0] == 's'){
            //pause is set.
            flag = 0;
            // spl("S");
            temp_breakpoint = 0;
            return;
        }
        else if (command[0] == 'n'){
            //if this line is a function, then close pause flag and set a breakpoint at next line
            //if this line is not a function, then it's just like 's'
            //python file will tell which the situation is.Only the first situation will be interpreted
            //as 'n', otherwise, even if the debuger give command line a 'n', it will be interpreted as 's'
            // spl("N");
            flag = 1;
            temp_breakpoint = line+1; 
            
            return;
            
        }

        //set or watch or change breaklist on base of command by serial input 
        else if(command[0] == 'm'){
            // modify the certain byte
            // m-addr-value ex:m-0x1200-43 set 43 at byte of address 0x1200
            // check point by python: value should be less than 256 and bigger than -1
            // spl("M");
            int temp[2];
            temp[0] = command.indexOf('-');
            temp[1] = command.lastIndexOf('-');
            char* addr = (char*) command.substring(temp[0]+1,temp[1]).toInt();
            char value = (unsigned char) command.substring(temp[1]+1).toInt();
            set(addr,value);
        }
        else if(command[0] == 'w'){
            spl("W");
            int temp[2];
            temp[0] = command.indexOf('-');
            temp[1] = command.lastIndexOf('-');
            char* addr = (char*) command.substring(temp[0]+1,temp[1]).toInt();
            int num = command.substring(temp[1]+1).toInt();
            for(int i=0;i<num;i++){
                spl((unsigned int) (watch(addr+i)));
            }
            spl("w");
        }
        else{
            //sp("not yet");
        }
    }
}//set a break point at the certain line.

inline unsigned char watch(char* addr){
  return (unsigned char) *addr;
}

inline void set(char* addr, char value){//give a address, set the value on it(0~255)
  *addr = value;
}


int index(int* array, int num){
    for(int i=0;i<max_num_breakpoint;i++){
        if(num == array[i]) return i;
    }
    return -1;
}