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
    
class Circle:
    def __init__(self, center=Point(0, 0), radius=0):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self.__center = center
        self.__radius = radius

    def getCenter(self):
        return self.__center

    def setCenter(self, center):
        self.__center = center

    def getRadius(self):
        return self.__radius

    def setRadius(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self.__radius = radius

    def area(self):
        return 3.14 * (self.__radius ** 2)

    def move(self, dx, dy):
        self.__center.movimentarPonto(dx, dy)
        
def main():
    print("Test of class Circle\n")
    
    ponto = Point(0,0)
    print(f"Point: ({ponto.getAbscissa()},{ponto.getOrdenada()})")
    
    ponto.setAbscissa(5)
    print(f'Point: ({ponto.getAbscissa()},{ponto.getOrdenada()})')

    ponto.setOrdenada(3)
    print(f'Point: ({ponto.getAbscissa()},{ponto.getOrdenada()})')

    ponto.movimentarPonto(1, 3)
    print(f'Point: ({ponto.getAbscissa()},{ponto.getOrdenada()}) \n')
    
    circle = Circle(ponto, 5)
    print(f"Center: ({circle.getCenter().getAbscissa()},{circle.getCenter().getOrdenada()})")
    print(f"Radius: {circle.getRadius()}")
    print(f"Area: {circle.area()}")

    circle.move(2, 2)
    print(f"Center after move: ({circle.getCenter().getAbscissa()},{circle.getCenter().getOrdenada()})")

main()