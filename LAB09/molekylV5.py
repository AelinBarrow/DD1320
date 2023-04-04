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
    elif q.peek()=='/':
        letter=q.dequeue()
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


def read_upper(q):
    #checks if the letter is big or small, returns True otherwise raises mistake
    if q.peekfirst().isupper():
        letter=q.dequeue()
        dq.enqueue(letter)
        if q.peekfirst().islower():
            read_lower(q)
            return
        return
    raise Syntaxfel("Saknad stor bokstav vid radslutet1 " )
    


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
    if q.peekfirst().isupper():
        print(q.peekfirst())
        read_atom(q)
        if q.peekfirst()==None:
            return
        elif q.peekfirst().isdigit():
            read_number(q)
            return
        return

    elif q.peekfirst()=='(' or q.peekfirst()==')':
        letter=q.dequeue()
        print(str(q))
        #read_molecule(q)
        if letter==')' :
            print('here')
            if q.peekfirst().isdigit():
                read_number(q)
            else:
                raise Syntaxfel("Saknad siffra vid radslutet ")
        elif letter!=')':
            raise Syntaxfel("Saknad högerparentes vid radslutet ")
       
        elif letter==')' and q.peek().isdigit():
            read_number(q)
            return

    elif q.peekfirst().isdigit():
        raise Syntaxfel("Felaktig gruppstart vid radslutet1 ")
    raise Syntaxfel("Felaktig gruppstart vid radslutet2 ") 
        
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
    if q.peek()!='/':
            if int(num) > 1:
                return
            #H01011
            elif q.peekfirst()=='0' and q.peek()<=1 or q.peekfirst()=='1' and q.peek().isdigit()!=True:
                
                raise Syntaxfel("För litet tal vid radslutet ")
            
            elif q.peek().isdigit():
                q.dequeue()
                read_number(q)
            
            elif q.peekfirst().isupper():
                read_atom(q)
            else:
                raise Syntaxfel("För litet tal vid radslutet ")
            
          
                
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