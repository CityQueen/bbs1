p = input('Gib ein wort ein:')
p = p.upper()
p = p.replace(' ','')
q = p[::-1]
if p == q:
    print('Es ist ein Palindrom')
else:
    print('Es ist kein Palindrom')