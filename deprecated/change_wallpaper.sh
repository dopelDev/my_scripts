#!/usr/bin/bash
cp ~/.config/leftwm/themes/current/background.jpg ~/tmp/wallpeper$(date -I).jpg;
if [ -e ~/tmp/wallpeper$(date -I).jpg ]; then
	rm ~/.config/leftwm/themes/current/background.jpg;
	cp $1 ~/.config/leftwm/themes/current/background.jpg;
	echo "wallpeper changed";
else
	echo "change failed";
fi
