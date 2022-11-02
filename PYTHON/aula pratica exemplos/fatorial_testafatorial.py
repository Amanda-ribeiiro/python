Python 3.10.6 (tags/v3.10.6c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def fatorial(n):
	fat = 1
	while (n > 1):
		fat = fat * n
		n = n - 1
	return fat


def testa_fatorial():
	if fatorial(1) == 1:
		print("Funciona para 1"
	else:
		print("Não funciona para 1")
	if fatorial(2) == 2:
		print("Funciona para 2")
	else:
		print("Não funciona para 2")
	if fatorial(0) == 1:
		print("Funciona para 0")
	else:
		print("Não funciona para 0")
	if fatorial(5) == 120:
		print("Funciona para 5")
	else:
		print("Não funciona para 5")
