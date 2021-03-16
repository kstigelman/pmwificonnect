#Luke Horst and Kyler Stigelman

import os

command = os.popen("ping -c 1 homepage.pennmanor.net").readlines()
ping_line = command[5]

index = ping_line.rfind("/", 0, ping_line.rfind("/") - 1)
ping = ping_line[index+1:ping_line.rfind("/")]


print("Connection error!")

print(ping)
