'''Implemente um sistema de Biblioteca com os tipos de acervo (livro, revista, DVD, CD,
etc.), evidenciando a classe Collection como uma classe abstrata.'''

from book import Book
from magazine import Magazine
from dvd import DVD
from cd import CD
from library import Library

def main():
    # Criando instâncias de cada tipo de acervo
    book = Book("1984", "George Orwell", 1949)
    magazine = Magazine("National Geographic", "January 2023", 2023)
    dvd = DVD("Inception", "Christopher Nolan", 2010)
    cd = CD("Thriller", "Michael Jackson", 1982)

    # Criando uma biblioteca
    library = Library()

    # Adicionando itens à biblioteca
    library.add_item(book)
    library.add_item(magazine)
    library.add_item(dvd)
    library.add_item(cd)

    # Exibindo a coleção da biblioteca
    library.display_collection()

if __name__ == "__main__":
    main()

# a classe Library contém (ou agrega) várias instâncias de outras classes, representando uma relação "tem um" entre a biblioteca e seus itens.


