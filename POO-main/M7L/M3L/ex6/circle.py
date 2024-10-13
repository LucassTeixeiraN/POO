from point import Point

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

# Classe fechada para modificação, pois n é necessário modificar o código para add funcionalidades