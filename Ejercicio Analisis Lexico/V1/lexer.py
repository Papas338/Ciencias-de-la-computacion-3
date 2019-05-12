import re


entrada = "4 c / 3 arbol b - * %"

"""
Separa la cadena de entrada en notacion posfija para separar
los posibles tokens
"""
def tokenize(entrada):
    return list(entrada.split(" "))

"""
Convierte una expresion posfija en un arbol de expresiones
"""
def convertir(lista, pila):  
    if lista != []:
        if lista[0] in "+-*/":
            nodo_der = pila.desapilar()
            nodo_izq = pila.desapilar()
            pila.apilar(Nodo(lista[0],nodo_izq,nodo_der))
        else:
            pila.apilar(Nodo(lista[0]))
        return convertir(lista[1:],pila)

"""
Reconvierte en lista 
"""
def posorden(arbol):
    lista = []
    print("Entro")
    if arbol != None:
        posorden(arbol.izq)
        posorden(arbol.der)
        return lista.insert(arbol.valor)
    if arbol == None:
        print("puta bida")


"""
Comprueba si la entrada es un valor numerico entero positivo
"""
def checkValues(entrada):
    regex = "^\d+$"
    candidates = re.findall(regex,entrada)
    return candidates != []


"""
Comprueba si la entrada es un operador +,-,/,*
"""
def checkOperator(entrada):
    regex = "^[+-/*]$"
    candidate = re.findall(regex, entrada)
    return candidate != []


"""
Comprueba si la entrada es un variable compuesta de un caracter
"""
def checkVariable(entrada):
    regex = "^[a-z]$"
    candidate = re.findall(regex,entrada)
    return candidate != []

"""
Identifica los posibles tokens y los clasifica por variable, valor
u operador. Si no esta en la clasificacion, se considera invalido
"""
def check(entrada):
    candidates = tokenize(entrada)
    print(candidates)
    results = []
    
    for elem in candidates:
        if checkValues(elem):
            results.append( elem + ": Valor")
        elif checkOperator(elem):
            results.append( elem + ": Operador")
        elif checkVariable(elem):
            results.append( elem + ": Variable")
        else:
            results.append( elem + ": Token no valido")
    for elem in results:
        print(elem)

print(check(entrada))

#print(tokenize(entrada))
#print(checkValues(entrada))

#x = re.findall("[a-z][a-z]*", entrada)
#y = re.findall("[+-/*]", entrada)
#z = re.findall("\d+", entrada)

#print(x)
#print(y)
#print(z)
