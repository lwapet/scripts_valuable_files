import matplotlib.pyplot as plt
import numpy as np
import math



############################################ datas for google pixel
#                                                             #-->9 : (1 big)                       //pour voir si les big mènent la danse
#                                                             #-->10: (2 big)                       //pour voir si les big mènent la danse
#                                                             #-->11: (1 little, 1 big) to print    //pour voir si les littles mènent la danse
#                                                             #-->12: (2 little, 1 big)             //pour voir si les littles mènent la danse



folder = "1_60ms_sleep_1s_interval"
number_of_cpus = ["1_Int_1_BE-0", "1_Int-1_BE" ,    "0-1_Int_1_BE",  "1_BE-0",  "0-1_BE"]
workload = [1.55,  7.72,  6.88 , 1.63, 7.08 ]
cpu_battery = [31.7,   24.5, 25.1 ,  32.2, 19.4   ]

'''
folder = "2_10s_sleep_20s_interval"
number_of_cpus = ["1_Int_1_BE-0", "1_Int-1_BE" ,    "0-1_Int_1_BE",  "1_BE-0",  "0-1_BE"]
workload = [1.57,  7.7,  7.72 , 1.63, 7.08 ]
cpu_battery = [31.9,   25.6, 24.9 ,  32.2, 19.4   ]


folder =  "3_900ms_sleep_1s_interval"
number_of_cpus = ["1_Int_1_BE-0", "1_Int-1_BE" ,    "0-1_Int_1_BE",  "1_BE-0",  "0-1_BE"]
workload = [1.46,  7.71,  7.58 , 1.63, 7.08 ]
cpu_battery = [31.3,   24.2, 24.5 ,  32.2, 19.4   ]
'''

fig = plt.figure()
plt.bar(number_of_cpus,cpu_battery, width=0.4)
 
# Add title and axis names
plt.title('Cpu consumption according to the \n number of Thread pinned on  cores')
plt.xlabel('Number of CPUs')
plt.ylabel('Battery cpu usage')

plt.savefig("Google_pixel_cpu_battery_usage_according_to_cpu.png")
plt.savefig(folder+"/Google_pixel_cpu_battery_usage_according_to_cpu.png")

plt.clf()
plt.cla()
plt.close()

#################################################

fig = plt.figure()
plt.bar(number_of_cpus,np.divide(workload,100000000000), width=0.4)

# Add title and axis names
plt.title('New computed Workload according to the number of CPUs \n ' + folder)
plt.xlabel('Number of CPUs')
plt.ylabel(r'Workload (\times 10E11)')

plt.savefig("Google_pixel_workload_according_to_cpu.png")
plt.savefig(folder+"/Google_pixel_workload_according_to_cpu.png")

plt.clf()
plt.cla()
plt.close()
################################################

fig = plt.figure()
plt.bar(number_of_cpus,np.divide(workload,cpu_battery), width=0.4)
# Add title and axis names
plt.title('Workload/Cpu Consumtion according to the number of CPUs (Higher is better) \n '+ folder)
plt.xlabel('Number of CPUs')
plt.ylabel(r'Workload/Energy ( \times 10E-11 )')

plt.savefig("Google_pixel_ratio_workload_by_energy_according_to_cpu.png")
plt.savefig(folder+"/Google_pixel_ratio_workload_by_energy_according_to_cpu.png")


fig = plt.figure()
plt.bar(number_of_cpus,np.divide(cpu_battery,workload), width=0.4)
# Add title and axis names
plt.title('Cpu Consumtion/Workload according to the number of CPUs (Higher is better) \n ' + folder)
plt.xlabel('Number of CPUs')
plt.ylabel(r'Energy/Workload ( \times 10E-11 )')

plt.savefig("Google_pixel_ratio_energy_by_workload_according_to_cpu.png")
plt.savefig(folder+"/Google_pixel_ratio_energy_by_workload_according_to_cpu.png")



plt.clf()
plt.cla()
plt.close()

################################################

