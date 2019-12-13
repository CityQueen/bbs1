tempfahrenheit = int(input("Bitte geben sie eine Temperatur in Fahrenheit ein"))
tempfahrenheit = float(tempfahrenheit)
tempcelsius = (tempfahrenheit-32)*5/9

print(" Die Temperatur", tempfahrenheit, "in Fahrenheit entspricht der Temeperatur", tempcelsius,"in celsius")

Tage = input("Bitte geben sie eine Anzahl Tage ein ")
Minuten = input("Bitte geben sie eine Anzahl Minuten ein ")
Sekunden = input("Bitte geben sie eine Anzahl Sekunden ein ")

Tage_als_int = int(Tage)
Minuten_als_int = int(Minuten)
Sekunden_als_int = int(Sekunden)

InsgesamtSekunden = Tage_als_int*24*60*60 + Minuten_als_int*60 + Sekunden_als_int

print(InsgesamtSekunden)

