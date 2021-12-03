#!/usr/bin/env python3

"""
Created on 

@author: Kevin Hofstetter

"""
import os
import time
import socket   

ERROR = "Please type a number 1-4"

def banner():

    os.system("clear")
    print("#####################################")
    print(">>>>>>>>>>>>//         //<<<<<<<<<<<<")
    print(">>>>>>>>>>>>//         //<<<<<<<<<<<<")
    print(">>>>>>>>>>>>//         //<<<<<<<<<<<<")
    print(">>>>>>>>>>>>/////////////<<<<<<<<<<<<")
    print(">>>>>>>>>>>>//         //<<<<<<<<<<<<")
    print(">>>>>>>>>>>>//         //<<<<<<<<<<<<")
    print(">>>>>>>>>>>>//         //<<<<<<<<<<<<")
    print("#####################################")

def help():

    print("Type one of these options:\n")
    print("     1) Print my IP")
    print("     2) Print all devices on the network")
    print("     3) Bruteforce wifi password (PATH to wordlist needed)")
    print("     4) NMAP")
    print("\nType 'help' to see this page again")

def find_my_ip():
    os.system("clear")

    hostname = socket.gethostname()   
    IPAddr = socket.gethostbyname(hostname)   
    print("\nYour Computer Name is: " + hostname)   
    print("Your Computer IP Address is: " + IPAddr)
    return
    
def print_all_devices():
    return
def bruteforce_wifi():
    return
def nmap():
    return


def cmds(number):
    if(number > 4 or number < 1):
        print(ERROR)
    if(number == 1):
        find_my_ip()
    if(number == 2):
        print_all_devices()
    if(number == 3):
        bruteforce_wifi()
    if(number == 4):
        nmap()
    

if __name__ == "__main__":
    banner()
    help()
    while(True):
        cmd = input(">> ")
        if(cmd == 'help'):
            help()
        if(cmd == 'quit'):
            quit()
        else:
            try:
                cmd = int(cmd)
                cmds(cmd)
            except:
                print("Please type 'help', 'quit', or a number (1-5)")