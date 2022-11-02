Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
temperatura = 102
if temperatura > 100:
    aguaFerve = True

    
aguaFerve
True
if temperatura > 100:
    aguaFerve = True
    evaporacao = "muito rapida"

    
aguaFerve
True
evaporacao
'muito rapida'



tempoDeJogo = input("Quanto tempo temos ja jogados?")
Quanto tempo temos ja jogados?
tempoDeJogo = int(input("Quando tempo temos ja jogados?"))
Quando tempo temos ja jogados? 
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    tempoDeJogo = int(input("Quando tempo temos ja jogados?"))
ValueError: invalid literal for int() with base 10: ' '
if tempoDeJogo <= 90:
    print("Ainda tem jogo pela frente")
    print("Que bom, eu adoro futebol")

    
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    if tempoDeJogo <= 90:
TypeError: '<=' not supported between instances of 'str' and 'int'
else:
    
SyntaxError: invalid syntax
print("Putz, ta acabando o jogo")
Putz, ta acabando o jogo
print("Apita logo, juiz")
Apita logo, juiz
import math
math.sqrt(8)
2.8284271247461903
import math
math.sqrt(9)
3.0
delta = 763167
math.sqrt(delta)
873.5942994319503
