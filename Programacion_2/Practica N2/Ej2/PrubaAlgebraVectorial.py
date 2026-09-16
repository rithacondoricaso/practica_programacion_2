from AlgebraVectorial import AlgebraVectorial


a = AlgebraVectorial(1, 2, 3)
b = AlgebraVectorial(2, 4, 6)

print("a =", a)
print("b =", b)

print("Perpendiculares:", a.perpendicular(b))
print("Paralelos:", a.paralelo(b))

print("Proyeccion de a sobre b:", a.proyeccion(b))

print("Componente de a en b:", a.componente(b))