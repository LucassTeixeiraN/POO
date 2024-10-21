from cards import Card

class Player:
    def __init__(self, name):
        self.name = name
        self.__hand: list[Card] = []
        
    @property
    def score(self):
        return sum(card.value for card in self.__hand)
        
    def add_card(self, card):
        self.__hand.append(card)
        self.showHand()
        
    def showHand(self):
        print(f"\nMão do {self.name}:")
        for card in self.__hand:
            print(card)
        
    def still_playing(self):
        if self.score > 21:
            return False
        return  True