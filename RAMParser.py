import ply.yacc as yacc
from RAMLexer import tokens

def p_ramstart(p):
  """ramwhole : ramin ramline"""
  p[0] = p[1] + p[2]

def p_ramin_givenvalue(p):
 'ramin : ram2 ram2'
 p[0] = p[1] + p[2]

def p_ram2_givenvalue(p):
 'ram2 : REG EQUAL NUMBER NEWLINE'
 p[0] = [['EQ',p[1],p[3]]]

def p_ramline_lines(p):
 'ramline : ramline ramline'
 p[0] = p[1] + p[2]

def p_ramline_line(p):
 'ramline : ram NEWLINE'
 p[0] = [p[1]]

def p_ramline_label(p):
 'ramline : LABEL'
 p[0] = [['LABEL',p[1]]]

def p_ram_empty(p):
 'ramline : NEWLINE'
 p[0] = []

def p_ram_increase(p):
 'ram : INC REG'
 p[0] = ['INC',p[2]]

def p_ram_cont(p):
 'ram : CON'
 p[0] = ['ENDE']

def p_ram_decrease(p):
 'ram : DEC REG'
 p[0] = ['DEC',p[2]]

def p_ram_move(p):
 'ram : MOV REG COMMA REG'
 p[0] = ['MOVE',p[2],p[4]]

def p_ram_clr(p):
 'ram : CLR REG'
 p[0] = ['CLR',p[2]]
	
def p_ram_jmp1(p):
 'ram : JMP LABEL ABOVE'
 p[0] = ['AJ',p[2]]

def p_ram_jmp2(p):
 'ram : JMP LABEL BELOW'
 p[0] = ['BJ',p[2]]

def p_ram_condjmp1(p):
 'ram : REG JMP LABEL ABOVE'
 p[0] = ['CAJ',p[1],p[3]]

def p_ram_condjmp2(p):
 'ram : REG JMP LABEL BELOW'
 p[0] = ['CBJ',p[1],p[3]]

def p_error(p):
  print("Syntax error in input!")


parser = yacc.yacc()
