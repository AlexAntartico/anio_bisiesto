#!/bin/python3

#dato de entrada - el año que se quiere comprobar
anio = int(input("Cual es el año a verificar?\n"))

#datos de salida - lo que se quiere que el programa regrese
def exito():
    print ("El año ingresado ", anio, " es bisiesto")
    pass

def fallo ():
    print ("El año ingresado ", anio, " no es bisiesto")
    pass

#algoritmo - si (anio divisble entre 4 y no multiplo de 100  or (divisible entre 400) 
# entonces -> output

def comprobar_anio():
    if ((anio % 4 == 0 ) and (anio % 100 != 0)) or (anio % 400 == 0):
        exito()
    else:
        fallo()
    pass

comprobar_anio()