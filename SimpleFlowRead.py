import serial
import re

# Sensor data in ppl (pulses per liter)
flow1_ppl = 450.
flow2_ppl = 450.

serialport = serial.Serial("/dev/ttyS0", 9600, timeout=0.5)

while True:
    response = serialport.readlines(None)

    try:
        matchObj = re.match(r'(.*)-(.*)-(.*)', response[0])
    except:
        matchObj=False
		
    if matchObj:
        flow1 = int(matchObj.group(2),16)
        flow2 = int(matchObj.group(3),16)
        flow1lpm = (flow1/flow1_ppl*30.)
        flow2lpm = (flow2/flow2_ppl*30.)		
        print "Flow 1:",'%.2f' % flow1lpm,"l/min\tFlow 2:",'%.2f' % flow2lpm,"l/min"        
    else:
        print "Error: Could not match data"