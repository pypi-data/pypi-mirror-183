//arduino端只实现三个函数
#pragma once
#include<Arduino.h>
unsigned char watch(char* addr);//give a address, return the value on it(0~255)
void set(char* addr, char value);//give a address, set the value on it(0~255)
void breakpoint(int line);//set a break point at the certain line.
#define max_num_breakpoint 20//num of breakpoints <= 20
#define sp Serial.print
#define spl Serial.println
#define max_num_command 20//length of command <= 20 
inline void p_info(int line) { 
    String info;
    info = String("breakpoint at ") + String(line) + String(" of ") + String(__FILE__);
    Serial.println(info);Serial.print(">>> ");
}


