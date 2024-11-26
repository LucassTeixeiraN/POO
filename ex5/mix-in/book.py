from collection import Collection
from mixins import AuthorMixin

class Book(Collection, AuthorMixin):
    def __init__(self, title, author, year):
        AuthorMixin.__init__(self, author)
        Collection.__init__(self, title, year)

    def get_info(self):
        return f'Livro: {self.title}, Autor: {self.author}, Ano: {self.year}'