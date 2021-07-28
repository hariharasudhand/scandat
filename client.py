import bluetooth

bd_addr = "9C:F5:31:6B:6D:06"

port = 2

sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
sock.connect((bd_addr, port))

sock.send("hello!!")

sock.close()