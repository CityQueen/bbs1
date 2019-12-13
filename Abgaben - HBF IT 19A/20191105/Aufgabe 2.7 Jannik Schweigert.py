menge = float(input('Eingefüllte menge in gram: '))
if menge == 150:
    print('Die exakte menge wurde ereicht')
elif menge < 165 and menge > 142.5:
    print('Menge ist im akzepstanz bereich')
elif menge > 165:
    print('Eingefülte menge ist zu Groß')
elif menge < 142.5:
    print('Eingefülte mege ist zu niedrig')
else:
    print('ERROR')