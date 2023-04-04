class Song():
    '''
    klass som representerar ett låt
    '''
    def __init__(self, trackid, songid, artist_name, song_name):
        #creates a song object with all the attributes bellow
        self.trackid=trackid
        self.songid=songid
        self.artist_name=artist_name
        self.song_name=song_name

    
    def __lt__(self, other):
        #compares artist names
        return self.artist_name < other.artist_name
    
