import subprocess as sp
import time

r = ""

#while("wlan0" not in r):
#	r = sp.check_output(["ifconfig"])

#r=""
while(True):
	try:	
		r = sp.check_output(["./is_inet_asignd.sh"])

	except	sp.CalledProcessError as e:
		if e.returncode > 1:
			raise

	if (r == ""):
		print "nothing yet"	
	else:
		print r.rstrip()
		break
	
	time.sleep(1)
#print r
