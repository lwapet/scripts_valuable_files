adb shell "am start -n com.opportunistask.scheduling.benchmarking_app_to_test_big_cores/com.opportunistask.scheduling.benchmarking_app_to_test_big_cores.MainActivity"
sleep 3
APP_PID=$(adb shell "ps -A | grep com.opportunistask.scheduling.benchmarking_app_to_test_big_cores" | awk '{ print $2 }')
 echo $APP_PID
