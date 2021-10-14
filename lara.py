#!/usr/bin/python
print("Loading LARA...")

import os
import sys
import crypt
import colorama
from colorama import Fore, Back

os.system("cls" if os.name == "nt" else "clear")


# PRINT BANNER
def print_banner():
    print(Fore.RED)
    print("   |         \      _ \      \  ")
    print("   |        _ \    |   |    _ \ ")
    print("   |       ___ \   __ <    ___ \ ")
    print("  _____| _/    _\ _| \_\ _/    _\ ")
    print("     c r y p t    b r e a k e r")
    print(Fore.RESET)

# SETUP OPTIONS:
print_banner()
# Get Hash:
print(Fore.RED + "Full Hash: " + Fore.RESET, end="")
full_hash = input()
# Extract Salt:
tmp = full_hash.split("$")
salt = "$" + tmp[1] + "$" + tmp[2] + "$"
print(Fore.RED + "Hash Salt: " + Fore.RESET + salt)
# Get Wordlist:
if len(sys.argv) == 2:
    wordlist = sys.argv[1]
    print(Fore.RED + "Wordlist: " + Fore.RESET + wordlist)
else:
    print(Fore.RED + "Wordlist: " + Fore.RESET, end="")
    wordlist = input()

# OPEN WORDLIST
try:
    with open(wordlist, "r") as fl:
        words = fl.read().split("\n")
    print(Fore.RED + "Wordlist Size: " + Fore.RESET + str(len(words)))
except Exception as error:
    print("")
    print(Fore.WHITE + Back.RED)
    print(error)
    print(Fore.RESET + Back.RESET)
    sys.exit()

# CRACKING LOOP:
input(Fore.RED + "Ready. Press ENTER to go." + Fore.RESET)
print("")
for word in words:
    tmp = crypt.crypt(word, salt)
    if tmp == full_hash:
        print(Fore.GREEN + "[+] {0} - {1}".format(word, tmp) + Fore.RESET)
        sys.exit()
    else:
        print(Fore.RED + "[-]" + Fore.RESET + " {0}".format(word) + Fore.RED + " - " + Fore.RESET + "{0}".format(tmp))
print("\n" + Fore.RED + "No password was found." + Fore.RESET)
