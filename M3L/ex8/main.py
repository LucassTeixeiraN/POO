from employee import Employee

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