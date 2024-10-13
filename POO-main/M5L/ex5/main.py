'''Crie uma classe chamada SocialNetwork que represente uma rede social online. Essa
classe deve ter funcionalidades para adicionar amigos, publicar mensagens,
comentar em posts e buscar por usuários.'''
from socialnetwork import SocialNetwork

def print_menu():
    print("\n--- Menu da Rede Social ---")
    print("1. Adicionar Usuário")
    print("2. Listar Usuários")
    print("3. Adicionar Amigo")
    print("4. Publicar Mensagem")
    print("5. Comentar em um Post")
    print("6. Listar Amigos")
    print("7. Sair")
    print("---------------------------")

def main():
    network = SocialNetwork()
    while True:
        print_menu()
        option = input("Escolha uma opção: ")

        if option == '1':
            username = input("Digite o nome do novo usuário: ")
            network.add_user(username)
            network.list_users()

        elif option == '2':
            print("Usuários cadastrados:", network.list_users())

        elif option == '3':
            user1_name = input("Digite o nome do usuário que deseja adicionar um amigo: ")
            user2_name = input("Digite o nome do amigo a ser adicionado: ")

            user1 = network.find_user(user1_name)
            user2 = network.find_user(user2_name)

            if isinstance(user1, str):
                print(user1)
            elif isinstance(user2, str):
                print(user2)
            else:
                print(user1.add_friend(user2))

        elif option == '4':
            username = input("Digite o nome do usuário que deseja publicar uma mensagem: ")
            user = network.find_user(username)
            if isinstance(user, str):
                print(user)
            else:
                message = input("Digite a mensagem: ")
                print(user.post_message(message))

        elif option == '5':
            username = input("Digite o nome do usuário que deseja comentar em um post: ")
            user = network.find_user(username)

            if isinstance(user, str):
                print(user)
            else:
                if not user.posts:
                    print("Este usuário não possui posts.")
                else:
                    print("Postagens do usuário:")
                    print(user.get_posts())
                    post_index = int(input("Escolha o número do post para comentar: ")) - 1

                    comment = input("Digite o comentário: ")
                    print(user.posts[post_index].add_comment(comment))

        elif option == '6':
            username = input("Digite o nome do usuário para listar amigos: ")
            user = network.find_user(username)

            if isinstance(user, str):
                print(user)
            else:
                print(f"Amigos de {user.username}: {user.get_friends()}")

        elif option == '7':
            print("Saindo da rede social...")
            break

        else:
            print("Opção inválida. Tente novamente.")

main()