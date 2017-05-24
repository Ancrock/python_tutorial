class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics
    
    def sing_a_song(self):
        for line in self.lyrics:
            print line
            
class Game(object):
    def __init__(self, Name):
        self.name = Name
    
    def set_genre(self, genre):
        self.genre =  genre
    
    def set_rating(self, ratings):
        self.rating = ratings


song1 = Song(["Jack and jill", "Went up the hill"])
song2 = Song(["London Bridge","Is falling down"])

song1.sing_a_song()
song2.sing_a_song()

game1 = Game("Prince of Persia")
game1.set_genre("Action/Adventure")
game2 = Game("God of War")
game2.set_genre("Action/rpg/Mythical")

print game1.name
print game1.genre
print game2.name
print game2.genre
            
            