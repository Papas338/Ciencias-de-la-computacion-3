## Ejercicio: Árbol de Expresiones Matemáticas

### Enunciado: 
Dado un archivo "expresiones.in", leer éste y evaluar la expresiones en notacion posfija. Para esto, se debe construir un árbol de expresión y se debe evaluar el mismo.
El resultado debe estar en un archivo "expresiones.out"

### Solución:
Se crea el árbol de expresión mediante una pila, con la cual se toma una cadena que contiene una expresión matemática en notación posfija y se transforma a un árbol de expresión.
Luego, el árbol resultante se evalúa para obtener la respuesta de la operación.

Ej: "32 2 / 4 8 + -" tiene como resultado 4 puesto que al realizar las operaciones correspondientes obtenemos:
- 32/2 = 16
- 4+8 = 12
- 16-12 = 4.

### Integrantes:
- Jhonathan Daniel Rojas Zora - 20151020041
- David Santiago Garces Benitez - 20151020032
- Daniel Alfonso Vargas Ortiz - 20152020009