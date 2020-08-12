lista = []
i = 0
for i in range(10):
    x = "Ingrese un numero: "
    y = int(input(x))
    lista.append(y)
    i += 10
print(lista)
lista.reverse()
print(*lista, sep=", ")
