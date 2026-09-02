from Estadistica import Estadistica


numeros = []

while len(numeros) < 10:
    entrada = input(f"Ingrese numeros ({len(numeros)}/10): ").split()

    for valor in entrada:
        if len(numeros) < 10:
            numeros.append(float(valor))

estadistica = Estadistica(numeros)

print(f"El promedio es {estadistica.promedio():.2f}")
print(f"La desviacion estandar es {estadistica.desviacion():.5f}")
