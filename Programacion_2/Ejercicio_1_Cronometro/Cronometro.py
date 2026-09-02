import time


class Cronometro:
    def __init__(self):
        self.__inicia = int(time.time() * 1000)
        self.__finaliza = 0

    def getInicia(self):
        return self.__inicia

    def getFinaliza(self):
        return self.__finaliza

    def inicia(self):
        self.__inicia = int(time.time() * 1000)

    def detener(self):
        self.__finaliza = int(time.time() * 1000)

    def lapsoDeTiempo(self):
        return self.__finaliza - self.__inicia
