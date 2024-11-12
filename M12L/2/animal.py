class Animal:

    def __init__(self, name: str) -> None:
        self.__name = name
        self.__breed = None

    def walk(self) -> str:
        print("O animal está andando")

    def setBreed(self, breed):
        self.__breed = breed

    def getName(self):
        return self.__name
    
    def getBreed(self):
        return self.__breed
    