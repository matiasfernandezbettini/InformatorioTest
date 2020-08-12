

x = 13
y = 14
z = 15

arraycontador = []

arraycontador.append(x)
arraycontador.append(y)
arraycontador.append(z)

resultadoEnsaladas = {13: 'Verduras', 14: 'Berenjenas', 15: 'Apio'}

ingredientes = {'v': 'Verduras', 'b': 'Berenjena', 'l': 'Lentejas', 'a':'Apio', 'm': 'Morron', 'c': 'Cebolla'}

x1 = 'b'
x2 = 'l'
x3 = 'a'

arraycontador2 = []

arraycontador2.append(x1)
arraycontador2.append(x2)
arraycontador2.append(x3)

print(arraycontador)
print(resultadoEnsaladas[arraycontador[0]])
print(len(arraycontador))
print('Tu receta ha sido elegida, sus ingredientes son: ' + ingredientes[arraycontador2[0]] + ', ' + ingredientes[arraycontador2[1]] + ', ' + ingredientes[arraycontador2[2]])


