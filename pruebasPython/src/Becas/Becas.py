print("Programa de becas injusto")

datos: dict = {"Distancia" : 0, "Hermanos": 0, "Dinero": 0}


def introducir_datos():
    datos["Distancia"] = int(input("Introduce distancia "))
    datos["Hermanos"] = int(input("Introduce hermanos "))
    datos["Dinero"] = int(input("Introduce dinero "))


def comprobar_beca(datos):
    if datos["Distancia"] >= 40 and datos["Hermanos"] >= 3 and datos["Dinero"] <= 20000:
        return True
    else:
        return False


def dar_beca(boleano):
    if boleano:
        print("Tiene usted derecho a beca")
    else:
        print("No tiene usted derecho a beca")


introducir_datos()
print(datos)
dar_beca(comprobar_beca(datos))
