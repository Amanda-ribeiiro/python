def maximo(numero1, numero2, numero3):
    maiorNumero = 0
    numeros = (numero1, numero2, numero3)

    for chave, numeroCorrente in enumerate (numeros):
        if numeroCorrente > maiorNumero:
            maiorNumero = numeroCorrente

    return maiorNumero

def maximoMElhorada(numeros = []):
    numeros.sort()
    return numeros[(len(numeros) - 1):len(numeros)]

def test_MaiorEntreNumerosPositivos():
    assert 1 == maximo (152, 19, 88)

def test_MaiorEntreNumerosNegativos():
    assert 0 == maximo(-3, -423, 0)

def test_MaiorEntreNumerosPositivosENegativos():
    assert 42 == maximo(- 7, 0, 51)
