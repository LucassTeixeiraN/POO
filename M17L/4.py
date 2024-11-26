from abc import ABC, abstractmethod

class Salario(ABC):
    @abstractmethod
    def salario(self):
        pass

class Descricao(ABC):
    @abstractmethod
    def descricao(self):
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

class Departamento:
    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = []

    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)

    def listar_funcionarios(self):
        for func in self.funcionarios:
            print(func.descricao())
            print(f"Salário: R${func.salario():.2f}")
            print("-" * 40)

class Empresa:
    def __init__(self):
        self.departamentos = []

    def adicionar_departamento(self, departamento):
        self.departamentos.append(departamento)

    def listar_funcionarios(self):
        for departamento in self.departamentos:
            print(f"Departamento: {departamento.nome}")
            departamento.listar_funcionarios()
            
class displayInput():
    departamento_vendas = Departamento("Vendas")
    departamento_vendas.adicionar_funcionario(Vendedor("Ana", 30, 3000, 1500))
    departamento_vendas.adicionar_funcionario(Recepcionista("Julia", 25, 2000))

    departamento_administracao = Departamento("Administração")
    departamento_administracao.adicionar_funcionario(Gerente("Carlos", 45, 5000, 2000))
    departamento_administracao.adicionar_funcionario(Secretario("Roberto", 35, 3000, 1000))

    empresa = Empresa()
    empresa.adicionar_departamento(departamento_vendas)
    empresa.adicionar_departamento(departamento_administracao)

    print("-" * 60, "FUNCIONÁRIOS", "-" * 60)
    empresa.listar_funcionarios()
displayInput()
