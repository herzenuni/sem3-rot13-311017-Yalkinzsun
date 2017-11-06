# ---------------------------
# Author: Skorobogatov kirill
# ---------------------------

a = {'A': 'N', 'B': 'O', 'C': 'P', 'D': 'Q', 'E': 'R', 'F': 'S'}
a1 = {'G': 'T', 'H': 'U', 'I': 'V', 'J': 'W', 'K': 'X', 'L': 'Y', 'M': 'Z'}

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
    """
    *Функция считывает строку из консоли/из файла
    *Сопоставляет каждый элент со значением/ключом из словаря для кодирования
    *Выводит результат в консоль/отдельный файл для результата
    """
    try:
      print('What do You want to do? \n (1) - to decrypt (ROT13 -> EN) \n (2) - to encrypt (EN -> ROT13)  ')
      x = float(input('> Enter operation number: '))
    except ValueError:
      print(' !Enter the number!')
    try:
      z = float(input(' (3) - from console or (4) - from document?: '))
    except ValueError:
      print(' !Enter the number!!')
    else:
      if z == 3:
        s = input('>> Enter the string: ')
        str = ''
        if x == 1:
          for item in s:
            if item in a.keys():
                str += a.get(item)
        print(">>> Decoding: ", str)
        if x == 2:
          inv_a = {v: k for k, v in a.items()}
          for item in s:
            if item in inv_a.keys():
                str += inv_a.get(item)
        print('>>> Encoding: ', str)

      elif z == 4:
       try:
        file = open("string.txt")
       except OSError:
        print('OSError!')
       try:
        cont = file.read()
        result = open("Result.txt","w")
       except OSError:
          print('OSError!')
       else:
        str = ''
        if x == 1:
          for item in cont:
            if item in a.keys():
                str += a.get(item)
          result.write(str)
          print(">>> Decoding was finished! ")
          print('>>>Result ',str)
        if x == 2:
          inv_a = {v: k for k, v in a.items()}
          for item in cont:
            if item in inv_a.keys():
                str += inv_a.get(item)

          result.write(str)
          print('>>> Encoding was finished! ')
          print('>>> Result ', str)
       finally:
        file.close()
        result.close()

ROT13()
