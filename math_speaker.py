#coding=utf-8
import ply.yacc as yacc
import ply.lex as lex
#from __future__ import absolute_import
from io import open
from gtts import gTTS
import os, sys

tokens = ('NUM','LLAVI','LLAVD','REDI','REDD', 'OPERBI', 'SUB', 'SUP', 'INT', 'SUM', 'DIF', 'LIMIT', 'TO', 'INFINITY', 'FRAC', 'RAIZ','MON','FUNCION')

#tokens default
t_ignore = "   \n"

lang =1

def t_NUM(t):
   r'-?[0-9]+'
   if t.value[0] == '-':
      t.value =  t.value[1:]
      if lang == 1:
         t.value = 'menos ' +  t.value
      elif lang == 2:
         t.value = 'minus ' +  t.value
   j=str(t.value)
   print(j)
   return t

#def t_VAR(t):
#   r'[a-z]|\\alpha|\\nu|\\beta|\\xi|\\gamma|o|\\delta|\\pi|\\epsilon|\\rho|\\zeta|\\sigma|\\eta|\\tau|\\theta|\\upsilon|\\iota|\\ph|\\kappa|\\chi|\\lambda|\\psi|\\mu|\\omega'
#   if t.value[0] == '\\':
#      t.value = t.value[1:] + ' ' #si es letra griega agarra todo menos el
#   return t

def t_LLAVI(t):
   r'\{'
   #t.value = 'abre llave x
   print(str(t.value))
   return t

def t_LLAVD(t):
   r'\}'
   #t.value = 'cierra llave '
   print(str(t.value))
   return t

def t_REDI(t):
   r'\('
   #t.value = 'abre paréntesis '
   t.value = ', '
   print(str(t.value))
   return t

def t_REDD(t):
   r'\)'
   #t.value = 'cierra paréntesis '
   t.value = ', '
   print(str(t.value))
   return t

def t_OPERBI(t):
   r'(\+|-|(\\times)|(\\cdot)|(\\div)|=|(\\neq)|(\\leq)|(\\geq))'
   if t.value == '+':
      if lang == 1:
         t.value = 'más '
      elif lang == 2:
         t.value = 'plus '
   if t.value == '-':
      if lang == 1:
         t.value = 'menos '
      elif lang == 2:
         t.value = 'minus '
   if t.value == '\\times' or t.value == '\\cdot':
      if lang == 1:
         t.value = 'multiplicado por '
      elif lang == 2:
         t.value = 'times '
   if t.value == '=':
      if lang == 1:
         t.value = 'igual a '
      elif lang == 2:
         t.value = 'equals '
   if t.value == '\\neq':
      if lang == 1:
         t.value = 'diferente de '
      elif lang == 2:
         t.value = 'not equal to '
   if t.value == '\\leq':
      if lang == 1:
         t.value = 'menor o igual que '
      elif lang == 2:
         t.value = 'less than or equal to '
   if t.value == '\\lt':
      if lang == 1:
         t.value = 'menor que '
      elif lang == 2:
         t.value = 'less than '
   if t.value == '\\geq':
      if lang == 1:
         t.value = 'mayor o igual que '
      elif lang == 2:
         t.value = 'greater than or equal to '
   if t.value == '\\geq':
      if lang == 1:
         t.value = 'mayor que '
      elif lang == 2:
         t.value = 'greater than '
   print(str(t.value))
   return t


def t_SUP(t):
   r'\^'
   print(str(t.value))
   return t

def t_SUB(t):
   r'_'
   print(str(t.value))
   return t

def t_INT(t):
   r'(\\(oi|i{1,4}|idotsi)nt)'   
   if t.value == '\\int':
      if lang == 1:
         t.value = 'La integral '
      elif lang == 2:
         t.value = 'The integral '      
   elif t.value == '\\iint':
      if lang == 1:
         t.value = 'La doble integral '
      elif lang == 2:
         t.value = 'The double integral '   
   elif t.value == '\\iiint':
      if lang == 1:
         t.value = 'La triple integral '
      elif lang == 2:
         t.value = 'The triple integral '   
   elif t.value == '\\iiiint':
      if lang == 1:
         t.value = 'La cuádruple integral '
      elif lang == 2:
         t.value = 'The cuadruple integral '   
   elif t.value == '\\idotsint':
      if lang == 1:
         t.value = 'La integral infinita '
      elif lang == 2:
         t.value = 'The infinet integral '   
   print(str(t.value))
   return t
   
def t_SUM(t):
   r'(\\sum)|(\\prod)'
   if t.value == '\\sum':
      if lang == 1:
         t.value = 'La sumatoria '
      elif lang == 2:
         t.value = 'The sum '
   elif t.value == '\\prod':
      if lang == 1:
         t.value = 'La productoria '
      elif lang == 2:
         t.value = 'The production '
   print(str(t.value))
   return t

