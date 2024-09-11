
# 2. Escreva uma classe chamada Bicycle que possua campos para a velocidade,
# cadência dos pedais (número de rotações dos pedais por minuto), marcha atual e
# número de série. A velocidade e a cadência dos pedais não podem ser menores que
# zero, a marcha atual deve estar entre 1 e 18 e o número de série deve ser maior que
# 1000. Crie constantes simbólicas e métodos de acesso e impressão que reflitam
# esses limites. Teste a classe implementada e seus métodos. A seguir, crie um método
# que calcule a velocidade relativa entre a bicicleta e outra dada como parâmetro. Teste
# o seu novo método.

class bycicle:
    def __init__(self,velocidade,cadencia, marcha , n_de_serie):
        self.velocidade=velocidade
        self.cadencia=cadencia
        self.marcha=marcha
        self._n_de_serie=n_de_serie

    def set_marcha(self,marcha):
        self.marcha=marcha

    def get_velocidade(self):
        return self.velocidade
    
    def get_n_de_serie(self):
       return self._n_de_serie
    
    def get_cadencia(self):
        return self.cadencia
    
    def set_n_de_serie(self,n_de_serie):
        if n_de_serie < 1000: print("insira um n de série válido!")
        else:self._n_de_serie=n_de_serie
    
def main():
    while True:
            try:
                velocidade=float(input("insira a velocidade da bicicleta : "))
                cadencia=float(input("insira a cadencia atual :"))
                marcha=int(input("insira a marcha atual:"))
                if marcha > 18 or marcha < 0 :
                    print("insira uma marcha valida")
                    continue
                n_de_serie=int(input("insira o numero de série: "))
            except ValueError: print("insira um numero válido")
                

            bicicleta1=bycicle(velocidade , cadencia,marcha ,n_de_serie)
            break
    print(bicicleta1.get_velocidade())
main()
