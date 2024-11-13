from animal import Animal

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
    
    def bark(self):
        pass

    def walk(self) -> str:
        print("O cachorro está andando")