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
#a=Bintree()
dq= LinkedQ()

'''#puts all the correct atoms into a binary tree
with open("atomlista.txt", 'r') as atomfile:
    for row in atomfile:
        row=row.strip()
        for atom in row: 
            a.put(atom) #puts all the words into our swedish binary tree
            

print(a.__contains__('Be'))'''

atoms = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca',
     'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y',
     'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe', 'Cs', 'Ba', 'La', 'Ce',
     'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir',
     'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm',
     'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn', 'Fl', 'Lv']


'''
problem with dq to empty after each time otherwise there are elements over to the next input 
'''


#Syntaxkontroll
class  Syntaxfel(Exception):
    pass

def read_molecule(q):
    '''
    checks each new molecule
    '''

    read_group(q)
    read_molecule(q)

def read_atom(q):
    if read_upper(q) and read_lower(q):
        if  str(dq.printq()) in atoms:
            while dq.isEmpty()!=True: #empties the second queue
                dq.dequeue()
            return
        else:
            raise Syntaxfel("Ökand atom vi radslutet ")

    elif read_lower(q):
        return
    
    
def read_upper(q):
    #checks if the letter is big or small, returns True otherwise raises mistake
    letter=q.dequeue()
    dq.enqueue(letter)  
    if letter.isupper():
       return
    raise Syntaxfel("Saknad stor bokstav vid radslutet " )

def read_lower(q):
    #comes always here and returns always True but takes only small letters from the queue
    for letter in str(q):
        #added a for-loop, deque-ar only small letters 
        if letter.islower():
            letter=q.dequeue()
            dq.enqueue(letter)
            return
    return


def read_group(q):
    '''
    <group> ::= <atom> |<atom><num> | (<mol>) <num>
    '''
    if q.peek()=='(':
        q.dequeue()
        if type(q.peek())==str:
            read_atom(q)
        elif q.peek().isdigit():
            read_number(q)
        elif q.peek()==')':
            q.dequeue()
            return
        else:
            raise Syntaxfel("Saknad höger parantes ")
    elif type(q.peek())==str:
        read_atom(q)

    elif q.peek()==')':
        raise Syntaxfel("sakand vänster parantes ")
'''
    elif q.peek().isdigit():
        raise Syntaxfel("Bara siffror ")

    elif q.peek().isupper():
        read_atom(q)
    else:
        raise Syntaxfel("IDK")
'''


def read_number(q):
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
        read_molecule(q)
        return "Formeln är syntaktiskt korrekt"
    except Syntaxfel as fel:
       
        return str(fel) + str(q)
    
for line in sys.stdin:
    if '#' == line.rstrip():
        break
    resultat = check_syntax(line)
    print(resultat)




