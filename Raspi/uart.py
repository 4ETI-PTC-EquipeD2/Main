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
# s = ser.read(10)        # read up to ten bytes (timeout)
ser.open()
print(ser,"\n")

line = ser.readline()
print(line)