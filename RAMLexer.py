import ply.lex as lex

reserved = {'MOV':'MOV','JMP':'JMP','DEC':'DEC','INC':'INC','CON':'CON','CLR':'CLR','END':'END'}

tokens = ['NEWLINE','COMMA','NUMBER','REG','LABEL','ABOVE','BELOW','EQUAL'] + \
 list(reserved.values())

t_ABOVE = r'[aA]'
t_BELOW = r'[bB]'
t_EQUAL = r'='
t_COMMA = r','
t_NEWLINE = r'\n'
t_MOV = r'[mM][oO][vV]'
t_JMP = r'[jJ][mM][pP]'
t_DEC = r'[dD][eE][cC]'
t_INC = r'[iI][nN][cC]'
t_CON = r'[cC][oO][nN][tT][iI][nN][uU][eE]'
t_CLR = r'[cC][lL][rR]'
t_END = r'[eE][nN][dD]'

def t_LABEL(t):
 r'[nN][0-9]+'
 t.value = int(t.value.replace("N",""))
 return t

def t_REG(t):
 r'[rR][1-9][0-9]*'
 t.value = int(t.value.replace("R","").replace("r",""))
 return t

def t_NUMBER(t):
 r'[-+]?[0-9]+(\.([0-9]+)?)?'
 t.value = float(t.value)
 t.type = 'NUMBER'
 return t

t_ignore = " \t\r"
t_ignore_COMMENT = r'\#.*'

def t_error(t):
  print("Illegal character " ,t.value)
  t.lexer.skip(1)
  raise Exception('LEXER ERROR')

lexer = lex.lex()

