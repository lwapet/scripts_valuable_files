import matplotlib.pyplot as plt
import numpy as np
import math



           #-->12: (2 little, 1 big)             //pour voir si les littles mènent la danse



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
