import matplotlib.pyplot as plt
import numpy as np
import math


"""
number_of_cpus = ["1_Int_1_BE-0", "1_Int-1_BE" ,    "0-1_Int_1_BE",  "1_BE-0",  "0-1_BE"]
workload = [      0.711,            2.3,              2.31 ,        1.23/2,      4.12/2 ]   # values obtained during a test of 10 mins are divided by tow because this test is for 5 mins
cpu_battery =     [8.74,           30.9,             21.4 ,         17.2/2,       59/2   ]  # values obtained during a test of 10 mins are divided by tow because this test is for 5 mins
"""
number_of_cpus = ["1_BE-0", "1_Int_1_BE-0",  "0-1_BE", "1_Int-1_BE" ,  "0-1_Int_1_BE" ]
workload = [     1.23/2,      0.711,           4.12/2,   2.3,            2.31  ]   # values obtained during a test of 10 mins are divided by tow because this test is for 5 mins
cpu_battery = [     17.2/2,   8.74,             59/2 ,   30.9,            21.4      ]  # values obtained during a test of 10 mins are divided by tow because this test is for 5 mins


fig = plt.figure()
plt.bar(number_of_cpus,cpu_battery, width=0.4)
 
# Add title and axis names
plt.title('Energy consumed according to the configuration \n and the interactive task present on the socket')
plt.xlabel('Configuration and presence of an interactive task')
plt.ylabel('Energy consumed')

plt.savefig("Energy_according_to_cpu.png")

plt.clf()
plt.cla()
plt.close()

#################################################

fig = plt.figure()
plt.bar(number_of_cpus,np.divide(workload,100000000000), width=0.4)

# Add title and axis names
plt.title('Workload according  to the configuration \n and the interactive task present on the socket \n ' )
plt.xlabel('Configuration and presence of an interactive task')
plt.ylabel(r'Workload (\times 10E11)')

plt.savefig("workload_according_to_cpu.png")


plt.clf()
plt.cla()
plt.close()
################################################



fig = plt.figure()
plt.bar(number_of_cpus,np.divide(cpu_battery,workload), width=0.4)
# Add title and axis names
plt.title('Energy efficiency (Energy/Workload) according to the configuration \n and to the interactive task present on the socket (lower is better)')
plt.xlabel('Configuration and presence of an interactive task')
plt.ylabel(r'Energy/Workload ($\times 10E-11$)')

plt.savefig("Energy_by_workload_according_to_cpu.png")



plt.clf()
plt.cla()
plt.close()

################################################

