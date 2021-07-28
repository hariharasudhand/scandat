import socket

s = socket.socket()
host = socket.gethostname()
port = 8080
s.bind((host,port))
print(host)
s.listen(1)
print("waiting for any incoming connections...")
Conn, addr = s.accept()
print(addr, "has connected to server")

filename = input(str("please enter the filename of the file:"))
file = open(filename, 'rb')
file_data = file.read(1024)
Conn.send(file_data)
print("data has been transmitted successfully")