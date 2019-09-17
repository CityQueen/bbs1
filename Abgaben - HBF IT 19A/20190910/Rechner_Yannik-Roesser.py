while True:
  print('Oprtation:')
  print('Plus=    1')
  print('Minus=   2')
  print('Mal=     3')
  print('Geteilt= 4')
  print('Exit=    5')
  op = int(input('1, 2, 3, 4 oder 5: '))
  if op == 5:
    break
  else:
    print('Erste Zahl:')
    i1 = int(input())
    print('Zweite Zahl:')
    i2 = int(input())
    if op == 1:
      print('Das Ergebnis ist:', i1 + i2)
    elif op == 2:
      print('Das Ergebnis ist:', i1 - i2)
    elif op == 3:
      print('Das Ergebnis ist:', i1 * i2)
    elif op == 4:
      if i1 == 0:
        print('Kann nicht durch "0" teilen')
      elif i2 == 0:
        print('Kann nicht durch "0" teilen')
      else:
        print('Das Ergebnis ist:', i1 / i2)
    else:
      print('Ein Fehler Ist aufgetreten bitte geben sie eine zahl von 1-5 an!')
  print('')