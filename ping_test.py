#!/usr/bin/env python3
'''
Name: Gavin Fletcher
Date: 9/8/23
Version: 1 
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
    result = subprocess.run("ip route | grep default", shell=True)
    # If no gateway is set, terminal returns 1
    if (result == 1):
        print("No gateway found!")
        return None
    else:
        result.split(" ")
        gateway = result[2]
        return gateway

def test_local_connection():
    gateway = find_Default_gateway()
    # Check if the ping was successful
    if (gateway == None):
        print("gateway cannot be found!")
        return
    result = subprocess.Popen(["ping", "-c", "3", gateway]) # idea for using .poll(): Hadrián on Stack Overflow
    result.wait()
    if (result.poll() == True):
        print("Local connection (", gateway,") was successful")
    else:
        print("Local connection (", gateway,") was unsuccessful")

def test_remote_connection():
    # Check if the ping was successful
    result = subprocess.Popen(["ping", "-c", "3", "129.21.3.17"])
    if (result == True):
        print("Local connection (129.21.3.17) was successful")
    else:
        print("Local connection (129.21.3.17) was unsuccessful")

def test_dns_resolution():
    # ping www.google.com
    result = subprocess.Popen(["ping", "-c", "3", "www.google.com"])
    if (result == True):
        print("Local connection (129.21.3.17) was successful")
    else:
        print("Local connection (129.21.3.17) was unsuccessful")
    pass

def main():
    user_input = None # Setting user_input so that the while loop can run

    while user_input != 5:
        # Prompt the user for the 5 options available
        print("Options avialable for the ping test:\n\n")
        print("(1.) Display the default gateway\n(2.) Test Local Connectivity\n(3.) Test Remote Connectivity\n(4.) Test DNS Resolution\n(5.) Exit / quit the script")
        # Simple check to make sure that user_input is actually an integer
        try:
            user_input = int(input("Type the number for the option you have selected: "))
            # Is user input in the range from 1 to 5
            if (user_input > 5) or (user_input < 1):
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
                    test_local_connection()
                    clear_input = input("Press enter to continue >> ")
                    subprocess.call("clear", shell=True)

                elif (user_input == 3):
                    test_remote_connection()
                    clear_input = input("Press enter to continue >> ")
                    subprocess.call("clear", shell=True)

                elif (user_input == 4):
                    test_dns_resolution()
                    clear_input = input("Press enter to continue >> ")
                    subprocess.call("clear", shell=True)


        except ValueError:
            subprocess.call("clear", shell=True)
            print("ERROR: Enter a acceptable value from 1-5!\n")




if __name__ == "__main__":
    main()