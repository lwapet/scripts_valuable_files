#!/bin/bash


#APK_PATH__WINDOWS_SYNTAX="C:\Users\lavoi\opportunist_task_on_android\benchmarking_app_to_test_big_cores\app\debug\app-debug.apk"
 APK_PATH__WINDOWS_SYNTAX="C:\Users\lavoi\opportunist_task_on_android\git_repositories\app_to_drain_battery.apk"
adb='/mnt/c/Program Files/Android/platform-tools_r33.0.1-windows/platform-tools/adb.exe'

ls "$adb"

"${adb}" root

"$adb" shell  "echo \"-----installing app"


"$adb" uninstall com.opportunistask.scheduling.benchmarking_app_to_test_big_cores  


echo "---- before installing!!"
#"$adb" install /mnt/c/Users/lavoi/opportunist_task_on_android/benchmarking_app_to_test_big_cores/app/debug/app-debug.apk
"$adb" install "$APK_PATH__WINDOWS_SYNTAX"
echo "------ after installation"

"$adb" shell pm grant com.opportunistask.scheduling.benchmarking_app_to_test_big_cores android.permission.DUMP   
"$adb" shell pm grant com.opportunistask.scheduling.benchmarking_app_to_test_big_cores android.permission.PACKAGE_USAGE_STATS  
  
sleep 3

"$adb" shell  "echo \"-----starting the app\"
        sleep 1
        am start -n com.opportunistask.scheduling.benchmarking_app_to_test_big_cores/com.opportunistask.scheduling.benchmarking_app_to_test_big_cores.MainActivity"
        sleep 1
APP_PID=$("$adb" shell "ps -A | grep com.opportunistask.scheduling.benchmarking_app_to_test_big_cores" | awk '{ print $2 }')
echo "----- app_pid =  $APP_PID " 


