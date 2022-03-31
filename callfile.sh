#!/usr/bin/bash

declare -a array;

echo "$(ls $1)" > /tmp/testing.txt

mapfile -t array < /tmp/testing.txt

for (( i=0; i<=${#array[@]}; i++ )); do
	echo "  $1/${array[$i]} "
done
