class Person:
    def __init__(self, name, age, cpf):
        self.__name = name
        self.__age = age
        self.__cpf = cpf
        
    def get_name(self):
        return self.__name
    
    def get_age(self):
        return self.__age
    
    def get_cpf(self):
        return self.__cpf
    
    def set_name(self, name):
        self.__name = name
        
    def set_age(self, age):
        self.__age = age
        
    def set_cpf(self, cpf):
        self.__cpf = cpf
        
    def __str__(self):
        return f'Nome: {self.__name}\nIdade: {self.__age}\nCPF: {self.__cpf}'