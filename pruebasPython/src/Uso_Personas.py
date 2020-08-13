from random import randint

from Persona import Samurai, Campesino

samurai1 = Samurai("Marina", randint(1, 5))
samurai2 = Campesino("Juan", randint(1, 5))
samurai3 = Samurai("David", randint(1, 5))
samurai4 = Campesino("Samuel", randint(1, 5))

for _ in range(0, randint(0, 25)):
    print(_)
    samurai1.crecer(randint(1, 5))
    samurai2.crecer(randint(1, 5))
    samurai3.crecer(randint(1, 5))
    samurai4.crecer(randint(1, 5))


def imprimir_todos():
    print("Nombre: ", samurai1.nombre, "--", samurai2.nombre, "--", samurai3.nombre, "--", samurai4.nombre)
    print("Edad           ", samurai1.edad, "-------------", samurai2.edad, "-------------", samurai3.edad,
          "-------------", samurai4.edad)
    print("Fuerza ", samurai1.fuerza, "-", samurai2.fuerza, "-", samurai3.fuerza, "-", samurai4.fuerza)
    print("Vivo:           ", samurai1.vivo, "----------", samurai2.vivo, "----------", samurai3.vivo, "----------",
          samurai4.vivo)


print(samurai1, "\n", samurai2, "\n", samurai3, "\n", samurai4)

imprimir_todos()

samurai1.pelear(samurai2)
samurai3.pelear(samurai4)
samurai1.pelear(samurai4)
samurai2.pelear(samurai3)
samurai1.pelear(samurai3)
