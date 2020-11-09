#!/bin/python3

#input data
anio = int(input("Cual es el año a verificar?\n"))

#output data
def exito():
    print ("El año ingresado ", anio, " es bisiesto")
    pass

def fallo ():
    print ("El año ingresado ", anio, " no es bisiesto")
    pass

#algo
def comprobar_anio():
    if ((anio % 4 == 0 ) and (anio % 100 != 0)) or (anio % 400 == 0):
        exito()
    else:
        fallo()
    pass

comprobar_anio()