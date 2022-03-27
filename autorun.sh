#!/usr/bin/bash

xrandr --output DP-3 --left-of DP-1 --output DP-1 --left-of HDMI-0;
fcitx5 -d &> /dev/null &
leftwm-command Reload;
