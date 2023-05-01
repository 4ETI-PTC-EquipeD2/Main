# pip instpiall pyserial
from serial import Serial

ser = Serial()
ser.baudrate = 19200 # standard Baudrate for STM32F4 devices
ser.port = 'COM7'
ser.bytesize=8
ser.parity='N'
ser.stopbits=1
ser.timeout=None
ser.xonxoff=0
ser.rtscts=0

# x = ser.read()          # read one byte
# s = ser.read(10)        # read up to 10 bytes (timeout)
# l= ser.readline()       # read line finishing by "\n"

print('here')
ser.open()
if ser.is_open:
    print("connected to", ser,"\n")
    
    """
    line = ser.readline()
    line = line.decode("utf-8")
    if line :
        print(line,'\n')"""
    while True:
        
        commande = input("Votre commande : ")
        if commande == 'z':   
            ser.write(b'z') 
        if commande == 'a' :
            ser.write(b'a')
        if commande == 'v' :
            ser.write(b'v')
        line = ser.readline()
        line = line.decode("utf-8")
        if line :
            print(line,'\n')
        
        
        
ser.close()
