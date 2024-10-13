'''Escreva uma classe Point descrito por coordenadas reais x, y. Crie métodos get e set
e faça um programa de teste para a sua classe. A seguir, crie e teste os seguintes
métodos para a classe Ponto:
a. O método que recebe como parâmetros um deslocamento dx e outro dy para
movimentar o Ponto.
b. O método que retorna a distância entre este ponto e outro dado como
parâmetro.
Crie e teste um construtor para a classe Point, que inicialize x e y em 1, mas que
também possa receber valores dados.'''

class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def getAbscissa(self):
        return self.__x
    
    def setAbscissa(self, x):
        self.__x = x

    def getOrdenada(self):
        return self.__y
    
    def setOrdenada(self, y):
        self.__y = y
    
    def movimentarPonto(self, dx, dy):
        self.__x += dx
        self.__y += dy

    def getDistanciaPontos(self, x, y):
        dx = abs(self.__x - x)
        dy = abs(self.__y - y)
        return ((dx ** 2) + (dy ** 2)) ** 0.5