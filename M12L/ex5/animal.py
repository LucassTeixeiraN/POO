class Animal:
    def emitir_som(self):
        pass

    def caminhar(self):
        return f'{self.__class__.__name__} está caminhando.'

    def comer(self):
        return 'O animal está comendo.'