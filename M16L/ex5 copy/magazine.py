from collection import Collection

class Magazine(Collection):
    def __init__(self, title, issue, year):
        super().__init__(title, year)
        self.issue = issue

    def get_info(self):
        return f'Revista: {self.title}, Edição: {self.issue}, Ano: {self.year}'