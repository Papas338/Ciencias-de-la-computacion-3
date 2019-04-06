# ordenar los libros
# -*- coding: utf-8 -*-
import csv
class Cola:
    """ Representa una cola con operaciones de encolar, desencolar y
        verificar si está vacía. """
 
    def __init__(self):
        """ Crea una cola vacía. """
        # La cola vacía se representa con una lista vacía
        self.items=[]

    def encolar(self, x):
        """ Agrega el elemento x a la cola. """
        # Encolar es agregar al final de la cola.
        self.items.append(x)

    def desencolar(self):
        """ Devuelve el elemento inicial y lo elimina de la cola.
            Si la cola está vacía levanta una excepción. """
        try:
            return self.items.pop(0)
        except IndexError:
            raise ValueError("La cola está vacía")

    def es_vacia(self):
        """ Devuelve True si la lista está vacía, False si no. """
        return self.items == []

class Pila:
    """ Representa una pila con operaciones de apilar, desapilar y
        verificar si está vacía. """
 
    def __init__(self):
        """ Crea una pila vacía. """
        # La pila vacía se representa con una lista vacía
        self.items=[]

    def apilar(self, x):
        """ Agrega el elemento x a la pila. """
        # Apilar es agregar al final de la lista.
        self.items.append(x)

    def desapilar(self):
        """ Devuelve el elemento tope y lo elimina de la pila.
            Si la pila está vacía levanta una excepción. """
        try:
            return self.items.pop()
        except IndexError:
            raise ValueError("La pila está vacía")

    def es_vacia(self):
        """ Devuelve True si la lista está vacía, False si no. """
        return self.items == []
    
class Libro:
    def __init__(self,titulo,autor):
        self.titulo = titulo
        self.autor = autor
    def getAutor(self):
        return self.autor
    def getTitulo(self):
        return self.titulo

if __name__ == '__main__':    
    original = Pila()
    ordenada = Pila()
    ordTemp = None
    ogTemp = None
    with open('Libros.csv','r') as f:
        reader = csv.reader(f)
        for row in reader:
            libro = Libro(row[0],row[1])
            original.apilar(libro)

    

    """
    # Impresion de los libros originales 
    while not originalCopia.es_vacia():
        print(originalCopia.desapilar().getAutor())
    """

    #Ordenamiento basado en ordenamiento de una pila#
    while not original.es_vacia():
        ogTemp = original.desapilar()
        while not ordenada.es_vacia():
            ordTemp = ordenada.desapilar()
            if ordTemp.getAutor() < ogTemp.getAutor():
                original.apilar(ordTemp)
            else:
                if ordTemp.getAutor() == ogTemp.getAutor():
                    if ordTemp.getTitulo() < ogTemp.getTitulo():
                        original.apilar(ordTemp)
                    else:
                        ordenada.apilar(ordTemp)
                        break
                
                else:
                    ordenada.apilar(ordTemp)
                    break
        ordenada.apilar(ogTemp)

    
   
        
    with open('ordenadito.csv','w') as csvfile:
        writer = csv.writer(csvfile)
        while not ordenada.es_vacia():
            x = ordenada.desapilar()
            print(x.getTitulo()+" del escritor "+ x.getAutor())
            writer.writerow([x.getTitulo(),x.getAutor()])
    csvfile.close()
