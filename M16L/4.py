from abc import ABC, abstractmethod

class Salario(ABC):
    @abstractmethod
    def salario(self):
        pass

class Descricao(ABC):
    @abstractmethod
    def descricao(self):
        pass

class Exibicao(ABC):
    @abstractmethod
    def exibir(self, funcionario):
        pass

class Employee(Salario, Descricao):
    def __init__(self, nome, idade, salario_base):
        self.nome = nome
        self.idade = idade
        self.salario_base = salario_base

    def descricao_base(self):
        return f"{self.nome} tem {self.idade} anos."

class Gerente(Employee):
    def __init__(self, nome, idade, salario_base, bonus):
        super().__init__(nome, idade, salario_base)
        self.bonus = bonus

    def salario(self):
        return self.salario_base + self.bonus

    def descricao(self):
        return f"{self.descricao_base()} Ele/a é o Gerente da empresa."

class Vendedor(Employee):
    def __init__(self, nome, idade, salario_base, comissao):
        super().__init__(nome, idade, salario_base)
        self.comissao = comissao

    def salario(self):
        return self.salario_base + self.comissao

    def descricao(self):
        return f"{self.descricao_base()} Ele/a é o Vendedor da empresa."

class Recepcionista(Employee):
    def __init__(self, nome, idade, salario_base):
        super().__init__(nome, idade, salario_base)

    def salario(self):
        return self.salario_base

    def descricao(self):
        return f"{self.descricao_base()} Ela/e é a Recepcionista da empresa."

class Secretario(Employee):
    def __init__(self, nome, idade, salario_base, bonus):
        super().__init__(nome, idade, salario_base)
        self.bonus = bonus

    def salario(self):
        return self.salario_base + self.bonus

    def descricao(self):
        return f"{self.descricao_base()} Ele/a é o Secretário da empresa."

class ExibicaoTexto(Exibicao):
    def exibir(self, funcionario):
        print(funcionario.descricao())
        print(f"Salário: R${funcionario.salario():.2f}")
        print("-" * 40)

class FuncionarioManager:
    def __init__(self, exibicao: Exibicao):
        self.exibicao = exibicao
        self.funcionarios = [
            Gerente("Carlos", 45, 5000, 2000),
            Vendedor("Ana", 30, 3000, 1500),
            Recepcionista("Julia", 25, 2000),
            Secretario("Roberto", 35, 3000, 1000)
        ]
    
    def exibir_funcionarios(self):
        print("-" * 60, "FUNCIONÁRIOS", "-" * 60)
        for funcionario in self.funcionarios:
            self.exibicao.exibir(funcionario)

exibicao_texto = ExibicaoTexto()
manager_texto = FuncionarioManager(exibicao_texto)
manager_texto.exibir_funcionarios()
