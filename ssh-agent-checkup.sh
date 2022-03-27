#!/usr/bin/bash
# author : Pedro Gonzalez (dopelDev)
# script para i3blocks
# github : https://github.com/dopelDev
# email : 322kuroneko@gmail.com

check_it=$(ssh-add -l)

verify=$(echo $check_it | cut -d' ' -f3) 


if [[ $check_it = "322kuroneko@gmail.com" ]];then
	echo "  322kuroneko@gmail.com"
elif [[ $check_it = "The agent has no identities." ]];then
	echo " incognito"
else
	echo "  $verify"
fi
