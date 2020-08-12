Pedrodict = {'nombre': 'Pedro' , 'direccion': 'Corrientes', 'correo': 'hotmail', 'preferente': True }
Juandict = {'nombre': 'Juan' , 'direccion': 'Reitencia', 'correo': 'gmail', 'preferente': True }
clientes = {'Pedro':Pedrodict, 'Juan': Juandict, 'Johnny':'', 'Martin':''}


nuevocliente = {}
x = input('Desea añadir un nuevo cliente? (si/no): ')

if x == 'si':
   y = input('Ingrese nombre de cliente: ')
   nuevocliente.update({'nombre': y})
   z = input('Ingrese correo de cliente: ')
   nuevocliente.update({'correo': z})
   v = input('Ingrese direccion del cliente: ')
   nuevocliente.update({'direccion': v})
   b = nuevocliente.copy()
   clientes.update({y:b})
   print(b)
   print(clientes)
elif x == 'no':
   print('desea continuar? (si/no): ')

