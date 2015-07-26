from decimal import *

import os
a = 1
res = os.open('vcgencmd measure_temp').readline()
resold = res.replace("tenp=","")
resnew = resold.replace("'C'","")
resint = float(Decimal(resnew))

while a ==1:
    print resint

