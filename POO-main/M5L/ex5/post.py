class Post:
    def __init__(self, user, message: str):
        self.user = user
        self.message = message
        self.comments = []

    @classmethod
    def create_post(cls, user, message: str):
        return cls(user, message)

    def add_comment(self, comment: str):
        self.comments.append(comment)
        return f"Comentário adicionado: '{comment}'"

    def __str__(self):
        return f"Post de {self.user.username}: {self.message} | Comentários: {len(self.comments)}"