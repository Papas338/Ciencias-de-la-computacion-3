from pila import *
from arbol import *

def convertir(lista, pila):
    """
    Convierte una expresion posfija en un arbol de expresiones
    """
    if lista != []:
        if lista[0] in "+-*/":
            nodo_der = pila.desapilar()
            nodo_izq = pila.desapilar()
            pila.apilar(Nodo(lista[0],nodo_izq,nodo_der))
        else:
            pila.apilar(Nodo(lista[0]))
        return convertir(lista[1:],pila)
            

def evaluar(arbol):
    """
    Evalua el arbol de expresiones creado y se toma el nodo raiz para ello
    """
    if arbol.valor == "+":
        return evaluar(arbol.izq) + evaluar(arbol.der)
    if arbol.valor == "-":
        return evaluar(arbol.izq) - evaluar(arbol.der)
    if arbol.valor == "/":
        return evaluar(arbol.izq) / evaluar(arbol.der)
    if arbol.valor == "*":
        return evaluar(arbol.izq) * evaluar(arbol.der)
    return int(arbol.valor)


"""
exp = raw_input("ingrese l expresion en posfija: ").split(" ")

pila = Pila()

convertir(exp, pila)

print evaluar(pila.desapilar())
"""


"Listas para la entrada de expresiones y su respectiva salida"
expressionsIn = []
expressionsOut = []

"Lectura del archivo expresiones.in"
archIn = open('expresiones.in','r')
for row in archIn:
    y = row.strip('\n')
    expressionsIn.append(y)
    print(y)
archIn.close()

"Tratamiento de la expresion para convertirla en arbol y evaluar el arbol"
for expression in expressionsIn:
    temp = expression.split(' ')
    stack = Pila()
    convertir(temp,stack)
    expressionsOut.append(evaluar(stack.desapilar()))

"Escritura de resultados en archivo expresiones.out"
archOut = open('expresiones.out','w')
for result in expressionsOut:
    archOut.write(str(result)+"\n")    
archOut.close()


