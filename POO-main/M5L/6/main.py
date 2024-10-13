'''6. Implemente uma classe chamada Library que represente uma biblioteca virtual. Essa
classe deve permitir cadastrar livros, fazer empréstimos, devolver livros e verificar a
disponibilidade de um livro.'''

from library import Library

def menu():
    try:
        print("-"*60)
        option = int(input("Escolha uma opção:\n1- Registrar livros\n2- Visualizar livros disponíveis\n3- Procurar livro pelo nome\n4- Emprestar livro\n5- Devolver livro\n6- Sair do programa\n"))
        print("-"*60)
        return option
    except ValueError:
        print("Opção inválida")

def userLogin():
    name = input("Insira seu nome: ")
    return name

def main():
    library = Library(userLogin())
    while True:
        if input("Pressione ENTER para mostrar o MENU") == "":
            option = menu()
        try:
            match option:
                case 1:
                    bookName = input("Insira no nome do livro: ")
                    bookAmount = int(input("Insira quantos livros desse serão registrados: "))
                    library.registerBook(bookName, bookAmount)
                case 2:
                    library.getBooks()
                case 3:
                    bookSearch = input("Insira no nome do livro que está buscando: ")
                    if library.bookDisponibility(bookSearch):
                        print(f"O livro {bookSearch} está disponível!")
                    else:
                        print(f"O livro procurado não está disponível ou não existe.")
                case 4:
                    bookSearch = input("Insira no nome do livro que deseja pegar emprestado: ")
                    if library.bookDisponibility(bookSearch):
                        library.takeBook(bookSearch)
                        library.decreaseBookAmount(bookSearch)
                    else:
                        print("O livro não está disponível ou não existe.")
                case 5:
                    bookSearch = input("Insira no nome do livro que deseja pegar emprestado: ")
                    if bookSearch in library.getUserBooks():
                        library.returnBook(bookSearch)
                        library.increaseBookAmount(bookSearch)
                    else:
                        print("Você não está com o livro inserido")
                case 6:
                    print("Saindo do programa")
                    print("-"*60)
                    break
                case _:
                    print("Opção inválida")
        except:
            print("Valor inválido")
main()

