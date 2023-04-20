# pip install pyserial
from serial import Serial

ser = Serial()
ser.baudrate = 19200 # standard Baudrate for STM32F4 devices
ser.port = 'COM5'
ser.bytesize=8
ser.parity='N'
ser.stopbits=1
ser.timeout=None
ser.xonxoff=0
ser.rtscts=0

# x = ser.read()          # read one byte
# s = ser.read(10)        # read up to 10 bytes (timeout)
# l= ser.readline()       # read line finishing by "\n"

if ser.open():
    print(ser,"\n")
    while True:
        line = str(ser.readline()) 
        print(line,"\n")