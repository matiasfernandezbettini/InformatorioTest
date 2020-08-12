x = int(input('Si la medida del pez es Normal presione 1, si la medida del pez esta por debajo de lo normal presione 2, si la medida del pez es un poco por encima de lo normal presione 3 , si el pez esta sobredimensionado presione 4: '))

if x == 1 :
    print('Pez en buenas condiciones')
if x == 2 :
    print("Pez con problemas de nutrición")
if x == 3 :
    print("Pez con síntomas de organismo contaminado")
if x == 4 : 
    print("Pez contaminado")
if x > 4:
    print('Ingrese un numero del 1 al 4 por favor')

