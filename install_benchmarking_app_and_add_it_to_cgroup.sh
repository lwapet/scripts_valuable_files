#!/bin/bash
adb root

adb shell  "echo \"-----installing app"

adb uninstall com.opportunistask.scheduling.benchmarking_app_to_test_big_cores  

adb install /home/patrick/opportunistic_tasks_android/from_collegue/benchmarking_app_to_test_big_cores/app/debug/app-debug.apk

adb shell pm grant com.opportunistask.scheduling.benchmarking_app_to_test_big_cores android.permission.DUMP   
adb shell pm grant com.opportunistask.scheduling.benchmarking_app_to_test_big_cores android.permission.PACKAGE_USAGE_STATS  
  
sleep 3

adb shell  "echo \"-----starting the app\"
        sleep 1
        am start -n com.opportunistask.scheduling.benchmarking_app_to_test_big_cores/com.opportunistask.scheduling.benchmarking_app_to_test_big_cores.MainActivity"
        
APP_PID=$(adb shell "ps -A | grep com.opportunistask.scheduling.benchmarking_app_to_test_big_cores" | awk '{ print $2 }')
echo "----- app_pid =  $APP_PID " 



adb shell "echo -----\"making best_effort_fl task group directory\"
        sleep 1
        mkdir /sys/fs/cgroup/cpu 
        mount -t cgroup -ocpu none /sys/fs/cgroup/cpu
        cd /sys/fs/cgroup/cpu
        mkdir best_effort_fl"
echo "----- adding task_pid =  $APP_PID to best effort group " 

adb shell "sleep 1
        echo $APP_PID > /sys/fs/cgroup/cpu/best_effort_fl/tasks
        echo \"-----task with pid =  $APP_PID , was added to best effort group,  \" 
        cat /sys/fs/cgroup/cpu/best_effort_fl/tasks "
        
       

