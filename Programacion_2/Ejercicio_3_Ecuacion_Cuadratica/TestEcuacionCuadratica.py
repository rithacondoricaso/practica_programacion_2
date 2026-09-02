from EcuacionCuadratica import EcuacionCuadratica


a, b, c = map(float, input("Ingrese a, b, c: ").split())

ecuacion = EcuacionCuadratica(a, b, c)
discriminante = ecuacion.getDiscriminante()

if discriminante > 0:
    print(
        "La ecuacion tiene dos raices",
        ecuacion.getRaiz1(),
        "y",
        ecuacion.getRaiz2()
    )
elif discriminante == 0:
    print("La ecuacion tiene una raiz", ecuacion.getRaiz1())
else:
    print("La ecuacion no tiene raices reales")
