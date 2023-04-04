'''
1. Create a Node-object
2. Assign root to point at the object
3. 2 scenarios- Linked list is empty
              - Linked list has a root
4. Point at the left and the right
5. create new node for left and for right---> new root node
6. comparing the new value
7. if its less than the root ---> left
-is left empty?
8. more than the root---> right
-is right empty?
9. Add the new value as a new node-object value attribute
'''



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
        self.root =putta(self.root, newvalue)

    def __contains__(self,value):
        # True om value finns i trädet, False annars
        return finns(self.root,value)

    
    def write(self):
         # Skriver ut trädet i inorder
        skriv(self.root)
        print("\n")
            


def putta(root, value):
    if root==None:
        return Node(value)
    if value < root.value:
        root.left=putta(root.left, value)
    else: 
        root.right=putta(root.right, value)
    
    return root
    
def skriv(root):
    if root != None:
        skriv(root.left) #L
        print(root.value) #P
        skriv(root.right) #R

def finns(root, value):
    #returnar värdet för oss att se
    if root == None: #när man når slutet av trädet
        return False
    if value == root.value:
        return True
    if value < root.value: 
        return finns(root.left, value) #vandra åt vänster
    if value > root.value: 
        return finns(root.right, value) #vandra åt höger

 
