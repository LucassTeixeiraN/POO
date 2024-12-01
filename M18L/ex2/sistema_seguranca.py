class SistemaSeguranca:
    def __init__(self):
        self.ativo = True

    def ativar(self):
        self.ativo = True
        print("Sistema de segurança ativado.")

    def desativar(self):
        self.ativo = False
        print("Sistema de segurança desativado.")

    def __str__(self):
        return "ativo" if self.ativo else "desativado"
