import ply.lex as lex

tokens = [ 'NAME','NUMBER','PLUS','MINUS','TIMES','DIVIDE', 'EQUALS' ]

t_ignore = ' \t'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EQUALS = r':='
t_NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'

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
entradaIn = []
salidasOut = []
archIn = open('entrada.in','r')
for row in archIn:
    y = row.strip('\n')
    entradaIn.append(y)
archIn.close()
print(entradaIn)

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


