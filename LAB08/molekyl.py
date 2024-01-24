#laboration 7

#DD1320

from linkedQFileV2 import LinkedQ
import sys
 

#Syntaxkontroll
class Syntax_mistake(Exception):
    pass

def read_molecule(q, molecule):
    read_atom(q, molecule) #first checks the letters               
    if q.peek() == "/" : #if there are only letters
        print('here')
        q.dequeue()
    else:                                                            
        read_number(q)  #checks the numbers

def read_atom(q, molecule):
    if read_upper(q, molecule):
        return
    else:
        read_lower(q)
                  
def read_upper(q, molecule):
    #checks if the letter is big or small, returns True otherwise raises mistake
    letter=q.dequeue()
    if letter.isupper():
        return 
    raise Syntax_mistake("Saknad stor bokstav vid radslutet "+ molecule )
            

def read_lower(q):
    #comes here if read_upper doesnt return True
    letter=q.dequeue()
    return
    
def read_number(q):
    num = q.dequeue()
    if int(num) > 1:
            return
    raise Syntax_mistake("För litet tal vid radslutet")





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
    except Syntax_mistake as fel:
        return str(fel)


'''for line in sys.stdin:
    if '#' == line.rstrip():
        break
    resultat = check_syntax(line)
    print(resultat)  '''
    

'''if __name__ == "__main__": 
    molecule = input("Write a molecule: ")
    resultat = check_syntax(molecule)
    print(resultat)   
                '''
            
  
            




