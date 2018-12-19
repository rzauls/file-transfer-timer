#! python3 
import socket, time, os
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create a socket object (s.SOCK_STREAM = TCP, s.SOCK_DGRAM = UDP)

# ======================================
# CHANGE THIS IP ADRESS TO THE SERVER IP
host = "192.168.8.110"  # destination IP
port = 3000           
# CHANGE THIS IP ADRESS TO THE SERVER IP
# ======================================

s.connect((host, port))
msg = "Hello server!"
s.send(msg.encode())
count = 0
startTime = time.time()
with open('received_file.dat', 'wb') as f:
    print('file opened')
    while True:
        print('receiving data'+ count*".")
        data = s.recv(1024)
        # print('data=%s', (data))
        if not data:
            break
        # write data to a file
        f.write(data)
        count+=1
        if (count>5):
            count=0

f.close()
totalTime = round(time.time() - startTime, 5)
print('Successfully get the file in %s seconds' % totalTime)
size = int(os.path.getsize('received_file.dat'))/1000
print("File size: %s kB" % size)
speed = size / totalTime
print("Average transfer speed: %s kB/s" % round(speed, 2))
print()
s.close()
print('connection closed')