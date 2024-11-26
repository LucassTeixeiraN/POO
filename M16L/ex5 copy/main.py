'''Implemente um sistema de Biblioteca com os tipos de acervo (livro, revista, DVD, CD,
etc.), evidenciando a classe Collection como uma classe abstrata.'''

from book import Book
from magazine import Magazine
from dvd import DVD
from cd import CD
from libraryService import LibraryService

def main():
    library_service = LibraryService()

    # Criando instâncias de cada tipo de acervo
    book = Book("1984", "George Orwell", 1949)
    magazine = Magazine("National Geographic", "January 2023", 2023)
    dvd = DVD("Inception", "Christopher Nolan", 2010)
    cd = CD("Thriller", "Michael Jackson", 1982)

    # Adicionando itens ao serviço de biblioteca
    library_service.add_item(book)
    library_service.add_item(magazine)
    library_service.add_item(dvd)
    library_service.add_item(cd)

    # Mostrando informações de cada acervo
    library_service.show_items()

if __name__ == "__main__":
    main()


# os módulos de alto nível (o serviço da biblioteca) dependem de abstrações (a interface CollectionService)
#  e não de implementações concretas.
