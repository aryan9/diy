#! /bin/sh

ret=
c=0
while [ -z "$ret" ]
do
	#echo Inside
	ret=`ifconfig | grep wlan0`
	c=`expr $c + 1 `
done
#echo $c

# Connect to AP
ret=1
while [ "$ret" -eq 1 ]
do
	ret=`/home/debian/dev/diy/cman.sh 1 | grep ret | grep -P "\d+" -o`
done
