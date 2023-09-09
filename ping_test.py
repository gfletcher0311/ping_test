#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Name: Gavin Fletcher
Date: 9/8/23
Version: 1.2 
Notes: Used as a ping test for:
1. Display the default gateway
2. Test Local Connectivity
3. Test Remote Connectivity
4. Test DNS Resolution
5. Exit/quit the script

Mentions: Hadrián on stack overflow: (https://stackoverflow.com/questions/35750041/check-if-ping-was-successful-using-subprocess-in-python)
'''
#Import useful package(s)
import subprocess

def find_Default_gateway():
    # Runs a command to immeidately get the line containing the default gateway
    result = subprocess.check_output("ip route | grep default", shell=True) 
    # If no gateway is set, terminal returns 1
    if (result == 1):
        print("No gateway found!")
        return None
    else:
        # Decodes the result to turn it into a string
        result = result.decode()
        result = result.strip().split(" ") # Remove special characters and split on spaces
        gateway = result[2] # Default Gateway is the 3rd item in the split string
        return gateway
    
def test_local_connection():
    gateway = find_Default_gateway()
    # Check if the ping was successful
    if (gateway == None):
        print("gateway cannot be found!")
        return
    result = subprocess.Popen(["ping", "-c", "3", gateway], shell=False, stdout=subprocess.DEVNULL) # idea for using .poll(): Hadrián on Stack Overflow
    result.wait()
    # Result will either be 0 (successful) or 2 (unsuccessful)
    if (int(result.poll()) == 0):
        print("Local connection (", gateway,") was successful")
    else:
        print("Local connection (", gateway,") was unsuccessful")

def test_remote_connection():
    # Check if the ping was successful
    result = subprocess.Popen(["ping", "-c", "3", "129.21.3.17"], shell=False, stdout=subprocess.DEVNULL)
    result.wait()
    if (int(result.poll()) == 0):
        print("Local connection (129.21.3.17) was successful")
    else:
        print("Local connection (129.21.3.17) was unsuccessful")

def test_dns_resolution():
    # ping www.google.com
    result = subprocess.Popen(["ping", "-c", "3", "www.google.com"], shell=False, stdout=subprocess.DEVNULL)
    result.wait()
    if (int(result.poll()) == 0):
        print("Local connection (www.google.com) was successful")
    else:
        print("Local connection (www.google.com) was unsuccessful")
    pass

def main():
    user_input = None # Setting user_input so that the while loop can run
    subprocess.call("clear", shell=True)
    while user_input != 5:
        # Prompt the user for the 5 options available
        print("Options avialable for the ping test:\n\n")
        print("(1.) Display the default gateway\n(2.) Test Local Connectivity\n(3.) Test Remote Connectivity\n(4.) Test DNS Resolution\n(5.) Exit / quit the script")
        # Simple check to make sure that user_input is actually an integer
        try:
            user_input = int(input("Type the number for the option you have selected: "))
            # Is user input in the range from 1 to 5
            if (user_input > 5) or (user_input < 1):
                # If not raise ValueError so they can re-input their number
                raise ValueError
            else:

                if (user_input == 5):
                    print("\nClosing script as requested. . . ")
                    break

                elif (user_input == 1):
                    print("Defualt gateway: ", find_Default_gateway())
                    clear_input = input("Press enter to continue >> ")
                    subprocess.call("clear", shell=True)

                elif (user_input == 2):
                    print("\n Pinging for local connectivity . . .")
                    test_local_connection()
                    clear_input = input("Press enter to continue >> ")
                    subprocess.call("clear", shell=True)

                elif (user_input == 3):
                    print("\n Pinging for remote connectivity . . .")
                    test_remote_connection()
                    clear_input = input("Press enter to continue >> ")
                    subprocess.call("clear", shell=True)

                elif (user_input == 4):
                    print("\n Pinging for DNS resolution . . .")
                    test_dns_resolution()
                    clear_input = input("Press enter to continue >> ")
                    subprocess.call("clear", shell=True)

        except ValueError:
            subprocess.call("clear", shell=True)
            print("ERROR: Enter a acceptable value from 1-5!\n")

if __name__ == "__main__":
    main()