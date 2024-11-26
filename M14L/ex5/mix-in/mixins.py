class AuthorMixin:
    def __init__(self, author):
        self.author = author

class ArtistMixin:
    def __init__(self, artist):
        self.artist = artist

class DirectorMixin:
    def __init__(self, director):
        self.director = director

class IssueMixin:
    def __init__(self, issue):
        self.issue = issue