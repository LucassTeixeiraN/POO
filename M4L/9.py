'''Crie uma classe chamada Date que inclui três variáveis de instância: dia (int), mês
(int) e ano (int). Sua classe deve ter um construtor que inicializa as três variáveis de
instância e assume que os valores fornecidos são corretos. Forneça um método get e
um set para cada variável. Forneça um método que exibe o dia, o mês e o ano
separados por barras “/”. Teste a classe implementada e seus métodos.'''
class Date:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def get_dia(self):
        return self.dia

    def set_dia(self, dia):
        self.dia = dia

    def get_mes(self):
        return self.mes

    def set_mes(self, mes):
        self.mes = mes

    def get_ano(self):
        return self.ano

    def set_ano(self, ano):
        self.ano = ano


class DateFormatter: # Nova classe pra formatar a data em string
    def formatDate(self, date):
        return f"{date.get_dia()}/{date.get_mes()}/{date.get_ano()}"


class DateInputHandler: # Nova classe pra receber e tratar a entrada do usuário
    def getInput(self, prompt):
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("Valor inválido. Tente novamente.")


def main():
    date = Date(23, 9, 2024)
    formatter = DateFormatter()
    input_handler = DateInputHandler()

    print(f"Data: {formatter.formatDate(date)}\n")

    date.set_dia(input_handler.getInput("Insira o novo dia: "))
    date.set_mes(input_handler.getInput("Insira o novo mês: "))
    date.set_ano(input_handler.getInput("Insira o novo ano: "))

    print("\nNova data:", formatter.formatDate(date))


main()