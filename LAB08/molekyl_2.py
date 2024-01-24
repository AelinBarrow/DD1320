
#DD1320
#Laboration 8

from linkedQFileV2 import LinkedQ
import sys
import re

#Syntaxkontroll
class  Syntaxfel(Exception):
    pass

def read_molecule(q, molecule):
    read_atom(q, molecule) #first checks the letters               
    if q.peek() == "/" : #if there are only letters
        q.dequeue()
    else:                                                            
        read_number(q, molecule)  #checks the numbers

def read_atom(q, molecule):
    if read_upper(q, molecule) and read_lower(q, molecule):
        return
    else:
        read_lower(q, molecule)

def read_upper(q, molecule):
    #checks if the letter is big or small, returns True otherwise raises mistake
    letter=q.dequeue()
    if letter.isupper():
        return 
    raise Syntaxfel("Saknad stor bokstav vid radslutet "+ molecule )
  
def read_lower(q, molecule):
    #comes always here and returns always True but takes only small letters from the queue
    for letter in molecule:
        #added a for-loop, deque-ar only small letters 
        if letter.islower():
            letter=q.dequeue()
            return
    return

def read_number(q, molecule):
    res=re.split('(\d+)', molecule) #splits input into letters and numbers in a list
    mol=str(res[1]) #takes the numbers from the list
    mol=list(mol)
    num = q.dequeue()
    if num.isdigit():
            mol.pop(0) 
            stri=''
            string=stri.join(mol)
            if q.peek()!='/':
                if int(num) > 1:
                    return
                #H01011
                elif q.peek()== '1'and int(num)>1 or q.peek()== '0'and int(num)>1 :
                    return
                elif q.peek()== '1'and int(num)<1 or q.peek()== '0'and int(num)<1:
                    raise Syntaxfel("För litet tal vid radslutet " + str(string)) #put all the rest from the queue
                elif q.peek()== '0'and int(num)==1:
                    return
                elif int(num)==0:
                    raise Syntaxfel("För litet tal vid radslutet "+ str(string))
            else:
                #H10100
                if int(num) > 1:
                    return
                else:
                    raise Syntaxfel("För litet tal vid radslutet")
        
def store_molecule(molecule):
    q = LinkedQ()
    molecule = list(molecule)
    for letter in molecule:
        q.enqueue(letter)
    q.enqueue("/") #to just know end of the input
    return q

def check_syntax(molecule):
    q = store_molecule(molecule)
    try:
        read_molecule(q, molecule)
        return "Formeln är syntaktiskt korrekt"
    except Syntaxfel as fel:
        return str(fel) + str(q)
    
'''def printQueue(q):
    while not q.isEmpty():
        word = q.dequeue()
        print(word, end = " ")
    print()'''

for line in sys.stdin:
    if '#' == line.rstrip():
        break
    resultat = check_syntax(line)
    print(resultat)

'''if __name__ == "__main__": 
    molecule = input("Write a molecule: ")
    resultat = check_syntax(molecule)
    print(resultat) '''
