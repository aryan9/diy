#! /bin/sh

connmanctl scan wifi
ret=`connmanctl services | grep Sachin | grep -P "wifi.*" -o`
val=0
if [ -z "$ret" ]
then
	val=1
else

	if [ $1 -eq 1 ]
	then
	       	connmanctl connect $ret
	else
	       	connmanctl disconnect $ret
	fi
fi
echo "ret ${val}"
