def calcular_tempo(massa_inicial):
    # Define o intervalo de tempo em segundos
    intervalo = 50
    # Inicializa a quantidade de iterações
    quantidade = 0
    
    # Enquanto a massa inicial for maior ou igual a 0,5 gramas
    while massa_inicial >= 0.5:
        # Divide a massa pela metade
        massa_inicial /= 2
        # Incrementa a quantidade de iterações
        quantidade += 1
    
    # Calcula o tempo total em segundos
    tempo_total = quantidade * intervalo
    
    # Converte o tempo total para horas, minutos e segundos
    horas = tempo_total // 3600
    minutos = (tempo_total % 3600) // 60
    segundos = tempo_total % 60
    
    # Retorna o tempo formatado
    return horas, minutos, segundos

def main():
    while True:
        try:
            massa_inicial = float(input("Digite a massa inicial em gramas (digite 0 para parar): "))
            if massa_inicial == 0:
                print("Programa encerrado.")
                break
        except ValueError:
            print("Insira um número válido!")
        horas, minutos, segundos = calcular_tempo(massa_inicial)
        print(f"Tempo necessário para a massa ser menor que 0,5g: {horas} horas, {minutos} minutos e {segundos} segundos.")

main()
