#Shane Williams Hausaufgabe
#Bei der Aufgabe hatte ich hilfe von Florian und Bastian bekommen

zahlen_liste_1 = [5, 9, 4, 6, 11, 2, 33, 74, 90, 101]
mittelwert_1_addieren = (5 + 9 + 4 + 6 + 11 + 2 + 33 + 74 + 90 + 101)
mittelwert_1 = mittelwert_1_addieren / 10

zahlen_liste_2 = [88, 34, 667, 59, 777, 1021, 981]
mittelwert_2_addieren = (88 + 34 + 667 + 59 + 777 + 1021 + 981)
mittelwert_2 = mittelwert_2_addieren / 7

wort_liste_1 = ['Brille', 'Keloggs', 'Schrank', 'Traube', 'Auto']
laengstes_wort_1 = max(wort_liste_1, key = len)

wort_liste_2 = ['Pulli', 'Box', 'Flasche', 'Schlüssel']
laengstes_wort_2 = max(wort_liste_2, key = len)

wort_liste_3 = ['Himmel', 'Fee', 'Tiger']
laengstes_wort_3 = max(wort_liste_3, key = len)

wort_liste_4 = ['Tee', 'Fahrrad', 'Pizza']
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
