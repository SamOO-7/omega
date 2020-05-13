#!/bin/bash

#            ---------------------------------------------------
#                              Omega Framework                                
#            ---------------------------------------------------
#                  Copyright (C) <2020>  <Entynetproject>       
#
#        This program is free software: you can redistribute it and/or modify
#        it under the terms of the GNU General Public License as published by
#        the Free Software Foundation, either version 3 of the License, or
#        any later version.
#
#        This program is distributed in the hope that it will be useful,
#        but WITHOUT ANY WARRANTY; without even the implied warranty of
#        MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#        GNU General Public License for more details.
#
#        You should have received a copy of the GNU General Public License
#        along with this program.  If not, see <http://www.gnu.org/licenses/>.

RS="\033[1;31m"
YS="\033[1;33m"
CE="\033[0m"

printf '\033]2;install.sh\a'

#blue start 
	BS="\033[1;34m"
#color end
	CE="\033[0m"
#red start
	RS="\033[31m"
#green start
	GNS="-e \033[1;32m"
#white start
   WHS="\033[0m"

if [[ $EUID -ne 0 ]]
then
   echo -e ""$RS"[-] "$WHS"This script must be run as root!"$CE""
   exit
fi

{
ASESR="$(ping -c 1 -q www.google.com >&/dev/null; echo $?)"
} &> /dev/null
if [[ "$ASESR" != 0 ]]
then 
   echo -e ""$RS"[-] "$WHS"No Internet connection!"$CE""
   exit
fi

sleep 0.5
clear
sleep 0.5
cat banner/banner.txt
echo

sleep 1
echo -e ""$BS"[*]"$WHS" Installing dependencies..."$CE""
sleep 1

{
pkg update
pkg -y install git
pkg -y install python
apt-get update
apt-get -y install git
apt-get -y install python3
apt-get -y install python3-pip
apk update
apk add git
apk add python3
apk add py3-pip
pacman -Sy
pacman -S --noconfirm git
pacman -S --noconfirm python3
pacman -S --noconfirm python3-pip
zypper refresh
zypper install -y git
zypper install -y python3
zypper install -y python3-pip
yum -y install git
yum -y install python3
yum -y install python3-pip
dnf -y install git
dnf -y install python3
dnf -y install python3-pip
eopkg update-repo
eopkg -y install git
eopkg -y install python3
eopkg -y install pip
xbps-install -S
xbps-install -y git
xbps-install -y python3
xbps-install -y python3-pip
} &> /dev/null

if [[ -d ~/omega ]]
then
sleep 0
else
cd ~
{
git clone https://github.com/entynetproject/omega.git
} &> /dev/null
fi

{
python3 -m pip install setuptools
python3 -m pip install -r requirements.txt
} &> /dev/null

{
cd bin
cp omega /usr/local/bin
chmod +x /usr/local/bin/omega
cp omega /bin
chmod +x /bin/omega
cp omega /data/data/com.termux/files/usr/bin
chmod +x /data/data/com.termux/files/usr/bin/omega
} &> /dev/null

sleep 1
echo ""$GNS"[+]"$WHS" Successfully installed!"$CE""
sleep 1
