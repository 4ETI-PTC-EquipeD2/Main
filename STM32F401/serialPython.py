# pip install pyserial
from serial import Serial
import keyboard

ser = Serial()
ser.baudrate = 19200 # standard Baudrate for STM32F4 devices
ser.port = 'COM5'
ser.bytesize=8
ser.parity='N'
ser.stopbits=1
ser.timeout=None
ser.xonxoff=0
ser.rtscts=0
ser.timeout=1

# x = ser.read()          # read one byte
# s = ser.read(10)        # read up to 10 bytes (timeout)
# l= ser.readline()       # read line finishing by "\n"

if ser.open():
    print(ser,"\n")
    while True:
        if keyboard.is_pressed("a"):
            print("stop")
            ser.write(b"stop>")
        elif keyboard.is_pressed("z"):
            print("forward")
            ser.write(b"move:forward")
        elif keyboard.is_pressed("s"):
            print("backward")
            ser.write(b"move: backward")
        elif keyboard.is_pressed("q"):
            print("left")
            ser.write(b"turn: left")
        elif keyboard.is_pressed("d"):
            print("right")
            ser.write(b"turn: right")

        line = str(ser.readline()) 
        print(line,"\n") 