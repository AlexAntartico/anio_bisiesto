#!/bin/python3

#aqui solo probe la funcion para obtener el anio bisiesto

anio = (int(input("Cual es el año?\n")))

def comprobar_anio():
    if ((anio % 4 == 0 ) and (anio % 100 != 0)) or (anio % 400 == 0):
        print ("exito")
    else:
        pass

comprobar_anio()
