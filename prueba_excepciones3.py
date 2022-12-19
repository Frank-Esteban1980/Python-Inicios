# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 09:25:56 2022

@author: FRANK
"""

def evaluarEdad(edad):
    
    if edad<0:
        raise TypeError("No existen las edades negativas.")
        
    if edad<20:
        return "Eres muy joven"
    elif edad<40:
        return "Eres joven"
    elif edad<65:
        return "Eres maduro"
    elif edad<100:
        return"Cuidate"
        
edad=int(input('Indicar la edad: '))
print(evaluarEdad(edad))



import math

def raizCuadrada(num1):
    
    if num1<0:
        raise ValueError("No existen raices cuadradas de negativos.")
    else:
        return math.sqrt(num1)
    
    
num1=int(input('Calcular la raiz cuadrada del: '))    

try:
    print(raizCuadrada(num1))
except ValueError as ErrorNumeroNegativo:
    print(ErrorNumeroNegativo)
    
    
    
print(raizCuadrada(num1))
                