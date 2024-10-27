import locale
from person import Person
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

class Account:
    def __init__(self, person: Person, saldo):
        self.__person = person
        self.saldo = saldo
        
    def __str__(self):
        return f'Conta de {self.__person.get_name()} possui saldo de {locale.currency(self.saldo, grouping=True)}'

    def getPerson(self):
        return self.__person
    
    def debit(self, quantidade):
        if quantidade > self.saldo:
            print('Quantia de débito excedeu o saldo da conta.')
        else:
            print('Operação realizada com sucesso!')
            self.saldo -= quantidade
        print(f'Saldo disponível: {locale.currency(self.saldo, grouping=True)}\n')
        