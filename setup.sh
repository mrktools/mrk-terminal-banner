#!/bin/bash

# Color Codes
green='\e[1;32m'
blue='\e[1;34m'
yellow='\e[1;33m'
cyan='\e[1;36m'
clear='\e[0m'

clear
echo -e "${cyan}==========================================${clear}"
echo -e "${green}       WELCOME TO MRK BANNER TOOL          ${clear}"
echo -e "${cyan}==========================================${clear}"
echo ""

# Taking User Input
echo -e "${yellow}Enter the Name you want to display:${clear}"
read banner_name

# Permanent Setup in .bashrc
echo "clear" > ~/.bashrc

# Spacing to bring text to middle
for i in {1..7}; do echo "echo ''" >> ~/.bashrc; done

# Developer Identity (Styled)
echo "echo -e '              ${cyan}●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●${clear}'" >> ~/.bashrc
echo "echo -e '                    ${green}Developer: MRK (Official Tool)${clear}'" >> ~/.bashrc
echo "echo -e '              ${cyan}●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●${clear}'" >> ~/.bashrc
echo "echo ''" >> ~/.bashrc

# Stylish Large Font (Slant Style)
echo "figlet -f slant '  $banner_name' | lolcat" >> ~/.bashrc

# Extra stylish line at bottom
echo "echo ''" >> ~/.bashrc
echo "echo -e '          ${yellow}--- System Loaded Successfully ---${clear}'" >> ~/.bashrc

echo ""
echo -e "${green}DONE! Your stylish banner is permanently set.${clear}"
echo -e "${yellow}Close Termux and Re-open to see the magic!${clear}"
