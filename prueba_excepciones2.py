# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 22:09:05 2022

@author: FRANK
"""

def dividir(num1, num2):
    """El bloque try se intentará, pero si es entre 0 avisa que no lo acepta y sigue ejecutando"""
    try: 
       return num1/num2
    except ZeroDivisionError:
           print("No acepta dividir entre 0 ")
           return('Sigue ejecutando')
"""Pedimos dos números, si el usuario da una letra o signo, el bucle será falso y captura el VALUEERROR
    si son dos números, rompe el bucle y continua con la división"""
while True:
    try:
        num1=int(input('Di un número: '))
        num2=int(input('Di otro número: '))
        break
    except ValueError:
        print('Introducir un número. Intentar de nuevo.')
    
print("El cociente es: ", dividir(num1, num2))



"""La misma funcion sin parámetros pero los pide en la propia función y luego imprime la divisón 
El objetivo sería capturar todas las excepciones posibles"""

def division():
    try:
        num1=(float(input('Di un número: ')))
        num2=(float(input('Di otro número: ')))
    
        print('La división es: '+str(num1/num2))
        
    except ValueError:
        print("El valor introducido es incorrecto")
    except ZeroDivisionError:
        print("No se puede dividir entre 0.")
    finally:                        
        print('Calculo finalizado.')
    
        
division()
