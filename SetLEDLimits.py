This program sets the limits for the LED status according 
to the following rules:

too low:    LED = red       if  flow < limit_1
ok:         LED = green     if  flow > limit_1 AND flow < limit_2
too high:   LED = orange    if  flow > limit_2

