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
    if q.peek().isupper() or q.peek().islower() or q.peek().isdigit() or q.peek()=='(' or q.peek()==')':
        read_group(q)
        read_molecule(q)
    return
#Si(C3(COOH)2)4(H2O)7 
def read_group(q):
    if q.peek().isdigit():
        raise Syntaxfel("Felaktig gruppstart ")
    if q.peek()=='(':
        q.dequeue()
        read_molecule(q)
        if q.peek()==')':
            q.dequeue()
            if q.peek().isdigit():
                read_number(q)
                return
            raise Syntaxfel('Saknad siffra vid radslutet ' )
        raise Syntaxfel("Saknad högerparentes vid radslutet ")
    '''if q.peek()==')' and q.peeknext().isdigit():
        q.dequeue()
        read_number(q)
'''
    
    read_atom(q)
    if not q.isEmpty():
        read_number(q)
        

def read_atom(q):
    if q.peek().isupper():
        letter=q.dequeue()
        dq.enqueue(letter)
        if q.peek().islower() and q.isEmpty()!=True:
            letter=q.dequeue()
            dq.enqueue(letter)
    elif q.peek().islower():
        raise Syntaxfel("Saknad stor bokstav vid radslutet " )
    '''  else:
        raise Syntaxfel("Felaktig gruppstart ")
    '''
    if  str(dq.printq()) in atoms:
        while dq.isEmpty()!=True: #empties the second queue
            dq.dequeue()
        return
    elif str(dq.printq()) not in atoms:
        while dq.isEmpty()!=True: #empties the second queue
            dq.dequeue() 
        raise Syntaxfel("Okänd atom vid radslutet ")
    
        
def read_upper(q):
    #checks if the letter is big or small, returns True otherwise raises mistake
    if q.peek().isupper():
        letter=q.dequeue()
        dq.enqueue(letter)
        if q.peek().islower():
            read_lower(q)
            return 
        return
    raise Syntaxfel("Saknad stor bokstav vid radslutet " )
  
def read_lower(q):
    #comes always here and returns always True but takes only small letters from the queue
    letter=q.dequeue()
    dq.enqueue(letter)
    return
   
def read_number(q): 
    if q.peek().isdigit():
            first = q.dequeue()
            if first == "0":
                raise Syntaxfel("För litet tal ")
            if first == "1":
                if not q.peek().isdigit():
                    raise Syntaxfel("För litet tal ")
            while not q.isEmpty():
                if q.peek().isdigit() == True:
                    q.dequeue()
                else:
                    return True
          
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
        if q.peek()!='/':
            raise Syntaxfel('Felaktig gruppstart')
        return "Formeln är syntaktiskt korrekt"
    except Syntaxfel as fel:
        return str(fel) + str(q)

for line in sys.stdin:
    if '#' == line.rstrip():
        break
    resultat = check_syntax(line)
    print(resultat)

