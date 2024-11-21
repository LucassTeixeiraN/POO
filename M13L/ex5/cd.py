from collection import Collection

class CD(Collection):
    def __init__(self, title, artist, year):
        super().__init__(title, year)
        self.artist = artist

    def get_info(self):
        return f'CD: {self.title}, Artista: {self.artist}, Ano: {self.year}'