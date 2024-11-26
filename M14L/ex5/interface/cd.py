from collection import Collection
from artist import Artist

class CD(Collection, Artist):
    def __init__(self, title, artist, year):
        super().__init__(title, year)
        self.artist = artist

    def get_info(self):
        return f'CD: {self.title}, Artista: {self.artist}, Ano: {self.year}'

    def get_artist(self):
        return self.artist