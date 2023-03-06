#!/bin/bash
adb root
adb shell "echo -----\"making best_effort_fl_removed task group directory\"
        sleep 1
        cd /sys/fs/cgroup/cpu
        mkdir best_effort_fl_removed"

sleep 3
# NOTE: the cpu subsystem is designed to handle some personnalizabel behaviors in the scheduler. 
#  it is already defined in the linux code and its corresponding root folder exist in the userspace.
# This folder contains parameter files of other filesystems automatically created at system startup 
# its then contains a cgroup hierarchy wich its the parent folder
# we just create another folder in that herarchy associated whith the Mengh Zhu folder.
# We also modified the systems handler associated to the cpu subsystem, to handle the creation of this cgroup,
# and set the task group id that will be used by the scheduler. 
        
APP_PID=$(adb shell "ps -A | grep com.opportunistask.scheduling.benchmarking_app_to_test_big_cores" | awk '{ print $2 }')
echo "----- removing  task_pid =  $APP_PID from best effort group " 

adb shell "sleep 1
        echo $APP_PID > /sys/fs/cgroup/cpu/best_effort_fl_removed/tasks
        echo \"-----task with pid =  $APP_PID , was removed from best effort group,  \"
	 echo \"best_effort_fl file :    \"
        cat /sys/fs/cgroup/cpu/best_effort_fl/tasks 
        echo \"best_effort_fl_removed file :    \"
        cat /sys/fs/cgroup/cpu/best_effort_fl_removed/tasks "
       

