
def ciclo_nota():
    print()
    valor_numero = int(input("Introduzca nota numerica: "))
    print(notas(valor_numero))
    print("¿Quiere introducir nueva nota?")
    if input() == "s":
        ciclo_nota()
    else :
        print("Gracias por usar mis servicios")


def notas(nota):
    valoracion = "Suspenso"
    if nota > 4.9:
        valoracion = "Aprobado"

    return valoracion


ciclo_nota()
