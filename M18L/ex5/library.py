from book import Book
from magazine import Magazine
from dvd import DVD
from cd import CD

class Library:
    def __init__(self):
        self.collection = []

    def add_item(self, item):
        if isinstance(item, (Book, Magazine, DVD, CD)):
            self.collection.append(item)
        else:
            raise ValueError("Item must be a Book, Magazine, DVD, or CD.")

    def list_items(self):
        for item in self.collection:
            print(item.get_info())