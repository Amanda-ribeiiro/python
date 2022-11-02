meuCartão = int(input("Digite o numero do seu cartao de credito: "))

cartãoLido = 1
encontreiMeuCartãoNaLista = False

while cartãoLido != 0 and not encontreiMeuCartãoNaLista:
	cartãoLido = int(input("Digite o numero do proximo cartao de credito: "))
	if cartãoLido == meuCartão:
		encontreiMeuCartãoNaLista = True

if encontreiMeuCartãoNaLista:
	print("Eba!!! Meu cartão esta la!")
else:
	print("Xi!!! Meu cartão não esta la...")