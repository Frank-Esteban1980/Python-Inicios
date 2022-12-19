# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 10:13:42 2022

@author: FRANK
"""

import pickle

class Persona:
    
    def __init__(self, nombre, genero, edad):
        self.nombre=nombre
        self.genero=genero
        self.edad=edad
        print('Se ha creado una persona nueva con del nombre ',self.nombre)
        #El método str que convierte en cadena de texto la información de un objeto
        #Será util para poder ver la información de las personas que se van a guardar en el fichero de texto
    def __str__(self):
        return "{} {} {} ".format(self.nombre, self.genero, self.edad)
           
    
    def estado(self):
        return (f'Nombre: {self.nombre}. Género: {self.genero}. Edad: {self.edad}.')

"""Queremos crear personas o instancias de personas y se almacenen ahora y en un futuro en un fichero externo
para se debe:
        
    1. Primero creamos una clase llamada Lista personas con métodos que guarden, agreguen y muestren la información
        2. Después se crea al lista
        3. El método constructor debe crear el archivo o fichero donde se guardará en una lista cada objeto
            con el metodo ab+
            ***hay que desplazar el cursor al inicio del fichero para que cuando lea cada vez que lo llamemos lo lea
            desde el inicio. El cursos vuelve al inicio con seek(0)
        3. Debemos crear dos métodos:
            a. Metodo que grabe o guarde la lista
            b. Metodo que lea la información de la lista

"""
class ListaPersonas:
    
    personas=[]
    
    def __init__(self):#Dentro del constructor creamos un objeto que cree el earchivo binario y que cargue lo que tenga
        
        listaDePersonas=open("ficheroExterno", 'ab+')
        listaDePersonas.seek(0)  #SEEK(0) Lleva el cursor al inicio del fichero para volver a leer o rellenar
        
        try:
            self.personas=pickle.load(listaDePersonas)#Pedimos que se carge en la personas la listaDePersonas que está en el fichero
            print("se cargaron {} personas del fichero externo ".format(len(self.personas)))
        #Lo anterior se ejecutará sin problema desde que se ha guardado algo, pero al inicio está vacío
        #Para evitar que de error creamos una exception
        except:
            print("El fichero está vacío.")
        finally:#Para que cierre la listaDePersonas y si ya se leyó lo borre
            listaDePersonas.close()
            del(listaDePersonas)
     
    
    #Método que agregue cada nuevo objeto PERSONA que la pedirá a la lista de objetos PERSONAS
    def agregarPersonas(self, persona):
        self.personas.append(persona)#Agrega objetos en la lista de objetos
        self.guardarPersonasEnFicheroExterno()#es el que guarda cada objeto en el fichero externo
        
    #Metodo mostrar mostrará cada objeto PERSONA  que se guardó en la lista de objetos PERSONAS.
    def mostrarPersonas(self):
        for persona in self.personas:
            print(persona)
            
    #Creamos una función que guarde los objetos Personas en el fichero externo con wb para que escriba binario y lo guarde
    def guardarPersonasEnFicheroExterno(self):
        listaDePersonas=open("ficheroExterno","wb")
        pickle.dump(self.personas, listaDePersonas)#dumb hace el volcado de la listaDePersonas 
        listaDePersonas.close()
        del (listaDePersonas)#Una vez leida se puede borrar 17.18
        
    def mostrarInfoFicheroExterno(self):
        print("la información del fichero externo es: ")
        for persona in self.personas:
            print(persona)
        
#Creamos un objeto llamado miLista para sobre ese objeto ejecutar los métodos agregar y mostrarPersonas

miLista=ListaPersonas()

#Creamos varios objetos y llamamos al método agregarPersona para que se guarde
sandra=Persona('Sandra', "femenino", 21)
sandra.estado()
miLista.agregarPersonas(sandra)
miLista.mostrarInfoFicheroExterno()

pedro=Persona('Pedro', "masculino", 22)
miLista.agregarPersonas(pedro)

maria=Persona('María', "femenino", 25)
miLista.agregarPersonas(maria)


ximena=Persona('Ximena', "femenino", 20)
ximena.estado()
miLista.agregarPersonas(ximena)
"""

miLista.mostrarPersonas()

"""
        