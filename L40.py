class Song():

    def __init__(self, lyrics):
        self.lyrics = lyrics

    
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday_line1 = "Happy birthday to you", "I don't want to get sued"
happy_bday_line2 = "So I'll stop right there"

happy_bday = Song([happy_bday_line1, happy_bday_line2])


bull_song_line1 = "They rally around tha family"
bull_song_line2 = "With pockets full of shells"
bulls_on_parade = Song([bull_song_line1, bull_song_line2 ])


happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()

