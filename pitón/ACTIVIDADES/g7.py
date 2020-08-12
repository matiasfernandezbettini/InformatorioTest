''' 
    -----------------------------------------------------------------
    Ejercicio para practicar asignación de datos e 
    impresión de cálculos por pantalla por lo que no
    deben utilizar estructuras de control solo deben solicitar datos
    hacer el calculo e imprimirlo.
    -----------------------------------------------------------------
    EJERCICIO 1: 
    Convertir los grados Celsius ingresados por un usuario a grados Fahrenheit, 
    y grados Kelvin. Mostrar el resultado en pantalla y el valor ingresado.
'''
# Coloque la resolución del Ejercicio 1 debajo de esta línea



'''
    -----------------------------------------------------------------
    Ejercicio simple para practicar Estructuras de control.
    Para resolver este ejercicio deberá utilizar estructuras 
    condicionales.
    -----------------------------------------------------------------
    EJERCICIO 2: 
    Escribir un programa que reciba una palabra ingresada por el usuario
    e imprima la palabra ingresada y si inicia con una vocal o 
    con una consonante (no se pueden usar Listas).
'''
# Coloque la resolución del Ejercicio 2 debajo de esta línea


'''
    -----------------------------------------------------------------
    Ejercicio simple para practicar Estructuras de control.
    Para resolver este ejercicio deberá utilizar estructuras 
    repetitivas.
    -----------------------------------------------------------------
    EJERCICIO 3: 
    Desarrollar una solución que calcule la suma de los cuadrados 
    de los n primeros números naturales: 1 + 22 + 32 +… + n2.
    
'''
# Coloque la resolución del Ejercicio 3 debajo de esta línea

'''
    -----------------------------------------------------------------
    Ejercicio Desafío.
    Deberá aplicar las estructuras de control que crea conveniente
    para resolver el ejercicio, puede ser condicional/repetitiva
    o una mezcla de ambas.
    -----------------------------------------------------------------
    EJERCICIO 4: 
    Calcular el monto a pagar por cada cliente y total recaudado en una 
    estación de servicio. Debe diseñar un programa que permita monto por 
    cliente y el total recaudado por la gasolinera, tomando en cuenta lo siguiente:
    • El precio del litro es para el Tipo A $50, para el Tipo B $ 55 y para el Tipo C $60
    • El programa finaliza cuando se introduce una D como tipo de gasolina.
'''
# Coloque la resolución del Ejercicio 4 debajo de esta línea

tipoCliente= input("tipo cliente: ")  # A, B, C o D  
litros = int(input("cantidad de litros: "))
total = 0
x = litros * 50
y = litros * 55
z = litros * 60

precioLitroA = 50
totala = 0
precioLitroB = 55
totalb = 0
precioLitroC = 60
totalc = 0
sumaTotal = totala + totalb + totalc 

while tipoCliente == "A" or tipoCliente == "B" or tipoCliente == "C":
    
    if tipoCliente == "A":
        print(litros*precioLitroA)
        totala += (litros*precioLitroA)
        sumaTotal += totala
        tipoCliente= input("tipo cliente: ")  # A, B, C o D  
        litros = int(input("cantidad de litros: "))
    elif tipoCliente == "B":
        print(litros*precioLitroB)
        totalb += (litros*precioLitroB)
        sumaTotal += totalb
        tipoCliente = input("tipo cliente: ")  # A, B, C o D  
        litros = int(input("cantidad de litros: "))
    elif tipoCliente == "C":
        print(litros*precioLitroC)
        totalc += (litros*precioLitroC)
        sumaTotal += totalc
        tipoCliente = input("tipo cliente: ")  # A, B, C o D  
        litros = int(input("cantidad de litros: "))
       
if tipoCliente == "D":
    
    print("Lo recaudado del día es: ", sumaTotal)
    print("Total de cliente A: ", totala)
    print("Total de cliente B: ", totalb)
    print("Total de cliente C: ", totalc)
    exit


