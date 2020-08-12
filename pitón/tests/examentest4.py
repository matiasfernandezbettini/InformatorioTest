verduras = ["papa","cebolla","rucula","batata","lechuga"]
for contador, una_verdura in enumerate(verduras):
    print(f"En la posicion {contador} esta una {una_verdura}")

colores = ["azul","rojo","amarillo","negro"]
print (colores[-3])
print (colores[3])    


valor = 5.5
if valor <= 5:
    print("bajo")
elif valor <= 10:
    print("medio")
else:
    print("alto")

try:
    for letra in "Python":
        if letra == "h":
            pass    
        print("letra actual es:",letra)
except Exception as e:
    print("Ha ocurrido un error no previsto,", type(e).__name__)
    for letra in "Python":
        if letra == "h":
            pass
        print("letra actual:", letra)      

edades = (5,25,2,18,22,45,50,1,80,10)
cont = 0
for i in edades:
    if i > 20:
        cont +=1 

print("Hay", cont, "numeros mayores a 20")          


usuario = {
    "domicilio": {"calle":"asda", "localidad":"losvagarrios102931923"}

    
}

localidad_usuario = usuario['domicilio'].get('localidad')

print(localidad_usuario)

vocales = ("a","e","i","o","u")

mostrar_pos= vocales[2]

print("eaaaaaaaaaaaaaaaa: ",mostrar_pos)


x = 0
while x < 3 :
    x = x + 1
else:
    print(x)

def sumaDigitos(numero):
    suma=0
    while numero!=0:
        digito=numero%10
        suma=suma+digito
        numero=numero//10
    return suma

 
sumatoria=0
num=int(input("Número a procesar: "))
while num!=0:
    print("Suma:",sumaDigitos(num))
    sumatoria=sumatoria+num
    num=int(input("Número a procesar: "))
print("Sumatoria:", sumatoria)
print("Dígitos:", sumaDigitos(sumatoria))