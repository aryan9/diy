#!/bin/sh
number=0
while [ "$number" -lt 1 ]
do
        printf "\t%d" "$number"
	printf "\n"
        number=`expr $number + 1 `
	sudo iwlist wlxc4e98415edd0 scan | grep -A 5 B4:75:0E:BA:F7:0B | grep -B 3 "ESSID:\"[\\x0]*\"" | grep Signal | tail -c 10 >> readings.txt
done

