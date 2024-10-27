class Contact:
    def __init__(self, name, tel):
        self.name = name
        self.tel = tel

    def __str__(self):
        return f"Name: {self.name}, Tel: {self.tel}"

    def update(self, new_name, new_tel):
        self.name = new_name
        self.tel = new_tel
