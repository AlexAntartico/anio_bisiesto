#!/bin/python3
#-*- coding: utf-8-*-

año = int(input("Cual es el año a verificar?\n"))

def exito():
    print(f"El año ingresado {año} es bisiesto")

def fallo ():
    print(f"El año ingresado {año} no es bisiesto")

def run():
    if ((año % 4 == 0 ) and (año % 100 != 0)) or (año % 400 == 0):
        exito()
    else:
        fallo()
    pass


if __name__ == '__main__':
    run()