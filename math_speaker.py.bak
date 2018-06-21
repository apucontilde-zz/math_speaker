# coding=utf-8
import ply.yacc as yacc
import ply.lex as lex
#from __future__ import absolute_import
from io import open
from gtts import gTTS
import os, sys

tokens = (u'NUM',u'LLAVI',u'LLAVD',u'REDI',u'REDD', u'OPERBI', u'SUB', u'SUP', u'INT', u'SUM', u'DIF', u'LIMIT', u'TO', u'INFINITY', u'FRAC', u'RAIZ',u'MON',u'FUNCION')

#tokens default
t_ignore = u" \t\n"

def t_NUM(t):
	ur'-?[0-9]+'
	if t.value[0] == u'-':
		t.value =  t.value[1:]
		if lang == 1:
			t.value = u'menos ' +  t.value
		elif lang == 2:
			t.value = u'minus ' +  t.value
	j=unicode(t.value)
	print j
	return t

#def t_VAR(t):
#	r'[a-z]|\\alpha|\\nu|\\beta|\\xi|\\gamma|o|\\delta|\\pi|\\epsilon|\\rho|\\zeta|\\sigma|\\eta|\\tau|\\theta|\\upsilon|\\iota|\\ph|\\kappa|\\chi|\\lambda|\\psi|\\mu|\\omega'
#	if t.value[0] == '\\':
#		t.value = t.value[1:] + ' ' #si es letra griega agarra todo menos el
#	return t

def t_LLAVI(t):
	ur'\{'
	#t.value = 'abre llave x
	print unicode(t.value)
	return t

def t_LLAVD(t):
	ur'\}'
	#t.value = 'cierra llave '
	print unicode(t.value)
	return t

def t_REDI(t):
	ur'\('
	#t.value = 'abre paréntesis '
	t.value = u', '
	print unicode(t.value)
	return t

def t_REDD(t):
	ur'\)'
	#t.value = 'cierra paréntesis '
	t.value = u', '
	print unicode(t.value)
	return t

def t_OPERBI(t):
	ur'(\+|-|(\\times)|(\\cdot)|(\\div)|=|(\\neq)|(\\leq)|(\\geq))'
	if t.value == u'+':
		if lang == 1:
			t.value = u'más '
		elif lang == 2:
			t.value = u'plus '
	if t.value == u'-':
		if lang == 1:
			t.value = u'menos '
		elif lang == 2:
			t.value = u'minus '
	if t.value == u'\\times' or t.value == u'\\cdot':
		if lang == 1:
			t.value = u'multiplicado por '
		elif lang == 2:
			t.value = u'times '
	if t.value == u'=':
		if lang == 1:
			t.value = u'igual a '
		elif lang == 2:
			t.value = u'equals '
	if t.value == u'\\neq':
		if lang == 1:
			t.value = u'diferente de '
		elif lang == 2:
			t.value = u'not equal to '
	if t.value == u'\\leq':
		if lang == 1:
			t.value = u'menor o igual que '
		elif lang == 2:
			t.value = u'less than or equal to '
	if t.value == u'\\lt':
		if lang == 1:
			t.value = u'menor que '
		elif lang == 2:
			t.value = u'less than '
	if t.value == u'\\geq':
		if lang == 1:
			t.value = u'mayor o igual que '
		elif lang == 2:
			t.value = u'greater than or equal to '
	if t.value == u'\\geq':
		if lang == 1:
			t.value = u'mayor que '
		elif lang == 2:
			t.value = u'greater than '
	print unicode(t.value)
	return t


def t_SUP(t):
	ur'\^'
	print unicode(t.value)
	return t

def t_SUB(t):
	ur'_'
	print unicode(t.value)
	return t

def t_INT(t):
	ur'(\\(oi|i{1,4}|idotsi)nt)'	
	if t.value == u'\\int':
		if lang == 1:
			t.value = u'La integral '
		elif lang == 2:
			t.value = u'The integral '		
	elif t.value == u'\\iint':
		if lang == 1:
			t.value = u'La doble integral '
		elif lang == 2:
			t.value = u'The double integral '	
	elif t.value == u'\\iiint':
		if lang == 1:
			t.value = u'La triple integral '
		elif lang == 2:
			t.value = u'The triple integral '	
	elif t.value == u'\\iiiint':
		if lang == 1:
			t.value = u'La cuádruple integral '
		elif lang == 2:
			t.value = u'The cuadruple integral '	
	elif t.value == u'\\idotsint':
		if lang == 1:
			t.value = u'La integral infinita '
		elif lang == 2:
			t.value = u'The infinet integral '	
	print unicode(t.value)
	return t
	
def t_SUM(t):
	ur'(\\sum)|(\\prod)'
	if t.value == u'\\sum':
		if lang == 1:
			t.value = u'La sumatoria '
		elif lang == 2:
			t.value = u'The sum '
	elif t.value == u'\\prod':
		if lang == 1:
			t.value = u'La productoria '
		elif lang == 2:
			t.value = u'The production '
	print unicode(t.value)
	return t

