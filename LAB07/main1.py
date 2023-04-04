from pokemon import Pokemon
from dicthash import DictHash
from hashtable import Hashtable

def readfiles(hashlist):
    with open("pokemon.csv", encoding="utf8") as pokemonfile:
        i = 0
        for rad in pokemonfile:
            if i == 0:
                pass
            else:
                L = rad.split(",")

                hashlist.store(L[1].lower(), Pokemon(L[1].lower(),L[2],L[3],L[4],L[5],L[6],L[7],L[8],L[9],L[10],L[11],L[12].strip("\n")))
            i += 1



if __name__ == "__main__":
    hashlist = Hashtable(1400)
    readfiles(hashlist)

    user_input = input("What pokemon are you looking for? ").lower()
    hashlist.search(user_input)
    print("Total number of collisions: " + str(hashlist.collisions))
    print("The final table size is: " + str(hashlist.size))
    
