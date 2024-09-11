'''Crie uma classe chamada Employee que inclui três variáveis de instância: um nome
(string), um sobrenome (string) e um salário mensal (float). Sua classe deve ter um
construtor que inicializa as três variáveis. Forneça um método get e set para cada
variável. Se o salário mensal fornecido pelo usuário não for positivo, configure-o
como 0.0. Teste a classe implementada e seus métodos. Crie dois objetos Employee e
exiba o salário anual de cada objeto. Depois, dê 10% de aumento para cada
empregado e exiba novamente os salários.'''

class Employee:
    def __init__(self, nome: str, sobrenome: str, salario: float):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__salario = salario

    def getNome(self):
        return self.__nome

    def setNome(self,nome):
        self.__nome = nome


    def getSobrenome(self):
        return self.__sobrenome

    def setSobrenome(self,sobrenome):
        self.__sobrenome = sobrenome


    def getSalario(self):
        return self.__salario

    def setSalario(self,salario):
        if salario < 0:
            salario = 0
        self.__salario = salario

    def getSalarioAnual(self):
        return self.__salario * 12
    
    def setAumentoSalario(self, quantidade):
        self.__salario += quantidade * self.__salario

def main():
    employee1 = Employee('João Paulo', "Andrade", 2000)
    employee2 = Employee('Paulo', "Andrade", 3000)

    employee1.setNome("João Pedro")
    employee1.setSobrenome("Raimundo")
    employee1.setSalario(3000)
    employee1.setAumentoSalario(0.1)

    print("Employee 1:")
    print(f"Nome: {employee1.getNome()}")
    print(f"Sobrenome: {employee1.getSobrenome()}")
    print(f"Salário: R${employee1.getSalario():,.2f}")
    print(f"Salário Anual: R${employee1.getSalarioAnual():,.2f}")
    print()

    employee2.setNome("Pedro")
    employee2.setSobrenome("Souza")
    employee2.setSalario(5000)
    employee2.setAumentoSalario(0.1)

    print("Employee 2:")
    print(f"Nome: {employee2.getNome()}")
    print(f"Sobrenome: {employee2.getSobrenome()}")
    print(f"Salário: R${employee2.getSalario():,.2f}")
    print(f"Salário Anual: R${employee2.getSalarioAnual():,.2f}")

if __name__ == '__main__':
    main()