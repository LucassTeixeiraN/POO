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

    def get_abscissa(self):
        return self.__x
    
    def set_abscissa(self, x):
        self.__x = x

    def get_ordenada(self):
        return self.__y
    
    def set_ordenada(self, y):
        self.__y = y
    
    def movimentar_ponto(self, move_func):
        move_func(self)

    def get_distancia(self, x, y):
        dx = abs(self.__x - x)
        dy = abs(self.__y - y)
        return ((dx ** 2) + (dy ** 2)) ** 0.5

def move_to(new_x, new_y):
    def move(point: Point):
        point.set_abscissa(new_x)
        point.set_ordenada(new_y)
    return move

def move_by(dx, dy):
    def move(point: Point):
        point.set_abscissa(point.get_abscissa() + dx)
        point.set_ordenada(point.get_ordenada() + dy)
    return move