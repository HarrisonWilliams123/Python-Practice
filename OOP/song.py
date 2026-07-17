import random
class Song:
    def __init__(self, name):
        self.name = name

class Playlist:
    def __init__(self):
        self.playlist = []
    
    def add_song(self, song):
        self.playlist.append(song)
        print(f"Added {song} to the playlist.")
    
    def remove_song(self, song):
        self.playlist.remove(song)
        print(f"Removed: {song}")
    
    def show_playlist(self):
        print(f"Playlist: {self.playlist}")
    
    def shuffle_playlist(self):
        random.shuffle(self.playlist)
        print(f"After shuffle: {self.playlist}")

p1 = Playlist()
p1.add_song("Blinding Lights")
p1.add_song("Levitating")
p1.add_song("Peaches")
p1.show_playlist()
p1.remove_song("Levitating")
p1.shuffle_playlist()    
