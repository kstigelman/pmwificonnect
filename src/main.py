# Luke Horst and Kyler Stigelman

import os
import time
from datetime import datetime

# UI for users to input whether they want to run the test or not.
def ask(question):
    a = input(question)

    if a == 'Y' or a == 'y' or a == 'Yes' or a == 'yes':
        print('Testing...')
        return True
    elif a == 'N' or a == 'n' or a == 'No' or a == 'no':
        print('Goodbye!')
        return False
    else:
        ask("Invalid input! Please type 'y' for yes and 'n' for no")

def reconnect():
    if ask('You are disconnected from the Wi-Fi. Reconnect?'):
        os.popen("nmcli radio wifi off")
        time.sleep(1)
        os.popen("nmcli radio wifi on")
        disconnects.append(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        time.sleep(10)
def test():
    command = os.popen("ping -c 1 homepage.pennmanor.net").readlines()

    if not command:
        reconnect()

    else:
        print("Connection is fine")
        time.sleep(60)
        #ping_line = command[5]
        #index = ping_line.rfind("/", 0, ping_line.rfind("/") - 1)
        #ping = ping_line[index + 1:ping_line.rfind("/")]
        ping = 100

        if float(ping) > 150:
            reconnect()

    test()


disconnects = []
if ask("Would you like to run the internet test? Y/N "):
    test()
