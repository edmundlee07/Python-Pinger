
"""Python script contracted by Spencer McDonald to ping multiple devices 
"""
import subprocess
import os
with open(os.devnull, "wb") as limbo:
        for n in xrange(1, 254):
                ip="172.16.232.{0}".format(n)
                result=subprocess.Popen(["ping", "-n", "1", "-w", "200", ip],
                        stdout=limbo, stderr=limbo).wait()
                if result:
                        print ip, "inactive"
                else:
                        print ip, "active"