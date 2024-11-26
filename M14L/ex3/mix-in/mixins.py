class MixinEletrico:
    def __init__(self, capacidade_bateria):
        self.capacidade_bateria = capacidade_bateria

    def exibir_info_bateria(self):
        return f"Capacidade da Bateria: {self.capacidade_bateria}kWh"

class MixinTetoSolar:
    def __init__(self, possui_teto_solar):
        self.possui_teto_solar = possui_teto_solar

    def info_teto_solar(self):
        return "Possui teto solar" if self.possui_teto_solar else "Não possui teto solar"