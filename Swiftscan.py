#!/usr/bin/env python3

import os

print ("""\
#-----------------------------------------------#  
 _____         _  __ _    _____                 
/ ____|       (_)/ _| |  / ____|                
| (_____      ___| |_| |_| (___   ___ __ _ _ __  
 \___ \ \ /\ / / |  _| __|\___ \ / __/ _` | '_ \ 
 ____) \ V  V /| | | | |_ ____) | (_| (_| | | | |
|_____/ \_/\_/ |_|_|  \__|_____/ \___\__,_|_| |_|

#-----------------------------------------------#   
         By AJ Whitfield AKA "Hypercube"
    """)

target_ip = input("Input target Domain/IP: ")
print ("Target Domain/IP is: " + str(target_ip))

def menu(): 
    print("[1] NMAP Standard scan - Service/Version/OS")
    print("[2] NMAP Discovery scan - Detection")
    print("[3] NMAP Stealth scan - Silent")
    print("[4] NMAP Jackhammer scan - Loud")
    print("[5] NMAP Vulnerability scan - Vuln")
    print("[6] NMAP Hailmary scan - Everyprobe")
    print("[7] NMAP Firewalk scan - FW setup")
    print("[8] NMAP Decoy scan - Decoy")
    print("[0] Exit")
    
def option1():
    print ("Standard scan selected")
    os.system('sudo nmap -v -sVCO -p- -oN StanScan.txt ' + str(target_ip))
def option2():
    print ("Discovery scan selected")
    os.system('sudo nmap -v -sCN -p- -oN DetectScan.txt ' + str(target_ip))
def option3():
    print ("Stealth scan selected")
    os.system('sudo nmap -v -sSV -p- -oN StealthScan.txt ' + str(target_ip))
def option4():
    print ("Jackhammer scan selected")
    os.system('sudo nmap -v -sCVO -T5 -oN JHScan.txt ' + str(target_ip))
def option5():
    print ("Vulnerability scan selected")
    os.system('sudo nmap -v --script vuln -p- -oN VulnScan.txt ' + str(target_ip))
def option6():
    print ("Hailmary scan selected")
    os.system('sudo nmap -v -sC --version-all -p- -oN HMScan.txt ' + str(target_ip))
def option7():
    print ("Firewall scan selected")
    os.system('sudo nmap -v -sA -p- -oN FWScan.txt ' + str(target_ip)) 
def option8():
    print ("Decoy scan selected")
    decoy_ip = input("Insert Decoy IP: ")
    print ("Decoy IP is: " + str(decoy_ip))
    os.system('sudo nmap -v -D ' + str(decoy_ip) + ' ' + str(target_ip)) 
 
menu() 
option = int(input("Enter your option: "))

while option != 0: 
    if option == 1: 
        option1()
    elif option == 2:
        option2()
    elif option == 3: 
        option3()
    elif option == 4: 
        option4()
    elif option == 5: 
        option5()
    elif option == 6: 
        option6()
    elif option == 7: 
        option7()
    elif option == 8: 
        option8()
    else:
        print("Invalid option")

    print()
    menu() 
    option = int(input("Enter your option: "))
    
print("Goodbye")
