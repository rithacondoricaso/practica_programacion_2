import math



class AlgebraVectorial:

    
    def init(self, x: float, y: float):
        self.x = x
        self.y = y
        self.z = 0

    
    def init(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

    def longitud(self):
        return math.sqrt(
            self.x ** 2 +
            self.y ** 2 +
            self.z ** 2
        )

    def add(self, otro):
        return AlgebraVectorial(
            self.x + otro.x,
            self.y + otro.y,
            self.z + otro.z
        )

    def sub(self, otro):
        return AlgebraVectorial(
            self.x - otro.x,
            self.y - otro.y,
            self.z - otro.z
        )

    def productoEscalar(self, otro):
        return (
            self.x * otro.x +
            self.y * otro.y +
            self.z * otro.z
        )

    def productoVectorial(self, otro):
        return AlgebraVectorial(
            self.y * otro.z - self.z * otro.y,
            self.z * otro.x - self.x * otro.z,
            self.x * otro.y - self.y * otro.x
        )

    def perpendicular(self, otro):
        return self.productoEscalar(otro) == 0

    def paralelo(self, otro):
        producto = self.productoVectorial(otro)

        return (
            producto.x == 0 and
            producto.y == 0 and
            producto.z == 0
        )

    def proyeccion(self, otro):
        producto = self.productoEscalar(otro)
        longitud = otro.longitud()

        factor = producto / (longitud ** 2)

        return AlgebraVectorial(
            factor * otro.x,
            factor * otro.y,
            factor * otro.z
        )

    def componente(self, otro):
        producto = self.productoEscalar(otro)

        return producto / otro.longitud()

    def str(self):
        return "({}, {}, {})".format(
            self.x,
            self.y,
            self.z
        )