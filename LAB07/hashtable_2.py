import sys

class HashNode:
    def __init__(self, value, key):
        self.value=value
        self.key=key

class Hashtable:
    def __init__(self, size):
        self.size=size
        self.HD=[None]*size
        print("nu skapas en dict med storlek med storlek", size)

    def __contains__(self, nyckel):
        pass
        # return check_keyerror(nyckel)

    def store(self, key, data):
        hkey=hash2(key, self.size)
        if self.HD[hkey] is None:
            self.HD[hkey]=[HashNode(data, hkey)]
        else:
            conflict_list=self.HD[hkey]
            conflict_list.append(HashNode(data, hkey))
            self.HD[hkey]=conflict_list

    def search(self, key):
        key_hashed=hash2(key, self.size)
        try:
            if self.HD[key_hashed] is not None:
                returnlist=[]
                for i in range(len(self.HD[key_hashed])):
                    if key == self.HD[key_hashed][i].value.namn:
                        returnlist.append(self.HD[key_hashed][i])
                if len(returnlist) != 0:
                    return returnlist
            raise KeyError
        except KeyError:
            print("KeyError, artisten finns inte i listan")
            sys.exit()

def hash2(s,size):             # Beräknar hashkoden för en sträng enligt
    result = 0            # s[0]*32^[n-1] + s[1]*32^[n-2] + ... + s[n-1]
    for c in s:                    
        result = result*32 + ord(c)
    # print(result%size)#, "\n")
    return (result%size)