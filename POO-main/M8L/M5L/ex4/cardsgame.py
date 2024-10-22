import random
from cards import Card
from player import Player

class CardsGame:
    def __init__(self, cards: list[Card]):
        self.__cards = cards
        self.__players: list[Player] = []

    def shuffle(self):
        random.shuffle(self.__cards)
        
    def pull_card(self):
        return self.__cards.pop()
        
    def add_player(self, player):
        self.__players.append(player)
        
    def start_game(self):
        self.shuffle()
        for player in self.__players:
            player.add_card(self.pull_card())
            
        self.play()
            
    def play(self):
        print('-' * 30)
        print('Jogo iniciado!')
        print('-' * 30)
        
        for player in self.__players:
            player.showHand()
            still_playing = True
            
            while still_playing:
                choice = input(f"{player.name}, deseja puxar mais uma carta? (s/n) ")
                if choice.lower() == 's':
                    player.add_card(self.pull_card())
                    if not player.still_playing():
                        print(f"{player.name} estourou! Pontuação: {player.score}")
                        break
                elif choice.lower() == 'n':
                    still_playing = False
                else:
                    print("Opção inválida!")
        
        self.show_winner()
        
    def show_winner(self):
        winners = [player for player in self.__players if player.still_playing()]
        if winners:
            winner = max(winners, key=lambda x: x.score)
            print(f"O vencedor é {winner.name} com {winner.score} pontos!")
        else:
            print("Todos os jogadores estouraram!")
            