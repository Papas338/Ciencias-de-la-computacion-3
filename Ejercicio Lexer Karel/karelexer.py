import ply.lex as lex

tokens = ['VACIA','IDENTIFICADOR','NUMBER','CADENA','LETRA','DIGITO',"MIENTRAS","HACER","NO","Y","O"]
instrucciones = ["apagate","gira-izquierda","avanza","coge-zumbador","deja-zumbador",
"sal-de-instruccion","y","o"]

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


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
