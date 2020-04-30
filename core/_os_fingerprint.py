import os
import sys

def _os_scan(ip):
    string = "ping -c 1 "+ip+" | grep -P -o ttl=[0-9]\{1,3}"
    scan = os.system(string)
    print(scan)

_os_scan("127.0.0.1")