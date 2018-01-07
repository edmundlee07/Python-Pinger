"""Python script contracted by Spencer McDonald to ping multiple devices 
   Reads from text file in same directory 
   make sure each new ip address is on a new line
"""

import subprocess
import os

print "Hello, welcome to Python Pinger"

#repalce "address.txt" with whatever textfile has all your IPs
#MAKE SURE EACH ADDRESS IS ONE A NEW LINE 

addressList = []
with open("address.txt") as f:
    addressList = f.readlines()
addressList = [line.rstrip('\n') for line in open("address.txt")]

number = len(addressList)

with open(os.devnull, "wb") as limbo:
        for n in range(0, number):
                ip = addressList[n]
                result=subprocess.Popen(["ping", "-n", "1", "-w", "200", ip],
                        stdout=limbo, stderr=limbo).wait()
                if result:
                        print ip, ":Inactive"
                else:
                        print ip, ":Active"

pause = raw_input("Press enter to exit")


    