from collection import Collection
from mixins import IssueMixin

class Magazine(Collection, IssueMixin):
    def __init__(self, title, issue, year):
        IssueMixin.__init__(self, issue)
        Collection.__init__(self, title, year)

    def get_info(self):
        return f'Revista: {self.title}, Edição: {self.issue}, Ano: {self.year}'