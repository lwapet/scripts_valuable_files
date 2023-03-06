#!/bin/bash
adb root

adb shell  "echo \"-----installing app"

adb uninstall com.opportunistask.scheduling.interactive_benchmarking_app_to_test_big_cores  

adb install /home/patrick/opportunistic_tasks_android/Experiments_of_task_on_CPUs/interactive_benchmarking_app_to_test_big_cores/app/debug/app-debug.apk

adb shell pm grant com.opportunistask.scheduling.interactive_benchmarking_app_to_test_big_cores android.permission.DUMP   
adb shell pm grant com.opportunistask.scheduling.interactive_benchmarking_app_to_test_big_cores android.permission.PACKAGE_USAGE_STATS  
  
sleep 3

adb shell  "echo \"-----starting the app\"
        sleep 1
        am start -n com.opportunistask.scheduling.interactive_benchmarking_app_to_test_big_cores/com.opportunistask.scheduling.interactive_benchmarking_app_to_test_big_cores.MainActivity"
        sleep 1
APP_PID=$(adb shell "ps -A | grep com.opportunistask.scheduling.interactive_benchmarking_app_to_test_big_cores" | awk '{ print $2 }')
echo "----- app_pid =  $APP_PID " 


