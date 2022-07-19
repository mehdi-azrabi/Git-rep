import paramiko
import time
from getpass import getpass

ip = input('Enter IP: ')
username = input('Enter username: ')
password = input('Enter password: ')

SESSION = paramiko.SSHClient()
SESSION.set_missing_host_key_policy(paramiko.AutoAddPolicy())
SESSION.connect(ip,port=22,
                username=username,
                password=password,
                look_for_keys=False,
                allow_agent=False)

DEVICE_ACCESS = SESSION.invoke_shell()
DEVICE_ACCESS.send(b'term length 0\n')
#DEVICE_ACCESS.send(b'end\n')
#DEVICE_ACCESS.send(b'config vdom\n')
#DEVICE_ACCESS.send(b'edi root\n')
#DEVICE_ACCESS.send(b'get router info rout all\n')
DEVICE_ACCESS.send(b'show ip int bri\n')
time.sleep(2)
output = DEVICE_ACCESS.recv(65000)
print (output.decode('ascii'))
SESSION.close

#changes from Github
