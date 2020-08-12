# -*- coding: utf8 -*-

def iva():
    '''función básica para el calculo del IVA'''
    iva = 12
    costo = int(input('¿Cual es el monto a calcular?: '))
    calculo = costo * iva / 100
    x = str(calculo)
    print ("El calculo de IVA es: " , x)

iva()