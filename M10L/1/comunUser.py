from person import Person

class ComunUser(Person):

    def __init__(self, name, cpf, rg, phone):
        super().__init__(name, cpf, rg, phone)

    def showInfos(self):
        print(f"Informações do usuário:\nTipo de usuário: Comum\nNome: {self.getName()}\nCPF: {self.getCpf()}\nRG: {self.getRg()}\nTelefone: {self.getPhone()}")