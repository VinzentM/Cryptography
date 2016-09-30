"""
cryptography.py
Author: <your name here>
Credit: <list sources used, if any>

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
counter = 0
lisas = []
while counter < 88:
    lisas.append(associations[counter])
    counter+=1
aslis = list(range(0,86))
lis(list(zip(aslis, lisas)))

def encrypt(msgin, kyin):
    counter1 = 0
    laenge = len(msgin)
    msglis = []
    while counter1 < laenge+1:
        msglis.append(msgin(counter1))
    

"""
do = False
while do == False:
    befehl = str.lower(input("Enter e to encrypt, d to decrypt, or q to quit: "))
    if befehl == 'e':
        do = True
        msg = str(input("Message: "))
        ky = str(input("Key: "))

    elif befehl == 'd':
        do = True
        msg = str(input("Message: "))
        ky = str(input("Key: "))
    elif befehl == 'q':
        do = 3
        print("Goodbye")

    else:
        do = 0
        print("Did not understand command, try again.")

if befehl == 1:
    msg = str(input("Message: "))
    ky = str(input("Key: "))
if befehl == 2:
    msg = str(input("Message: "))
    ky = str(input("Key: "))
"""