def t_DIF(t):
   r'd'
   if lang == 1:
      t.value = 'diferencial de '
   elif lang == 2:
      t.value = 'differential of '
   print(str(t.value))
   return t

def t_LIMIT(t):
   r'\\lim'
   if lang == 1:
      t.value = 'El límite cuando '
   elif lang == 2:
      t.value = 'The limit when '
   print(str(t.value))
   return t

def t_TO(t):
   r'\\to'
   if lang == 1:
      t.value = 'tiende a '
   elif lang == 2:
      t.value = 'tends to '
   print(str(t.value))
   return t

def t_INFINITY(t):
   r'(-\\infty)|(\+?\\infty)'
   if t.value == '-\\infty':
      if lang == 1:
         t.value = 'menos infinito '
      elif lang == 2:
         t.value = 'minus infinity '
   elif t.value == '+\\infty' or t.value == '\\infty':
      if lang == 1:
         t.value = 'infinito '
      elif lang == 2:
         t.value = 'infinity '
   print(str(t.value))
   return t

def t_FRAC(t):
   r'\\frac'
   t.value = 'La fracción de '
   print(str(t.value))
   return t

def t_RAIZ(t):
   r'\\sqrt((\[([0-9]+|[a-z]|\\alpha|\\nu|\\beta|\\xi|\\gamma|o|\\delta|\\pi|\\epsilon|\\rho|\\zeta|\\sigma|\\eta|\\tau|\\theta|\\upsilon|\\iota|\\ph|\\kappa|\\chi|\\lambda|\\psi|\\mu|\\omega)\])?)'
   if t.value == '\\sqrt':
      t.value = 'La raíz cuadrada de '
   elif t.value[0:5] == '\\sqrt[':
      t.value = 'La raíz ' +  t.value[6:-1] + ' ésima de '
   print(str(t.value))
   return t

def t_MON(t):
   r'(-?([0-9]*[a-z]+|[0-9]*(\\alpha|\\nu|\\beta|\\xi|\\gamma|o|\\delta|\\pi|\\epsilon|\\rho|\\zeta|\\sigma|\\eta|\\tau|\\theta|\\upsilon|\\iota|\\ph|\\kappa|\\chi|\\lambda|\\psi|\\mu|\\omega)))'
   j = str(t.value)
   print(j)
   if t.value[0] == '-':
      if t.value[1] == '\\':
         t.value =  t.value[2:]
      else:
         t.value =  t.value[1:]
         if lang == 1:
            p = ''
            for c in t.value:
               if c == 'x':
                  c = 'equis'
               elif c == 'v':
                  c = 'uve'
               elif c == 'y':
                  c = 'ye'
               p = p + ' ' + c
            t.value = p+' '
      t.value = 'menos ' +  t.value
      t.value = t.value + ''   
   else:
      if t.value[0] == '\\':
         t.value =  t.value[1:]
      else:
         if lang == 1:
            p = ''
            for c in t.value:
               if c == 'x':
                  c = 'equis'
               elif c == 'v':
                  c = 'uve'
               elif c == 'y':
                  c = 'ye'
               p = p + ' ' + c
            t.value = p+' '
         t.value = t.value + ''
      
   print(str(t.value))
   return t

def t_FUNCION(t):
   r'([A-Z]\([a-z]|\\alpha|\\nu|\\beta|\\xi|\\gamma|o|\\delta|\\pi|\\epsilon|\\rho|\\zeta|\\sigma|\\eta|\\tau|\\theta|\\upsilon|\\iota|\\ph|\\kappa|\\chi|\\lambda|\\psi|\\mu|\\omega(,[a-z]|\\alpha|\\nu|\\beta|\\xi|\\gamma|o|\\delta|\\pi|\\epsilon|\\rho|\\zeta|\\sigma|\\eta|\\tau|\\theta|\\upsilon|\\iota|\\ph|\\kappa|\\chi|\\lambda|\\psi|\\mu|\\omega*\)))'
   t.value = 'La funcion ' + t.value[0] + ' de ' + t.value[2:-1]
   print(str(t.value))
   return t

def t_error (t):
   print("¡Error léxico!")
   t.lexer.skip(1)

def t_newline(t):
   r'\n'
   t.lexer.lineno += t.value.count("\n")



#----------------------------------------------------------------------------------------

def p_alll(p):
   'alll : all'
   p[0] = p[1]
   print(p[0])
   outf = open('result.txt', 'a')
   outf.write(p[0]+ '\n\n')
   if lang == 1:
      tts = gTTS(text=p[0], lang='es')
   elif lang == 2:
      tts = gTTS(text=p[0], lang='en')
   
   tts.save('output.mp3')
