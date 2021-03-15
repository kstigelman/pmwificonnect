#Luke Horst and Kyler Stigelman

import os
import string

command = os.popen("ping -c 1 homepage.pennmanor.net").readlines()
ping_line = command[5]
