# -*- coding: utf-8 -*-
class Pila:
    """ Representa una pila con operaciones de apilar, desapilar y
        verificar si est� vac�a. """
 
    def __init__(self):
        """ Crea una pila vac�a. """
        # La pila vac�a se representa con una lista vac�a
        self.items=[]

    def apilar(self, x):
        """ Agrega el elemento x a la pila. """
        # Apilar es agregar al final de la lista.
        self.items.append(x)

    def desapilar(self):
        """ Devuelve el elemento tope y lo elimina de la pila.
            Si la pila est� vac�a levanta una excepci�n. """
        try:
            return self.items.pop()
        except IndexError:
            raise ValueError("La pila est� vac�a")

    def es_vacia(self):
        """ Devuelve True si la lista est� vac�a, False si no. """
        return self.items == []