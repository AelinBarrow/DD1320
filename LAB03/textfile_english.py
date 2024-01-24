#DD1320

#Laboration 3


from bintreeFile import Bintree

svenska=Bintree()
english=Bintree() #creates two trees, one for each language

with open("word3.txt", "r", encoding = "utf-8") as svenskfil:
    for rad in svenskfil:
        ordet = rad.strip()                #seperates the rows
        if ordet in svenska:
            print(ordet, end = " ") 
        else:
            svenska.put(ordet)             #puts the words in the tree
print("\n")


with open('engelska.txt', 'r', encoding = "utf-8") as englishfile:
    for row in englishfile:
        word=row.split() 
        for element in word:            #takes each element of the word list so we get str() to compare later on
            if element not in english:  #if the element isnt already in the tree it will be addded
                english.put(element) 
                if svenska.__contains__(element): #returns true if the word is in the swedish tree
                    print(element, end=' ')

print("\n")


