print('login')
print()
print()
print()

user = input('USUARIO: ')
pss = input('CONTRASENIA: ')

i = 1

while (i < 3) & (pss != 'INFO 2020'):
    print('contrasenia incorrecta')
    pss = input('ingrese nuevemente: ')
    i += 1


if pss == 'INFO 2020':
    print('login correcto')
    print('hola', user)
else:
    print('cuenta inhabilitada')

