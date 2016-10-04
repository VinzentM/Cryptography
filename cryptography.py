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
while counter < 84:
    lisas.append(associations[counter])
    counter+=1
aslis = list(range(0,86))
lis = list(zip(aslis, lisas))
counter1 = 0
def encrypt(msgin, kyin):
    counter1 = 0
    counter1 = int(counter1)
    laenge = int(len(msgin))
    msglis = []
    msglis = list(msglis)
    eqmsg = []
    while counter1 < laenge:
        msglis = list(msglis)
        msglis.append(msgin[counter1])
        counter1 += 1
        eqmsg.append(associations.find(msgin[counter1-1]))
    laengeky = int(len(kyin))
    kywrk = kyin
    if laengeky < laenge+1:
        laengekywrk = int(len(kywrk))
        while laengekywrk < laenge+10:
            kywrk = kywrk + kyin
    #    print(kywrk)

        #eqmsg.append(associations.find(msgin[counter1-1]))
    #print(msglis) its the msg in a list
    #print(eqmsg) its the msg in the eq in a list
    do = False

do = False
while do == False:
    befehl = str.lower(input("Enter e to encrypt, d to decrypt, or q to quit: "))
    if befehl == 'e':
        do = True
        msg = str(input("Message: "))
        ky = str(input("Key: "))
        encrypt(msg, ky)
        do = False
    elif befehl == 'd':
        do = True
        msg = str(input("Message: "))
        ky = str(input("Key: "))
    elif befehl == 'q':
        do = 3
        print("Goodbye")

    else:
        do = True
        print("Did not understand command, try again.")
        do = False