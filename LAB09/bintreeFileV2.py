#DD1320

#Laboration 4

'''
Startord: söt
Slutord: sur
Det finns en väg från söt till sur.
'''

'''
1. Lägg ursprungsordet som första och enda ord i en kö.
2.Upprepa sedan följande så länge det finns ord kvar i kön:
    Plocka ut det första ordet ur kön,
    ...skapa alla barn till det,
    ...och lägg in dom sist i kön.

'''
#DD1320
#Michaela Jankulicova
#Laboration 3

class Node():
    '''
    Node-object with one attribute for data and one attribute 
    left and one right, binary tree expands to either direction
    '''
    def __init__(self, value, left=None, right=None):
        self.value=value
        self.left=left
        self.right=right

class Bintree():
    def __init__(self, root=None):
        '''
        Binary tree starts with a root
        '''
        self.root=root

    def put(self, newvalue):
        self.root =putta(self.root, newvalue) #recursive function untill it reaches an empty spot for a new Node-object

    def __contains__(self,value):
        # True if the value already exists, False otherwise
        return finns(self.root,value)

    def write(self):
         # Prints out in in-order (from smallest to biggest)
        skriv(self.root)
        print("\n")
            

def putta(root, value):
    if root==None: #once there are no more Node-objects it creates a new one, Best case
        return Node(value)
    if value < root.value:
        root.left=putta(root.left, value) #goes left
    else: 
        root.right=putta(root.right, value) #goes right
    
    return root
    
def skriv(root):
    if root != None:
        skriv(root.left) #L
        print(root.value) #P
        skriv(root.right) #R

def finns(root, value):
    #returns value for us to see
    if root == None: #end of the tree
        return False
    if value == root.value:
        return True
    if value < root.value: 
        return finns(root.left, value) #goes left
    if value > root.value: 
        return finns(root.right, value) #goes right
