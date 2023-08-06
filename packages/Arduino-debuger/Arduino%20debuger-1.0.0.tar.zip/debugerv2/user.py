import debugerv2

port = 'COM3'
baud_rate = 9600
folder = "C:\\Users\\xingxing\\Documents\\Arduino\\test4"
file = "test4.ino"

debug = debugerv2.debuger(port=port,baud_rate=baud_rate,folder=folder,file=file)