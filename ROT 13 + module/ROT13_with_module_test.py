# ---------------------------
# Author: Skorobogatov kirill
# ---------------------------

a = {'A': 'N', 'B': 'O', 'C': 'P', 'D': 'Q', 'E': 'R', 'F': 'S'}
a1 = {'G': 'T', 'H': 'U', 'I': 'V', 'J': 'W', 'K': 'X', 'L': 'Y', 'M': 'Z'}  #'H': 'U'

b = {'N': 'A', 'O': 'B', 'P': 'C', 'Q': 'D', 'R': 'E', 'S': 'F'}
b1 = {'T': 'G', 'U': 'H', 'V': 'I', 'W': 'J', 'X': 'K', 'Y': 'L', 'Z': 'M'}

a.update(a1)
b.update(b1)
a.update(b)  # capitalization dictionary

w = {'a': 'n', 'b': 'o', 'c': 'p', 'd': 'q', 'e': 'r', 'f': 's'}
w1 = {'g': 't', 'h': 'u', 'i': 'v', 'j': 'w', 'k': 'x', 'l': 'y', 'm': 'z'}

v = {'n': 'a', 'o': 'b', 'p': 'c', 'q': 'd', 'r': 'e', 's': 'f'}
v1 = {'t': 'g', 'u': 'h', 'v': 'i', 'w': 'j', 'x': 'k', 'y': 'l', 'z': 'm'}

w.update(w1)
v.update(v1)
w.update(v)  # lowercase dictionary

a.update(w)  # full dictionary

def ROT13():
    def from_concole(s, _str=''):
        for item in s:
            if item in a.keys():
                _str += a.get(item)
        return _str

    def from_file(file, result, _str=''):
        cont = file.read()
        for item in cont:
            if item in a.keys():
                _str += a.get(item)
        result.write(_str)
        return 'Finished'

    if __name__ == "main":
        import test_ROT13 as ROT13
        ROT13.test_console(from_concole)
        ROT13.test_file(from_file, from_concole)

    print('What do you want? \n'
          '(1) - to decrypt (ROT13 -> EN) \n'
          '(2) - to encrypt (EN -> ROT13)')

    x = float(input('> Enter operation number: '))

    z = float(input(' (3) - from console or (4) - from document?: '))

    if z == 3:
        s = input('>> Enter the string: ')
        if x == 1:
            print(">>> Decoding: ", from_concole(s))
        elif x == 2:
            print('>>> Encoding: ', from_concole(s))

    elif z == 4:
        _file = open("string(ROT13)_test.txt")
        _result = open("Result.txt", "w")
        if x == 1:
            print(">>> Decoding: ", from_file(_file, _result))
            _file.close()
        elif x == 2:
            _file = open("string(EN)_test.txt")
            print('>>> Encoding: ', from_file(_file, _result))
            _file.close()
            _result.close()

ROT13()
