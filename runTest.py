import subprocess as sp
import socket

#r = sp.call(["./test.sh"],shell=True)

#print r


TCP_IP = '192.168.1.146'
TCP_PORT = 5005
BUFFER_SIZE = 20  # Normally 1024, but we want fast response

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()
print 'Connection address:', addr
while 1:
    data = conn.recv(BUFFER_SIZE)
    if not data: break
    print "received data:", data
    if(data[:2] == "do"):
    	print "executing instructions!"
    	r = sp.call(["./test.sh"],shell=True)
    	#print r
    	conn.send(str(r) + " done\n")  # echo
    conn.send("normal echo\n")
conn.close()