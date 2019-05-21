## Ejercicio: Lexer para Karel

### Enunciado: 
Basandose en una implementación de Karel para JavaScript, escribir un lexer usando la gramatica del mismo. El Lexer debe devolver una tirilla de tokens diciendo si es valido o no, y en caso de serlo el tipo de Token que es.

### Solución:

#### Ej:
iniciar-programa
    inicia-ejecucion
        repetir 3 veces
        avanza;
		hola;
    termina-ejecucion
finalizar-programa

Salida:
iniciar-programa - DeclaracionDePrograma
inicia-ejecucion - DeclaracionDePrograma
repetir 3 veces - ExpresionPara
avanza; - Expresion
hola; - Token invalido
termina-ejecucion - DeclaracionDePrograma
finalizar-programa - DeclaracionDePrograma

### Integrantes:
- Jhonathan Daniel Rojas Zora - 20151020041
- David Santiago Garces Benitez - 20151020032
- Daniel Alfonso Vargas Ortiz - 20152020009