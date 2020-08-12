arraycontador =[]
ingredientes = {'v': 'Verduras', 'b': 'Berenjena', 'l': 'Lentejas', 'a':'Apio', 'm': 'Morron', 'c': 'Cebolla'}
intro = print('Bienvenido a Vegan Salad , ofrecemos una ensalada con base de Verduras y/o Berenjenas \n\nLuego podras elegir entre dos recetas,\nReceta 1: Lentejas y/o Apio\n Receta 2: Morron y/o Cebolla\n Recuerda, solo podras elegir 3 ingredientes')
ele = 'Eleccion registrada'

x = input('Si quieres Verduras presiona v  sino presiona x:- ')
if x == 'v':
    arraycontador.append(x)
    print(ele)
elif x == 'x':
    print(ele)
else:
    print('Presiona una tecla correcta')
    x = input('Si quieres Verduras presiona v  sino presiona x:- ')

y = input('Si quieres Berenjas presiona b sino presiona x:-')
if y == 'b':
    arraycontador.append(y)
    print(ele)
elif y == 'x':
    print(ele)
else:
    print('Presiona una tecla correcta')
    y = input('Si quieres Berenjas presiona b sino presiona x:-')
    
z = input('Quieres la Receta 1? (Lentejas y/o Apio) Escribe receta1-\nQuieres la Receta 2? (Morron y/o Cebolla) Escribe receta2-\n Tu eleccion es: ')
if z == 'receta1':
    z1a = input('Si quieres Lenteja presiona l  sino presiona x:- ')
    if z1a == 'l':
        arraycontador.append(z1a)
        print(ele)
    elif z1a == 'x':
        print(ele)
    else:
        print('Presiona una tecla correcta')
        z1a = input('Si quieres Lenteja presiona l  sino presiona x:- ')
    if len(arraycontador) <= 2:
        z1b = input('Si quieres Apio presiona a sino presiona x:- ')
        if z1b == 'a':
            arraycontador.append(z1b)
            print(ele)
        elif z1b == 'x':
            print(ele)
        else:
            print('Presiona una tecla correcta')
            z1b = input('Si quieres Apio presiona a sino presiona x:- ')
    print(arraycontador)
    if len(arraycontador) >= 3:
        print('Tu ensalada ha sido elegida, tus ingredientes son: '+ ingredientes[arraycontador[0]] + ', ' + ingredientes[arraycontador[1]] + ', ' + ingredientes[arraycontador[2]] + '.')
    elif len(arraycontador) <= 3:
        print('Tu ensalada ha sido elegida, tus ingredientes son: '+ ingredientes[arraycontador[0]] + ', ' + ingredientes[arraycontador[1]] + '.')   
elif z == 'receta2':
    z2a = input('Si quieres Morron presiona m  sino presiona x:- ')
    if z2a == 'm':
        arraycontador.append(z2a)
        print(ele)
    elif z2a == 'x':
        print(ele)
    else:
        print('Presiona una tecla correcta')
        z2a = input('Si quieres Morron presiona m  sino presiona x:- ')
    if len(arraycontador) <= 2:
        z2b = input('Si quieres Cebolla presiona c sino presiona x:- ')
        if z2b == 'c':
            arraycontador.append(z2b)
            print(ele)
        elif z2b == 'x':
            print(ele)
    print(arraycontador)
    if len(arraycontador) >= 3:
        print('Tu ensalada ha sido elegida, sus ingredientes son: '+ ingredientes[arraycontador[0]] + ', ' + ingredientes[arraycontador[1]] + ', ' + ingredientes[arraycontador[2]] + '.')
    else:
        print('Tu ensalada ha sido elegida, sus ingredientes son: '+ ingredientes[arraycontador[0]] + ', ' + ingredientes[arraycontador[1]] + '.')

    print('smaakligt maaltid, ha det bra och kom tillbaka!!!')
else:
    print('Presiona una tecla correcta')
    z = input('Quieres la Receta 1? (Lentejas y/o Apio) Escribe receta1-\nQuieres la Receta 2? (Morron y/o Cebolla) Escribe receta2-\n Tu eleccion es: ')

    





