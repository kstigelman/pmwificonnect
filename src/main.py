# Luke Horst and Kyler Stigelman

import os
import time
from datetime import datetime


def ask():
    a = os.system('zenity --question --title="Connection Test" --text="Would you like to run the internet test?"')
    if a == 0:
        os.system('zenity --info --text="Testing..."')

        def test():
            disconnects = []
            global ping
            command = os.popen("ping -c 1 homepage.pennmanor.net").readlines()
            if not command:
                os.system('zenity --error --text="There is no connection!"')
                os.popen("sudo tee /etc/modprobe.d/hp.conf && sudo rfkill unblock all")
                os.popen("sudo ip link set wlp4s0 up")

                # Need a command to reconnect to internet
                disconnects.append(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
                time.sleep(10)
                test()
            else:
                ping_line = command[5]
                index = ping_line.rfind("/", 0, ping_line.rfind("/") - 1)
                ping = ping_line[index + 1:ping_line.rfind("/")]

            if float(ping) > 150:
                os.system('zenity --error --title="Connection Error" --text="Ping is too high!"')
                os.popen("sudo service network-manager restart")

                disconnects.append(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
            else:
                os.system('zenity --info --text="Connection ok"')

            time.sleep(10)
            test()

            b = os.system('zenity --question --title="Disconnected" --text="Would you like to reconnect?"')
            if b == 0:
                os.system('zenity --info --text="Reconnecting..."')
            elif b == 1:
                os.system('zenity --info --text="Ok. Closing..."')
        # root.mainloop()
        # print(test())

    elif a == 1:
        os.system('zenity --info --text="You may now close the window."')


ask()
