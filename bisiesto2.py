#!/bin/python3
#-*- coding: utf-8-*-

#algo
def comprobar_año():
    año = int(input("Cual es el año a verificar?\n"))

    if ((año % 4 == 0 ) and (año % 100 != 0)) or (año % 400 == 0):
        print ("El año ingresado {} es bisiesto".format(año))
    else:
        print ("El año ingresado {} no es bisiesto".format(año))
    pass

if __name__ == '__main__':
    comprobar_año()