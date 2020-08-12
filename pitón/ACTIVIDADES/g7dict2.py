divisas = {'Euro':'???', 'Dolar':'$$$', 'Yen':'"""', 'Corona':'###'}
x = input('Averigue si la divisa se encuentra disponible: ')

while x in divisas:
    print("Su divisa, ",x," ",divisas[x], " se encuentra disponible")
    break
else:
    print('Su divisa no se encuentra disponible')