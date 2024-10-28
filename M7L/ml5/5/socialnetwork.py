from user import User

class SocialNetwork:
    def __init__(self):
        self.users = []

    def add_user(self, username: str):
        user = User(username)
        self.users.append(user)

    def list_users(self):
        return [user.username for user in self.users] if self.users else "Nenhum usuário cadastrado ainda."

    def _find_user(self, username: str):
        for user in self.users:
            if user.username == username:
                return user
        return None

    def find_user(self, username: str):
        user = self._find_user(username)
        if user:
            return user
        return f"Usuário {username} não encontrado."