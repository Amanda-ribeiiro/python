def main():

    num = int(input("Digite um numero (0 para terminar): "))

    cont = 0
    while num != 0:
        if eh_primo(num):
            cont += 1
        num = int(input("Digite um numero (0 para terminar): "))

    print("Achei %d primos na sequencia"% (cont))

def eh_primo(n):
    ''' (int) -> bool
