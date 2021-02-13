zahlen_liste_1 = [3, 62, 9, 18, 45, 23, 67, 56, 19, 110]
mittelwert_1_addieren = (3 + 62 + 9 + 18 + 45 + 23 + 67 + 56 + 19 + 110)
mittelwert_1 = mittelwert_1_addieren / 10

zahlen_liste_2 = [13, 12, 9, 3, 4, 4560, 6782]
mittelwert_2_addieren = (13 + 12 + 9 + 3 + 4 + 4560 + 6782)
mittelwert_2 = mittelwert_2_addieren / 7

wort_liste_1 = ['Handy', 'Korb', 'Kobe', 'Killy', 'Doomsday']
laengstes_wort_1 = max(wort_liste_1, key = len)

wort_liste_2 = ['No Sad', 'No Bad', 'Days', 'In LA']
laengstes_wort_2 = max(wort_liste_2, key = len)

wort_liste_3 = ['Haus', 'Auto', 'C63 AMG']
laengstes_wort_3 = max(wort_liste_3, key = len)

wort_liste_4 = ['Couch', 'Schreibtisch', 'Lieferservice']
laengstes_wort_4 = max(wort_liste_4, key = len)

print('Die erste Liste lautet: ', zahlen_liste_1)
print('Die größte Zahl der ersten Liste ist', max(zahlen_liste_1))
print('Die kleinste Zahl der ersten Liste ist', min(zahlen_liste_1))
print('Der Mittelwert der ersten Liste ist', mittelwert_1)

print('')

print('Die Liste lautet: ', zahlen_liste_2)
print('Die größte Zahl der zweiten Liste ist', max(zahlen_liste_2))
print('Die kleinste Zahl der zweiten Liste ist', min(zahlen_liste_2))
print('Der Mittelwert der zweiten Liste ist', mittelwert_2)

print(' ')

print('Die erste Wortliste lautet: ', wort_liste_1)
print('Das längste Wort in der ersten Wortliste ist', laengstes_wort_1)


print('Die zweite Wortliste lautet: ', wort_liste_2)
print('Das längste Wort in der zweiten Wortliste ist', laengstes_wort_2)

print('')

print('Die dritte Wortliste lautet: ', wort_liste_3)
print('Das längste Wort in der dritten Wortliste ist', laengstes_wort_3)

print('')

print('Die vierte Wortliste lautet: ', wort_liste_4)
print('Das längste Wort in der vierten Wortliste ist', laengstes_wort_4)