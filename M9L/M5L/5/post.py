class Post:
    def __init__(self, user, message: str):
        self.user = user
        self.message = message
        self.comments = []

    @classmethod
    def create_post(cls, user, message: str, function):
        return function(user, message)

    def add_comment(self, comment: str):
        self.comments.append(comment)
        return f"Comentário adicionado: '{comment}'"

    def __str__(self):
        return f"Post de {self.user.username}: {self.message} | Comentários: {len(self.comments)}"

def post_text(user, message):
    return Post(user, f"{message}")

def post_image(user, message):
    return Post(user, f"{message} [imagem]")

def post_video(user, message):
    return Post(user, f"{message} [video]")