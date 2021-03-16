#Luke Horst and Kyler Stigelman

#repeat the ping command for every iteration of the program that is run
import os

command = os.popen("ping -c 1 homepage.pennmanor.net").readlines()
ping_line = command[5]

index = ping_line.rfind("/", 0, ping_line.rfind("/") - 1)
ping = ping_line[index+1:ping_line.rfind("/")]

#if the ping is too high, have a system that changes the network/connections
if float(ping) > 150:
    print("Connection error!")
else:
    print("Connection ok")

print(ping)
