from animal import Animal

class Cachorro(Animal):
    def emitir_som(self):
        return 'O cachorro está latindo.'

    def comer(self):
        return 'O cachorro come ração.'