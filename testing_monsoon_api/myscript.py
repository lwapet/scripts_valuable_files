# myscript.py

import time
from physalia.power_meters import MonsoonPowerMeter
from physalia.energy_profiler import AndroidUseCase

power_meter = MonsoonPowerMeter(voltage=3.7, serial=29363)#(voltage=3.8, serial=12886)
#power_meter.SetUsbPassthrough(1)

def run(_):
    time.sleep(5)
    print(" Android user case ok")
use_case = AndroidUseCase('physalia-simple-tutorial', None, 'na', 'na', run=run)

measurement = use_case.run(power_meter=power_meter)
print(measurement)
