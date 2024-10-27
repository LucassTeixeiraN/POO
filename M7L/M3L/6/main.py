'''Escreva uma classe Circle composta de um ponto para indicar o centro e o tamanho
do raio, que não deve ser menor que zero. Utilize a classe Point criada anteriormente.
Crie métodos get e set para testar sua classe. A seguir crie:
a. Um método que retorne a área do círculo.
b. Um método move que movimente o centro do círculo (utilize o método move
da classe ponto).
Crie e teste um construtor para a classe Circle com todos os valores zerados, mas
que também possa receber valores dados.'''
from point import Point
from circleWithColor import CircleWithColor

def main():
    print("Test of class Circle\n")

    ponto = Point(0, 0)
    print(f"Point: ({ponto.getAbscissa()},{ponto.getOrdenada()})")

    ponto.setAbscissa(5)
    print(f'Point: ({ponto.getAbscissa()},{ponto.getOrdenada()})')

    ponto.setOrdenada(3)
    print(f'Point: ({ponto.getAbscissa()},{ponto.getOrdenada()})')

    ponto.movimentarPonto(1, 3)
    print(f'Point: ({ponto.getAbscissa()},{ponto.getOrdenada()}) \n')

    circle = CircleWithColor(ponto, 5, "red")
    print(f"Center: ({circle.getCenter().getAbscissa()},{circle.getCenter().getOrdenada()})")
    print(f"Radius: {circle.getRadius()}")
    print(f"Area: {circle.area()}")
    print(f"Color: {circle.getColor()}")

    circle.move(2, 2)
    print(f"Center after move: ({circle.getCenter().getAbscissa()},{circle.getCenter().getOrdenada()})")


main()