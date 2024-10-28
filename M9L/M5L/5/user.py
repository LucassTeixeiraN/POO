from post import Post

class User:
    def __init__(self, username: str):
        self.username = username
        self._friends = []
        self.posts = []

    def add_friend(self, friend):
        if friend not in self._friends:
            self._friends.append(friend)
            friend._friends.append(self)
            return f"{friend.username} foi adicionado(a) como amigo(a)."
        return f"{friend.username} já é seu amigo."

    def post_message(self, message: str, function):
        new_post = Post.create_post(self, message, function)
        self.posts.append(new_post)
        return f"Mensagem publicada: '{message}'"

    def get_friends(self):
        return [friend.username for friend in self._friends]
    
    def get_posts(self):
        return [(i + 1, self.posts[i].message) for i in range(len(self.posts))]

    def __str__(self):
        return f"Usuário: {self.username}"