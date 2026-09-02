import math


def promedio(numeros):
    suma = 0

    for numero in numeros:
        suma += numero

    return suma / len(numeros)


def desviacion(numeros):
    pro = promedio(numeros)
    suma = 0

    for numero in numeros:
        suma += (numero - pro) ** 2

    return math.sqrt(suma / (len(numeros) - 1))


numeros = []

while len(numeros) < 10:
    entrada = input(f"Ingrese numeros ({len(numeros)}/10): ").split()

    for valor in entrada:
        if len(numeros) < 10:
            numeros.append(float(valor))

pro = promedio(numeros)
desv = desviacion(numeros)

print(f"El promedio es {pro:.2f}")
print(f"La desviacion estandar es {desv:.5f}")
