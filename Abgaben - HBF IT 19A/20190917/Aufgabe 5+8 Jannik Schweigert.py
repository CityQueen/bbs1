sekunden = int(input('wie viele sekunden haben wir noch?: '))

Tage = sekunden//86400
rest1 = sekunden - Tage * 86400
stunden = rest1//3600
rest2 = rest1 - stunden * 3600
minuten = rest2//60
sekunden = rest2 - minuten*60

print(Tage, 'Tage')
print(stunden, 'Stunden')
print(minuten, 'Minuten')
print(sekunden, 'Sekunden')