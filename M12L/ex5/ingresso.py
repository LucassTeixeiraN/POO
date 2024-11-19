# ingresso.py
class Ingresso:
    def __init__(self, tipo):
        self.tipo = tipo

    def valor(self):
        if self.tipo == 1:
            return 50  # Normal
        elif self.tipo == 2:
            return 100  # VIP
        return 0

    def tipo_ingresso(self):
        if self.tipo == 1:
            return "Normal"
        elif self.tipo == 2:
            return "VIP"