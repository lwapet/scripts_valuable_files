import matplotlib.pyplot as plt
import numpy as np
import math



############################################ datas for google pixel
#                                                             #-->9 : (1 big)                       //pour voir si les big mènent la danse
#                                                             #-->10: (2 big)                       //pour voir si les big mènent la danse
#                                                             #-->11: (1 little, 1 big) to print    //pour voir si les littles mènent la danse
#                                                             #-->12: (2 little, 1 big)             //pour voir si les littles mènent la danse



number_of_cpus = ["6-0","0-2","6-2"]
workload =  [10.4, 12.6, 22.8]
cpu_battery = [176, 32, 197]


fig = plt.figure()
plt.bar(number_of_cpus,cpu_battery, width=0.4)
 
# Add title and axis names
plt.title('Energy consumed according to the configuration')
plt.xlabel('Number of CPUs')
plt.ylabel('Battery cpu usage')

plt.savefig("Google_pixel_energy_consumed_according_to_cpu.png")

plt.clf()
plt.cla()
plt.close()

#################################################

fig = plt.figure()
plt.bar(number_of_cpus,np.divide(workload,100000000000), width=0.4)

# Add title and axis names
plt.title('New computed Workload according to the number of CPUs')
plt.xlabel('Number of CPUs')
plt.ylabel(r'Workload ($\times 10E11$)')

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
plt.ylabel(r'Battery cpu/Workload ($\times 10E-11$)')

plt.savefig("Google_pixel_ratio_energy_by_workload_according_to_cpu.png")

plt.clf()
plt.cla()
plt.close()

################################################

############################################### temperature and frequencies for 6-0

ind = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
ind = np.divide(ind,2)

temperature = [30000.0, 30000.0, 30000.0, 30000.0, 30000.0, 30000.0, 30000.0, 30000.0, 30000.0, 30000.0, 30000.0, 30000.0, 30000.0, 30000.0, 30000.0, 30000.0, 30000.0, 30000.0, 30000.0, 30000.0]
cores_frequencies = [[1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0], 
          [1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0],
          [1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0],
          [1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0],
          [1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0],
          [1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0],
          [652800.0,652800.0,652800.0,652800.0,652800.0,652800.0,652800.0,652800.0,652800.0,652800.0,652800.0,652800.0,652800.0,652800.0,652800.0,652800.0,652800.0,652800.0,652800.0,652800.0],
          [806400.0,806400.0,806400.0,806400.0,806400.0,806400.0,806400.0,806400.0,806400.0,806400.0,806400.0,806400.0,806400.0,806400.0,806400.0,806400.0,806400.0,806400.0,806400.0,806400.0] ]



fig = plt.figure()
plt.bar(ind, np.divide(temperature,1000), width=0.4)
 
# Add title and axis names
plt.title('Cpu temperature')
plt.xlabel('time')
plt.ylabel('Temperature (celcius)')

plt.savefig("cpu_temperature_6-0.png")

plt.clf()
plt.cla()
plt.close()

#################################################

fig = plt.figure()

plt.plot(ind, cores_frequencies[0], label = "core 1")
plt.plot(ind, cores_frequencies[1], label = "core 2")
plt.plot(ind, cores_frequencies[2], label = "core 3")
plt.plot(ind, cores_frequencies[3], label = "core 4")
plt.plot(ind, cores_frequencies[4], label = "core 5")
plt.plot(ind, cores_frequencies[5], label = "core 6")
plt.plot(ind, cores_frequencies[6], label = "core 7")
plt.plot(ind, cores_frequencies[7], label = "core 8")
plt.legend()

# Add title and axis names
plt.title('Cpu frequency ')
plt.xlabel('time')
plt.ylabel("Frequency")

plt.savefig("cpu_frequencies_6-0.png")

plt.clf()
plt.cla()
plt.close()
#################################################


############################################### temperature and frequencies for 0-2

ind = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
ind = np.divide(ind,2)


