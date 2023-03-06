import matplotlib.pyplot as plt
import numpy as np
import math





number_of_cpus = ["1-0","2-0","3-0","4-0","0-1","0-2","0-3","1-1", "1-2","2-1"  ]
workload =      [  1.23, 2.57, 3.93, 5.09, 4.12, 8.08, 11 , 5.46, 9.38,  6.88]
cpu_battery =   [  17.2,  33.9, 47.8, 62.8, 59, 98.4, 116 , 130,  139, 157 ]

# for the presentation to del
number_of_cpus = ["1-0","0-1" ]
workload =      [  1.23,  4.12]
cpu_battery =   [  17.2,  59]



fig = plt.figure()
plt.bar(number_of_cpus,cpu_battery, width=0.4)
 
# Add title and axis names
plt.title('Energy consumed according to the configuration')
plt.xlabel('Configuration')
plt.ylabel('Energy consumed (mAh)')

plt.title('Energy consumed according to the configuration.', fontsize=15)
plt.xlabel('Configuration', fontsize=15) 
plt.ylabel(r'Energy consumed (Ah)',  fontsize=15)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.savefig("Samsung_S_8_energy_consumed_according_to_cpu.png")

plt.clf()
plt.cla()
plt.close()

#################################################

fig = plt.figure()
plt.bar(number_of_cpus,np.divide(workload,100000000000), width=0.4)

# Add title and axis names
plt.title('Workload according to the configuration')
plt.xlabel('Configuration')
plt.ylabel(r'$Workload (\times 10E11)$')

plt.savefig("Samsung_S_8_workload_according_to_cpu.png")

plt.clf()
plt.cla()
plt.close()
################################################

fig = plt.figure()
plt.bar(number_of_cpus,np.divide(cpu_battery,workload), width=0.4)
# Add title and axis names
plt.title('Energy efficiency (Energy/Workload) according configuration \n (lower is better)')
plt.xlabel('Configuration')

plt.ylabel(r'$Workload (\times 10E-11 )$')

plt.savefig("Samsung_S_8_ratio_energy_by_workload_according_to_cpu.png")

plt.clf()
plt.cla()
plt.close()

################################################
