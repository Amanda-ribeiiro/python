def DivisorSemResto(numero, divisor =3):
    return True if numero % divisor == 0 else False

def fizzbuzz(numero):
    if DivisorSemResto(numero) and DivisorSemResto(numero, 5):
        return 'FizzBuzz'
    elif DivisorSemResto(numero) and not DivisorSemResto(numero, 5):
        return 'Fizz'
    elif not DivisorSemResto(numero) and DivisorSemResto(numero, 5):
        return 'Buzz'
    else:
        return numero

def test_DivisePorTresECinco():
    assert 'FizzBuzz'== fizzbuzz(15)

def test_DivisiveApenasPorTres():
    assert 'Fizz'== FizzBuzz(3)

def test_DiviseApenasPorCinco():
    assert 'Buzz' == fizzbuzz(5)

def test_NaoDivisePorTresECinco():
    assert 4 == fizzbuzz(4)

    
