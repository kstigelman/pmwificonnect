#Luke Horst and Kyler Stigelman

#repeat the ping command for every iteration of the program that is run
import os

def test():
    command = os.popen("ping -c 1 homepage.pennmanor.net").readlines()
    ping_line = command[5]

    index = ping_line.rfind("/", 0, ping_line.rfind("/") - 1)
    ping = ping_line[index+1:ping_line.rfind("/")]

    if float(ping) > 150:
        return("Connection error! Ping is", ping)
        os.popen("sudo service network-manager restart")
        test()
    else:
        return("Connection ok")
print(test())
