// https://pt.stackoverflow.com/questions/312704/o-que-est%c3%a1-errado-no-c%c3%b3digo-em-python-bhaskara#:~:text=import%20math%20def%20Bhaskara%20%28%29%3A%20a%20%3D%20int,%7B%7D%27.format%20%28x2%29%29%20if%20%28__name__%20in%20%27__main__%27%29%3A%20Bhaskara%20%28%29
// se o delta for igual a 0 ela nao ter raizes reais. 
// delta < 0 = essa equacao nao possui raizes reais 
// delta   0 = a raiz dessa equacao è 
// delta > 0 = as raizes da equacao sao ...
// math.sqrt(x) (precisa importar no IDLE = import math
//  return the square root of x.


entrada 3 valores: a,b e c = constantes da equacao de 2 grau
usando a formula de mascara vai imprimir as raizes
a = 
b = 
c =

import math

def Bhaskara():
a = int(input('Digite um valor para A '))
b = int(input('Digite um valor para B '))
c = int(input('Digute um valor para C '))

#(-b +- {-b² - 4 * a * c} ) / 2 * c

operacao = -b
raiz = (operacao * operacao) - 4 * a * c
raiz = math.sqrt(raiz)
divisao = 2 * c
# (operacao +- raiz) / divisao
x1 = (operacao + raiz) / divisao
x2 = (operacao - raiz) / divisao
print('X1 = {}'.format(x1))
print('X2 = {}'.format(x2))
if(__name__ in '__main__'):
Bhaskara()







import math
math.srt(colocar o numero)

delta = valor do resultado
math.sqrt(numero)
00.000000000000
ax2 + bx + c = 0

if 
else 
