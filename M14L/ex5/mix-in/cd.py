from collection import Collection
from mixins import ArtistMixin

class CD(Collection, ArtistMixin):
    def __init__(self, title, artist, year):
        ArtistMixin.__init__(self, artist)
        Collection.__init__(self, title, year)

    def get_info(self):
        return f'CD: {self.title}, Artista: {self.artist}, Ano: {self.year}'