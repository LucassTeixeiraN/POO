from point import Point, move_by, move_to

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
    print("4. Movimentar ponto para um novo destino")
    print("5. Movimentar ponto por um deslocamento")
    print("6. Calcular distância para um ponto")
    print("7. Sair")

def main():
    x = inputVerificado("Digite a abscissa inicial do ponto: ")
    y = inputVerificado("Digite a ordenada inicial do ponto: ")
    ponto = Point(x, y)
    
    while True:
        mostrarMenu()
        escolha = input("Escolha uma opção: ")

        match escolha:
            case '1':
                print(f'Ponto: ({ponto.get_abscissa()}, {ponto.get_ordenada()})')
            case '2':
                nova_x = inputVerificado("Digite a nova abscissa: ")
                ponto.set_abscissa(nova_x)
            case '3':
                nova_y = inputVerificado("Digite a nova ordenada: ")
                ponto.set_ordenada(nova_y)
            case '4':
                # Movimentar ponto para um novo destino
                nova_x = inputVerificado("Digite a nova abscissa do ponto destino: ")
                nova_y = inputVerificado("Digite a nova ordenada do ponto destino: ")
                ponto.movimentar_ponto(move_to(nova_x, nova_y))
            case '5':
                # Movimentar ponto por um vetor
                delta_x = inputVerificado("Digite o deslocamento em X: ")
                delta_y = inputVerificado("Digite o deslocamento em Y: ")
                ponto.movimentar_ponto(move_by(delta_x, delta_y))
            case '6':
                x_destino = inputVerificado("Digite a abscissa do ponto destino: ")
                y_destino = inputVerificado("Digite a ordenada do ponto destino: ")
                distancia = ponto.get_distancia(x_destino, y_destino)
                print(f"Distância: {distancia:.2f}")
            case '7':
                print("Saindo...")
                break
            case _:
                print("Opção inválida. Por favor, escolha uma opção do menu.")

main()
