"""
Модуль содержит 2 функции:
    1-ая 'test_console(fun1)' - проверяет работу шифрования/дешифрования 
    функции fun1
    2-ая 'test_file(fun2,fun1)' - проверяет работу шифрования/дешифрования
    функции fun2, полученной из файла. Проверяет на сходность результатов 
    выполнения fun1 и fun2 при одинаковых исходных данных (одиноковой строке)
"""


def test_console(fun1):
    # assert fun1([0 - 9]), 'Only letters were support!'
    assert fun1('uryyb') == 'hello', 'test_console : assert 1'
    assert fun1('hello') == 'uryyb', 'test_console : assert 2'


def test_file(fun1, fun2):
    source = open("string(EN)_test.txt", "r")  # Hello
    result = open("Result.txt", "w")
    assert fun1(source, result) == 'Uryyb', 'test_file : assert 1'
    assert fun1(source, result) == fun2(source.read()), 'test_file : assert 2'
    source.close()
    source = open("string(ROT13)_test.txt")  # Uryyb
    assert fun1(source, result) == 'Hello', 'test_file : assert 3'
    assert fun1(source, result) == fun2(source.read()), 'test_file : assert 4'
    source.close()
    result.close()

