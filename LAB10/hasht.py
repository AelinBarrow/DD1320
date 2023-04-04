class HashNode:
    def __init__(self,key,object,next):
        self.key = key
        self.object = object
        self.next = next

class Hashtabell:
    def __init__(self, size):
        self.size = size*2+1
        self.slots = [None]*self.size
        self.col = 0
        
    def __getitem__(self, key):
        return self.get(key)
    def put(self,key,object):
        hashKey = hashfunction(key, self.size)
        if not exist(self,hashKey,self.size):
            self.slots[hashKey] = HashNode(key,object, None)
        else:
            self.col += 1
            copy = False
            node = self.slots[hashKey]
            while node.next != None:
                if node.key == key:
                    print('Key already exists. Object will be overwritten')
                    copy = True
                    break
                node = node.next
            if copy:
                node.object = object
            else:
                node.next = HashNode(key,object, None)
    def get(self,key):
        d = {}
        hashKey = hashfunction(key,self.size)
        if exist(self,hashKey,self.size):
            node = self.slots[hashKey]
            while (node.key != key) and (node.next != None):
                node = node.next
            if node.key == key:
                return node.object
            else:
                d['1'] #Genererar KeyError
        else:
            d['1']
def hashfunction(key, size):
    result = 0
    for tecken in key:
        result = result*32 + ord(tecken)
    return (result%size)

def exist(hashtabell,hashKey,size):
    if hashtabell.slots[hashKey] == None:
        return False
    else:
        return True