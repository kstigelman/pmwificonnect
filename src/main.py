#Luke Horst and Kyler Stigelman

import os
import string

command = os.popen("ping -c 1 homepage.pennmanor.net").readlines()
ping_line = command[5]

index = ping_line.rfind("/", 0, ping_line.rfind("/") - 1)
ping = ping_line[index+1:ping_line.rfind("/")]

if float(ping) > 250:
    print("Connection error!")
else:
    print('Ok')

print(ping)

