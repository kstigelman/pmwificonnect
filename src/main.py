#Luke Horst and Kyler Stigelman

#repeat the ping command for every iteration of the program that is run
import os
import time
from datetime import datetime

from tkinter import *
import tkinter.messagebox

def test():
    command = os.popen("ping -c 1 homepage.pennmanor.net").readlines()
    if not command:
        print("There is no connection!")
        os.popen("sudo tee /etc/modprobe.d/hp.conf && sudo rfkill unblock all")
        os.popen("sudo ip link set wlp4s0 up")

        # Need a command to reconnect to internet
        disconnects.append(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        time.sleep(10)
        test()
    else:
        ping_line = command[5]
        index = ping_line.rfind("/", 0, ping_line.rfind("/") - 1)
        ping = ping_line[index+1:ping_line.rfind("/")]

        if float(ping) > 150:
            print("Connection error: Ping is too high!")
            os.popen("sudo service network-manager restart")

            disconnects.append(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))

            time.sleep(10)
            test()

        else:
            return "Connection ok"


disconnects = []
root=Tk()

answer = tkinter.messagebox.askquestion('Wi-Fi Connector','You are disconnected from the Wi-Fi. Reconnect?')
if answer == 'yes':
    #do this
else:
    #do this

#root.mainloop()
#print(test())
