from random import randint, uniform, random

class Persona:

    def __init__(self, nombre: str, edad_inicial=0):
        self.edad: int = edad_inicial
        self.nombre: str = nombre
        self.vivo = True
        self.fuerza = uniform(0, 10)
        self.limite = 101

    def morir(self):
        self.vivo = False

    def crecer(self, anios: int):

        if self.vivo:
            self.fuerza += uniform(0, 1)
            self.edad += anios
            if uniform(0, 30) + self.edad > self.limite:
                self.morir()
            self.envejecer()

    def envejecer(self):
        if self.edad > 40:
            self.fuerza -= randint(0, 2)

    def estado(self):
        return "La persona con nombre ", self.nombre, " con edad ", self.edad, " está ", self.vivo

    def pelear(self, persona):
        if not self.vivo:
            print(self.nombre, "está muerto antes del duelo!!!")
            return
        elif not persona.vivo:
            print(persona.nombre, "está muerto antes del duelo!!!")
            return

        if self.edad < 14:
            print(self.nombre, "es demasiado joven para un duelo!!!")
            return
        elif persona.edad < 14:
            print(persona.nombre, "es demasiado joven para un duelo!!!")
            return

        resultado = self.fuerza - persona.fuerza

        if resultado < 0:
            self.morir()
        elif resultado > 0:
            persona.morir()
        else:
            print("¡Empate!")

        print(self.nombre, "vivo: ", self.vivo, ", ", persona.nombre, "vivo: ", persona.vivo)

    def __str__(self):
        return "Nombre: {} -- Edad: {} -- Vivo: {} -- Fuerza: {}".format(self.nombre, self.edad, self.vivo, self.fuerza)


##### HERENCIA PARA SAMURAI #####
class Samurai(Persona):
    def __init__(self, nombre: str, edad=0):
        super().__init__("Samurai " + nombre, edad)
        self.fuerza += 2


##### HERENCIA PARA CAMPESINO #####
class Campesino(Persona):
    def __init__(self, nombre: str, edad=0):
        super().__init__("Campesino " + nombre, edad)
        self.fuerza -= 2
        self.limite = 80