# Luke Horst and Kyler Stigelman

import os
import time
from datetime import datetime

def reconnect():
    #os.system('zenity --error --text="There is no connection!"')

    b = os.system('zenity --question --title="Disconnected" --text="Would you like to reconnect?"')
    if b == 0:
        os.system('zenity --info --text="Reconnecting..."')
    elif b == 1:
        os.system('zenity --info --text="Ok. Closing..."')

    os.popen("nmcli radio wifi off")
    time.sleep(1)
    os.popen("nmcli radio wifi on")

    disconnects.append(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
    time.sleep()

def ask():
    a = os.system('zenity --question --title="Connection Test" --text="Would you like to run the internet test?"')
    if a == 0:
        os.system('zenity --info --text="Testing..."')

        def test():
            global ping
            command = os.popen("ping -c 1 homepage.pennmanor.net").readlines()

            if not command:
                reconnect()
            else:
                os.system('zenity --info --text="Connection ok"')

            time.sleep(10)
            test()




    elif a == 1:
        os.system('zenity --info --text="You may now close the window."')

disconnects = []
ask()
