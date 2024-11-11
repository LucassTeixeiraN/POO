# Implemente um sistema de Empresa com os tipos de funcionários (gerente, vendedor,
# recepcionista, secretário, etc.), evidenciando a classe Employee como uma classe
# abstrata.


from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    @abstractmethod
    def salario(self):
        pass

    @abstractmethod
    def descricao(self):
        pass

    def get_nome(self):
        return self.nome
    
    def get_idade(self):
        return self.idade


class Gerente(Employee):
    def __init__(self, nome, idade, salario_base, bonus):
        super().__init__(nome, idade)
        self.salario_base = salario_base
        self.bonus = bonus

    def salario(self):
        return self.salario_base + self.bonus

    def descricao(self):
        return f"{self.get_nome()} é o Gerente da empresa, com {self.get_idade()} anos."


class Vendedor(Employee):
    def __init__(self, nome, idade, salario_base, comissao):
        super().__init__(nome, idade)
        self.salario_base = salario_base
        self.comissao = comissao

    def salario(self):
        return self.salario_base + self.comissao

    def descricao(self):
        return f"{self.get_nome()} é um Vendedor com {self.get_idade()} anos."


class Recepcionista(Employee):
    def __init__(self, nome, idade, salario_base):
        super().__init__(nome, idade)
        self.salario_base = salario_base

    def salario(self):
        return self.salario_base

    def descricao(self):
        return f"{self.get_nome()} é a Recepcionista da empresa, com {self.get_idade()} anos."

class Secretario(Employee):
    def __init__(self, nome, idade, salario_base, bonus):
        super().__init__(nome, idade)
        self.salario_base = salario_base
        self.bonus = bonus

    def salario(self):
        return self.salario_base + self.bonus

    def descricao(self):
        return f"{self.get_nome()} é o Secretário da empresa, com {self.get_idade()} anos."




class show():
    def main():
        gerente = Gerente("Carlos", 45, 5000, 2000)
        vendedor = Vendedor("Ana", 30, 3000, 1500)
        recepcionista = Recepcionista("Julia", 25, 2000)
        secretario = Secretario("Roberto", 35, 3000, 1000)

        funcionarios = [gerente, vendedor, recepcionista, secretario]
        
        for func in funcionarios:
    
            print(func.descricao())
            print(f"Salário: R${func.salario():.2f}")
            print("-" * 40)
    main()
