#  This program sets the limits for the LED status according 
#  to the following rules:
# 
#  too low:    LED = red       if  flow <  limit
#  ok:         LED = green     if  flow >= limit
# 

limit1 = 75      # 5 liter/minute * 450 pulses/liter * 2 / 60 

import serial

serialport = serial.Serial("/dev/ttyAMA0", 9600, timeout=0.5)

