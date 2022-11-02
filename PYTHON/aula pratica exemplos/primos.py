def èPrimo (x):
    fator = 2
    if x == 2:
        return True

    while x % fator != 0 and fator <= x/2:
        fator = fator + 1
    if x % fator == 0:
        return False
    else:
        return True


n = int(input("Digite um nùmero inteiro: "))

while n > 0:
    if èPrimo(n):
        print (n, "è primo!")
    else:
        print (n, "não è primo :-(")
    n = int(input("Digite um nùmero inteiro: "))
    
