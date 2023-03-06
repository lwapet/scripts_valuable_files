import matplotlib.pyplot as plt
import numpy as np
import math



############################################ datas for google pixel
#                                                             #-->9 : (1 big)                       //pour voir si les big mènent la danse
#                                                             #-->10: (2 big)                       //pour voir si les big mènent la danse
#                                                             #-->11: (1 little, 1 big) to print    //pour voir si les littles mènent la danse
#                                                             #-->12: (2 little, 1 big)             //pour voir si les littles mènent la danse


'''
number_of_cpus = ["1_Int_1_BE-0", "1_Int-1_BE" ,    "0-1_Int_1_BE",  "2_BE-0", "1_BE-1_BE",  "0-2_BE"]
workload = [3.48,  9.31,  13.9 , 3.5,  9.16,  15.6 ]
cpu_battery = [57,   51.2, 36,  62.1,   46.5  , 36.5 ]
'''
'''
number_of_cpus = ["1_Int_1_BE-0", "1_Int-1_BE" ,    "0-1_Int_1_BE",  "2_BE-0", "1_BE-1_BE",  "0-2_BE"]
workload = [4.1,  8.6,  12 , 3.5,  9.16,  15.6 ]
cpu_battery = [51.9,  43.2, 34.2,  62.1,   46.5  , 36.5 ]
'''
number_of_cpus = ["1_Int_1_BE-0", "1_Int-1_BE" ,    "0-1_Int_1_BE",  "2_BE-0", "1_BE-1_BE",  "0-2_BE"]
workload = [2.47,  8.08,  9.55 , 3.5,  9.16,  15.6 ]
cpu_battery = [42,  29.4, 24.8,  62.1,   46.5  , 36.5 ]


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

