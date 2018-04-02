#!/usr/bin/python
# -*- coding: utf8 -*-
#sys_dhcp.py

import subprocess
import re
from ipaddress import ip_address

__author__ = "Jerzy Kołosowski"

# Checks if MAC Address given is valid. Returns empty string if it is valid.
def isValidMAC(mac_address):
    if mac_address == "":
        return "The MAC Address cannot be left as empty"
    else:
        if re.match("[0-9a-f]{2}([-:])[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$", mac_address.lower()):
            return ""
        return "This is not a valid MAC Address. A valid one's format is XX:XX:XX:XX:XX:XX"

def addHost():
    # Entering DNS Server
    while True:
        try:
            SERVER = input("DNS Server [192.168.2.11] - ")
            SERVER = '192.168.2.11'
            break
        except ValueError:
            print("This is not a valid IP Address. Please try again")
    # Entering DNS Scope
    while True:
        try:
            SCOPE = input("Scope DNS [1 = 192.168.2.0] or [2 = 192.168.22.0] - ")
            if SCOPE == 1:
                print("SCOPE - 192.168.2.0 ")
                SCOPE = '192.168.2.0'
                break
            elif SCOPE == 2:
                print("SCOPE - 192.168.22.0 ")
                SCOPE = '192.168.22.0'
                break
            else:
                print("Invalis number. Try again...")   
        except ValueError:
            print("This is not a valid SCOPE. Please try again")
    # Entering host IP
    while True:
        try:
            ipaddress = input("IP - ")
            IP = ip_address(ipaddress)
            break
        except ValueError:
            print("This is not a valid IP Address. Please try again")
    # Entering host MAC
    while True:
        try:
            macaddress = input("MAC [XX-XX-XX-XX-XX-XX]- ")
            if isValidMAC(macaddress) == "":
                MAC = macaddress
                break
            else:
                print("This is not a valid MAC Address. Please try again")
        except ValueError:
            print("This is not a valid MAC Address. Please try again")
    # Entering host Name
    NAME = input("Host Name - ")
    # Entering Description
    DESCRIPTION = input("Description - ")

    res = 'netsh dhcp server ' + SERVER + ' scope ' + SCOPE + ' add reservedip ' + IP + ' ' + MAC + ' ' + NAME + ' ' + DESCRIPTION + ' "" BOTH'

    print(res)

    netshcmd = subprocess.Popen(
        'netsh dhcp server ' + SERVER + ' scope '
        + SCOPE + ' add reservedip '
        + IP + ' '
        + MAC + ' '
        + NAME + ' '
        + DESCRIPTION + ' BOTH', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    output, errors = netshcmd.communicate()
    if errors:
        print("WARNING: ", errors)
    else:
        print("SUCCESS: ", output)

def delHost():
    print("Function is In progress")

def main():
    ans=True
    while ans:
        print("""
        1.Add a Host to DHCP
        2.Delete a Host from DHCP
        3.Look Up Hosts Record
        4.Exit/Quit
        """)
        ans=input("What would you like to do? ")
        if ans=="1":
            addHost()
            print("\nHost Added")
        elif ans=="2":
            delHost()
            print("\n Host Deleted")
        elif ans=="3":
            print("\n Hosts Record Found")
        elif ans=="4":
            print("\n Goodbye") 
            ans = None
        else:
            print("\n Not Valid Choice Try again")

if __name__ == '__main__':
    main()
