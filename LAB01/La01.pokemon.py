#DD1320
#Michaela Jankulicova
#Lab01

import random
import csv

class Pokemon:
    #minst fem metoder
    def __init__(self, number,name, type1, type2, total, hp, attack, defense, spatk, spdef, speed, generation, legendary): #attribut för varje egenskap
        self.number=number
        self.name=name
        self.type1=type1
        self.type2=type2
        self.total=total
        self.hp=hp
        self.attack=attack
        self.defense=defense
        self.spatk=spatk
        self.spdef=spdef
        self.speed=speed
        self.generation=generation
        self.legendary=legendary

    def __str__(self):
        return 
    
    def __lt__(self):
        return

    def attackDmg(self):
        return self.attack + random.randint(0,1)*self.spAtk
    
    def health(self, attack_by_enemy):
        return self.hp - attack_by_enemy + random.randint(0,1)*self.defense

    def __str__(self):
        return ("Din pokemon heter " + self.namn.title() + " och har dessa attributer\n" +
            "Typ1: " + self.typ1 + "\n" +
            "Typ2: " + self.typ2 + "\n" +
            "Total: " + self.total + "\n" +
            "HP: " + self.hp + "\n" +
            "Attack: " + self.attack + "\n" +
            "Defense: " + self.defense + "\n" +
            "Sp. Atk: " + self.spAtk + "\n" + 
            "Sp. Def: " + self.spDef + "\n" +
            "Speed: " + self.speed + "\n" +
            "Generation: " + self.generation + "\n"
            "Legendary: " + str(self.legendary))

#funktion som skapar ett pokemon objekt-testa metoderna
"""
funktion som:
läser in alla rader från filen --->done
skapar objekt --> does it?
lagrar objektet i en lista (Pythons list()) ---> yes
returnerar listan --->yes
"""
#Funktion för att söka efter en pokemon i listan
def search_pokemon():
    return

def read():
    #opens file
    with open('pokemon.csv', 'r') as file:
        characteristics=['number', 'name', 'type1', 'type2', 'total', 'hp', 'attack', 'defense', 'spatk', 'spdef', 'speed', 'generation', 'legendary']
        reader=csv.DictReader(file, delimiter='\t', fieldnames=characteristics) #DictReader splits the rows into categories
        header=next(reader)                         #skips the header
    entry=input("Write the number/name of the pokemon you wnat to see, write All if you want to see all: ")
    if entry=="All": #doesnt work
        for key, value in reader.items():
            print("Number" + str(key))
            print("Name" + value + "\n")
    elif reader.insert(entry)==True:
        print("It works")
    reader.close()

def write(): #skapar nytt pokemon
    #writting in file
    with open('pokemon.csv', 'a',newline='') as file:
        characteristics=['number', 'name', 'type1', 'type2', 'total', 'hp', 'attack', 'defense', 'spatk', 'spdef', 'speed', 'generation', 'legendary']
        writer=csv.DictWriter(file, fieldnames=characteristics) #sorts the file into pokemon characteristics
        number_rows=pd.read_csv('pokemon.csv')                  #gives number of rows in the csv file
        writer.writerow({'number':(len(number_rows)-79)+1, 'name':input('Write the name of your pokemon:'),  })
        writer.close()
        return writer


def menu():
    ch=0
    print('Menu: ') #prints the whole menu
    while ch==0: #condition for jumping out of the loop
        ch=input('Choose a menu option: ') #initial input
        if ch==1:

            break
        elif ch==2:
            break
        elif ch==3:
            break
        elif ch==4:
            break
        else:
            continue


