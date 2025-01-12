#!/usr/bin/env python

import os
from colorama import init, Fore
from pyfiglet import Figlet

# Initialize Colorama
init()

os.system("apt-get install figlet")
os.system("clear")

f = Figlet(font='slant')
print(Fore.BLUE + f.renderText('Mac Channger') + Fore.RESET)

# os.system(Fore.BLUE + "figlet Mac Channger" + Fore.RESET)
print(Fore.RED + "          | - | Made By : Fenrir - Cyber Security Specialist | - |         " + Fore.RESET)
    
print("""

{0}1){2} Mac Address Random
{0}2){2} Mac Address Manual
{0}3){2} Mac Address Original

""".format(Fore.RED, "0", Fore.RESET, "1", "2", "3", "4", "5", "6", "7", "8", "9", Fore.RESET))

choice = input(Fore.CYAN + "Enter Transaction Number: " + Fore.RESET)

if(choice=="1"):
    os.system("ifconfig eth0 down")
    os.system("macchanger -r eth0")
    os.system("ifconfig eth0 up")
    
    print("\033[92mNew Mac Address Random Created !")
    
elif(choice=="2"):
    macaddress = input("Enter New Mac Address: ")
    os.system("ifconfig eth0 down")
    os.system("macchanger --mac " + macaddress + " eth0 ")
    os.system("ifconfig eth0 up")
    
    print("\033[92mNew Mac Address Manual Created !")
    
elif(choice=="3"):
    os.system("ifconfig eth0 down")
    os.system("macchanger -p eth0")
    os.system("ifconfig eth0 up")
    
    print("\033[92mNew Mac Address Original Created !")
    
else:
    print("You made a wrong choice, it's restarting...")
    print("python3 mac_channger.py")
