#DD1320
#Michaela Jankulicova
#Laboration 4
from bintreeFileV2 import Bintree
from linkedQFileV2 import LinkedQ


swedish=Bintree() #ordlistan
dumbkids=Bintree()   #dumbarn

q=LinkedQ() #creates a queue

def makechildren(startword, q):
    alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'ö', 'å', 'ä'] #for-loop to compare each list element 
    for i in range(0, len(startword)):
        for letter in alphabet:
            word=startword[:i]+ letter+ startword[i+1:]
            if word in swedish and word not in dumbkids:
                dumbkids.put(word)
                q.enqueue(word)
         
                   
with open("word3.txt", 'r', encoding = "utf-8") as swedishfile:
    for row in swedishfile:
        word=row.strip()
        if word not in swedish:
            swedish.put(word) #puts all the words into our swedish binary tree
    

if __name__=="__main__":
    firstword=input("Start: ")
    lastword=input("Finish: ")
    q.enqueue(firstword) #puts the firstword into the queue

    while not q.isEmpty():
        node = q.dequeue()
        
        makechildren(node, q)
        if node==lastword:
            print("There is a path to", lastword)
            break
        elif node !=lastword and node in swedish:
            if q.isEmpty()==True:
                print("There is no path between ", firstword, "and ", lastword)
                break
            else:
                continue
        
        
        