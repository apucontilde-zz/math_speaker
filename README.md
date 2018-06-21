# math_speaker
Por 
Ricardo Apú Chinchilla  y Alonso Mondal Durán 
como proyecto para el curso de Autómatas y Compiladores 
de la Escuela de Ciencias de Computación e Informática 
de la Universidad de Costa Rica
Julio, 2016

Descripción:

Convierte fórmulas matemáticas en formato TeX a su correspondiente desarrollo en palabras en Español.
dependencias: 
- PLY - Python Lex-Yaxx (http://www.dabeaz.com/ply/)
- OS, SYS

Uso:
OPCION 1:
1. Correr, de alguna manera, 'python mathspeaker.py'.
2. Escribir fórmulas matemáticas en tex.
OPCIÓN 2:
python3 mathspeaker_file.py --filepath <filepath> --lang <lang: es | en>


Gramática: 

all : limit;
all : integral;
all : fraction;
all : root;
all : monomiall y;
all : NUM;
all : MON;
all : FUNCION;
all : REDI all x;
x : OPERBI all x;
x : REDD y;
y : exp;
y : ;
exp : SUP LLAVI all LLAVD;
monomiall : monomial monomiall;
monomiall : monomial;
monomial : MON NUM;
monomial : NUM MON;
fraction : FRAC LLAVI all LLAVD LLAVI all LLAVD;
root : RAIZ LLAVI all LLAVD;
integral : INT all DIF MON;
integral : INT SUB LLAVI all LLAVD SUP LLAVI all LLAVD all DIF MON;
integral : SUM SUB LLAVI all LLAVD SUP LLAVI all LLAVD all; 
limit : LIMIT SUB LLAVI MON TO INFINITY LLAVD all
limit : LIMIT SUB LLAVI MON TO MON LLAVD all
limit : LIMIT SUB LLAVI MON TO NUM LLAVD all
limit : LIMIT SUB LLAVI INFINITY TO MON LLAVD all


EJEMPLOS:
(\frac{4}{5} + \frac{x}{7\xi} + \frac{(x)^{2}}{3}) 

\sum_{(i=0)}^{1000} (\frac{1}{(x)^{2}} = \frac{(\pi)^{2}}{6}) 

\lim_{x \to \infty} \iint_{5}^{x} (4y+5) dy

\sqrt{(\frac{45z}{56y} + 4z + 7)^{\alpha}}

\iint_{(5+x)}^{7} ( \frac{\frac{x}{3}}{7} + 5x + 8) dx



Existen lectores de matemáticas dirigidos a exploradores ( ver https://github.com/mathjax/MathJax-docs/wiki/List-of-math-enabled-screen-readers) este repositorio busca lograr crear un lector para exámenes y documentos matemáticos hechos en LaTeX.
