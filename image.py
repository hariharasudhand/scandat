from socket import *

port = 8888
s = socket(AF_INET, SOCK_STREAM)
s.bind(('', port))
s.listen(1) #listens to 1 connection
conn, addr = s.accept()
print("Connected by the ",addr)

with open('image.jpg', 'wb') as file:
    while True:
        data = conn.recv(1024)
        if not data: break
        file.write(data)


conn.close()