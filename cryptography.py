"""
cryptography.py
Author: <your name here>
Credit: <list sources used, if any>

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
do = 0
while do == 0:
    befehl = str.lower(input("Enter e to encrypt, d to decrypt, or q to quit: "))
    if befehl == 'e':
        do = 1
    elif befehl == 'd':
        do = 2
    elif befehl == 'q':
        do = 3
    else:
        do = 0
        print("Did not understand command, try again.")

if befehl == 1:
    msg = str(input("Message: "))
    ky = str(input("Key: "))
if befehl == 2:
    msg = str(input("Message: "))
    ky = str(input("Key: "))
if befehl == 3:
    print("Goodbye")
