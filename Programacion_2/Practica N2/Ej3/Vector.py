import math


class Vector:

    def init(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def add(self, otro):
        return Vector(
            self.x + otro.x,
            self.y + otro.y,
            self.z + otro.z
        )

    def mul(self, escalar):
        return Vector(
            self.x * escalar,
            self.y * escalar,
            self.z * escalar
        )

    def longitud(self):
        return math.sqrt(
            self.x ** 2 +
            self.y ** 2 +
            self.z ** 2
        )

    def normal(self):
        l = self.longitud()

        return Vector(
            self.x / l,
            self.y / l,
            self.z / l
        )

    def matmul(self, otro):
        return (
            self.x * otro.x +
            self.y * otro.y +
            self.z * otro.z
        )

    def productoVectorial(self, otro):
        return Vector(
            self.y * otro.z - self.z * otro.y,
            self.z * otro.x - self.x * otro.z,
            self.x * otro.y - self.y * otro.x
        )

    def str(self):
        return "({}, {}, {})".format(
            self.x,
            self.y,
            self.z
        )