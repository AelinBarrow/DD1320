from bintreeFileV2 import Bintree
from linkedQFileV2 import LinkedQ
from parentfile import ParentNode

swedish=Bintree() #ordlistan
dumbkids=Bintree()   #dumbarn

q=LinkedQ() #creates a queue

with open("word3.txt", 'r', encoding = "utf-8") as swedishfile:
    for row in swedishfile:
        word=row.strip()
        if word not in swedish:
            swedish.put(word) #puts all the words into our swedish binary tree

def makechildren(startword, q, finishword):
    alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] #for-loop to compare each list element 
    print(startword)
    for i in range(0, startword.__len__()): #lenght of the word
        for letter in alphabet:
            word=startword.word[:i]+ letter+ startword.word[i+1:]
            if word in swedish and word not in dumbkids:
                
                if word==finishword:
                    new_kid=ParentNode(word, startword)
                    new_kid.writechain(new_kid)
                    return True
                    
                else:
                    new_kid=ParentNode(word, startword)
                    q.enqueue(new_kid) #new word in the queue
                    dumbkids.put(new_kid.word) #new word into the bintrre of dumbkids
                    if q.isEmpty():
                        print("There is no path between ", firstword, "and ", lastword)
                        break
                    else:
                        continue



               
                
            
             
                    
                    
                

if __name__=="__main__":
    firstword=input("Start: ")
    lastword=input("Finish: ")
    
    p=ParentNode(firstword) #creates Node-object 
    q.enqueue(p) #puts the first parentnode into the queue
    while not q.isEmpty():
        node=q.dequeue()

        if makechildren(node, q, lastword):
            print("There is a path to", lastword)
            break

        elif q.isEmpty():
                print("There is no path between ", firstword, "and ", lastword)

        