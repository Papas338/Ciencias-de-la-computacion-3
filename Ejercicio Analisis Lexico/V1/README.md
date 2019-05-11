## Ejercicio: Análisis léxico V1

### Enunciado: 
A partir de una entrada en una cadena de texto que representa unas operaciones en notación posfija, generar una tirilla de tokens que identifica cuales 
son las variables, operadores y valores.

### Solución:
No se usa la librería ply. Se usa la librería re de Python para manejar las expresiones regulares.
Se usan las expresiones regulares:
- ^[a-z]$: Para identificar las variables de un caracter alfabético.
- ^\d+$: Para identificar los valores enteros positivos.
- ^[+-/*]$: Para identificar los operadores aritméticos.
- En otro caso se considera token no válido.
Ej: "32 f / a base + %"
- 32: Valor
- f: Variable
- /: Operador
- a: Variable
- base: Token no válido
- +: Operador
- %: Token no valido

### Integrantes:
- Jhonathan Daniel Rojas Zora - 20151020041
- David Santiago Garces Benitez - 20151020032
- Daniel Alfonso Vargas Ortiz - 20152020009