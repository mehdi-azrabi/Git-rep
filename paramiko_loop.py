import paramiko
import time
from getpass import getpass

ip = "192.168.100.251"
username = "admin"
password = input("Enter your password: ")


SESSION = paramiko.SSHClient()
SESSION.set_missing_host_key_policy(paramiko.AutoAddPolicy())
SESSION.connect(ip,port=22,
                username=username,
                password=password,
                look_for_keys=False,
                allow_agent=False)

DEVICE_ACCESS = SESSION.invoke_shell()
DEVICE_ACCESS.send(b'config t\n')
for i in range(1, 10):
    DEVICE_ACCESS.send('int lo ' +str(i) + '\n')
    DEVICE_ACCESS.send('ip address 1.1.1.'+str(i) +' 255.255.255.255\n')
 

time.sleep(3)

DEVICE_ACCESS.send(b'do show ip int bri\n \n \n')
time.sleep(3)
output = DEVICE_ACCESS.recv(65000)
print (output.decode('ascii'))
SESSION.close

#a little changes

