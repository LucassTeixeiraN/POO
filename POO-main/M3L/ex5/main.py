from point import Point

def inputVerificado(input_string):
    try:
        valor = float(input(input_string))
        return valor
    except:
        print("Número inválido. Digite novamente!")
        return inputVerificado(input_string)

def mostrarMenu():
    print("\nMenu:")
    print("1. Mostrar coordenadas do ponto")
    print("2. Atualizar abscissa")
    print("3. Atualizar ordenada")
    print("4. Movimentar ponto")
    print("5. Calcular distância para um ponto")
    print("6. Sair")

def main():
    print("TESTE DA CLASSE POINT: \n")

    # Solicita a entrada inicial do usuário
    x = inputVerificado("Digite a abscissa inicial do ponto: ")
    y = inputVerificado("Digite a ordenada inicial do ponto: ")
    ponto = Point(x, y)
    
    while True:
        mostrarMenu()
        escolha = input("Escolha uma opção: ")

        match escolha:
            case '1':
                print(f'Ponto: ({ponto.getAbscissa()},{ponto.getOrdenada()})')
            case '2':
                nova_x = inputVerificado("Digite a nova abscissa: ")
                ponto.setAbscissa(nova_x)
            case '3':
                nova_y = inputVerificado("Digite a nova ordenada: ")
                ponto.setOrdenada(nova_y)
            case '4':
                delta_x = inputVerificado("Digite o deslocamento em X: ")
                delta_y = inputVerificado("Digite o deslocamento em Y: ")
                ponto.movimentarPonto(delta_x, delta_y)
            case '5':
                x_destino = inputVerificado("Digite a abscissa do ponto destino: ")
                y_destino = inputVerificado("Digite a ordenada do ponto destino: ")
                distancia = ponto.getDistanciaPontos(x_destino, y_destino)
                print(f"Distância: {distancia}")
            case '6':
                print("Saindo...")
                break
            case _:
                print("Opção inválida. Por favor, escolha uma opção do menu.")

main()