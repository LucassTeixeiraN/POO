import random

class GuessingGameInterface:
    def make_guess(self, guess):
        raise NotImplementedError("Subclasses must implement this method.")

class GuessingGame(GuessingGameInterface):
    def __init__(self, number_to_guess):
        self.number_to_guess = number_to_guess
    
    @classmethod
    def create_game(cls, number_to_guess):
        return cls(number_to_guess)
    
    @staticmethod
    def is_correct_guess(number_to_guess, guess):
        return number_to_guess == guess
    
    def make_guess(self, guess):
        if self.is_correct_guess(self.number_to_guess, guess):
            return "Acertou!"
        elif guess < self.number_to_guess:
            return "Muito baixo!"
        else:
            return "Muito alto!"

class Counting:
    def __init__(self):
        self.attempts = 0
    
    def increment_attempts(self):
        self.attempts += 1
    
    def get_attempts(self):
        return self.attempts

class CountingGuessingGame:
    def __init__(self, number_to_guess):
        self.game = GuessingGame(number_to_guess)
        self.counter = Counting()
    
    def make_guess(self, guess):
        self.counter.increment_attempts()
        result = self.game.make_guess(guess)
        if self.game.is_correct_guess(self.game.number_to_guess, guess):
            return f"{result} Você acertou em {self.counter.get_attempts()} tentativas!"
        return f"{result} Tentativas até agora: {self.counter.get_attempts()}"

# Criação do jogo
game = CountingGuessingGame(random.randint(1, 100))
print(game.make_guess(20))
print(game.make_guess(30))
print(game.make_guess(25))
