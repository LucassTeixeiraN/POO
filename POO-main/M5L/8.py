# Implemente uma classe chamada GuessingGame que represente um jogo de
# adivinhação. Essa classe deve gerar um número aleatório, permitir que o jogador faça
# palpites e informar se o palpite está correto, informando se é maior ou menor que o
# número gerado.
import random

class GuessingGame:
    def __init__(self, number_to_guess):
        self.number_to_guess = number_to_guess
    
    @classmethod
    def create_game(cls, number_to_guess):
        return cls(number_to_guess)
    
    @staticmethod
    def is_correct_guess(number_to_guess, guess):
        return number_to_guess == guess
    
    def make_guess(self, guess):
        if GuessingGame.is_correct_guess(self.number_to_guess, guess):
            return "Acertou!"
        elif guess < self.number_to_guess:
            return "Muito baixo!"
        else:
            return "Muito alto!"


game = GuessingGame.create_game(random.randint(1,100))
print(game.make_guess(20)) 
print(game.make_guess(30)) 
print(game.make_guess(25))  