def t_DIF(t):
	ur'd'
	if lang == 1:
		t.value = u'diferencial de '
	elif lang == 2:
		t.value = u'differential of '
	print unicode(t.value)
	return t

def t_LIMIT(t):
	ur'\\lim'
	if lang == 1:
		t.value = u'El límite cuando '
	elif lang == 2:
		t.value = u'The limit when '
	print unicode(t.value)
	return t

def t_TO(t):
	ur'\\to'
	if lang == 1:
		t.value = u'tiende a '
	elif lang == 2:
		t.value = u'tends to '
	print unicode(t.value)
	return t

def t_INFINITY(t):
	ur'(-\\infty)|(\+?\\infty)'
	if t.value == u'-\\infty':
		if lang == 1:
			t.value = u'menos infinito '
		elif lang == 2:
			t.value = u'minus infinity '
	elif t.value == u'+\\infty' or t.value == u'\\infty':
		if lang == 1:
			t.value = u'infinito '
		elif lang == 2:
			t.value = u'infinity '
	print unicode(t.value)
	return t

def t_FRAC(t):
	ur'\\frac'
	t.value = u'La fracción de '
	print unicode(t.value)
	return t

def t_RAIZ(t):
	ur'\\sqrt((\[([0-9]+|[a-z]|\\alpha|\\nu|\\beta|\\xi|\\gamma|o|\\delta|\\pi|\\epsilon|\\rho|\\zeta|\\sigma|\\eta|\\tau|\\theta|\\upsilon|\\iota|\\ph|\\kappa|\\chi|\\lambda|\\psi|\\mu|\\omega)\])?)'
	if t.value == u'\\sqrt':
		t.value = u'La raíz cuadrada de '
	elif t.value[0:5] == u'\\sqrt[':
		t.value = u'La raíz ' +  t.value[6:-1] + u' ésima de '
	print unicode(t.value)
	return t

def t_MON(t):
	ur'(-?([0-9]*[a-z]+|[0-9]*(\\alpha|\\nu|\\beta|\\xi|\\gamma|o|\\delta|\\pi|\\epsilon|\\rho|\\zeta|\\sigma|\\eta|\\tau|\\theta|\\upsilon|\\iota|\\ph|\\kappa|\\chi|\\lambda|\\psi|\\mu|\\omega)))'
	j = unicode(t.value)
	print j
	if t.value[0] == u'-':
		if t.value[1] == u'\\':
			t.value =  t.value[2:]
		else:
			t.value =  t.value[1:]
			if lang == 1:
				p = ''
				for c in t.value:
					if c == u'x':
						c = 'equis'
					elif c == u'v':
						c = 'uve'
					elif c == u'y':
						c = 'ye'
					p = p + ' ' + c
				t.value = p+u' '
		t.value = u'menos ' +  t.value
		t.value = t.value + u''	
	else:
		if t.value[0] == u'\\':
			t.value =  t.value[1:]
		else:
			if lang == 1:
				p = ''
				for c in t.value:
					if c == u'x':
						c = 'equis'
					elif c == u'v':
						c = 'uve'
					elif c == u'y':
						c = 'ye'
					p = p + ' ' + c
				t.value = p+u' '
			t.value = t.value + u''
		
	print unicode(t.value)
	return t

def t_FUNCION(t):
	ur'([A-Z]\([a-z]|\\alpha|\\nu|\\beta|\\xi|\\gamma|o|\\delta|\\pi|\\epsilon|\\rho|\\zeta|\\sigma|\\eta|\\tau|\\theta|\\upsilon|\\iota|\\ph|\\kappa|\\chi|\\lambda|\\psi|\\mu|\\omega(,[a-z]|\\alpha|\\nu|\\beta|\\xi|\\gamma|o|\\delta|\\pi|\\epsilon|\\rho|\\zeta|\\sigma|\\eta|\\tau|\\theta|\\upsilon|\\iota|\\ph|\\kappa|\\chi|\\lambda|\\psi|\\mu|\\omega*\)))'
	t.value = u'La funcion ' + t.value[0] + u' de ' + t.value[2:-1]
	print unicode(t.value)
	return t

def t_error (t):
	print u"¡Error léxico!"
	t.lexer.skip(1)

def t_newline(t):
	ur'\n'
	t.lexer.lineno += t.value.count(u"\n")



#----------------------------------------------------------------------------------------

