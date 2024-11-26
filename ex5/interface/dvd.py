from collection import Collection
from director import Director

class DVD(Collection, Director):
    def __init__(self, title, director, year):
        super().__init__(title, year)
        self.director = director

    def get_info(self):
        return f'DVD: {self.title}, Diretor: {self.director}, Ano: {self.year}'

    def get_director(self):
        return self.director