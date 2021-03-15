#Luke Horst and Kyler Stigelman

import os
import string

ping = os.popen("ping -c 1 homepage.pennmanor.net").readlines()
print(ping)
