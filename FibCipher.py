
def fibseq(x):
  mylist = [0,1]
  iterator = 3
  while True:
    if x == len(mylist) - 1:
      break
    if len(mylist) < 3:
      mylist.append(mylist[0] + mylist[1])
    else:
      for a in mylist:
        if x == len(mylist) - 1:
          return mylist[x]
          break
        else:
          temp = mylist[iterator - 1] + mylist[iterator - 2]
          mylist.append(temp)
        iterator += 1

def reversefibseq(x):
  mylist = [0,1]
  iterator = 3
  while True:
    if x == len(mylist) - 1:
      break
    if len(mylist) < 3:
      mylist.append(mylist[0] + mylist[1])
    else:
      for a in mylist:
        if x == len(mylist) - 1:
          return mylist
          break
        else:
          temp = mylist[iterator - 1] + mylist[iterator - 2]
          mylist.append(temp)
        iterator += 1



def cipher(strvar, ciphernumber):
    DictofValues = {"Z":1, "Y":2, "X":3, 'W': 4, 'V': 5, "U": 6, "T": 7, "S": 8, "R": 9, "Q": 10, 'P': 11, 'O': 12, 'N': 13, 'M': 14, 'L': 15, 'K': 16, 'J': 17, 'I': 18, 'H': 19, 'G': 20, 'F': 21, 'E': 22, 'D':23, 'C': 24, 'B': 25, 'A':26, ' ':27, '.':28, '?':29, '!':30, ',':31, 'a':32, 'b':33, 'c': 34, 'd':35, 'e':36, 'f':37, 'g':38, 'h':39, 'i':40, 'j': 41, 'k': 42, 'l': 43, 'm': 44, 'n': 45, 'o': 46, 'p': 47, 'q': 48, 'r': 49, 's': 50,'t': 51, 'u': 52, 'v': 53, 'w': 54, 'x': 55, 'y': 56, 'z': 57, '*': 58}
    templist = []
    keylist = list(DictofValues.keys())
    valuelist = list(DictofValues.values())
    for x in strvar:
        if x in keylist:
            
            templist.append(valuelist[keylist.index(x)])
        else:
            templist.append(58)

    cipherlist = []
    for x in templist:
        temp = x * ciphernumber
        #Note, the ciphernumber should be between 1-5
        mytemp = fibseq(temp)
        cipherlist.append(mytemp)
    print(cipherlist)
    return cipherlist

def decipher(cipherlist, ciphernumber):
    DictofValues = {"Z":1, "Y":2, "X":3, 'W': 4, 'V': 5, "U": 6, "T": 7, "S": 8, "R": 9, "Q": 10, 'P': 11, 'O': 12, 'N': 13, 'M': 14, 'L': 15, 'K': 16, 'J': 17, 'I': 18, 'H': 19, 'G': 20, 'F': 21, 'E': 22, 'D':23, 'C': 24, 'B': 25, 'A':26, ' ':27, '.':28, '?':29, '!':30, ',':31, 'a':32, 'b':33, 'c': 34, 'd':35, 'e':36, 'f':37, 'g':38, 'h':39, 'i':40, 'j': 41, 'k': 42, 'l': 43, 'm': 44, 'n': 45, 'o': 46, 'p': 47, 'q': 48, 'r': 49, 's': 50,'t': 51, 'u': 52, 'v': 53, 'w': 54, 'x': 55, 'y': 56, 'z': 57, '*': 58}
    mylist = reversefibseq(ciphernumber * 59)
    keylist = list(DictofValues.keys())
    valuelist = list(DictofValues.values())
    decipherlist = []
    for x in cipherlist:
        location = mylist.index(x)
        tempnum = int(location/ciphernumber)
        tempstr = keylist[valuelist.index(tempnum)]
        decipherlist.append(tempstr)
    decipheredword = ""
    for z in decipherlist:
        decipheredword += z
    return decipheredword



print(decipher(cipher("B'ens f'ood'", 3), 3))