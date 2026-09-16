import math



class MiPunto:

    
    def init(self):
        self.x = 0
        self.y = 0

    
    def init(self, x: float, y: float):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    
    def distancia(self, p: 'MiPunto'):
        return math.sqrt(
            (self.x - p.x) ** 2 +
            (self.y - p.y) ** 2
        )

    
    def distancia(self, x: float, y: float):
        return math.sqrt(
            (self.x - x) ** 2 +
            (self.y - y) ** 2
        )

    def str(self):
        return "({}, {})".format(self.x, self.y)