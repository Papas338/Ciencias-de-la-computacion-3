import ply.lex as lex

tokens = ['VACIA','IDENTIFICADOR','NUMBER','CADENA','LETRA','DIGITO',"MIENTRAS","HACER","NO","Y","O"]
instrucciones = ["apagate","gira-izquierda","avanza","coge-zumbador","deja-zumbador",
"sal-de-instruccion","y","o"]
funcionesBooleanas = ["frente-libre","frente-bloqueado","izquierda-libre","izquierda-bloqueada","derecha-libre",
"derecha-bloqueada","junto-a-zumbador","no-junto-a-zumbador","algun-zumbador-en-la-mochila",
"ningun-zumbador-en-la-mochila","orientado-al-norte","orientado-al-sur",
"orientado-al-este","orientado-al-oeste","no-orientado-al-norte","no-orientado-al-sur",
"no-orientado-al-este","no-orientado-al-oeste"]

t_VACIA = r''
t_IDENTIFICADOR = r'[A-Za-z][A-Za-Z0-9-]*'
t_CADENA = r'\".*'
t_LETRA = r'[A-Za-z]'
t_DIGITO = r'[0-9]'
t_MIENTRAS = r'mientras'
t_HACER = r'hacer'
t_NO = r'no'
t_Y = r'y'
t_O = r'o'
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


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
