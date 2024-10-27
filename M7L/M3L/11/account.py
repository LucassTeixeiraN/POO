class Account:
    def __init__(self, name, pin, balance=0.0):
        self.name = name
        self.pin = pin
        self.balance = balance

    def __str__(self):
        result = 'Name:' + self.name + '\n'
        result += 'PIN:' + str(self.pin) + '\n'
        result += 'Balance:' + str(self.balance)
        return result

    def get_balance(self):
        return self.balance

    def get_name(self):
        return self.name

    def get_pin(self):
        return self.pin

    def deposit(self, amount):
        self.balance += amount
        return None

    def withdraw(self, amount):
        if amount < 0:
            return "Amount must be >= 0"
        elif self.balance < amount:
            return "Insufficient funds"
        else:
            self.balance -= amount
            return None
        
    def compute_interest(self):
        pass
