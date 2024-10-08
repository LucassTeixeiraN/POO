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

class CountingGuessingGame(GuessingGame):
    def __init__(self, number_to_guess):
        super().__init__(number_to_guess)
        self.attempts = 0
    
    def make_guess(self, guess):
        self.attempts += 1
        result = super().make_guess(guess)
        if self.is_correct_guess(self.number_to_guess, guess):
            return f"{result} Você acertou em {self.attempts} tentativas!"
        return f"{result} Tentativas até agora: {self.attempts}"


game = CountingGuessingGame.create_game(random.randint(1, 100))
print(game.make_guess(20))
print(game.make_guess(30))
print(game.make_guess(25))
