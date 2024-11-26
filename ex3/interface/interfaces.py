from abc import ABC, abstractmethod

class VeiculoEletrico(ABC):
    @abstractmethod
    def exibir_info_bateria(self):
        pass

class VeiculoTetoSolar(ABC):
    @abstractmethod
    def info_teto_solar(self):
        pass