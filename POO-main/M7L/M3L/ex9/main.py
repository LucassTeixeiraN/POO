'''Crie uma classe chamada Date que inclui três variáveis de instância: dia (int), mês
(int) e ano (int). Sua classe deve ter um construtor que inicializa as três variáveis de
instância e assume que os valores fornecidos são corretos. Forneça um método get e
um set para cada variável. Forneça um método que exibe o dia, o mês e o ano
separados por barras “/”. Teste a classe implementada e seus métodos.'''
from date import Date
from formattedDate import FormattedDate

def main():
    date = FormattedDate(21, 10, 2024, "{}/{}/{}")

    print(f"HOJE: {date}\n")
    while True:
        try:
            date.setDia(int(input("Insira o novo dia: ")))
            date.setMes(int(input("Insira o novo mes: ")))
            date.setAno(int(input("Insira o novo ano: ")))
            break
        except(ValueError):
            print("Invalid date, Try again.")

    print("\nNova data:", date)

main()