temperature = [35000.0, 35000.0, 35000.0, 35000.0, 35000.0, 35000.0, 35000.0, 35000.0, 35000.0, 35000.0, 35000.0, 35000.0, 35000.0, 35000.0, 35000.0, 35000.0, 35000.0, 35000.0, 35000.0, 35000.0]
cores_frequencies = [[1363200.0,1363200.0,864000.0,576000.0,576000.0,576000.0,576000.0,576000.0,576000.0,576000.0,576000.0,576000.0,576000.0,576000.0,576000.0,576000.0,576000.0,576000.0,576000.0,576000.0],
        [1804800.0,1363200.0,576000.0,576000.0,576000.0,576000.0,576000.0,576000.0,576000.0,576000.0,576000.0,576000.0,576000.0,576000.0,576000.0,576000.0,576000.0,576000.0,576000.0,576000.0],
        [1804800.0,864000.0,576000.0,576000.0,576000.0,576000.0,576000.0,576000.0,576000.0,576000.0,576000.0,576000.0,1363200.0,576000.0,576000.0,1363200.0,576000.0,576000.0,576000.0,576000.0],
        [1804800.0,864000.0,576000.0,576000.0,576000.0,576000.0,576000.0,576000.0,576000.0,576000.0,576000.0,576000.0,576000.0,576000.0,576000.0,1363200.0,576000.0,576000.0,576000.0,576000.0],
        [1804800.0,576000.0,576000.0,576000.0,576000.0,576000.0,576000.0,576000.0,576000.0,576000.0,576000.0,576000.0,576000.0,576000.0,576000.0,576000.0,576000.0,576000.0,576000.0,576000.0],
        [864000.0,576000.0,576000.0,576000.0,576000.0,576000.0,576000.0,576000.0,864000.0,576000.0,576000.0,576000.0,864000.0,576000.0,576000.0,576000.0,576000.0,576000.0,576000.0,576000.0],
        [1900800.0,1900800.0,1900800.0,1900800.0,1728000.0,1728000.0,1728000.0,1728000.0,1728000.0,1728000.0,1728000.0,1728000.0,1728000.0,1728000.0,1728000.0,1728000.0,1728000.0,1728000.0,1728000.0,1728000.0],
        [2304000.0,2304000.0,2304000.0,2304000.0,2188800.0,1996800.0,1996800.0,1996800.0,1996800.0,1996800.0,1996800.0,1996800.0,1996800.0,1996800.0,1996800.0,1996800.0,1996800.0,1996800.0,1996800.0,1996800.0]]



fig = plt.figure()
plt.bar(ind, np.divide(temperature,1000), width=0.4)
 
# Add title and axis names
plt.title('Cpu temperature')
plt.xlabel('time')
plt.ylabel('Temperature (celcius)')

plt.savefig("cpu_temperature_0-2.png")

plt.clf()
plt.cla()
plt.close()

#################################################

fig = plt.figure()

plt.plot(ind, cores_frequencies[0], label = "core 1")
plt.plot(ind, cores_frequencies[1], label = "core 2")
plt.plot(ind, cores_frequencies[2], label = "core 3")
plt.plot(ind, cores_frequencies[3], label = "core 4")
plt.plot(ind, cores_frequencies[4], label = "core 5")
plt.plot(ind, cores_frequencies[5], label = "core 6")
plt.plot(ind, cores_frequencies[6], label = "core 7")
plt.plot(ind, cores_frequencies[7], label = "core 8")
plt.legend()

# Add title and axis names
plt.title('Cpu frequency ')
plt.xlabel('time')
plt.ylabel("Frequency")

plt.savefig("cpu_frequencies_0-2.png")

plt.clf()
plt.cla()
plt.close()
#################################################


############################################### temperature and frequencies for 6-2

ind = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
ind = np.divide(ind,2)


temperature = [27000.0, 27000.0, 27000.0, 27000.0, 27000.0, 27000.0, 27000.0, 27000.0, 27000.0, 27000.0, 27000.0, 27000.0, 27000.0, 27000.0, 27000.0, 27000.0, 27000.0, 27000.0, 27000.0]

cores_frequencies = [[1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1363200.0,1363200.0],
            [1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1363200.0,1363200.0],
            [1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1363200.0,1363200.0],
            [1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1363200.0,1363200.0],
            [1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1363200.0,1363200.0],
            [1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1804800.0,1363200.0,1363200.0],
            [2208000.0,2208000.0,2208000.0,1900800.0,1900800.0,1900800.0,1728000.0,1728000.0,1728000.0,1728000.0,1728000.0,1728000.0,1728000.0,1728000.0,1728000.0,1728000.0,1728000.0,1478400.0,1478400.0],
            [2400000.0,2400000.0,2400000.0,2304000.0,2304000.0,2304000.0,2188800.0,1996800.0,1996800.0,1996800.0,1996800.0,1996800.0,1996800.0,1996800.0,1996800.0,1996800.0,1996800.0,1766400.0,1766400.0]]




fig = plt.figure()
plt.bar(ind, np.divide(temperature,1000), width=0.4)
 
# Add title and axis names
plt.title('Cpu temperature')
plt.xlabel('time')
plt.ylabel('Temperature (celcius)')

plt.savefig("cpu_temperature_6-2.png")

plt.clf()
plt.cla()
plt.close()

#################################################

fig = plt.figure()

plt.plot(ind, cores_frequencies[0], label = "core 1")
plt.plot(ind, cores_frequencies[1], label = "core 2")
plt.plot(ind, cores_frequencies[2], label = "core 3")
plt.plot(ind, cores_frequencies[3], label = "core 4")
plt.plot(ind, cores_frequencies[4], label = "core 5")
plt.plot(ind, cores_frequencies[5], label = "core 6")
plt.plot(ind, cores_frequencies[6], label = "core 7")
plt.plot(ind, cores_frequencies[7], label = "core 8")
plt.legend()

# Add title and axis names
plt.title('Cpu frequency ')
plt.xlabel('time')
plt.ylabel("Frequency")

plt.savefig("cpu_frequencies_6-2.png")

plt.clf()
plt.cla()
plt.close()
#################################################
