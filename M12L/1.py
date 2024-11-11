# Implemente a classe Employee com nome, número de matrícula e salário.
# a. Crie um método para exibir os dados.
# b. Crie as classes AdministrativeAssistant e TecnicalAssistent, herdando de
# Employee.
# c. Sabendo que os assistentes técnicos possuem um bônus salarial e que os
# assistentes administrativos possuem um turno (dia ou noite) e um adicional
# noturno, sobrescreva o método que exibe os dados.

class Employee:
    def __init__(self, name, registration_number, salary):
        self.name = name
        self.registration_number = registration_number
        self.salary = salary

    def show_data(self):
        print(f'Name: {self.name}\nRegistration number: {self.registration_number}\nSalary: {self.salary}')     
        
class AdministrativeAssistant(Employee):
    def __init__(self, name, registration_number, salary, shift,night_bonus):
        super().__init__(name, registration_number, salary)
        self.shift = shift
        self.night_bonus = night_bonus

    def show_data(self):
        print(f'Name: {self.name}\nRegistration number: {self.registration_number}\nSalary: {self.salary}\nShift: {self.shift}')
        
    def display_data(self):
        """Sobrescreve o método para incluir o turno e o adicional noturno."""
        base_data = super().display_data()
        return f"{base_data}\nTurno: {self.shift}\nAdicional Noturno: R${self.night_bonus:.2f}"

class TechnicalAssistant(Employee):
    def __init__(self, name, registration_number, salary, bonus):
        super().__init__(name, registration_number, salary)
        self.bonus = bonus

    def show_data(self):
        print(f'Name: {self.name}\nRegistration number: {self.registration_number}\nSalary: {self.salary}\nBonus: {self.bonus}')
