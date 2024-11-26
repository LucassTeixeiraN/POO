from collection import Collection
from abc import ABC, abstractmethod

# Interfaces
class Author(ABC):
    @abstractmethod
    def get_author(self):
        pass

class Artist(ABC):
    @abstractmethod
    def get_artist(self):
        pass

class Director(ABC):
    @abstractmethod
    def get_director(self):
        pass

class Issue(ABC):
    @abstractmethod
    def get_issue(self):
        pass

# Classes concretas
class Book(Collection, Author):
    def __init__(self, title, author, year):
        super().__init__(title, year)
        self.author = author

    def get_info(self):
        return f'Livro: {self.title}, Autor: {self.author}, Ano: {self.year}'

    def get_author(self):
        return self.author

class Magazine(Collection, Issue):
    def __init__(self, title, issue, year):
        super().__init__(title, year)
        self.issue = issue

    def get_info(self):
        return f'Revista: {self.title}, Edição: {self.issue}, Ano: {self.year}'

    def get_issue(self):
        return self.issue

class CD(Collection, Artist):
    def __init__(self, title, artist, year):
        super().__init__(title, year)
        self.artist = artist

    def get_info(self):
        return f'CD: {self.title}, Artista: {self.artist}, Ano: {self.year}'

    def get_artist(self):
        return self.artist

class DVD(Collection, Director):
    def __init__(self, title, director, year):
        super().__init__(title, year)
        self.director = director

    def get_info(self):
        return f'DVD: {self.title}, Diretor: {self.director}, Ano: {self.year}'

    def get_director(self):
        return self.director