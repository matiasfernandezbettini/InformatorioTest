str = "Si vas a salir usá barbijo, recuerda que si te cuidas, me cuidas."
separador = " "
x = str.split(separador)
result = []

for i in range(len(x)):
    result.append(x[i])

print(x)    
print(" ".join(result)) 
