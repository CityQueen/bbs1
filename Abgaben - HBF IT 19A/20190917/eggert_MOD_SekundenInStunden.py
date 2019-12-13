rest = 255%7
print(rest)

AnzahlSekunden = float(input("Bitte geben sie eine Anzahl Sekunden ein "))
Restsekunden = AnzahlSekunden%3600
anzahlstunden = AnzahlSekunden/3600
anzahlminuten = Restsekunden/60
endrestsekunden = Restsekunden%60

print(int(AnzahlSekunden), "Sekunden sind ", int(anzahlstunden), " Stunden ", int(anzahlminuten), " Minuten und ", int(endrestsekunden), " Sekunden ")


