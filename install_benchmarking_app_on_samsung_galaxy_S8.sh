#!/bin/bash


 APK_PATH__WINDOWS_SYNTAX="C:\Users\lavoi\opportunist_task_on_android\git_repositories\benchmarking_app_to_test_big_cores\app\debug\app-debug.apk"
adb='/mnt/c/Program Files/Android/platform-tools_r33.0.1-windows/platform-tools/adb.exe'

ls "$adb"

"$adb" shell  "echo \"-----installing app"

"$adb" uninstall com.opportunistask.scheduling.benchmarking_app_to_test_big_cores  

"$adb" install $APK_PATH__WINDOWS_SYNTAX


"$adb" shell "su -c pm grant com.opportunistask.scheduling.benchmarking_app_to_test_big_cores android.permission.DUMP"   
"$adb" shell "su -c pm grant com.opportunistask.scheduling.benchmarking_app_to_test_big_cores android.permission.PACKAGE_USAGE_STATS"  
"$adb" shell "su -c pm grant com.opportunistask.scheduling.benchmarking_app_to_test_big_cores android.permission.READ_EXTERNAL_STORAGE" 
"$adb" shell "su -c pm grant com.opportunistask.scheduling.benchmarking_app_to_test_big_cores android.permission.WRITE_EXTERNAL_STORAGE" 

  


"$adb" shell  " echo \"-----starting the app\";
        sleep 5;
        am start -n com.opportunistask.scheduling.benchmarking_app_to_test_big_cores/com.opportunistask.scheduling.benchmarking_app_to_test_big_cores.MainActivity"
        sleep 3
APP_PID=$("$adb" shell "ps | grep com.opportunistask.scheduling.benchmarking_app_to_test_big_cores" | awk '{ print $2 }')
echo "----- app_pid =  $APP_PID " 

#adb shell "am start -n com.opportunistask.scheduling.benchmarking_app_to_test_big_cores/com.opportunistask.scheduling.benchmarking_app_to_test_big_cores.MainActivity"
#APP_PID=$(adb shell "ps | grep com.opportunistask.scheduling.benchmarking_app_to_test_big_cores" | awk '{ print $2 }') ; echo "----- app_pid =  $APP_PID " 
