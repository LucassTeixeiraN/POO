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
    