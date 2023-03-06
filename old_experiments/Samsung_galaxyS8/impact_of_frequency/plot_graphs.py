import matplotlib.pyplot as plt
import numpy as np
import math



############################################ datas for google pixel
#                                                             #-->9 : (1 big)                       //pour voir si les big mènent la danse
#                                                             #-->10: (2 big)                       //pour voir si les big mènent la danse
#                                                             #-->11: (1 little, 1 big) to print    //pour voir si les littles mènent la danse
#                                                             #-->12: (2 little, 1 big)             //pour voir si les littles mènent la danse



#folder = "interactive_and_cpu_intensive_on_little_socket"
configuration = [ "1_min-0", "1_mid-0","1_max-0", "0-1_min", "0-1_mid",   "0-1_max"]
workload = [0.187,  0.422,   1.23/2,      0.69,  1.4    ,4.12/2  ] # values obtained during a test of 10 mins are divided by tow because this test is for 5 mins
energy =  [  5.27, 5.30,   17.2/2,  5.87,     12.5  ,    59/2 ] # values obtained during a test of 10 mins are divided by tow because this test is for 5 mins

"""
#folder = "interactive_and_cpu_intensive_on_little_socket"
configuration = [ "1_min-0", "1_mid-0", "0-1_min", "0-1_mid", "1-0",  "0-1"]
workload = [0.187,  0.422,        0.69,  1.4    ,1.23/2, 4.12/2  ] # values obtained during a test of 10 mins are divided by tow because this test is for 5 mins
energy =  [  5.27, 5.30, 5.87,     12.5  ,   17.2/2, 59/2 ] # values obtained during a test of 10 mins are divided by tow because this test is for 5 mins
"""





fig = plt.figure()
plt.bar(configuration,energy, width=0.4)
 
# Add title and axis names
plt.title('Energy consumed according to the configuration and to the frequency')
plt.xlabel('Configuration and frequency level')
plt.ylabel('Energy consumed')

plt.savefig("energy_according_to_configuration_and_frequency.png")
#plt.savefig("folder+"/"energy_according_to_sleep_time.png")

#plt.savefig(folder+"/energy_according_to_sleep_time.png")

plt.clf()
plt.cla()
plt.close()

#################################################

fig = plt.figure()
plt.bar(configuration,np.divide(workload,100000000000), width=0.4)

# Add title and axis names
plt.title('Workload according to the configuration and the frequency \n ')
plt.xlabel('Configuration and frequency level')
plt.ylabel(r'Workload ($\times 10E11$)')

plt.savefig("workload_according_to_configuration_and_frequency.png")


plt.clf()
plt.cla()
plt.close()
################################################


fig = plt.figure()
plt.bar(configuration,np.divide(energy,workload), width=0.4)
# Add title and axis names
plt.title('Energy efficiency (Energy/Workload) according to configuration \n and frequency (lower is better) ')
plt.xlabel('Configuration')
plt.ylabel(r'Energy/Workload ($\times 10E-11$)')

plt.savefig("ratio_energy_by_workload_according_to_sleep_time.png")

#plt.savefig(folder+"/ratio_energy_by_workload_according_to_sleep_time.png")


plt.clf()
plt.cla()
plt.close()

################################################

