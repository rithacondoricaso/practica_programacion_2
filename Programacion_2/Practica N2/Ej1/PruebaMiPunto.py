from MiPunto import MiPunto


p1 = MiPunto()
p2 = MiPunto(10, 30.5)

print("p1 =", p1)
print("p2 =", p2)

d = p1.distancia(p2)

print("distancia =", d)