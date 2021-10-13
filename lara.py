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
print(Fore.RED + "Wordlist: " + Fore.RESET, end="")
wordlist = input()

# OPEN WORDLIST
print("")
try:
    with open(wordlist, "r") as fl:
        words = fl.read().split("\n")
except Exception as error:
    print(Fore.WHITE + Back.RED)
    print(error)
    print(Fore.RESET + Back.RESET)
    sys.exit()

# CRACKING LOOP:
print("")
for word in words:
    if crypt.crypt(word, salt) == full_hash:
        print(Fore.GREEN + "[+]" + Fore.RESET + " {0}".format(word))
        sys.exit()
    else:
        print(Fore.RED + "[-]" + Fore.RESET + " {0}".format(word))
print("\n" + Fore.RED + "No password was found." + Fore.RESET)
