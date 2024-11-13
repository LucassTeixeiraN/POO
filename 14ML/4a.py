from abc import ABC, abstractmethod

class SalarioMixin(ABC):
    @abstractmethod
    def salario(self):
        pass
    
    def salario_base(self):
        return self.salario_base  

class DescricaoMixin(ABC):
    @abstractmethod
    def descricao(self):
        pass

    def descricao_base(self):
        return f"{self.nome} tem {self.idade} anos." 


class Employee(SalarioMixin, DescricaoMixin):
    def __init__(self, nome, idade, salario_base):
        self.nome = nome
        self.idade = idade
        self.salario_base = salario_base


class Gerente(Employee):
    def __init__(self, nome, idade, salario_base, bonus):
        super().__init__(nome, idade, salario_base)
        self.bonus = bonus

    def salario(self):
        return self.salario_base + self.bonus

    def descricao(self):
        return f"{self.descricao_base()} Ele é o Gerente da empresa."


class Vendedor(Employee):
    def __init__(self, nome, idade, salario_base, comissao):
        super().__init__(nome, idade, salario_base)
        self.comissao = comissao

    def salario(self):
        return self.salario_base + self.comissao

    def descricao(self):
        return f"{self.descricao_base()} Ele é o Vendedor da empresa."


class Recepcionista(Employee):
    def __init__(self, nome, idade, salario_base):
        super().__init__(nome, idade, salario_base)

    def salario(self):
        return self.salario_base

    def descricao(self):
        return f"{self.descricao_base()} Ela é a Recepcionista da empresa."


class Secretario(Employee):
    def __init__(self, nome, idade, salario_base, bonus):
        super().__init__(nome, idade, salario_base)
        self.bonus = bonus

    def salario(self):
        return self.salario_base + self.bonus

    def descricao(self):
        return f"{self.descricao_base()} Ele é o Secretário da empresa."


class InputDisplay:
    
    def showInput():
        funcionarios = [
            Gerente("Carlos", 45, 5000, 2000),
            Vendedor("Ana", 30, 3000, 1500),
            Recepcionista("Julia", 25, 2000),
            Secretario("Roberto", 35, 3000, 1000)
        ]

        print("-" * 60, "FUNCIONÁRIOS", "-" * 60)
        for func in funcionarios:
            print(func.descricao())
            print(f"Salário: R${func.salario():.2f}")
            print("-" * 40)


    showInput()
