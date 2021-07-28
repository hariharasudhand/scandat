import socket,os
import time

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("192.168.43.1", 57961))

dst="E:\\Kiosk\\"

while True:

 fln = client_socket.recv(4)
os.chdir(dst);
dst = "G:\\labelimg\\"+fln+"\\"
if not os.path.exists(dst): os.makedirs(dst)
fname = client_socket.recv(4)
os.chdir(dst)
fname = fname+'.jpg'
fp = open(fname,'wb')
# image
while True:
    strng = client_socket.recv(1024)
    if not strng:
        break
    fp.write(strng)
fp.close()
print ("Data Received successfully")
exit()