#/usr/bin/bash

# Description: A simple script to choose a VPN connection from a list of available connections (OpenVPN).
# Author: DopelDev

echo """Choose a VPN connection:
1) VPN1 (PE)
2) VPN2 (US)
3) VPN3 (JP)
0) Exit
"""

pathToPE="$HOME/vpn/elastika/openvpn-gnu-linux/"
pathToUS="$HOME/vpn/personal_vpn/openvpn-gnu-linux/"
pathToJP="$HOME/vpn/japon-vpn/desktop/openvpn-gnu-linux/"

read -p "Enter your choice: " choice

if [ $choice -eq 1 ]; then
		cd $pathToPE
		sudo openvpn --config client.ovpn
elif [ $choice -eq 2 ]; then
		cd $pathToUS
		sudo openvpn --config client.ovpn
elif [ $choice -eq 3 ]; then
		cd $pathToJP
		sudo openvpn --config client.ovpn
elif [ $choice -eq 0 ]; then
		exit 0
else
		echo "Invalid choice"
fi
