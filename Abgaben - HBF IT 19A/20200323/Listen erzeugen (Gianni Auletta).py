zahlen_liste_1 = [1, 2, 3, 5, 9, 10, 34, 7, 345, 49]
mittelwert_1_addieren = (1 + 2 + 3 + 5 + 9 + 10 + 34 + 7 + 345 + 49)
mittelwert_1 = mittelwert_1_addieren/10

zahlen_liste_2 = [3, 4, 45, 12, 2, 454, 3432, 4324, 43, 333]
mittelwert_2_addieren = (3 + 4 + 45 + 12 + 2 + 454 + 3432 + 4324 + 43 + 333)
mittel_wert_2 = mittelwert_2_addieren/7

wort_liste_1 = ['Hallo','wie','geht','es','dir']
laengstes_wort_1 = max(wort_liste_1,key = len)

wort_liste_2 = ['Mir','alles','gut','was','du']
laengstes_wort_2 = max(wort_liste_2,key = len)

wort_liste_3 = ['machst','käse','gerade','gleich']
laengstes_wort_3 = max(wort_liste_3,key = len)

wort_liste_4 = ['bin','im','Bus','und','sonst']
laengstes_wort_4 = max(wort_liste_4,key = len)

print('---------------------------------------------------------------------------')

print('Die erste Zahlenliste lautet:',zahlen_liste_1                          )
print('Die größte Zahl der ersten Zahlenliste ist', max(zahlen_liste_1)       )
print('Die kleinste zahl der ersten Zahlenliste ist', min(zahlen_liste_1)     )
print('Der Mittelwert der ersten Zahlenliste ist', mittelwert_1               )
     
print('---------------------------------------------------------------------------')

print('Die zweite Zahlenliste lautet:',zahlen_liste_2                         )
print('Die größte Zahl der zweiten Zahlenliste ist', max(zahlen_liste_2)      )
print('Die kleinste zahl der zweiten Zahlenliste ist', min(zahlen_liste_2)    )
print('Der Mittelwert der zweiten Zahlenliste ist', mittel_wert_2             )

print('---------------------------------------------------------------------------')

print('Die erste Wortliste lautet:',wort_liste_1                              )
print('Das längste Wort in der ersten Wortliste ist',laengstes_wort_1         )

print('---------------------------------------------------------------------------')

print('Die zweite Wortliste lautet:',wort_liste_2                             )
print('Das längste Wort in der zweiten Wortliste ist',laengstes_wort_2        )

print('---------------------------------------------------------------------------')

print('Die dritte Wortliste lautet:',wort_liste_3                             )
print('Das längste Wort in der dritten Wortliste ist',laengstes_wort_3        )

print('---------------------------------------------------------------------------')

print('Die vierte Wortliste lautet:',wort_liste_4                             )
print('Das längste Wort in der vierten Wortliste ist',laengstes_wort_4        )

print('---------------------------------------------------------------------------')