#! python3 
import socket                   

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a socket object (s.SOCK_STREAM = TCP, s.SOCK_DGRAM = UDP)

# ======================================
# CHANGE THIS IP ADDRESS TO THE SERVER IP
host = "192.168.8.110"   # local server IP
port = 3000           
# CHANGE THIS IP ADDRESS TO THE SERVER IP
# ======================================

s.bind((host, port))            # Bind to the port
s.listen(5)                     # Now wait for client connection.

print('Server listening...')

while True:
    conn, addr = s.accept()     # Establish connection with client.
    print('Got connection from', addr)
    data = conn.recv(1024)
    print('Server received', repr(data.decode()))
    filename='data.dat' #In the same folder or path is this file running must the file you want to tranfser to be
    f = open(filename,'rb')
    l = f.read(1024)
    while (l):
        conn.send(l)
        # print('Sent ',repr(l))
        l = f.read(1024)
    f.close()
    print('Done sending')
    conn.send('Thank you for connecting'.encode())
    conn.close()