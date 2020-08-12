
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