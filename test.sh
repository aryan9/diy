#!/bin/bash

number=0
zero=0
sav=$1
substring="busy"
str1="I am busy"
proceed=0
#printf "%d" "$1"

sleep 2
while [ "$number" -lt 10 ]
do
#        printf "\t%d" "$number"
#	printf "\n"
#        number=`expr $number + 1`
	str=`iwlist wlan0 scan | grep -B 3 cc3200`
	#echo $str >>  /home/debian/dev/diy/check.txt
	#[ "$str" =~ "$substring" ] && proceed=1
	if [[ -z "$str" ]] #=~ $substring ]]
	then
		#echo Nothing
		echo "`date` : Nothing" >>  /home/debian/dev/diy/check.txt
		sleep 2
	else
		echo "`date` : ${str}" >>  /home/debian/dev/diy/check.txt
		#echo Something
		number=`expr $number + 1`
		str=`echo $str | grep Signal | grep -P '(-?)\d+\s+(dBm)' -o | grep -P "(-?)\d+" -o` #>> readings.txt
	#	iwconfig wlan0 | grep Signal | tail -c 9 >> readings.txt
	#	str=`iwconfig wlan0 | grep Signal | grep -P '(-)\d+' -o`
		sav="${sav},${str}"
		sleep 1
	fi
done

echo $sav >> /home/debian/dev/diy/readings.txt

