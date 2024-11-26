class Library:
    def __init__(self):
        self.collection = []

    def add_item(self, item):
        self.collection.append(item)

    def display_collection(self):
        for item in self.collection:
            print(item.get_info())