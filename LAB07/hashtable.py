
#DD1320
#Laboration 7

#more elements in smaller hashtable will increase collisions and decrese efficiency

class Node:
    def __init__(self, key, data=None, next=None):
        self.key=key
        self.data=data
        self.next=next

class Hashtable:
    def __init__(self, size):
        self.hashtable=[None]*2*size
        self.size=len(self.hashtable) 
        self.collisions=0
    
    def store(self, key, data):
        '''
        inserts data into the hashtable
        if: empty
        else: collision adding
        '''
        hashvalue=self.hashfunction(key)
        if self.hashtable[hashvalue]==None:
            self.hashtable[hashvalue]=Node(key, data)
        else:
            self.collisions+=1
            collision=self.hashtable[hashvalue]
            self.hashtable[hashvalue]=Node(key, data)
            self.hashtable[hashvalue].next=collision


    def search(self,key):
        '''
        searches through hashtable
    
        '''
        hashvalue=self.hashfunction(key)
        node=self.hashtable[hashvalue]
        if node != None:
            found = False
            if node.key==key:
                return node.data
            else:
                while not found:
                    node=node.next
                    if node.key==key:
                        return node.data
        else:
            raise KeyError()
        
    def __contains__(self, key):
        if self.hashlist:
            return True
        else:
            return False        
        
    def hashfunction(self,key):
        sum_of_string = 0
        for letter in key:
            sum_of_string = sum_of_string*32 + ord(letter)
        hashvalue = sum_of_string % self.size
        return hashvalue
    
