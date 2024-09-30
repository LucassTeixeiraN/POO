class Card:
    SUITS = ["Copas", "Ouro", "Espada", "Paus"]
    RANKS = {
        "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8,
        "9": 9, "10": 10,"Valete": 11, "Dama": 12, "Rei": 13, "Ás": 1
    }

    def __init__(self, suit, rank, value):
        self.suit = suit
        self.rank = rank
        self.value = value

    def __str__(self):
        return f"{self.rank} de {self.suit}"


class Deck:
    def __init__(self):
        self.cards = [Card(suit, rank, Card.RANKS[rank]) for suit in Card.SUITS for rank in Card.RANKS]
        
    def __str__(self) -> str:
        return "\n".join([str(card) for card in self.cards])