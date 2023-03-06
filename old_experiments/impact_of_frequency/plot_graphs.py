import matplotlib.pyplot as plt
import numpy as np
import math



############################################ datas for google pixel
#                                                             #-->9 : (1 big)                       //pour voir si les big mènent la danse
#                                                             #-->10: (2 big)                       //pour voir si les big mènent la danse
#                                                             #-->11: (1 little, 1 big) to print    //pour voir si les littles mènent la danse
#                                                             #-->12: (2 little, 1 big)             //pour voir si les littles mènent la danse



#folder = "interactive_and_cpu_intensive_on_little_socket"
configuration = [ "1_BE_min-0", "1_BE_mid-0", "0-1_BE_min", "0-1_BE_mid", "1_BE-0",  "0-1_BE"]
workload = [0.35, 0.72, 1.46, 3.18,  1.63/2, 7.08/2 ] # values obtained during a test of 10 mins are divided by tow because this test is for 5 mins
energy =  [7.83, 12.8, 7.53,  12.4,  32.2/2, 19.4/2] # values obtained during a test of 10 mins are divided by tow because this test is for 5 mins






fig = plt.figure()
plt.bar(configuration,energy, width=0.4)
 
# Add title and axis names
plt.title('Cpu consumption according to the \n interactive sleep time')
plt.xlabel('Configuration')
plt.ylabel('Battery cpu usage')

plt.savefig("energy_according_to_sleep_time.png")
#plt.savefig("folder+"/"energy_according_to_sleep_time.png")

#plt.savefig(folder+"/energy_according_to_sleep_time.png")

plt.clf()
plt.cla()
plt.close()

#################################################

fig = plt.figure()
plt.bar(configuration,np.divide(workload,100000000000), width=0.4)

# Add title and axis names
plt.title('New computed Workload according to the \n interactive sleep time \n ')
plt.xlabel('Configuration')
plt.ylabel(r'Workload (\times 10E11)')

plt.savefig("workload_according_to_sleep_time.png")

plt.savefig("workload_according_to_sleep_time.png")

#plt.savefig(folder+"/workload_according_to_sleep_time.png")

plt.clf()
plt.cla()
plt.close()
################################################


fig = plt.figure()
plt.bar(configuration,np.divide(energy,workload), width=0.4)
# Add title and axis names
plt.title('Cpu Consumtion/Workload according to the number of CPUs (Higher is better) \n ')
plt.xlabel('Configuration')
plt.ylabel(r'Energy/Workload ( \times 10E-11 )')

plt.savefig("ratio_energy_by_workload_according_to_sleep_time.png")

#plt.savefig(folder+"/ratio_energy_by_workload_according_to_sleep_time.png")


plt.clf()
plt.cla()
plt.close()

################################################

