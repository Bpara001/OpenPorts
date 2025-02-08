import os
import sys
import socket
import time
from datetime import datetime

# Grab HostName and IP Address to Display
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
print("Your Computer Name is:" + hostname)
print("Your Computer IP Address is:" + IPAddr)

#IFCONFIG Optional Setting
ifconfigDisplay = input("Would You like your ifconfig settings displayed? Y/N: ")
if(ifconfigDisplay.casefold() == 'Y'.casefold()):
    print("Here is your ifconfig current settings:")
    print("-" * 50)
    print(os.system('ipconfig'))



# OPEN/CLOSED Port on local server(hostname) logic
server = socket.gethostbyname(hostname)
print("-" * 50)
print("Scanning Target: " + server)
print("Scanning started at:" + str(datetime.now()))
print("-" * 50)

try:
    # Scan ports from range selected below
    start = time.time()
    for port in range(1, 999):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)

        # 0: Open Port
        result = s.connect_ex((server, port))
        if result == 0:
            print("Port {} is open".format(port))
        s.close()

except socket.gaierror:
    print("Hostname not found")
    sys.exit()
except socket.error:
    print("Unable to connect with the socket-server")
    sys.exit()

#Print how long program took
end = str(datetime.now())
end = time.time()
hours, rem = divmod(end-start, 3600)
minutes, seconds = divmod(rem, 60)
print("Total Length of Scan: Days:{:0>2}:Minutes:{:0>2}:Seconds:{:05.2f}".format(int(hours),int(minutes),seconds))