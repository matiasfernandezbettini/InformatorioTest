import random
#De una cantidad de palabras aleatorias necesito jugar con 1 sola.
# Entonces lo que puedo hacer es generar 3 listas con palabras de diferentes dificultades.

facil = ["auto", "casa", "moto", "tren", "piso", "saco", "perro", "gato", "bici"]
medio = ["tenedor", "cuchara", "cucaracha", "cuchillo", "martillo", "espada","lanza","armadura"]
dificil = ["concupiscencia", "prodigo", "fatidico", "inexorable", "atemporal", "vetusto", "invariable", "insolito"]

#luego de que el jugador elija la dificultad deseada debera jugar al ahorcado
#lo que se me ocurre es: una funcion que compare el input con la posicion de la letra que se quiere añadir
# si es correcta debe imprimir la palabra con esa letra correcta de lo contrario debe quitar una vida , imprimir el error
#y devolver la palabra MAS una letra descubierta al azar

def intro():
    f = random.randint(0, (len(facil) - 1))
    m = random.randint(0, (len(medio) - 1))
    d = random.randint(0, (len(dificil) - 1))
    x = int(input("Si quiere jugar al ahorcado en dificultad facil: presione 1, medio: presione 2, dificil: presione 3:- "))
    if x == 1:
        print (facil[f])
        return facil[f]
    elif x == 2:
        print (medio[m])
        return medio[m]
    elif x == 3:
        print (dificil[d])
        return dificil[d]  
    else:
        print("¿Para qué inicias el programa si no vas a jugar?")
        exit()          

def listatostring(listerooni, separador="-"):
    return separador.join(listerooni)



#en la comparacion puedo utilizar el string METHOD find() + 1(indexacion basada en 0) o index() + 1, para obtener
#la posicion de la letra en cuestion
#TAMBIEN PUEDO HACER LO QUE HICE EN VOWEL IN STRING:

def comparacion():
    palabra = intro()

    listapalabra = list(palabra)

    largolistapalabra = len(listapalabra)

    listavacia = []

    i = 0
    for i in range(largolistapalabra):
        listavacia.append(str(i))
    print(listavacia)
    
    copialistapalabra = listapalabra.copy()
    print(copialistapalabra)
    print(listatostring(copialistapalabra))
  #hasta aca asigne el return de intro a una string"palabra", luego converti esa palabra en lista.
  #cree una lista "vacia" del mismo tamaño que la lista palabra
  # ahora queda comparar las letras a la STRING palabra para luego SI COINCIDEN,reemplazarlas en la LISTAVACIA
  # ahora realizo una copia de la lista y la convierto en una string
  # #devuelve la posicion de la letra encontrada
    seisvidas = 0
    seisvidasyang = 6
    x = copialistapalabra.count("*")
    y = len(copialistapalabra)
    
    while seisvidas < 6 and x != y:
        query = input("ingrese una letra para completar la palabra: ")
        
        try: 
            compararletra = copialistapalabra.index(query)  
            print(compararletra)
            copialistapalabra.pop(compararletra)
            copialistapalabra.insert(compararletra, "*")

            listavacia.pop(compararletra)
            listavacia.insert(compararletra, query)
            print(query,"! existe en la palabra! SIGUE JUGANDO :D")
            print(copialistapalabra)
            print(listavacia)
            x = copialistapalabra.count("*")
            y = len(copialistapalabra)
            
            
            

        except ValueError:
            seisvidas += 1
            seisvidasyang -= 1
            print("LA LETRA NO EXISTE EN LA PALABRA, BOOOOOOOOOOM")
            print("te quedan", seisvidasyang , " vidas.")
            print(listavacia)
    else:
        if x == y:
            print("HAS GANADO MORDERFOKKER")
        else:
            print("has perdido BOIIIIIIIIIIIIIIIIII, la palabra era: ",palabra,".")        
            
     
        
        
    



#tengo que crear una lista vacia con una cantidad de items iguales a la cantidad de letras que tiene cada palabra        

#voy a convertir el RETURN DE INTRO a LIST.
#luego voy a utilizar los metodos FIND , para obtener la POSICION. y luego utilizare el metodo REPLACE para 
# colocar los VALORES CORRECTOS en una LISTA NUEVA.
#si find da -1 RESTO -1 A MI ARRAY CONTADOR, 6 errores es game over
comparacion()        




