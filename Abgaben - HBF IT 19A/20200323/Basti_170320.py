# Basti Schien
# Ich hatte bei der Bearbeitung dieser Aufgabe Hilfe von Florian und Shane (Sahne)
# Erzeugen Sie mindestens sechs verschiedene Listen, die nur Zahlen bzw. nur Wörter oder Sätze beinhalten. Entwerfen Sie Quellcode, der die nachfolgenden Aufgaben realisiert:
# a) Für Listen, die Zahlen enthalten, soll der Mittelwert sowie das kleinste und das größte Element ausge- geben werden.
# b) Für Listen, die Wörter bzw. Sätze enthalten, soll das Element mit den meisten Zeichen ausgegeben werden.



zahlen_liste_1 = [3, 8, 2, 9, 5, 7, 121, 67, 188, 88]
mittelwert_1_addieren = (3 + 8 + 2 + 9 + 5 + 7 + 121 + 67 + 188 + 88)
mittelwert_1 = mittelwert_1_addieren / 10

zahlen_liste_2 = [425, 420, 55129, 1234, 4321, 9876, 92155]
mittelwert_2_addieren = (425 + 420 + 55129 + 1234 + 4321 + 9876 + 92155)
mittelwert_2 = mittelwert_2_addieren / 7

wort_liste_1 = ['Hallo', 'Ich', 'Heiße', 'Basti', 'Schien']
laengstes_wort_1 = max(wort_liste_1, key = len)

wort_liste_2 = ['Na', 'Höhr', 'Mal', 'Mensch']
laengstes_wort_2 = max(wort_liste_2, key = len)

wort_liste_3 = ['Hund', 'Katze', 'Mausi']
laengstes_wort_3 = max(wort_liste_3, key = len)

wort_liste_4 = ['Groß', 'Größer', 'Am größten']
laengstes_wort_4 = max(wort_liste_4, key = len)

print('Die erste Zahlenliste lautet: ', zahlen_liste_1)

print('Die größte Zahl ist', max(zahlen_liste_1))

print('Die kleinste Zahl ist', min(zahlen_liste_1))

print('Der Mittelwert ist', mittelwert_1)


print('********************************')


print('Die zweite Zahlenliste lautet: ', zahlen_liste_2)

print('Die größte Zahl der zweiten Zahlenliste ist', max(zahlen_liste_2))

print('Die kleinste Zahl der zweiten Zahlenliste ist', min(zahlen_liste_2))

print('Der Mittelwert der zweiten Zahlenliste ist', mittelwert_2)


print('********************************')


print('Die erste Wortliste lautet: ', wort_liste_1)

print('Das längste Wort in der ersten Wortliste ist', laengstes_wort_1)


print('********************************')


print('Die zweite Wortliste lautet: ', wort_liste_2)

print('Das längste Wort in der zweiten Wortliste ist', laengstes_wort_2)


print('********************************')


print('Die dritte Wortliste lautet: ', wort_liste_3)

print('Das längste Wort in der dritten Wortliste ist', laengstes_wort_3)


print('********************************')


print('Die vierte Wortliste lautet: ', wort_liste_4)

print('Das längste Wort in der vierten Wortliste ist', laengstes_wort_4)
