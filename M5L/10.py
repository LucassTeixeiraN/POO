class NoughtsAndCrosses:
    
    def __init__(self):
        self.gridDeJogo = [[' ' for _ in range(3)] for _ in range(3)]
    
    def display_gridDeJogo(self):
        for row in self.gridDeJogo:
            print(' | '.join(row))
            print('-' * 9)
    
    def display_positions(self):
        print("Posições das casas:")
        for i in range(3):
            for j in range(3):
                print(f"({i},{j})", end=' ')
            print()  
        print()  

    def play_game(self):
        self.display_positions()  
        player = 'X'  # jogador com X é o primeiro a jogar
        for _ in range(9):  
            self.display_gridDeJogo()
            print(f"Jogador {'1' if player == 'X' else '2'} ({player}), faça sua jogada!")
            row, col = self.get_move()
            
            if self.gridDeJogo[row][col] == ' ':
                self.gridDeJogo[row][col] = player
                
                if self.check_win(player):
                    self.display_gridDeJogo()
                    print(f"Jogador {'1' if player == 'X' else '2'} ({player}) venceu!")
                    return
                #Troca de Jogadores
                player = 'O' if player == 'X' else 'X'
            else:
                print("Casa ocupada! Tente novamente.")
        
        self.display_gridDeJogo()
        print("Empate!")

    def get_move(self):
        while True:
            try:
                row, col = map(int, input("Digite linha e coluna (0, 1 ou 2, separados por espaço): ").split())
                if row in range(3) and col in range(3):
                    return row, col
                else:
                    print("Valores devem estar entre 0 e 2.")
            except ValueError:
                print("Entrada inválida! Digite dois números separados por espaço.")

    def check_win(self, player):
        win_conditions = [
            # Linhas
            [self.gridDeJogo[0][0], self.gridDeJogo[0][1], self.gridDeJogo[0][2]],
            [self.gridDeJogo[1][0], self.gridDeJogo[1][1], self.gridDeJogo[1][2]],
            [self.gridDeJogo[2][0], self.gridDeJogo[2][1], self.gridDeJogo[2][2]],
            # Colunas
            [self.gridDeJogo[0][0], self.gridDeJogo[1][0], self.gridDeJogo[2][0]],
            [self.gridDeJogo[0][1], self.gridDeJogo[1][1], self.gridDeJogo[2][1]],
            [self.gridDeJogo[0][2], self.gridDeJogo[1][2], self.gridDeJogo[2][2]],
            # Diagonais
            [self.gridDeJogo[0][0], self.gridDeJogo[1][1], self.gridDeJogo[2][2]],
            [self.gridDeJogo[0][2], self.gridDeJogo[1][1], self.gridDeJogo[2][0]]
        ]
        return [player, player, player] in win_conditions

game = NoughtsAndCrosses()
game.play_game()