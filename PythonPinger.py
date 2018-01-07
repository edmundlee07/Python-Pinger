"""Python script contracted by Spencer McDonald to ping multiple devices 
   Reads from text file in same directory 
   make sure each new ip address is on a new line
"""

import subprocess
import os

print "Hello, welcome to your python pinger"

#repalce "address.txt" with whatever textfile has all your IPs
file = open("address.txt", "r")

addressList = []
for line in file:
    addressList.append(line)

number = len(addressList)

for i in range (0,number):
    hostname = addressList[i]

    response = os.system("ping -n 4 " + hostname)
    if response == 0:
        pingstatus = hostname + ": Network Active"
    else:
        pingstatus = hostname + ": Network Error"
    print pingstatus

pause = raw_input("Press enter to exit")

file.close()
    