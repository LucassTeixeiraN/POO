'''6. Implemente uma classe chamada Library que represente uma biblioteca virtual. Essa
classe deve permitir cadastrar livros, fazer empréstimos, devolver livros e verificar a
disponibilidade de um livro.'''

from library import Library
from user import User
from book import Book

def menu():
    print("Bem-vindo à Biblioteca!")
    print("1. Registrar Livros")
    print("2. Visualizar Livros Disponíveis")
    print("3. Procurar Livro pelo Nome")
    print("4. Emprestar Livro")
    print("5. Devolver Livro")
    print("6. Ver Meus Livros")
    print("7. Sair")
    option = input("\nEscolha uma opção: ")
    return option

def errorMessage(str):
    print(str)

def intVerify(num):
    try:
        number = int(num)
        return number
    except ValueError:
        errorMessage("Quantidade inválida")

def bookDispVerify():
    bookName = input("Insira o nome do livro que deseja verificar: ")
    if library.bookDisponibility(bookName):
        print(f"O livro {bookName} está disponível!")
    else:
        print(f"O livro procurado não está disponível ou não existe.")

def bookAlreadyExists(book, bookList):
    for i in bookList:
        if i == book:
            return False
    return True

def userLogin():
    name = input("Insira seu nome: ")
    user = User(name)
    return user

def newBook(num):
    bookName = input("Insira no nome do livro: ")
    bookAmount = input("Insira quantos livros desse serão registrados: ")
    if intVerify(bookAmount):
        book = Book(num, bookName, bookAmount)
        return book
    else:
        newBook()

def main():
    user = userLogin()
    global library
    library = Library()
    booksAmount = 0
    while True:
        if input("Pressione ENTER para mostrar o MENU") == "":
            option = menu()
        match option:
            case '1':
                book = newBook(booksAmount+1)
                if bookAlreadyExists(book, library.getBooks()):
                   library.registerBook(book)
                   booksAmount += 1
                else:
                   errorMessage("Esse livro já está registrado")
            case '2':
                library.showBooks()
            case '3':
                bookDispVerify()
            case '4':
                bookName = input("Insira o nome do livro que deseja pegar emprestado: ")
                library.takeBook(bookName, user)
            case '5':
                bookName = input("Insira o nome do livro que deseja pegar emprestado: ")
                library.returnBook(bookName, )
            case '6':
                print(f"Livros do usuário {library.getUserName(user)}: ")
                library.userBooks(user)
            case '7':
                print("Saindo do programa")
                print("-"*60)
                break
            case _:
                print("Opção inválida")

main()