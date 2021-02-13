# Dario Principato


zahlenliste1 = [ 18,26,29,53,69,2 ]
mittelwert1addieren = (18 + 26 + 29 + 53 + 69 + 2)
mittelwert1 = mittelwert1addieren / 6

zahlenliste2 = [83,87,5,6,99,10,15,18]
mittelwert2addieren = ( 83 + 87 + 5 + 6 + 99 + 10 + 15 + 18)
mittelwert2 = mittelwert2addieren / 8

wortliste1 = ['BBS1', 'Dario', 'Juul', 'Gym', 'Corona']
laengsteswort1 = max(wortliste1, key = len)

wortliste2 = ['WarZone', 'Minecraft', 'Battelfield 4', 'Black Squad']
laengsteswort2 = max(wortliste2, key = len)

wortliste3 = ['BBS3', 'Mainz', 'Deutschland','Rheinland-Pfalz']
laengsteswort3 = max(wortliste3, key = len)

wortliste4 = ['Tyga', 'Offset', 'Juice WRLD','Migos']
laengsteswort4 = max(wortliste4, key = len)

print('Die erste Liste lautet: ', zahlenliste1)
print('Die größte Zahl der ersten Liste ist', max(zahlenliste1))
print('Die kleinste Zahl der ersten Liste ist', min(zahlenliste1))
print('Der Mittelwert der ersten Liste ist', mittelwert1)
print('##########')
print('Die zweite Liste lautet: ', zahlenliste2)
print('Die größte Zahl der zweiten Liste ist', max(zahlenliste2))
print('Die kleinste Zahl der zweiten Liste ist', min(zahlenliste2))
print('Der Mittelwert der zweiten Liste ist', mittelwert2)
print('##########')
print('Die erste Wortliste lautet: ', wortliste1)
print('Das längste Wort in der ersten Liste ist', laengsteswort1)
print('##########')
print('Die zweite Wortliste lautet: ', wortliste2)
print('Das längste Wort in der zweiten Liste ist', laengsteswort2)
print('##########')
print('Die dritte Wortliste lautet: ', wortliste3)
print('Das längste Wort in der dritten Liste ist', laengsteswort3)
print('##########')
print('Die vierte Wortliste lautet: ', wortliste4)
print('Das längste Wort in der vierten Liste ist', laengsteswort4)

