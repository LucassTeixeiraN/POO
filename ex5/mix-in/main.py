'''Implemente um sistema de Biblioteca com os tipos de acervo (livro, revista, DVD, CD,
etc.), evidenciando a classe Collection como uma classe abstrata.'''

from book import Book
from magazine import Magazine
from dvd import DVD
from cd import CD

def main():
    book = Book("1984", "George Orwell", 1949)
    magazine = Magazine("National Geographic", "January 2023", 2023)
    dvd = DVD("Inception", "Christopher Nolan", 2010)
    cd = CD("Thriller", "Michael Jackson", 1982)

    print(book.get_info())
    print(magazine.get_info())
    print(dvd.get_info())
    print(cd.get_info())

if __name__ == "__main__":
    main()

# As classes de coleção (Book, CD, DVD, Magazine) herdam de Collection e do mixin apropriado,
# permitindo que cada classe tenha os atributos relevantes sem duplicação de código.