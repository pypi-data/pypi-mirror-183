# 使用手册：

## 一、调试命令集合

### lx

*使用例子*：l32：

打印接下来32行代码。如果剩余代码＜32行，则把剩余代码全部打印。

x可缺省。缺省时，默认打印接下来7行代码

lall：打印完整代码

lthis：打印**接下来要执行**的某一行

### c

继续运行代码

### p

暂停代码执行。点击回车后打印出暂停后**接下来要执行的**一行代码

### s

执行下一行指令。点击回车后，打印出**刚刚执行过**的指令。

### n

执行下一行指令，若下一行指令是函数，则跳过函数执行结果。

### g-variable-value

将某个variable改变为特定value的值

### d-variable

打印某个variable的值



## 二、使用方法





arduino-cli compile -b arduino:avr:uno C:\Users\xingxing\Documents\Arduino\button2

arduino-cli upload -b arduino:avr:uno -p COM3 C:\Users\xingxing\Documents\Arduino\button2
