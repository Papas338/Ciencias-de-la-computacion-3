## Ejercicio: An�lisis l�xico V1

### Enunciado: 
A partir de una entrada en una cadena de texto que representa unas operaciones en notaci�n posfija, generar una tirilla de tokens que identifica cuales 
son las variables, operadores y valores.

### Soluci�n:
No se usa la librer�a ply. Se usa la librer�a re de Python para manejar las expresiones regulares.
Se usan las expresiones regulares:
- ^[a-z]$: Para identificar las variables de un caracter alfab�tico.
- ^\d+$: Para identificar los valores enteros positivos.
- ^[+-/*]$: Para identificar los operadores aritm�ticos.
- En otro caso se considera token no v�lido.
Ej: "32 f / a base + %"
- 32: Valor
- f: Variable
- /: Operador
- a: Variable
- base: Token no v�lido
- +: Operador
- %: Token no valido

### Integrantes:
- Jhonathan Daniel Rojas Zora - 20151020041
- David Santiago Garces Benitez - 20151020032
- Daniel Alfonso Vargas Ortiz - 20152020009