Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# content of test_sample.py
def func(x):
    return x + 1

def test_answer():
    assert func(3) == 5