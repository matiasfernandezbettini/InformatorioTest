materias = ["Matematica", "Historia", "Aleman", "Ingles", "Biologia", "Quimica"]
materiasdict = {}

i = 0
for materia in materias:
    x = "¿Cuanto sacaste en " + materias[i] + "?: "
    y = int(input(x))
    materiasdict.update({materias[i] : y})
    i += 1

print(materiasdict)    

z = 0
print(materiasdict[materias[z]])
for nota in materiasdict:
    if materiasdict.get(materias[z]) >= 6:
        z += 1
    else:
        print("Necesitás recuperar " + materias[z])
        z += 1
    
    