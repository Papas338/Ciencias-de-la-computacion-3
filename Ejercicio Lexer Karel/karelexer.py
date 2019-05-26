import ply.lex as lex
tokens = ['NAME','NUMBER']

"apagate","gira-izquierda","avanza","coge-zumbador","deja-zumbador",
"sal-de-instruccion","y"

t_identificador = r'[A-Za-z][A-Za-Z0-9-]*'
t_cadena = r'\".*'


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
