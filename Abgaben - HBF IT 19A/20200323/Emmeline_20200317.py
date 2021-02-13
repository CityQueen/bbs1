# Von Florian Schmitz
# Erzeugen Sie mindestens sechs verschiedene Listen, die nur Zahlen bzw. nur Wörter oder Sätze beinhalten. Entwerfen Sie Quellcode, der die nachfolgenden Aufgaben realisiert:
# a) Für Listen, die Zahlen enthalten, soll der Mittelwert sowie das kleinste und das größte Element ausge- geben werden.
# b) Für Listen, die Wörter bzw. Sätze enthalten, soll das Element mit den meisten Zeichen ausgegeben werden.
from time import sleep

zahlen_liste1=[3,8,12,56,33,2,48,93,40,14]
mittelwert1=(3+8+12+56+33+2+48+93+40+14)/10
zahlen_liste2=[52,1,834,29,16,23,11,5,20,10]
mittelwert2=(52+1+834+29+16+23+11+5+20+10)/10
zahlen_liste3=[90,44,20,15,6]
mittelwert3=(90+44+20+15+6)/5
wörter_liste1=['Mond','Lampen','Zange','Igel']
wörter_liste2=['Internet','Flage','Runde','Leben']
wörter_liste3=['Stein','Kisten','Hallo','Bilder']
#zahlen_liste1
print("Die erste Zahlenliste lautet:", zahlen_liste1)
print("Die größte Zahl der ersten Zahlenliste ist", max(zahlen_liste1))
print("Die kleinste Zahl der ersten Zahlenliste ist", min(zahlen_liste1))
print("Der Mittelwert der ersten Zahlenliste ist", mittelwert1)
#zahlen_liste2
print("Die zweite Zahlenliste lautet:", zahlen_liste2)
print("Die größte Zahl der zweite Zahlenliste ist", max(zahlen_liste2))
print("Die kleinste Zahl der zweite Zahlenliste ist", min(zahlen_liste2))
print("Der Mittelwert der zweite Zahlenliste ist", mittelwert2)
#zahlen_liste3
print("Die dritte Zahlenliste lautet:", zahlen_liste3)
print("Die größte Zahl der dritte Zahlenliste ist", max(zahlen_liste3))
print("Die kleinste Zahl der dritte Zahlenliste ist", min(zahlen_liste3))
print("Der Mittelwert der dritte Zahlenliste ist", mittelwert3)
#wörter_liste1
print('Die erste Wörterliste lautet: ', wörter_liste1)
print('Das längste Wort in der ersten Wörterliste ist', max(wörter_liste1, key = len))
#wörter_liste2
print('Die zweite Wörterliste lautet: ', wörter_liste2)
print('Das längste Wort in der zweite Wörterliste ist', max(wörter_liste2, key = len))
#wörter_liste3
print('Die dritten Wörterliste lautet: ', wörter_liste3)
print('Das längste Wort in der dritten Wörterliste ist', max(wörter_liste3, key = len))