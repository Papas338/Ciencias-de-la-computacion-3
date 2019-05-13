## Ejercicio: Análisis léxico V2

### Enunciado: 
A partir de una entrada en un archivo de texto que representa unas operaciones en notación posfija, generar una tirilla de tokens que identifica cuales son las variables, operadores y valores.

### Solución:
Se utiliza la librería ply.
Con la librería ply se separan los valores ingresados para analizarlos individualmente.

#### Ej: "4 c / 3 arbol b - * %"
4 - NUMBER
c - NAME
/ - DIVIDE
3 - NUMBER
arbol - NAME
b - NAME
- - MINUS
* - TIMES

### Integrantes:
- Jhonathan Daniel Rojas Zora - 20151020041
- David Santiago Garces Benitez - 20151020032
- Daniel Alfonso Vargas Ortiz - 20152020009