import math


class Estadistica:
    def __init__(self, numeros):
        self.__numeros = numeros

    def promedio(self):
        suma = 0

        for numero in self.__numeros:
            suma += numero

        return suma / len(self.__numeros)

    def desviacion(self):
        pro = self.promedio()
        suma = 0

        for numero in self.__numeros:
            suma += (numero - pro) ** 2

        return math.sqrt(suma / (len(self.__numeros) - 1))
