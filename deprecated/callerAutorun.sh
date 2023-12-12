#1/usr/bin/bash

# script para agregar un autorun al bashrc 

# Vars
CHECKER="/home/dopel/tmp/autorun-checker"
LOG="/home/dopel/tmp/autorun.log"

uptimeMinute=$(uptime | cut -d " " -f5)
uptimeNumver=$(uptime | cut -d " " -f4)

# checking script log
if [ ! -e $LOG  ];then
	touch $LOG;
fi

# verificando que Minute no esta vacio
if [ -z $uptimeMinute ];then
	exit 0
fi

# caller autorum script
if [ $uptimeMinute == "min," ];then
	if [ $uptimeNumver == "0" ] && [ ! -e $CHECKER ];then
		touch $CHECKER;
		autorun.sh;
		echo "Run script- $(date)" >> $LOG;
	else
		if [ -e $CHECKER ];then
			if [ ! $uptimeNumver == "0" ];then
				rm $CHECKER
			fi
		fi
		echo "Not run script- $(date)" >> $LOG;
	fi
fi
