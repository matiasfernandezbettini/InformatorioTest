palabra = input("ingrese palabra: ")
primera = palabra[0]
if primera in "aeiouAEIOU":
    print(palabra + " empieza con vocal.")
else:
    print(palabra + " empieza con consonante.")    