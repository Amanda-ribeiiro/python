def PegarEntrada():
    return int(input("Forneça um numero inteiro: "))


def RetanguloCheio(dimensoes):
    largura, altura = dimensoes
    preencherVertical = 1

    while preencherVertical <= altura:
        preencherHorizontal = 1

        while preencherHorizontal <= largura:
            print("#", end="")
            preencherHorizontal += 1
        print ("")
        preencherVertical += 1

def Main():
    dimensoes = (PegarEntrada(), PegarEntrada())
    RetanguloCheio(dimensoes)
    
Main()
