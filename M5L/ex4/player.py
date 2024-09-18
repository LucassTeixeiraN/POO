class Player:
    def __init__(self, name):
        self.name = name
        self.__hand = []
        
    @property
    def score(self):
        return sum(card[1] for card in self.__hand)
        
    def add_card(self, card):
        self.__hand.append(card)
        self.showHand()
        
    def showHand(self):
        print(f"\nMão do {self.name}:")
        for card in self.__hand:
            print(card[0])
        
    def still_playing(self):
        if self.score > 21:
            print(f"{self.name} estourou! Pontuação: {self.score}")
            return False
        else:
            return  True
        
    def get_playing(self):
        return self.__playing