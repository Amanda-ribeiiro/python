import math

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

delta = b ** 2 - 4 * a * c

if delta == 0:
	raiz1= (-b + math.sqrt(delta)) / (2 * a)
	print("A unica raiz e: ", raiz1)
else:
	if delta < 0:
		print("esta equacao nao possui raizes reias")
	else:
		raiz1= (-b + math.sqrt(delta)) / (2 * a)
		raiz2= (-b - math.sqrt(delta)) / (2 * a)
		print("A primeira raiz e: ", raiz1)
		print("A primeira raiz e: ", raiz2)
