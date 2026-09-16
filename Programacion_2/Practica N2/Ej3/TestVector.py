from Vector import Vector


a = Vector(1, 2, 3)
b = Vector(4, 5, 6)

print("a =", a)
print("b =", b)

print("Suma =", a + b)

print("Multiplicacion por escalar =", a * 2)

print("Longitud de a =", a.longitud())

print("Normal de a =", a.normal())

print("Producto escalar =", a @ b)

print("Producto vectorial =", a.productoVectorial(b))