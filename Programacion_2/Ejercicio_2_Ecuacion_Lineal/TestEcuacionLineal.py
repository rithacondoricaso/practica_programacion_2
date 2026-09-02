from EcuacionLineal import EcuacionLineal


a, b, c, d, e, f = map(
    float,
    input("Ingrese a, b, c, d, e, f: ").split()
)

ecuacion = EcuacionLineal(a, b, c, d, e, f)

if ecuacion.tieneSolucion():
    print(f"x = {ecuacion.getX()}, y = {ecuacion.getY()}")
else:
    print("La ecuacion no tiene solucion")
