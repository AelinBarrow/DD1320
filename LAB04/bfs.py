#DD1320

#Laboration 4

from bintreeFileV2 import Bintree

swedish=Bintree() #ordlistan
dumbkids=Bintree()   #dumbarn


def makechildren(startword):
    alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] #for-loop to compare each list element 
    for i in range(0, len(startword)):
        for letter in alphabet:
            word=startword[:i]+ letter+ startword[i+1:] #slicing
            if word in swedish and word not in dumbkids:
                dumbkids.put(word)
                print(word)
            

with open("word3.txt", 'r', encoding = "utf-8") as swedishfile:
    for row in swedishfile:
        word=row.strip()
        if word not in swedish:
            swedish.put(word) #puts all the words into our swedish binary tree
    firstword=input("Start: ")
    lastword=input("Finish: ")
    makechildren(firstword)
