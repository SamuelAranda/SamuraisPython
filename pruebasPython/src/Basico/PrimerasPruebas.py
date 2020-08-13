variable1 = 1
variable2 = 1.2
variable3 = """que pasa"""
variable4 = [1, 2, 3, 4, 5, 6, 7]


# esto es un comentario de prueba
print(type(variable1))
print(type(variable2))
print(type(variable3))
print(type(variable4))

if variable2 < variable1:
    print("hola")
else:
    print(variable3)

print(variable4[1])
print(variable4[:])
print(variable4[-1])
print(variable4[-1])
print(variable4[1:4])

variable4.insert(5, "hola")

print(variable4)


