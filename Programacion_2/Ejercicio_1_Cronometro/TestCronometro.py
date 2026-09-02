import random
from Cronometro import Cronometro


numeros = []

for _ in range(100000):
    numeros.append(random.randint(0, 100000))

cronometro = Cronometro()
cronometro.inicia()

# Ordenamiento por seleccion
for i in range(len(numeros) - 1):
    indice_minimo = i

    for j in range(i + 1, len(numeros)):
        if numeros[j] < numeros[indice_minimo]:
            indice_minimo = j

    numeros[i], numeros[indice_minimo] = numeros[indice_minimo], numeros[i]

cronometro.detener()

print("Tiempo de ejecucion:", cronometro.lapsoDeTiempo(), "milisegundos")
