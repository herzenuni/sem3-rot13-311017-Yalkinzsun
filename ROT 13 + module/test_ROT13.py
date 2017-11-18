def test_console(fun1):
    assert fun1([0 - 9]), 'Only letters were support!'
    assert fun1('Uryyb') == 'Hello', 'Decoding is NOT ok!'
    assert fun1('Hello') == 'Uryyb', 'Decryption is NOT ok!'


def test_file(fun2, fun1):
    x = open("string(EN).txt")  # Hello
    y = open("Result.txt", "w")
    assert fun2(x, y) == 'Uryyb', 'Decryption is NOT ok!'
    assert fun2(x, y) == fun1('Hello'), 'Functions give DIFFERENT results with the same data! - (1)'
    x.close()
    x = open("string(ROT13).txt")  # Uryyb
    assert fun2(x, y) == 'Hello', 'Decoding is NOT ok!'
    assert fun2(x, y) == fun1('Uryyb'), 'Functions give DIFFERENT results with the same data! - (2)'
    x.close()
    y.close()
