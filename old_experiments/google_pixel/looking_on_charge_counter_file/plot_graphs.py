import matplotlib.pyplot as plt
import numpy as np
import math



           #-->12: (2 little, 1 big)             //pour voir si les littles mènent la danse



ind = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
ind = np.divide(ind,2)
ind2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
ind2 = np.divide(ind2,2)

charge_counter = [4032000.0, 4032000.0, 4032000.0, 4032000.0, 4032000.0, 4032000.0, 4032000.0, 4032000.0, 4032000.0, 4032000.0, 4032000.0, 4032000.0, 4032000.0, 4032000.0, 4032000.0, 4032000.0, 4032000.0, 4032000.0, 4032000.0, 4029177.0] 
temperature  =[28000.0, 28000.0, 28000.0, 29000.0, 29000.0, 29000.0, 29000.0, 29000.0, 30000.0, 30000.0, 30000.0, 30000.0, 30000.0, 30000.0, 30000.0, 30000.0, 30000.0, 30000.0, 30000.0, 30000.0]


fig = plt.figure()
plt.bar(ind, np.divide(charge_counter, 1000000.0), width=0.4)
 
# Add title and axis names
plt.title('Charge counter on Big core (*1000000) (?), \n diff = ' + str(4032000-4029177))
plt.xlabel('time')
plt.ylabel("Charge counter")

plt.savefig("charge_counter_0-1.png")

plt.clf()
plt.cla()
plt.close()

#################################################


fig = plt.figure()
plt.bar(ind, np.divide(temperature,1000.0), width=0.4)
 
# Add title and axis names
plt.title('Cpu temperature')
plt.xlabel('time')
plt.ylabel('Temperature (celcius)')

plt.savefig("cpu_temperature_0-1.png")

plt.clf()
plt.cla()
plt.close()

#################################################


ind = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
ind = np.divide(ind,2)
ind2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
ind2 = np.divide(ind2,2)

charge_counter = [4032000.0, 4032000.0, 4032000.0, 4032000.0, 4032000.0, 4032000.0, 4032000.0, 4032000.0, 4032000.0, 4030790.0, 4029580.0, 4028774.0, 4027161.0, 4026355.0, 4025145.0, 4023532.0, 4022726.0, 4021516.0, 4019904.0, 4019097.0]
temperature  =[28000.0, 28000.0, 28000.0, 28000.0, 28000.0, 28000.0, 27000.0, 27000.0, 27000.0, 27000.0, 27000.0, 27000.0, 27000.0, 27000.0, 27000.0, 27000.0, 27000.0, 27000.0, 27000.0, 27000.0]
fig = plt.figure()
plt.bar(ind, np.divide(charge_counter, 1000000.0), width=0.4)
 
# Add title and axis names
plt.title('Charge counter (*1000000),  \n Big core stopped, thread not pinned  diff = '  + str(4032000-4019097))
plt.xlabel('time')
plt.ylabel("Charge counter)")

plt.savefig("charge_counter_1-0.png")

plt.clf()
plt.cla()
plt.close()

#################################################


fig = plt.figure()
plt.bar(ind, np.divide(temperature,1000.0), width=0.4)
 
# Add title and axis names
plt.title('Cpu temperature')
plt.xlabel('time')
plt.ylabel('Temperature when Big core are stopped, thread is not pinned (celcius)')

plt.savefig("cpu_temperature_1-0.png")

plt.clf()
plt.cla()
plt.close()

#################################################

'''

number_of_cpus = ["1_p-Big_stp","1-Big_stp", "1-0","0-1_b","0-1_B"]
workload = [ 1.45, 1.45, 1.55, 7.03,  7.69 ]
cpu_battery = [ 33.7, 34.4,  33.3, 19.4,  26.1  ]


fig = plt.figure()
plt.bar(number_of_cpus,cpu_battery, width=0.4)
 
# Add title and axis names
plt.title('Cpu consumption according to the \n number of Thread pinned on  cores')
plt.xlabel('Number of CPUs')
plt.ylabel('Battery cpu usage')

plt.savefig("Google_pixel_cpu_battery_usage_according_to_cpu.png")

plt.clf()
plt.cla()
plt.close()

#################################################

fig = plt.figure()
plt.bar(number_of_cpus,np.divide(workload,100000000000), width=0.4)

# Add title and axis names
plt.title('New computed Workload according to the number of CPUs')
plt.xlabel('Number of CPUs')
plt.ylabel(r'Workload (\times 10E11)')

plt.savefig("Google_pixel_workload_according_to_cpu.png")

plt.clf()
plt.cla()
plt.close()
################################################

fig = plt.figure()
plt.bar(number_of_cpus,np.divide(cpu_battery,workload), width=0.4)
# Add title and axis names
plt.title('Cpu consumption/ Workload according to the number of CPUs')
plt.xlabel('Number of CPUs')
plt.ylabel(r'Battery cpu/Workload ( \times 10E-11 )')

plt.savefig("Google_pixel_ratio_cpu_battery_workload_according_to_cpu.png")

plt.clf()
plt.cla()
plt.close()

################################################
'''