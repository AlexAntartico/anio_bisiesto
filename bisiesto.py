#!/bin/python3
#-*- coding: utf-8-*-

año = int(input("Cual es el año a verificar?\n"))

def exito():
    print ("El año ingresado {} es bisiesto".format(año))

def fallo ():
    print ("El año ingresado {} no es bisiesto".format(año))

#algo
def comprobar_año():
    if ((año % 4 == 0 ) and (año % 100 != 0)) or (año % 400 == 0):
        exito()
    else:
        fallo()
    pass

if __name__ == '__main__':
    comprobar_año()