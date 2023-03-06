import matplotlib.pyplot as plt
import numpy as np
import math



############################################ datas for google pixel
#                                                             #-->9 : (1 big)                       //pour voir si les big mènent la danse
#                                                             #-->10: (2 big)                       //pour voir si les big mènent la danse
#                                                             #-->11: (1 little, 1 big) to print    //pour voir si les littles mènent la danse
#                                                             #-->12: (2 little, 1 big)             //pour voir si les littles mènent la danse


number_of_cpus = ["1-0","2-0","3-0","4-0","5-0","6-0","6-1","6-2", "0-1","0-2", "1-1" , "2-1"   ]
workload = [1.63, 3.50, 4.56, 7.11, 7.95, 9.53, 18.2, 21.6,         7.08,15.6,   9.16, 9.83 ]
cpu_battery = [32.2, 62.1, 98.7, 127, 147, 176, 200, 222,           19.4,36.5,   46.5,  82 ]


fig = plt.figure()
plt.bar(number_of_cpus,cpu_battery, width=0.4)
 
# Add title and axis names
plt.title('Energy consumed according to the configuration')
plt.xlabel('Configuration')
plt.ylabel('Energy consumed (mAh)')

plt.savefig("Google_pixel_energy_consumed_according_to_cpu.png")

plt.clf()
plt.cla()
plt.close()

#################################################

fig = plt.figure()
plt.bar(number_of_cpus,np.divide(workload,100000000000), width=0.4)

# Add title and axis names
plt.title('Workload according to the configuration')
plt.xlabel('Configuration')
plt.ylabel(r'Workload ($\times 10E11$)')

fig.autofmt_xdate()
plt.savefig("Google_pixel_workload_according_to_cpu.png")

plt.clf()
plt.cla()
plt.close()
################################################

fig = plt.figure()
plt.bar(number_of_cpus,np.divide(cpu_battery,workload), width=0.4)
# Add title and axis names
plt.title('Energy consumed/ Workload according to the configuration')
plt.xlabel('Configuration')
plt.ylabel(r'Energy/Workload ($\times 10E-11$)')

fig.autofmt_xdate()
plt.savefig("Google_pixel_ratio_energy_by_workload_according_to_cpu.png")

plt.clf()
plt.cla()
plt.close()

################################################

############################################### Just to verify Vlad assumption (fixing big cores)



number_of_cpus = [ "0-1", "1-1",  "2-1", "3-1",   "4-1",  "5-1",  "6-1", "0-2", "1-2","2-2","3-2","4-2","5-2" , "6-2"  ]
workload =      [7.08,   9.16, 9.83,     9.88  ,  11.3,   13.5,    18.2,  15.6,  12.0, 12.1, 13.8, 17.8, 21.4, 21.6 ]
cpu_battery = [19.04,   46.5, 82.2,      114,   141,     167,      200,     36.5, 62.6 , 95.4 , 120, 149, 190, 222 ]




fig = plt.figure()
plt.bar(number_of_cpus,cpu_battery, width=0.4)
 
# Add title and axis names
plt.title('Energy consumed according to the \n number of Thread pinned on cores')
plt.xlabel('Configuration')
plt.ylabel('Energy consumed (mAh)')

fig.autofmt_xdate()
plt.savefig("Fixing_big_cores_number_Google_pixel_energy_consumed_according_to_cpu.png")

plt.clf()
plt.cla()
plt.close()

#################################################

fig = plt.figure()
plt.bar(number_of_cpus,np.divide(workload,100000000000), width=0.4)

# Add title and axis names
plt.title('Workload according to the configuration')
plt.xlabel('Configuration')
plt.ylabel(r'Workload ($\times 10E11$)')

fig.autofmt_xdate()
plt.savefig("Fixing_big_cores_Google_pixel_workload_according_to_cpu.png")

plt.clf()
plt.cla()
plt.close()
################################################

fig = plt.figure()
plt.bar(number_of_cpus,np.divide(cpu_battery,workload), width=0.4)
# Add title and axis names
plt.title('Energy consumed/ Workload according to the configuration')
plt.xlabel('Configuration')
plt.ylabel(r'Energy/Workload ($\times 10E-11$)')

fig.autofmt_xdate()
plt.savefig("Fixing_big_cores_Google_pixel_ratio_energy_by_workload_according_to_cpu.png")

plt.clf()
plt.cla()
plt.close()

################################################



############################################### Just to verify Vlad assumption (fixing little cores)


