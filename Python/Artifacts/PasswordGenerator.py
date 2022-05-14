import random
import socket
import os
s="abcdefghijkl\
   mnoqrstuvwxyz1234\
   567890ABCDEFGHIJKLM\
   NOPQRSTUVWXYZ!@$%^&*\
   ()_-+[];/';.,"
passwordlen=16
#Random Password generator
print("#1")
password1="".join(random.sample(s,passwordlen))
print(password1)
print("#2")
password2="".join(random.sample(s,passwordlen))
print(password2)

#Get IP Address
hostname=socket.gethostname()
ip_address=socket.gethostbyname(hostname)
print(f"Hostname: {hostname}")
print(f"IP Address: {ip_address}")


#Check Internet Speed
os.system('cmd /k "ping localhost')
