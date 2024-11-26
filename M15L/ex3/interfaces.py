from abc import ABC, abstractmethod

class IVeiculo(ABC):
    @abstractmethod
    def registrar(self):
        pass

class IAutomovel(IVeiculo):
    @abstractmethod
    def info_bateria(self):
        pass

class IMoto(IVeiculo):
    @abstractmethod
    def info_cilindrada(self):
        pass

class ICaminhao(IVeiculo):
    @abstractmethod
    def info_capacidade_carga(self):
        pass