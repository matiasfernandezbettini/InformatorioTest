x = int(input('Si existe matorral en su campo presione 1, sino presione 2: '))
y = int(input('De cuanto es el porcentaje por hectarea del compuesto necesario que su campo posee?: '))

if x == 1 :
    print('No puede utilizar fertilizante debido a la presencia de matorrales.')
if x == 2 and y >= 10 :
    print('Puede utilizar fertilizante debido a la ausencia de matorrales y cantidad necesaria del compuesto.')
if y < 10:
    print('No puede utilizar fertilizante debido a la falta de compuesto.')