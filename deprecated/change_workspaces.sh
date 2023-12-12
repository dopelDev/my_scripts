#!/usr/bin/bash

currentFile='/home/dopel/.config/leftwm/config.toml'
workSpaces1='/home/dopel/left-themes/config/ws1.toml'
workSpaces2='/home/dopel/left-themes/config/ws2.toml'
workSpaces3='/home/dopel/left-themes/config/ws3.toml'
backUP='/home/dopel/.config/leftwm/config.backUP'

if [ -z $1 ]; then
	echo 'no hay argumento';
	exit 0;
fi

if [ -e $backUP ]; then
		rm $backUP;
fi

cp $currentFile $backUP;

if [ $1 = 'wk1' ]; then
	echo 'argumento wk1';
	rm $currentFile;
	cp $workSpaces1 $currentFile;
	exit 0;
elif [ $1 = 'wk2' ]; then
	echo 'argumento wk2';
	rm $currentFile;
	cp $workSpaces2 $currentFile;
	exit 0;
elif [ $1 = 'wk3' ]; then
	echo 'argumento wk3';
	rm $currentFile;
	cp $workSpaces3 $currentFile;
	exit 0;
fi
echo 'el argumento no es valido'
	

