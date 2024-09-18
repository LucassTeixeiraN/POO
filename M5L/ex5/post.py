from user import User

class Post:
    def __init__(self, user, message):
        self.user: User = user
        self.message = message
        self.comments: list[tuple[User, str]] = []

    def add_comment(self, comment, user):
        self.comments.append((user, comment))

    def show_post(self):
        print(f"{self.user.name} diz: {self.message}")
        print("Comentários:")
        for user, comment in self.comments:
            print(f"  {user.name}: {comment}")