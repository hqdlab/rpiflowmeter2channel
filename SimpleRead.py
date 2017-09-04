import serial

serialport = serial.Serial("/dev/ttyAMA0", 9600, timeout=0.5)

while True:
    response = serialport.readlines(None)
    print resonse
    