#!/usr/bin/bash
# func de marco
function marco() {
  for (( i = 0; i < 48; i++ )); do
    if [ $i -lt 47 ];then
      echo -n '#'
    else
      echo '#'
    fi
  done
}
marco
echo "#       __                 ______
#  ____/ /___  ____  ___  / / __ \___ _   __
# / __  / __ \/ __ \/ _ \/ / / / / _ \ | / /
#/ /_/ / /_/ / /_/ /  __/ / /_/ /  __/ |/ /
#\__,_/\____/ .___/\___/_/_____/\___/|___/
#          /_/
#"
marco
echo "#Date : $(date)"
echo "#GitHub :  https://github.com/dopelDev"
echo "#Facebook : https://www.facebook.com/profile.php?id=100036185774355"
echo "#Mail : 322kuroneko2@gmail.com"
marco
