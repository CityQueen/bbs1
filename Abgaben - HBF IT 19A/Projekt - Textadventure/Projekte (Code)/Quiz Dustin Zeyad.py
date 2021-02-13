
punkte = 0
 
print("Dieses Quiz wurde von Zeyad und Dustin erstellt 8====D")

print ("Das hier ist die erste Frage.")
print (" ")
print ("Was ist Mahmud's echter Name?")
print ("1)Mohammed")
print ("2)Moamen")
print ("3)Mahmoud")

print (" ")
antwort = input ("Gebe deine Antwort ein: ")
if antwort == "2":
    punkte = punkte + 1
    print (" ")
    print ("Zu wild! Das war die richtige Antwort!")
    print ("Dein Punktestand ist jetzt auf: ", punkte)
else:
    print (" ")
    print ("Falsch! Die richtige Antwort war Moamen!")
    print ("Dein Punktestand ist jetzt auf: ", punkte)

print (" ")
print ("Das hier ist die zweite Frage.")
print ("Von wem kam der Satz 'Wir sind keine IT-Klasse!'")
print ("1)Artjom")
print ("2)Berkant")
print ("3)Frau Lorenz")

print (" ")
antwort = input ("Gebe deine Antwort ein: ")
if antwort == "3":
    punkte = punkte + 1
    print (" ")
    print ("Zu wild! Das war die richtige Antwort!")
    print ("Dein Punktestand ist jetzt auf", punkte)
else:
    print (" ")
    print ("Falsch! Die richtige Antwort war Frau Lorenz!")
    print ("Dein Punktestand ist jetzt auf: ", punkte)
    
print (" ")
print ("Das hier ist die dritte Frage.")
print ("Wer sagt immer 'im Prinzip'? Also im Prinzip sagt es immer...")
print ("1)Eddy")
print ("2)Dario")
print ("3)Artjom")

print (" ")
antwort = input ("Gebe deine Antwort ein: ")
if antwort == "3":
    punkte = punkte + 1
    print (" ")
    print ("Zu wild! Das war die richtige Antwort!")
    print ("Dein Punktestand ist jetzt auf: ", punkte)
else:
    print (" ")
    print ("Falsch! Die richtige Antwort war Artjom!")
    print ("Dein Punktestand ist jetzt auf: ", punkte)

print (" ")
print("Das hier ist die vierte Frage.")
print ("Minüs und Plüs. Von wem kommt das?")
print ("1)Herr Beicht")
print ("2)Sharmarke")
print ("3)Zeyad")

print (" ")
antwort = input ("Gebe deine Antwort ein: ")
if antwort == "2":
    punkte = punkte + 1
    print (" ")
    print ("Zu wild! Das war die richtige Antwort!")
    print ("Dein Punktestand ist jetzt auf: ", punkte)
else:
    print (" ")
    print ("Falsch! Die richtige Antwort war Sharmarke!")
    print ("Dein Punktestand ist jetzt auf: ", punkte)
    
print (" ")
print ("Das hier ist die fünfte und letzte Frage.")
print ("Rechne aus(1+2*5-4/2)*(9-2*4)")
print ("1)9")
print ("2)12")
print ("3)Wieso machen wir jetzt Mathe du Hund")

print (" ")
antwort = input ("Gebe deine Antwort ein: ")
if antwort == "1":
    punkte = punkte + 1
    print (" ")
    print ("Zu wild! Das war die richtige Antwort!")
    print ("Dein Punktestand ist jetzt auf: ", punkte)
else:
    print (" ")
    print ("Falsch! Die richtige Antwort war 9!")
    print ("Dein Punktestand ist jetzt auf: ", punkte)
print (" ")

print ("Das war unser Quiz!")
quit