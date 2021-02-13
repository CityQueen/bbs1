# Von Leon M. Biskin
# Erzeugen Sie mindestens sechs verschiedene Listen, die nur Zahlen bzw. nur Wörter oder Sätze beinhalten. Entwerfen Sie Quellcode, der die nachfolgenden Aufgaben realisiert:
# a) Für Listen, die Zahlen enthalten, soll der Mittelwert sowie das kleinste und das größte Element ausge- geben werden.
# b) Für Listen, die Wörter bzw. Sätze enthalten, soll das Element mit den meisten Zeichen ausgegeben werden.


zahlen_liste_1 = [1, 7, 3, 9, 4, 8, 12, 67, 120, 89]
mittelwert_1_addieren = (1 + 7 + 3 + 9 + 4+ 8 + 12 + 67 + 120 + 89)
mittelwert_1 = mittelwert_1_addieren / 10

zahlen_liste_2 = [40, 580, 1678, 548, 1946, 4152, 1793, 1623]
mittelwert_2_addieren = (40 + 580 + 1678 + 548 + 1946 + 4152 + 1793 + 1623)
mittelwert_2 = mittelwert_2_addieren / 7

wort_liste_1 = ['Hallo', 'Welt', 'Ich', 'Bin', 'Es']
laengstes_wort_1 = max(wort_liste_1, key = len)

wort_liste_2 = ['Flasche', 'Dechel', 'Corona', 'Bier']
laengstes_wort_2 = max(wort_liste_2, key = len)

wort_liste_3 = ['Vogel', 'Hund', 'Sebastian']
laengstes_wort_3 = max(wort_liste_3, key = len)

wort_liste_4 = ['Taste', 'Wort', 'Nudeln']
laengstes_wort_4 = max(wort_liste_4, key = len)

print('Die erste Zahlenliste lautet: ', zahlen_liste_1)

print('Die größte Zahl der ersten Zahlenliste ist', max(zahlen_liste_1))

print('Die kleinste Zahl der ersten Zahlenliste ist', min(zahlen_liste_1))

print('Der Mittelwert der ersten Zahlenliste ist', mittelwert_1)

print('Die zweite Zahlenliste lautet: ', zahlen_liste_2)

print('Die größte Zahl der zweiten Zahlenliste ist', max(zahlen_liste_2))

print('Die kleinste Zahl der zweiten Zahlenliste ist', min(zahlen_liste_2))

print('Der Mittelwert der zweiten Zahlenliste ist', mittelwert_2)

print('Die erste Wortliste lautet: ', wort_liste_1)

print('Das längste Wort in der ersten Wortliste ist', laengstes_wort_1)

print('Die zweite Wortliste lautet: ', wort_liste_2)

print('Das längste Wort in der zweiten Wortliste ist', laengstes_wort_2)

print('Die dritte Wortliste lautet: ', wort_liste_3)

print('Das längste Wort in der dritten Wortliste ist', laengstes_wort_3)

print('Die vierte Wortliste lautet: ', wort_liste_4)

print('Das längste Wort in der vierten Wortliste ist', laengstes_wort_4)
