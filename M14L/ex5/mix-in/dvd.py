from collection import Collection
from mixins import DirectorMixin

class DVD(Collection, DirectorMixin):
    def __init__(self, title, director, year):
        DirectorMixin.__init__(self, director)
        Collection.__init__(self, title, year)

    def get_info(self):
        return f'DVD: {self.title}, Diretor: {self.director}, Ano: {self.year}'