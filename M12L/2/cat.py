from animal import Animal

class Cat(Animal):

    def __init__(self, name):
        super().__init__(name)

    def meow(self):
        pass

    def walk(self) -> str:
        print("O gato está andando")
