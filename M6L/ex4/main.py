'''Implemente uma classe chamada CardsGame que represente um jogo de cartas
simples, como o Uno. Essa classe deve ter métodos para embaralhar as cartas,
distribuir as cartas aos jogadores e permitir jogadas.'''
from cardsgame import CardsGame
from player import Player

if __name__ == "__main__":
    game = CardsGame()
    game.add_player(Player("João"))
    game.add_player(Player("Pedro"))
    game.add_player(Player("Paulo"))
    game.start_game()