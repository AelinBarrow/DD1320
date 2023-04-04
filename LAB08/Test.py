from linkedQFileV2 import LinkedQ

import string
import sys

class Syntaxfel(Exception):
    pass

def readMolecule(q):
    readAtom(q)
    if q.peek() == ".": #GÖR NÅGOT ANNAT HÄR
        q.dequeue()
    else:
        readNumber(q)

def readAtom(q):
    readLETTER(q)
    if q.peek() not in list(string.ascii_lowercase):
        return
    else:
        readletter(q)

def readLETTER(q):
    letter = q.dequeue()
    alphabet = list(string.ascii_uppercase)
    if letter in alphabet:
        return
    raise Syntaxfel("Saknad stor bokstav ")

def readletter(q):
    letter = q.dequeue()
    return

def readNumber(q):
    num = q.dequeue()
    print(num)
    if int(num) > 1:
        return
    raise Syntaxfel("För litet tal")


def storeMolecule(molecule):
    q =LinkedQ()
    molecule = list(molecule)
    for letter in molecule:
        q.enqueue(letter)
    q.enqueue(".")
    return q
    

def checkStructure(molecule):
    q = storeMolecule(molecule)

    try:
        readMolecule(q)
        return "Formeln är syntatiskt korrekt"
    except Syntaxfel as fel:
        return str(fel)
    

for line in sys.stdin:
    if '#' == line.rstrip():
        break
    resultat = checkStructure(line)
    print(resultat)  

'''def main():
    molecule = input("Write a molecule: ")
    result = checkStructure(molecule)
    print(result)

if __name__ == "__main__":
    main()'''