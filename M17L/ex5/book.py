from collection import Collection

class Book(Collection):
    def __init__(self, title, author, year):
        super().__init__(title, year)
        self.author = author

    def get_info(self):
        return f'Livro: {self.title}, Autor: {self.author}, Ano: {self.year}'