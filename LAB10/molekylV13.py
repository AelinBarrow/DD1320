from linkedQFileV2 import LinkedQ
import sys
from molgrafik import *
from atomlista import *

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
    mol = read_group(q)
    if q.peek().isupper() or q.peek().islower() or q.peek().isdigit() or q.peek()=='(':
        mol.next=read_molecule(q)
    return mol

def read_group(q):
    rutan = Ruta() 
    if q.peek()=='/':
        return rutan
    if q.peek() == '(': 
        q.dequeue()
        if q.peek() == ')':
            raise Syntaxfel('Felaktig gruppstart vid radslutet ')
        rutan.down=read_molecule(q)
        if q.peek() != ')':
            raise Syntaxfel('Saknad högerparentes vid radslutet ')
        q.dequeue()
        if not q.peek().isdigit():
            raise Syntaxfel('Saknad siffra vid radslutet ')
        rutan.num=read_number(q)
        return rutan
    rutan.atom=read_atom(q) 
    rutan.num=read_number(q)
    return rutan


def read_atom(q):
    if q.peek().isdigit() or q.peek()==')':
        raise Syntaxfel("Felaktig gruppstart vid radslutet ")
    if q.peek().isupper()!=True and q.peek()!=')':
        raise Syntaxfel("Saknad stor bokstav vid radslutet ")
    letter=q.dequeue()
    dq.enqueue(letter)

    if q.peek().islower():
        lower=q.dequeue()
        dq.enqueue(lower)
    if str(dq.printq())in atoms:
        atom=str(dq.printq())
        while dq.isEmpty()!=True: #empties the second queue
            dq.dequeue()
        return atom
    else:
        while dq.isEmpty()!=True: #empties the second queue
            dq.dequeue()
        raise Syntaxfel("Okänd atom vid radslutet ")

    

def read_number(q): 
    if q.peek().isdigit():
            num = q.dequeue()
            if num == "0":
                raise Syntaxfel("För litet tal vid radslutet ")
            if num == "1":
                if not q.peek().isdigit():
                    raise Syntaxfel("För litet tal vid radslutet ")
            while not q.isEmpty():
                if q.peek().isdigit() == True:
                    q.dequeue()
                else:
                    return int(num)       
    return True
                
def store_molecule(molecule):
    q = LinkedQ()
    molecule = list(molecule)
    for letter in molecule:
        q.enqueue(letter)
    q.enqueue("/") #to just know end of the input
    return q

def check_syntax(molecule):
    while True:
        q = store_molecule(molecule)
        try:
            mol=read_molecule(q)
            if not q.isEmpty():
                if q.peek() == ")":
                    mol=read_molecule(q)
            molmass = atom_weight(mol)
            mg = Molgrafik() #molgrafik object
            mg.show(mol) #uses molgrafik method
            return ("Weight of the molecule " + str(molecule)+ " is " + str(molmass))
        except Syntaxfel as fel:
            return str(fel) + str(q)

def atom_weight(atom):
    '''
    atom=weight and name 
    based on the number of atoms (atoms)*weight of one
    we can go=down or next
    -i check first if there is any input
    -then i check if there is down or next
    -if there is down i go down first
    -if not then i go next

    '''
    
    if atom != None:
        #if
        #atom.down
        #else
        #atom.next
        atoms = skapaAtomlista() #atomlista function
        hashtable = lagraHashtabell(atoms) #atomlista function that uses hashtable file
        if atom.down:
            #rekursion, as long as there is down, it goes down
            weight_single=atom_weight(atom.down)
            amount=atom.num
            weight = weight_single*amount
        else:
            finder= hashtable.search(atom.atom).vikt #searches 
            weight_single = int(atom.num) 
            weight=finder*weight_single
        return weight + atom_weight(atom.next)
    return True
            
for line in sys.stdin:
    if '#' == line.rstrip():
        break
    resultat = check_syntax(line)
    print(resultat)

