from post import Post

class User:
    def __init__(self, name):
        self.name = name
        self.friends = []
        self.posts: list[Post] = []

    def add_friend(self, friend):
        if friend not in self.friends:
            self.friends.append(friend)
            friend.friends.append(self) 
            print(f"{self.name} e {friend.name} são amigos.")

    def create_post(self, post: Post):
        self.posts.append(post)
        print(f"{self.name} publicou: {post.message}")

    def comement_post(self, post: Post, comentario):
        post.add_comment(comentario, self)
    
    def __str__(self):
        return self.name