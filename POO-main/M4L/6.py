'''Escreva uma classe Circle composta de um ponto para indicar o centro e o tamanho
do raio, que não deve ser menor que zero. Utilize a classe Point criada anteriormente.
Crie métodos get e set para testar sua classe. A seguir crie:
a. Um método que retorne a área do círculo.
b. Um método move que movimente o centro do círculo (utilize o método move
da classe ponto).
Crie e teste um construtor para a classe Circle com todos os valores zerados, mas
que também possa receber valores dados.'''

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

    def move(self, dx, dy):
        self.__x += dx
        self.__y += dy

    def distance_to(self, x, y):
        dx = abs(self.__x - x)
        dy = abs(self.__y - y)
        return ((dx ** 2) + (dy ** 2)) ** 0.5


class Circle:
    def __init__(self, center=Point(0, 0), radius=0):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self.__center = center
        self.__radius = radius

    def get_center(self):
        return self.__center

    def set_center(self, center):
        self.__center = center

    def get_radius(self):
        return self.__radius

    def set_radius(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self.__radius = radius

    def area(self):
        return 3.14 * (self.__radius ** 2)

    def move(self, dx, dy):
        self.__center.move(dx, dy)

# Nova classe para  printar as informações do circulo
class CirclePresenter:
    def __init__(self, circle):
        self.__circle = circle

    def print_circle_info(self):
        print(f"Center: ({self.__circle.get_center().get_abscissa()},{self.__circle.get_center().get_ordenada()})")
        print(f"Radius: {self.__circle.get_radius()}")
        print(f"Area: {self.__circle.area()}")


def main():
    print("Test of class Circle\n")

    ponto = Point(0, 0)
    print(f"Point: ({ponto.get_abscissa()},{ponto.get_ordenada()})")

    ponto.set_abscissa(5)
    print(f'Point: ({ponto.get_abscissa()},{ponto.get_ordenada()})')

    ponto.set_ordenada(3)
    print(f'Point: ({ponto.get_abscissa()},{ponto.get_ordenada()})')

    ponto.move(1, 3)
    print(f'Point: ({ponto.get_abscissa()},{ponto.get_ordenada()}) \n')

    circle = Circle(ponto, 5)
    presenter = CirclePresenter(circle)
    presenter.print_circle_info()

    circle.move(2, 2)
    presenter.print_circle_info()


main()