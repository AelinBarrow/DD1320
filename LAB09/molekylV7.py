from linkedQFileV2 import LinkedQ
import sys

atoms = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca',
     'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y',
     'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe', 'Cs', 'Ba', 'La', 'Ce',
     'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir',
     'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm',
     'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn', 'Fl', 'Lv']

dq= LinkedQ()

#Syntaxkontroll
class  Syntaxfel(Exception):
    pass

def read_molecule(q):
    '''
    checks each new molecule
    '''
    read_group(q)
    if q.isEmpty():
        return
    else:
        read_molecule(q)
    
def read_atom(q):
    if q.peekfirst().isupper():
        letter=q.dequeue()
        dq.enqueue(letter)
        if q.peekfirst().islower():
            read_lower(q)
            if  str(dq.printq()) in atoms:
                while dq.isEmpty()!=True: #empties the second queue
                    dq.dequeue()
                return    
            else:
                raise Syntaxfel("Okänd atom vid radslutet ")
        else:
            if  str(dq.printq()) in atoms:
                
                while dq.isEmpty()!=True: #empties the second queue
                    dq.dequeue()
                return    
            else:
                while dq.isEmpty()!=True: #empties the second queue
                    dq.dequeue()
                raise Syntaxfel("Okänd atom vid radslutet ")
    raise Syntaxfel("Saknad stor bokstav vid radslutet " )

def read_lower(q):
    #comes always here and returns always True but takes only small letters from the queue
    if q.peekfirst().islower():
        letter=q.dequeue()
        dq.enqueue(letter)
        return
    return

def read_group(q):
    #check paranthesis
        #check letters
        #check finished paranthesis
    #check letters
        #check numbers
    #check numbers
    if q.isEmpty():
        raise Syntaxfel("Felaktig gruppstart vid radslutet3 ")
    
    elif q.peekfirst().isdigit():
        raise Syntaxfel()
    
    elif q.peekfirst().isupper():
        read_atom(q)
        if q.peekfirst()==None:
            return
        elif q.peekfirst().isdigit():
            read_number(q)
            
        return
    elif q.peekfirst() == '(':
        q.dequeue()
        read_molecule(q)
        if q.peekfirst()!=')':
            raise Syntaxfel("Saknad högerparentes vid radslutet ")
        elif q.isEmpty():
            raise Syntaxfel("Saknad siffra vid radslutet ")
        else:
            q.dequeue()
            if q.isEmpty():
                raise Syntaxfel("Saknad siffra vid radslutet ")
            read_number(q)
    raise Syntaxfel("Felaktig gruppstart vid radslutet3 ") 
	



def read_number(q): 
    num = q.dequeue()
    '''
    check first number:
    if its a 0-->raise
    if its a 1--> and peek() number exists--> return
                else: raise
    if its >1 --> return
    if the next is a letter-->atom
    if the queue is empty -->return?
    '''
    if not q.peekfirst().isnumeric():
        raise Syntaxfel('Saknad siffra vid radslutet ' )
    num = q.dequeue()
    if (int(num) == 0):
        raise Syntaxfel('För litet tal vid radslutet ' )
    if (int(num) == 1):
        if q.isEmpty() or not q.peekfirst().isnumeric():
            raise Syntaxfel('För litet tal vid radslutet ' )
    while not q.isEmpty() and q.peekfirst().isnumeric():
        q.dequeue()
          
                
def store_molecule(molecule):
    q = LinkedQ()
    molecule = list(molecule)
    for letter in molecule:
        q.enqueue(letter)
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