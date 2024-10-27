'''Implemente uma classe chamada CardsGame que represente um jogo de cartas
simples, como o Uno. Essa classe deve ter métodos para embaralhar as cartas,
distribuir as cartas aos jogadores e permitir jogadas.'''
from cardsgame import CardsGame
from player import Player

def main():
    game = CardsGame()
    game.add_player(Player("João"))
    game.add_player(Player("Pedro"))
    game.add_player(Player("Paulo"))
    startGame(game)
    
def startGame(game: CardsGame):
    try:
        value = input('Deseja que o baralho seja embaralhado? (s/n) ')
        if value.lower() == 's':
            game.start_game(game.shuffle)
        elif value.lower() == 'n':
            game.start_game(game.ordenate)
        else:
            raise Exception
    except:
        print("Digite um valor válido!")
        startGame(game)

if __name__ == "__main__":
    main()