from user import User

class SocialNetwork:
    def __init__(self):
        self.users = []

    def add_user(self, nome):
        user = User(nome)
        self.users.append(user)
        print(f"Usuário {nome} adicionado à rede social.")

    def search_user(self, nome):
        for user in self.users:
            if user.nome == nome:
                return user
        return None

    def adicionar_amigos(self, nome1, nome2):
        user1 = self.buscar_User(nome1)
        user2 = self.buscar_User(nome2)
        if user1 and user2:
            user1.adicionar_amigo(user2)
        else:
            print("Um ou ambos os usuários não foram encontrados.")

    def publicar(self, nome, mensagem):
        user = self.buscar_User(nome)
        if user:
            user.publicar_mensagem(mensagem)
            return Post(user, mensagem)
        else:
            print("Usuário não encontrado.")