from collectionService import CollectionService

class LibraryService(CollectionService):
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def show_items(self):
        for item in self.items:
            print(item.get_info())