from collection import Collection

class DVD(Collection):
    def __init__(self, title, director, year):
        super().__init__(title, year)
        self.director = director

    def get_info(self):
        return f'DVD: {self.title}, Diretor: {self.director}, Ano: {self.year}'