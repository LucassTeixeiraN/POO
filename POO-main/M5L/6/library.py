'''6. Implemente uma classe chamada Library que represente uma biblioteca virtual. Essa
classe deve permitir cadastrar livros, fazer empréstimos, devolver livros e verificar a
disponibilidade de um livro.'''

class Library:
    __books = {
        "Harry Potter": 3,
        "Senhor dos Aneis": 1,
        "Dom Casmurro": 4
    }

    def __init__(self, name):
        self.__name = name
        self.__userBooks = []

    def getName(self):
        return self.__name
    
    def getUserBooks(self):
        return self.__userBooks


    @classmethod
    def getBooks(cls):
        i = 1
        for key, value in cls.__books.items():
            print(f"{i}. {key}: {value} unidades restantes")
            i += 1 
        print("-"*60)

    @classmethod
    def registerBook(cls, bookName, amount):
        cls.__books[bookName] = amount

    def takeBook(self, bookName):
        self.__userBooks.append(bookName)
        # print(self.__userBooks)

    @classmethod
    def decreaseBookAmount(cls, bookName):
        cls.__books[bookName] -= 1
        # print(cls.__books)
    
    @classmethod
    def bookDisponibility(cls, bookName):
        if cls.__books.get(bookName) != None and cls.__books.get(bookName) > 0:
            return True
        return False

    def returnBook(self, bookName):
        bookIndex = self.__userBooks.index(bookName)
        del self.__userBooks[bookIndex]

    @classmethod
    def increaseBookAmount(cls, bookName):
        cls.__books[bookName] += 1




