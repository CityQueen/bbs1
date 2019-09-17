sekunden = int(input('wie viele sekunden haben wir noch?: '))

stunden = sekunden//3600
rest1 = sekunden - stunden * 3600
minuten = rest1//60
rest2 = rest1 - minuten*60

print(stunden, 'stunden', minuten, 'minuten', rest2, 'sekunden')