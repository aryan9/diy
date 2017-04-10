#! /bin/sh

ret=
while [ -z "$ret" ]
do
        ret=`ifconfig wlan0 | grep "inet addr" | grep -P "(\d+\.)+\d+" -o | grep -m1 ""`
done
echo $ret
