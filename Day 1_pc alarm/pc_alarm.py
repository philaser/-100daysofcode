import os
import platform
import psutil
from win10toast import ToastNotifier


operating_system = platform.system()

wintoast = ToastNotifier()


def main():

    BATTERY_ALARM = False
    CPU_ALARM = False
    POWER_ALARM = False


    battery = psutil.sensors_battery()
    cpu_percentage = psutil.cpu_percent(interval=1)


    if operating_system == 'Windows':

        if battery.percent < 20:
            BATTERY_ALARM = True

        if cpu_percentage > 80:
            CPU_ALARM = True

        if battery.power_plugged == False:
            POWER_ALARM = True

        alert = buildAlert(BATTERY_ALARM, CPU_ALARM, POWER_ALARM)
        
        print(alert)
        wintoast.show_toast('PC STATUS ALARM',alert, duration=10)
        
    else:

        print("Sorry, your Operating system isnt supported yet")
    #  


def buildAlert(BAT, CPU, POW):
    alert = ''

    if BAT == True:
        alert = alert + 'Battery level is below 20%\n'
    
    if CPU == True:
        alert = alert + 'CPU usage above 80%\n'

    if POW == True:
        alert = alert + 'Power is unplugged\n'
    return alert


if __name__ == '__main__':
    main()