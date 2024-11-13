from .ticket import Ticket

class Normal(Ticket):
    def __init__(self, value):
        super().__init__(value)
        