number_of_cpus_ = [ "0-1", "0-2",   "1-0", "1-1", "1-2",    "2-0", "2-1", "2-2",    "3-0", "3-1" , "3-2",    "4-0" ,  "4-1", "4-2", "5-0", "5-1", "5-2", "6-0", "6-1", "6-2" ]
workload_ =      [7.08,     15.6,    1.63, 9.16, 12.01,     3.5,  9.83, 12.1 ,   4.56,  8.88,  13.8,         7.11,  11.3,  17.8,   7.95, 13.5, 21.4,    9.53, 18.2, 21.6 ]
cpu_battery_ =   [19.04,    36.5,    32.2,  46.5, 62.6 , 62.1,  82.2,  95.4 ,   98.7,  114, 120,            127,   141, 149,     147,  167,  190,     176, 200,  222 ]



fig = plt.figure()
plt.bar(number_of_cpus_,cpu_battery_, width=0.4)
 
# Add title and axis names
plt.title('Energy consumed according to the \n number of Thread pinned on cores')
plt.xlabel('Configuration')
plt.ylabel('Energy consumed (mAh)')

fig.autofmt_xdate()
plt.savefig("Fixing_little_cores_number_Google_pixel_energy_consumed_according_to_cpu.png")

plt.clf()
plt.cla()
plt.close()

#################################################

fig = plt.figure()
plt.bar(number_of_cpus_,np.divide(workload_,100000000000), width=0.4)

# Add title and axis names
plt.title('Workload according to the configuration')
plt.xlabel('Configuration')
plt.ylabel(r'Workload ($\times 10E11$)')

fig.autofmt_xdate()
plt.savefig("Fixing_little_cores_Google_pixel_workload_according_to_cpu.png")

plt.clf()
plt.cla()
plt.close()
################################################

fig = plt.figure()
plt.bar(number_of_cpus_,np.divide(cpu_battery_,workload_), width=0.4)
# Add title and axis names
plt.title('Energy efficiency (Energy/Workload) according to the configuration')
plt.xlabel('Configuration')
plt.ylabel(r'Energy/Workload ($\times 10E-11$)')

fig.autofmt_xdate()
plt.savefig("Fixing_little_cores_Google_pixel_ratio_energy_by_workload_according_to_cpu.png")

plt.clf()
plt.cla()
plt.close()

################################################




############################################### Just to verify if the heat has an impact on energy



number_of_cpus_ = [ "N-0-2", "N-1-2","N-2-2","N-3-2","N-4-2","N-5-2" , "N-6-2", "C-0-2", "C-1-2",  "C-2-2", "C-3-2",   "C-4-2",  "C-5-2",  "C-6-2",   ]
workload_ =      [  15.6,  12.0, 12.1, 13.8, 17.8, 21.4, 21.6,                    15.2 , 13.0 ,       13.5 , 18.3 ,     21.1 , 23.1 ,  21.8  ]
cpu_battery_ = [    36.5, 62.6 , 95.4 , 120, 149, 190, 222,                      41.7  , 62.6 ,       98.3 , 128 ,     157 , 182,   213  ]




fig = plt.figure()
plt.bar(number_of_cpus_,cpu_battery_, width=0.4)
 
# Add title and axis names
plt.title('Normal & Cooled phone: Energy consumed according to \n the configuration ')
plt.xlabel('Configuration')
plt.ylabel('Energy consumed (mAh)')

fig.autofmt_xdate()
plt.savefig("Cooled_Fixing_big_cores_number_Google_pixel_energy_consumed_according_to_cpu.png")

plt.clf()
plt.cla()
plt.close()

#################################################

fig = plt.figure()
plt.bar(number_of_cpus_,np.divide(workload_,100000000000), width=0.4)

# Add title and axis names
plt.title('Normal & Cooled phone: Workload according to the configuration')
plt.xlabel('Configuration')
plt.ylabel(r'Workload ($\times 10E11$)')
fig.autofmt_xdate()
plt.savefig("Cooled_Fixing_big_cores_Google_pixel_workload_according_to_cpu.png")

plt.clf()
plt.cla()
plt.close()
################################################

fig = plt.figure()
plt.bar(number_of_cpus_,np.divide(cpu_battery_,workload_), width=0.4)
# Add title and axis names
plt.title('Normal & Cooled phone: Energy/Workload \n according to the configuration (lower is better)')
plt.xlabel('Configuration')
plt.ylabel(r'Energy/Workload ($\times 10E-11$)')

fig.autofmt_xdate()
plt.savefig("Cooled_Fixing_big_cores_Google_pixel_ratio_energy_by_workload_according_to_cpu.png")

plt.clf()
plt.cla()
plt.close()

################################################
