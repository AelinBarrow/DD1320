import timeit
from songFile import Song
from sorting import quicksort, sel_sort

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



def linear_search(list_song, key): #timecomplexity O(n)
    for element in list_song:
        if element == key:
            
            return True
        
    return False

def binary_search(other_list, key): #timecomplexity O(logn)
    #below taken from lecture 4 
    low=0
    high=len(other_list)-1
    found=False

    while low <= high and not found:
        middle=(low+high)//2 #heltalsdivision
        if other_list[middle]==key:
            found=True
        else:
            if key < other_list[middle]:
                high=middle-1
            else:
                low=middle+1
    return found

def dict_search(dict, key): #timecomplexity O(1)
    #creates hash of the key
    #finds the locations connected to the hash value
    final=dict[key.artist_name]

def main():
    
    filename = "unique_tracks.txt.crdownload"
   
    lista, dictionary = readfile(filename)
    
    lista=lista[0:100000]
    n = len(lista)
    
    print("Antal element =", n)

    sista = lista[n-1] #last element 
    testartist = sista
    
    '''quicktid=timeit.timeit(stmt = lambda: quicksort(lista), number = 1)
    print("Quicksortering tog", round(quicktid, 4) , "sekunder")
    
    seltid = timeit.timeit(stmt = lambda: sel_sort(lista), number = 1)
    print("Urvalsortering tog", round(seltid, 4) , "sekunder")'''

    linjtid = timeit.timeit(stmt = lambda: linear_search(lista, testartist), number = 1000) #lambda passes a small function as argument
    print("Linjärsökningen tog", round(linjtid, 4) , "sekunder")

    lista.sort() #sorts the list in ascending order
    bintid= timeit.timeit(stmt = lambda: binary_search(lista, testartist), number = 1000)
    print("Binärtsökningen tog", round(bintid, 4) , "sekunder")

    dicttid=timeit.timeit(stmt = lambda: dict_search(dictionary, testartist), number = 1000)
    print("Dictsökningen tog", round(dicttid, 4) , "sekunder")
   
main()

'''
Väldigt stora skillander i tidskomplexitet mellan alla tre sökmetoder och de två soteringsmetoder ovan.
om man hantera små data mängder syns inte skillanden så tydligt men när man ökar data mängder är linjärsök och urvalsortering nästa oanväntbart
'''