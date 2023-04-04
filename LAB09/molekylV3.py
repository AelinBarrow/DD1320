#Michaela Jankulicova
#DD1320
#Laboration 9

from linkedQFileV2 import LinkedQ
import sys
from bintreeFileV2 import Bintree


'''
<formel>::= <mol> \n
<mol>   ::= <group> | <group><mol>
<group> ::= <atom> |<atom><num> | (<mol>) <num>
<atom>  ::= <LETTER> | <LETTER><letter>
<LETTER>::= A | B | C | ... | Z
<letter>::= a | b | c | ... | z
<num>   ::= 2 | 3 | 4 | ...

'''
a=Bintree()
#puts all the correct atoms into a binary tree
with open("atomlista.txt", 'r') as atomfile:
    for row in atomfile:
        atom=row.strip()
        if atom not in a:
            a.put(atom) #puts all the words into our swedish binary tree

#Syntaxkontroll
class  Syntaxfel(Exception):
    pass

def read_molecule(q, dq):
    read_group(q, dq)
    '''if q.peek()=='/':
        letter=q.dequeue()
        dq.enqueue(letter)
    else:
        read_number(q, dq)
    #raise Syntaxfel("Okänd atom vid radslutet " )'''
    
def read_atom(q, dq):
    if read_upper(q, dq) and read_lower(q, dq):
        
        if dq.printq() in a:
            print(dq.printq())
            return
    elif read_lower(q, dq):
        return
    

def read_upper(q, dq):
    #checks if the letter is big or small, returns True otherwise raises mistake
    letter=q.dequeue()
    dq.enqueue(letter)
    if letter.isupper():
        
        return
    raise Syntaxfel("Saknad stor bokstav vid radslutet " )

def read_lower(q,dq):
    #comes always here and returns always True but takes only small letters from the queue
    for letter in str(q):
        #added a for-loop, deque-ar only small letters 
        if letter.islower():
            letter=q.dequeue()
            dq.enqueue(letter)
           
            return
    return


def read_group(q,dq):
    '''
    <group> ::= <atom> |<atom><num> | (<mol>) <num>
    '''
    if q.isEmpty():
        return
    if q.peek().isupper():
        read_atom(q, dq)
    '''else:
        if not q.peek() == '(' or q.peek() == ')' :
            raise SyntaxError('Felaktig gruppstart vid radslutet ')'''

    if q.peek() == '(':
        q.dequeue()
        while not q.isEmpty():
            read_group(q, dq)
            if q.isEmpty():
                break
            if (not q.peek().isupper()):
                break

        if not q.peek() == ')':
            raise SyntaxError('Saknad högerparentes vid radslutet ')
        q.dequeue()
        read_number(q, dq)

    if not q.isEmpty():
        if (q.peek() == ')' ):
            raise SyntaxError('Felaktig gruppstart vid radslutet ')
    
    

def read_number(q, dq):
    num = q.dequeue()
    if num.isdigit():
            if q.peek()!='/':
                if int(num) > 1:
                    return
                #H01011
                elif q.peek()== '1'and int(num)>1 or q.peek()== '0'and int(num)>1 :
                    return
                elif q.peek()== '1'and int(num)<1 or q.peek()== '0'and int(num)<1:
                    raise Syntaxfel("För litet tal vid radslutet ") #put all the rest from the queue
                elif q.peek()== '0'and int(num)==1:
                    return
                elif int(num)==0:
                    raise Syntaxfel("För litet tal vid radslutet ")
            else:
                #H10100
                if int(num) > 1:
                    return
                else:
                    raise Syntaxfel("För litet tal vid radslutet")
    else:
        read_molecule(q, dq)
        
def store_molecule(molecule):
    q = LinkedQ()
    molecule = list(molecule)
    for letter in molecule:
        q.enqueue(letter)
    q.enqueue("/") #to just know end of the input
    return q

def check_syntax(molecule):
    dq= LinkedQ()
    q = store_molecule(molecule)
    try:
        read_molecule(q, dq)
       
        return "Formeln är syntaktiskt korrekt"
    except Syntaxfel as fel:
       
        return str(fel) + str(q)
    


for line in sys.stdin:
    if '#' == line.rstrip():
        break
    resultat = check_syntax(line)
    print(resultat)

'''if __name__ == "__main__": 
    molecule = input("Write a molecule: ")
    resultat = check_syntax(molecule)
    print(resultat) '''



