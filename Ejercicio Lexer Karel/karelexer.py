import ply.lex as lex

tokens = ['NUMBER','CADENA','LETRA','DIGITO',"MIENTRAS","HACER","NO","Y","O",



"INICIOPROGRAMA",
"DECLARACION",
"COMODECLARACION",
"INICIAEJECUCION",
"FINEJECUCION",
"FINPROGRAMA",


"APAGAR",
"GIRAIZQ",
"AVANZA",
"COGZUM",
"DEJZUM",
"SALINS",
"REPETIR",
"VECES",
"SI",
"ENTONCES",
"SINO",


"INICIO",
"FIN",

"FLIBRE",
"FBLOQUADO",
"ILIBRE",
"IBLOQUEADA",
"DLIBRE",
"DBLOQUEADA",
"JZUMBADOR",
"NJZUMBADOR",
"MOZUMBADOR",
"NOMOZUMBADOR",
"ORNORTE",
"ORSUR",
"OROESTE",
"ORESTE",
"NORNORTE",
"NORSUR",
"NOROESTE",
"NORESTE"]








instrucciones = ["apagate","gira-izquierda","avanza","coge-zumbador","deja-zumbador",
"sal-de-instruccion","y","o"]


funcionesBooleanas = ["frente-libre","frente-bloqueado","izquierda-libre","izquierda-bloqueada","derecha-libre",
"derecha-bloqueada","junto-a-zumbador","no-junto-a-zumbador","algun-zumbador-en-la-mochila",
"ningun-zumbador-en-la-mochila","orientado-al-norte","orientado-al-sur",
"orientado-al-este","orientado-al-oeste","no-orientado-al-norte","no-orientado-al-sur",
"no-orientado-al-este","no-orientado-al-oeste"]





#Expresiones#
t_APAGAR = r'apagate'
t_GIRAIZQ = r'gira-izquierda'
t_AVANZA = r'avanza'
t_COGZUM = r'coge-zumbador'
t_DEJZUM = r'deja-zumbador'
t_SALINS = "sal-de-instruccion"

#Funcion Booleana#
t_FLIBRE = r'frente-libre'
t_FBLOQUADO = r'frente-bloqueado'
t_ILIBRE = r'izquierda-libre'
t_IBLOQUEADA = r'izquierda-bloqueada'
t_DLIBRE = r'derecha-libre'
t_DBLOQUEADA = r'derecha-bloqueada'
t_JZUMBADOR = r'junto-a-zumbador'
t_NJZUMBADOR = r'no-junto-a-zumbador'
t_MOZUMBADOR = r'algun-zumbador-en-la-mochila'
t_NOMOZUMBADOR = r'ningun-zumbador-en-la-mochila'
t_ORNORTE = r'orientado-al-norte'
t_ORSUR = r'orientado-al-sur'
t_OROESTE = r'orientado-al-oeste'
t_ORESTE = r'orientado-al-este'
t_NORNORTE = r'no-orientado-al-norte'
t_NORSUR = r'no-orientado-al-sur'
t_NOROESTE = r'no-orientado-al-oeste'
t_NORESTE = r'no-orientado-al-este'



t_INICIOPROGRAMA = r'iniciar-programa'
t_DECLARACION = r'define-nueva-instruccion'
t_COMODECLARACION = r'como'
t_INICIAEJECUCION = r'inicia-ejecucion'
t_FINEJECUCION = r'termina-ejecucion'
t_FINPROGRAMA = r'finalizar-programa'



t_CADENA = r'\".*'
t_LETRA = r'^[A-Za-z]$'
t_DIGITO = r'[0-9]'
t_MIENTRAS = r'mientras'
t_HACER = r'hacer'
t_REPETIR = r'repetir'
t_VECES = r'veces'
t_SI = r'si'
t_ENTONCES = r'entonces'
t_SINO = r'sino'

t_INICIO = r'inicio'
t_FIN = r'fin'

t_NO = r'no'
t_Y = r'y'
t_O = r'o'


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)






lex.lex() # Build the lexer

#lectura de archivo

entradaAux = []

entradaIn = []
salidasOut = []
archIn = open('entrada.in','r')
for row in archIn:
    y = row.strip('\n')
    entradaAux.append(y)
archIn.close()
print(entradaAux)

for x in entradaAux:
    p = x.rsplit()
    entradaIn = entradaIn + p

#analisis lexico
lex.input(str(entradaIn))
while True:
    tok = lex.token()
    if not tok: break
    salidasOut.append(str(tok.value) + " - " + str(tok.type))
    print (str(tok.value) + " - " + str(tok.type))


archOut = open('salidas.out','w')
for result in salidasOut:
    archOut.write(str(result)+"\n")    
archOut.close()


    
