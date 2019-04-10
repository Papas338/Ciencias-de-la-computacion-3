## Ejercicio: �rbol de Expresiones Matem�ticas

### Enunciado: 
Dado un archivo "expresiones.in", leer �ste y evaluar la expresiones en notacion posfija. Para esto, se debe construir un �rbol de expresi�n y se debe evaluar el mismo.
El resultado debe estar en un archivo "expresiones.out"

### Soluci�n:
Se crea el �rbol de expresi�n mediante una pila, con la cual se toma una cadena que contiene una expresi�n matem�tica en notaci�n posfija y se transforma a un �rbol de expresi�n.
Luego, el �rbol resultante se eval�a para obtener la respuesta de la operaci�n.

Ej: "32 2 / 4 8 + -" tiene como resultado 4 puesto que al realizar las operaciones correspondientes obtenemos:
- 32/2 = 16
- 4+8 = 12
- 16-12 = 4.

### Integrantes:
- Jhonathan Daniel Rojas Zora - 20151020041
- David Santiago Garces Benitez - 20151020032
- Daniel Alfonso Vargas Ortiz - 20152020009