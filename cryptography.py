"""
cryptography.py
Author: Vinzent
Credit: Liam

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
counter = 0
lisas = []
while counter < 85:
    lisas.append(associations[counter])
    counter+=1
aslis = list(range(0,86))
lis = list(zip(aslis, lisas))
counter1 = 0
def encrypt(msgin, kyin):
    counter1 = 0
    laenge = int(len(msgin))
    msglis = []
    eqmsg = []
    while counter1 < laenge:
        msglis.append(msgin[counter1])
        eqmsg.append(associations.find(msgin[counter1]))
        counter1 += 1
    kydone = kyanpassen(laenge, kyin)
    kylis = []
    eqky = []
    counter2 = 0
    laengekydone = int(len(kydone))
    while counter2 < laengekydone:
        kylis.append(kydone[counter2])
        eqky.append(associations.find(kydone[counter2]))
        counter2 += 1
    wrkend = []
    counter3 = 0
    while counter3 < laengekydone:
        wrkend.append(int(eqky[counter3])+int(eqmsg[counter3]))
        counter3+=1
    #check if to big
    counter4 = 0
    while laengekydone > counter4:
        if wrkend[counter4] > 84:
            wrkend[counter4] = int(wrkend[counter4])-int(85)
        counter4 += 1
    counter5 = 0
    cryptd = []
    while counter5 < laengekydone:
        cryptd.append(associations[wrkend[counter5]])
        counter5 += 1
    print(''.join(cryptd))
def decrypt(msgin, kyin):
    counter1 = 0
    laenge = int(len(msgin))
    msglis = []
    eqmsg = []
    while counter1 < laenge:
        msglis.append(msgin[counter1])
        eqmsg.append(associations.find(msgin[counter1]))
        counter1 += 1
    kydone = kyanpassen(laenge, kyin)
    kylis = []
    eqky = []
    counter2 = 0
    laengekydone = int(len(kydone))
    while counter2 < laengekydone:
        kylis.append(kydone[counter2])
        eqky.append(associations.find(kydone[counter2]))
        counter2 += 1
    wrkend = []
    counter3 = 0
    while counter3 < laengekydone:
        wrkend.append(eqmsg[counter3]-eqky[counter3])
        counter3+=1
    #check negative
    counter4 = 0
    while laengekydone > counter4:
        if wrkend[counter4] <= -1:
            wrkend[counter4] = int(wrkend[counter4]+int(85))
        counter4 += 1
    counter5 = 0
    dcryptd = []
    while counter5 < laengekydone:
        dcryptd.append(associations[wrkend[counter5]])
        counter5 += 1
    print(''.join(dcryptd))
def kyanpassen(msglaenge, kywrk1):
    laengeky = int(len(kywrk1))
    kywrk = kywrk1
    if laengeky < msglaenge+1:
        laengekywrk = int(len(kywrk))
        while laengekywrk < msglaenge:
            kywrk = kywrk + kywrk1
            laengekywrk = int(len(kywrk))
        laengekywrk = int(len(kywrk))
        if laengekywrk > msglaenge:
            while laengekywrk > msglaenge:
                kywrk = kywrk[:-1]
                laengekywrk = int(len(kywrk))
    kydonedef = kywrk
    return kydonedef
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
        decrypt(msg, ky)
        do = False
    elif befehl == 'q':
        do = 3
        print("Goodbye!")
    else:
        print("Did not understand command, try again.")