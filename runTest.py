import subprocess as sp
import socket
import time

#r = sp.call(["./test.sh"],shell=True)

#print r

while (True):
	
	r = sp.check_output(["/home/debian/dev/diy/is_inet_asignd.sh"])
	r=""
	c=0
	while(True):
        	try:
                	r = sp.check_output(["/home/debian/dev/diy/get_inet_addr.sh"])

	        except  sp.CalledProcessError as e:
        	        if e.returncode > 1:
                	        raise

	        if (r != ""):
      			break

	        time.sleep(1)

	TCP_IP = r.rstrip()
	TCP_PORT = 5006
	BUFFER_SIZE = 20  # Normally 1024, but we want fast response

	#r = sp.check_output()
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	s.bind((TCP_IP, TCP_PORT))
	s.listen(1)

	conn, addr = s.accept()
	print 'Connection address:', addr

	br=0
	while (br==0):
	    data = conn.recv(BUFFER_SIZE)
	    if not data: break
	    print "received data:", data
	    #print data[:len(data)-2]
	    if(data[:len(data)-1].isdigit() == True):
		c+=1
	#    	print "executing instructions!"
	#    	r = sp.call(["/home/debian/dev/diy/test.sh " + data[:len(data)-1]],shell=True)
	    	#print r
	    	conn.send(str(c) + " done\n")  # echo
		conn.close()
		print "executing instructions!"
	        r = sp.call(["/home/debian/dev/diy/test.sh " + data[:len(data)-1]],shell=True)
	    else:
		conn.send("normal echo\n")
		conn.close()
	    br=1
	#conn.close()
	s.close()
	r = sp.call(["/home/debian/dev/diy/reset_wifi.sh"],shell=True)
