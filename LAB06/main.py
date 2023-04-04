import timeit

class Song():
    '''
    klass som representerar ett låt
    '''
    def __init__(self, trackid, songid, artist, name):
        #creates a song object with all the attributes bellow
        self.trackid=trackid
        self.songid=songid
        self.artist=artist
        self.name=name

    
    def __lt__(self, other):
        #compares artist names
        return self.artist < other.artist
        

def readfile(input_file): #reading of a file
    song_list=[]
    song_dict={}
    with open (input_file, 'r', encoding = "utf-8") as songs:
        #opens the song file
        for row in songs:
            row=row.strip("\n")
            song=row.split("<SEP>") #gets rid of <sep>
            
            song_data=Song(song[0], song[1], song[2], song[3]) #instead of having for loop for each, much quicker
            #first column, second....
            song_list.append(song_data) #puts song-objects into the empty list we created
            song_dict[song[2]]=song_data
            #small_list=song_list[0:250000]
            
    return song_list, song_dict
            
def linear_search(list_song, key):
    for x in list_song:
        if key == x.artist:
            return True
    return False

        
def binary_search(list, artist):
    
    #below taken from lecture 4 
    low=0
    high=len(list)-1
    found=False

    while low <= high and not found:
        middle=(low+high)//2 #heltalsdivision
        if list[middle].artist==artist:
            found=True
        else:
            if artist < list[middle].artist:
                high=middle-1
            else:
                low=middle+1
    return found
    

def dict_search(dict, artist):
    final=dict[artist]
    

def main():
    
    filename = "unique_tracks.txt.crdownload"
   
    lista, dict = readfile(filename)
    
    lista=lista[0:250000]
    n = len(lista)
    
    print("Antal element =", n)

    sista = lista[n-1]
    #sista=lista[n-1] #last element
    testartist = sista.artist
    
    linjtid = timeit.timeit(stmt = lambda: linear_search(lista, testartist), number = 100)
    print("Linjärsökningen tog", round(linjtid, 4) , "sekunder")
'''
    lista.sort() #sorts the list in ascending order
    bintid= timeit.timeit(stmt = lambda: binary_search(lista, testartist), number = 10000)
    print("Binärtsökningen tog", round(bintid, 4) , "sekunder")

    dicttid=timeit.timeit(stmt = lambda: dict_search(dict, testartist), number = 10000)
    print("Dictsökningen tog", round(dicttid, 4) , "sekunder")
'''

main()