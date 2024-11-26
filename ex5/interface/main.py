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

'''
Collection: Define um método abstrato get_info(), que deve ser implementado por qualquer classe que herde dela.
Author: Define um método abstrato get_author(), que deve ser implementado por classes que precisam fornecer informações sobre um autor.
Artist: Define um método abstrato get_artist(), que deve ser implementado por classes que precisam fornecer informações sobre um artista.
Director: Define um método abstrato get_director(), que deve ser implementado por classes que precisam fornecer informações sobre um diretor.
Issue: Define um método abstrato get_issue(), que deve ser implementado por classes que precisam fornecer informações sobre uma edição.
'''