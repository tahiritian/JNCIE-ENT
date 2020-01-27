import subprocess
import os

with open('prod-ips.txt', 'r') as f:
        for ip in f:
            result=subprocess.Popen(["ping", "-c", "1", "-n", "-W", "2",    ip],stdout=f, stderr=f).wait()
            if result:
                print(ip, "inactive")
            else:
                print(ip, "active")

