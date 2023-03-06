import matplotlib.pyplot as plt
import numpy as np
import math



############################################ datas for google pixel
#                                                             #-->9 : (1 big)                       //pour voir si les big mènent la danse
#                                                             #-->10: (2 big)                       //pour voir si les big mènent la danse
#                                                             #-->11: (1 little, 1 big) to print    //pour voir si les littles mènent la danse
#                                                             #-->12: (2 little, 1 big)             //pour voir si les littles mènent la danse



folder = "interactive_and_cpu_intensive_on_little_socket"
interactive_sleep_time = ["300", "400", "500","600", "700", "800" ,"900", "CPU_int_alone"]
workload = [0.921, 0.939 ,0.833, 0.906, 0.831, 0.9390, 0.913,  1.63/2 ]
energy = [ 16.8, 16.8, 16.7, 17.1, 17, 16.4, 17.5, 32.2/2 ]



fig = plt.figure()
plt.bar(interactive_sleep_time,energy, width=0.4)
 
# Add title and axis names
plt.title('Cpu consumption according to the \n interactive sleep time')
plt.xlabel('Interactive app simulation sleep time (ms)')
plt.ylabel('Battery cpu usage')

plt.savefig("energy_according_to_sleep_time.png")
plt.savefig(folder+"/energy_according_to_sleep_time.png")

plt.clf()
plt.cla()
plt.close()

#################################################

fig = plt.figure()
plt.bar(interactive_sleep_time,np.divide(workload,100000000000), width=0.4)

# Add title and axis names
plt.title('New computed Workload according to the \n interactive sleep time \n ' + folder)
plt.xlabel('Interactive app sleep time (ms)')
plt.ylabel(r'Workload (\times 10E11)')

plt.savefig("workload_according_to_sleep_time.png")
plt.savefig(folder+"/workload_according_to_sleep_time.png")

plt.clf()
plt.cla()
plt.close()
################################################


fig = plt.figure()
plt.bar(interactive_sleep_time,np.divide(energy,workload), width=0.4)
# Add title and axis names
plt.title('Cpu Consumtion/Workload according to the number of CPUs (Higher is better) \n ' + folder)
plt.xlabel('Interactive sleep time (ms)')
plt.ylabel(r'Energy/Workload ( \times 10E-11 )')

plt.savefig("ratio_energy_by_workload_according_to_sleep_time.png")
plt.savefig(folder+"/ratio_energy_by_workload_according_to_sleep_time.png")


plt.clf()
plt.cla()
plt.close()

################################################

