from collection import Collection
from author import Author

class Book(Collection, Author):
    def __init__(self, title, author, year):
        super().__init__(title, year)
        self.author = author

    def get_info(self):
        return f'Livro: {self.title}, Autor: {self.author}, Ano: {self.year}'

    def get_author(self):
        return self.author