def p_alll(p):
	u'alll : all'
	p[0] = p[1]
	print p[0]
	outf = open(u'result.txt', u'a')
	outf.write(p[0]+ u'\n\n')
	if lang == 1:
		tts = gTTS(text=p[0], lang=u'es')
	elif lang == 2:
		tts = gTTS(text=p[0], lang=u'en')
	
	tts.save(u'output.mp3')
	path = os.getcwd() 
	if sys.platform.startswith('darwin'):
		os.system("open "+path+"/output.mp3")
	elif sys.platform.startswith('linux'):
		os.system("open "+path+"/output.mp3")
	elif "win" in sys.platform:
		os.system("start "+path+"/output.mp3")


def p_all1(p):
	u'all : limit'
	p[0] = p[1]

def p_all2(p):
	u'all : integral'
	p[0] = p[1]

def p_all3(p):
	u'all : fraction'
	p[0] = p[1]

def p_all4(p):
	u'all : root'
	p[0] = p[1]

def p_all5(p):
	u'all : monomiall y'
	if not p[2]:			
		p[0] = p[1]
	else:
		p[0] = p[1] + p[2]

def p_all51(p):
	u'all : NUM'
	p[0] = p[1] + u' '
def p_all52(p):
	u'all : MON'
	p[0] = p[1] + u' '

def p_all6(p):
	u'all : FUNCION'
	p[0] = p[1]

def p_all7(p):
	u'all : REDI all x'
	p[0] = p[1] + p[2] + p[3]
def p_x(p):
	u'x : OPERBI all x'
	p[0] = u', '+ p[1] + u', ' + p[2] + p[3]
def p_x2(p):
	u'x : REDD y'
	if not p[2]:			
		p[0] = p[1]
	else:
		p[0] = p[1] + p[2]
def p_y(p):
	u'y : exp'
	p[0] = p[1]
def p_y2(p):
	u'y : '

def p_exp(p):
	u'exp : SUP LLAVI all LLAVD'
	p[0] = u'elevado a , ' + p[3] + u', '

def p_monomiall(p):
	u'monomiall : monomial monomiall'
	p[0] = p[1] + p[2]

def p_monomiall1(p):
	u'monomiall : monomial'
	p[0] = p[1]

def p_monomial(p):
	u'monomial : MON NUM'
	p[0] = p[1] + u' ' + p[2] + u' '

def p_monomial1(p):
	u'monomial : NUM MON'
	p[0] = p[1] + u' ' + p[2] + u' '

def p_fraction(p):
	u'fraction : FRAC LLAVI all LLAVD LLAVI all LLAVD'
	p[0] = p[1] + p[3] + u' dividido entre ' + p[6]

def p_root(p):
	u'root : RAIZ LLAVI all LLAVD'
	p[0] = p[1] + p[3]

def p_integral(p):
	u'integral : INT all DIF MON'
	p[0] = p[1] + u'de ' + p[2] + p[3] + p[4]

def p_integral2(p):
	u'integral : INT SUB LLAVI all LLAVD SUP LLAVI all LLAVD all DIF MON'
	p[0] = p[1] + u'desde ' + p[4] + u'hasta, ' + p[8] + u'de ' + p[10] + p[11] + p[12]

def p_sum(p):
	u'integral : SUM SUB LLAVI all LLAVD SUP LLAVI all LLAVD all'
	p[0] = p[1] + u'desde ' + p[4] + u'hasta, ' + p[8] + u'de ' + p[10]

def p_limit(p):
	u'limit : LIMIT SUB LLAVI MON TO INFINITY LLAVD all'
	p[0] = p[1]  + p[4] + p[5] + p[6]+ u'de ' + p[8]

def p_limit1(p):
	u'limit : LIMIT SUB LLAVI MON TO MON LLAVD all'
	p[0] = p[1]  + p[4] + p[5] + p[6]+ u'de ' + p[8]

def p_limit2(p):
	u'limit : LIMIT SUB LLAVI MON TO NUM LLAVD all'
	p[0] = p[1]  + p[4] + p[5] + p[6]+ u'de ' + p[8]


def p_error(p):
	print u"¡Error sintáctico!"

if __name__== "__main__":
	try:
		lex.lex()
		yacc.yacc()

		choice = 3
		while choice != 0:
			choice = raw_input("\t1-Español\n\t2-English\n\t0-Salir\n>")
			choice = int(choice)
			if choice > 3:
				print "Opción inválida\n"
			elif choice == 1:
				try:
					print u"\n"
					ms = raw_input("Escriba la fórmula TeX>")
				except EOFError:
					break
				if not ms:
					continue
				
			elif choice == 2:
				lang = 2 #English
				# print u"Coming Soon!"
				# sys.exit(0)
				try:
                                        print u"\n"
                                        ms = raw_input("Write the TeX fórmula>")
                                except EOFError:
                                        break
                                if not ms:
                                        continue
			else :
				print u"Hasta Luego"
				sys.exit(0)
			yacc.parse(ms)
	except KeyboardInterrupt:
        	print "Shutdown requested...exiting"
    	except Exception:
        	traceback.print_exc(file=sys.stdout)
    	sys.exit(0)
