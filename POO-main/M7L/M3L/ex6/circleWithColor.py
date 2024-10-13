from point import Point
from circle import Circle

class CircleWithColor(Circle):
    def __init__(self, center=Point(0, 0), radius=0, color="white"):
        super().__init__(center, radius)
        self.__color = color

    def getColor(self):
        return self.__color

    def setColor(self, color):
        self.__color = color

    def description(self):
        return f"Circle with center at ({self.getCenter().getAbscissa()}, {self.getCenter().getOrdenada()}), radius {self.getRadius()}, area {self.area()}, color {self.getColor()}."

# "subclasse" de circle para adicionar a propriedade adicional de cor, adicionando novas funcionalidades à classe circle sem modificar o código existente
# classe aberta para extensão, pois podemos adicionar novas propriedades ou métodos sem modificar a classe Circle