from book import Book

class User: 
    
    def __init__(self, userName):
        self.__userName = userName
        self.__userBooks = []

    def getUserName(self):
        return self.__userName
    
    def getUserBooks(self):
        return self.__userBooks
    
    def showUserBooks(self):
        for i in self.getUserBooks():
            print(f"{i.getName()}")
    
    def setUserName(self, name):
        self.__userName = name

    def addBook(self, book: Book):
        self.__userBooks.append(book)

    def returnUserBook(self, bookName):
        for book in self.__userBooks:
            if book.getName() == bookName:
                self.__userBooks.remove(book)
                break