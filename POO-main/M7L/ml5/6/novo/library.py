from book import Book
from user import User

class Library:
    
    def __init__(self):
        self.__books = []

    def getUserName(self, user: User):
        return user.getUserName()

    def getBooks(self):
        return self.__books

    def showBooks(self):
        for book in self.__books:
            print(book)

    def userBooks(self, user: User):
        user.showUserBooks()

    def registerBook(self, book: Book):
        self.__books.append(book)

    def bookIdx(self, bookName):
        for i, book in enumerate(self.__books):
            if book.getName() == bookName:
                return i
        return -1
    
    def takeBook(self, bookName, user: User):
        if self.bookDisponibility(bookName):
            idx = self.bookIdx(bookName)
            user.addBook(self.__books[idx])
            self.decreaseBookAmount(idx)
        else:
            print("Livro não encontrado para empréstimo.")

    def decreaseBookAmount(self, idx):
        book = self.__books[idx]
        book.setAmount(book.getAmount() - 1)
 
    def bookDisponibility(self, bookName):
        idx = self.bookIdx(bookName)
        if idx != -1:
            return self.__books[idx].getAmount() > 0
        return False
    
    @staticmethod
    def verifyUserBooks(bookName, user: User):
        return bookName in [book.getName() for book in user.getUserBooks()]

    def returnBook(self, bookName, user: User): 
        if self.verifyUserBooks(bookName, user):
            user.returnUserBook(bookName)
            idx = self.bookIdx(bookName)
            if idx != -1:
                self.increaseBookAmount(idx)

    def increaseBookAmount(self, idx):
        book = self.__books[idx]
        book.setAmount(book.getAmount() + 1)

