flow1limit = 6.0    # l/m
flow2limit = 6.0    # l/m

# Sensor data in p/l (pulses per liter)
flow1_ppl = 450.
flow2_ppl = 450.

limit1 = int(round(flow1limit*flow1_ppl/30))
limit2 = int(round(flow2limit*flow2_ppl/30))

print "Setting limits for the LED status"
print "Limit1: %.2f l/m (%.1f Hz)" % (flow1limit, limit1/2.)
print "Limit2: %.2f l/m (%.1f Hz)" % (flow2limit, limit2/2.)

lstr1 = "%04X" % limit1
lstr2 = "%04X" % limit2

import serial

serialport = serial.Serial("/dev/ttyS0", 9600, timeout=0.5)

serialport.write("SL1" + lstr1 + "\n")
serialport.write("SL2" + lstr2 + "\n")
serialport.write("STO\n")
