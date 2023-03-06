import matplotlib.pyplot as plt
import numpy as np
import math



############################################ datas for google pixel
#                                                             #-->9 : (1 big)                       //pour voir si les big mènent la danse
#                                                             #-->10: (2 big)                       //pour voir si les big mènent la danse
#                                                             #-->11: (1 little, 1 big) to print    //pour voir si les littles mènent la danse
#                                                             #-->12: (2 little, 1 big)             //pour voir si les littles mènent la danse


"""
#folder = "interactive_and_cpu_intensive_on_little_socket"
configuration = [ "1_Inter_1BE_mid - 0", "1_Inter - 1_BE_mid",  "1_Inter_1BE - 0", "1_Inter - 1_BE"]
workload =        [0.57,                   1.41,                   0.71,               2.30 ]  # values obtained during a test of 10 mins are divided by tow because this test is for 5 mins
energy =  [      6.39,                   12.0,                    8.74,                  30.9 ] # values obtained during a test of 10 mins are divided by tow because this test is for 5 mins
"""
#folder = "interactive_and_cpu_intensive_on_little_socket"
configuration = ["1_Inter_1BE - 0", "1_Inter_1BE_mid - 0",    "1_Inter - 1_BE", "1_Inter - 1_BE_mid",]
workload = [        0.71,            0.57,                 2.30,                     1.41   ]  # values obtained during a test of 10 mins are divided by tow because this test is for 5 mins
energy =  [       8.74,               6.39,                 30.9,                        12.0  ] # values obtained during a test of 10 mins are divided by tow because this test is for 5 mins




fig = plt.figure()
plt.bar(configuration,energy, width=0.4)
 
# Add title and axis names
plt.title('Energy consumed according to the presence of an interactive task on the socket  \n and to the CPU frequency level')
plt.xlabel('Configuration, frequence and presence of interactive task')
plt.ylabel('Energy consumed')

plt.savefig("energy_according_to_interactive_task_and_frequency.png")
#plt.savefig("folder+"/"energy_according_to_sleep_time.png")

#plt.savefig(folder+"/energy_according_to_sleep_time.png")

plt.clf()
plt.cla()
plt.close()

#################################################

fig = plt.figure()
plt.bar(configuration,np.divide(workload,100000000000), width=0.4)

# Add title and axis names
plt.title('Workload according to the presence of an interactive task on the socket  \n and to the CPU frequency level')
plt.xlabel('Configuration, frequence and presence of interactive task')
plt.ylabel(r'Workload ($\times 10E11$)')


plt.savefig("workload_according_to_interactive_task_and_frequency.png")

#plt.savefig(folder+"/workload_according_to_sleep_time.png")

plt.clf()
plt.cla()
plt.close()
################################################


fig = plt.figure()
plt.bar(configuration,np.divide(energy,workload), width=0.4)
# Add title and axis names
plt.title('Energy efficiency according to the presence of an interactive task \n and to the CPU frequency (lower is better)')
plt.xlabel('Configuration, frequence and presence of interactive task')
plt.ylabel(r'Energy/Workload ($\times 10E-11$)')

plt.savefig("ratio_energy_by_workload_according_to_interactive_task_and_frequency.png")

#plt.savefig(folder+"/ratio_energy_by_workload_according_to_sleep_time.png")


plt.clf()
plt.cla()
plt.close()

################################################