#    path = os.getcwd() 
#    if sys.platform.startswith('darwin'):
#       os.system("open "+path+"/output.mp3")
#    elif sys.platform.startswith('linux'):
#       os.system("open "+path+"/output.mp3")
#    elif "win" in sys.platform:
#       os.system("start "+path+"/output.mp3")


def p_all1(p):
   'all : limit'
   p[0] = p[1]

def p_all2(p):
   'all : integral'
   p[0] = p[1]

def p_all3(p):
   'all : fraction'
   p[0] = p[1]

def p_all4(p):
   'all : root'
   p[0] = p[1]

def p_all5(p):
   'all : monomiall y'
   if not p[2]:         
      p[0] = p[1]
   else:
      p[0] = p[1] + p[2]

def p_all51(p):
   'all : NUM'
   p[0] = p[1] + ' '
def p_all52(p):
   'all : MON'
   p[0] = p[1] + ' '

def p_all6(p):
   'all : FUNCION'
   p[0] = p[1]

def p_all7(p):
   'all : REDI all x'
   p[0] = p[1] + p[2] + p[3]
def p_x(p):
   'x : OPERBI all x'
   p[0] = ', '+ p[1] + ', ' + p[2] + p[3]
def p_x2(p):
   'x : REDD y'
   if not p[2]:         
      p[0] = p[1]
   else:
      p[0] = p[1] + p[2]
def p_y(p):
   'y : exp'
   p[0] = p[1]
def p_y2(p):
   'y : '

def p_exp(p):
   'exp : SUP LLAVI all LLAVD'
   p[0] = 'elevado a , ' + p[3] + ', '

def p_monomiall(p):
   'monomiall : monomial monomiall'
   p[0] = p[1] + p[2]

def p_monomiall1(p):
   'monomiall : monomial'
   p[0] = p[1]

def p_monomial(p):
   'monomial : MON NUM'
   p[0] = p[1] + ' ' + p[2] + ' '

def p_monomial1(p):
   'monomial : NUM MON'
   p[0] = p[1] + ' ' + p[2] + ' '

def p_fraction(p):
   'fraction : FRAC LLAVI all LLAVD LLAVI all LLAVD'
   p[0] = p[1] + p[3] + ' dividido entre ' + p[6]

def p_root(p):
   'root : RAIZ LLAVI all LLAVD'
   p[0] = p[1] + p[3]

def p_integral(p):
   'integral : INT all DIF MON'
   p[0] = p[1] + 'de ' + p[2] + p[3] + p[4]

def p_integral2(p):
   'integral : INT SUB LLAVI all LLAVD SUP LLAVI all LLAVD all DIF MON'
   p[0] = p[1] + 'desde ' + p[4] + 'hasta, ' + p[8] + 'de ' + p[10] + p[11] + p[12]

def p_sum(p):
   'integral : SUM SUB LLAVI all LLAVD SUP LLAVI all LLAVD all'
   p[0] = p[1] + 'desde ' + p[4] + 'hasta, ' + p[8] + 'de ' + p[10]

def p_limit(p):
   'limit : LIMIT SUB LLAVI MON TO INFINITY LLAVD all'
   p[0] = p[1]  + p[4] + p[5] + p[6]+ 'de ' + p[8]

def p_limit1(p):
   'limit : LIMIT SUB LLAVI MON TO MON LLAVD all'
   p[0] = p[1]  + p[4] + p[5] + p[6]+ 'de ' + p[8]

def p_limit2(p):
   'limit : LIMIT SUB LLAVI MON TO NUM LLAVD all'
   p[0] = p[1]  + p[4] + p[5] + p[6]+ 'de ' + p[8]


def p_error(p):
   print("¡Error sintáctico!")

def init(language):
      if language == 'es':
            lang = 1
      elif language == 'en':
            lang = 2
      lex.lex()
      yacc.yacc()

def math_tts(expresion):
      yacc.parse(expresion)

if __name__== "__main__":
   try:
      lex.lex()
      yacc.yacc()
      choice = 3
      while choice != 0:
         choice = input("  1-Español\n  2-English\n  0-Salir\n>")
         choice = int(choice)
         if choice > 3:
            print("Opción inválida\n")
         elif choice == 1:
            try:
               print("\n")
               formula = input("Escriba la fórmula TeX>")
            except EOFError:
               break
            if not formula:
               continue
            
         elif choice == 2:
            lang = 2 #English
            # print u"Coming Soon!"
            # sys.exit(0)
            try:
               print("\n")
               formula = input("Write the TeX fórmula>")
            except EOFError:
               break
            if not formula:
               continue
         else:
            print("Hasta Luego")
            sys.exit(0)
         yacc.parse(formula)
   except KeyboardInterrupt:
      print("Shutdown requested...exiting")
   except Exception:
      traceback.print_exc(file=sys.stdout)
   sys.exit(0)
