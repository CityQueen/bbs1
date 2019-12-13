ewicht = float(input("Bitte geben sie ihr Gewicht in Kilogramm ein"))
Groesse = float(input("Bitte geben sie ihre Größe in Meter ein"))

BMI = Gewicht / Groesse**2

print(BMI)

Netto = float(input("Bitte geben sie den Bruttopreis ein"))
Preis7 = Netto*1.07
Preis19 = Netto*1.19

Betrag = float(input("Bitte geben sie einen Startbetrag ein"))
Zinssatz = float(input("Bitte geben sie einen Zinssatz an"))

Jahreszinsen = Betrag*(Zinssatz/100)
print(Jahreszinsen)