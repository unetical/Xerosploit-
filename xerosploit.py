 #!/bin/bash
#XeroSploit Kurucu  v1.0



printf "\n"

printf " \e[1;31m \t\tBy- Unetical \e[0m \n"

printf "\n"
echo More Tools at- https://github.com/CrazyIndianDeveloper
printf "\n"
printf " \e[1;31m \t\t---------------------------------------------------- \e[0m \n"


sudo echo "deb http://http.kali.org/kali kali-rolling main non-free contrib" | sudo tee -a /etc/apt/sources.list
sudo echo "deb-src http://http.kali.org/kali kali-rolling main non-free contrib" | sudo tee -a /etc/apt/sources.list

sudo apt-get update
sudo apt-get install nmap 
sudo apt-get install hping3 
sudo apt-get install build-essential 
sudo apt-get install ruby-dev 
sudo apt-get install libpcap-dev 
sudo apt-get install libgmp3-dev 
sudo apt-get install python-pip 
sudo apt install python3-pip 
sudo pip install --upgrade pip 
sudo pip3 install --upgrade pip  
sudo pip install terminaltables 
sudo pip3 install terminaltables 
sudo pip install tabulate 
sudo pip3 install tabulate 
sudo git clone https://github.com/LionSec/xerosploit
cd xerosploit
python install.py



printf "\n"
firefox https://github.com/CrazyIndianDeveloper
