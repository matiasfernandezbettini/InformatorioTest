barrio = input("Ingresa el nombre de tu barrio: ")
centrico = input("Si tu barrio es centrico escribe SI, de lo contrario escribe NO: ")
abecedario = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"]


x = barrio[:1]
negativo = abecedario.index(x) if x in abecedario else -1

if x in abecedario and centrico == "SI":
    print("Tu Barrio es Seccion A")
elif negativo == -1 and centrico == "NO":
    print("Tu Barrio es Seccion A")
else: 
    print("Tu barrio es seccion B")    
   
