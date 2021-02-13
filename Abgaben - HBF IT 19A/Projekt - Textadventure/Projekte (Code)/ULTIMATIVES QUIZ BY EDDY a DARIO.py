
punktzahl = 0
 
print("Willkommen bei dem ULTIMATIVEN Quiz von und über Eddy und Dario")

print (" Tipp: Wir empfehlen das Ausgabe Fenster etwas zu vergrößern damit man alles erkennen kann")
print ("Nun zu der Ersten Frage.")
print (" ")
print ("Woher kennen sich Eddy und Dario?")
print ("1)von der BBS ")
print ("2)Von der Grundschule Nierstein")
print ("3)von der IGS Oppenheim ")

antwort = input ("Woher wohl?: ")
if antwort == "3":
    punktzahl = punktzahl + 1
    print (" ")
    print ("Gut gemacht! Das war aber nicht die schwerste Frage ;)")
    print ("Deine Punktzahl ist : ", punktzahl)
else:
    print (" ")
    print ("Falsch! Es war die IGS. Das hätte man doch wissen müssen! :( ")
    print ("Dein Punktestand ist jetzt immernoch null :( ")

print ("Frage nummer 2:")
print ("Was haben Eddy und Dario früher über sich gegenseitig gedacht?'")
print ("1)Dario mochte Eddy aber er ihn aber nicht")
print ("2)Sie hatten keinen Kontakt")
print ("3)Sie dachten beide das jeweils der andere voll der idiot ist")

print (" ")
antwort = input ("Na was wird es wohl sein?: ")
if antwort == "3":
    punktzahl = punktzahl + 1
    print (" ")
    print ("Nicht schlecht!")
    print ("Dein Punktestand ist jetzt:", punktzahl)
else:
    print (" ")
    print ("Falsch! Sie haben sich gehasst aber sowas von!")
    print ("Dein Punktestand ist jetzt: ", punktzahl )
    

print ("Dritte Frage.")
print ("Wer von Eddy und Dario wohnt zum Teil im Fitness")
print ("1)Dario weil er immer da ist")
print ("2)Eddy")
print ("3)Keiner von beiden")

antwort = input ("Wir wissen alle wer es ist ;): ")
if antwort == "1":
    punktzahl = punktzahl + 1
    print (" ")
    print ("Das war nicht schwer, aber trotzdem gut gemacht  ")
    print ("Dein Punktestand ist jetzt: ", punktzahl)
else:
    print (" ")
    print ("Falsch! Das weiß man doch")
    print ("Dein Punktestand ist jetzt: ", punktzahl)

print("Soo jetzt zur 4. Frage")
print ("Was macht Eddy jeden Tag?")
print ("1)Lernen weil das wichtig ist")
print ("2)Zocken")
print ("3)Die Juul hitten")

print (" ")
antwort = input ("Gebe deine Antwort ein: ")
if antwort == "3":
    punktzahl = punktzahl + 1
    print (" ")
    print ("Richtig! war aber auch leicht ;) ")
    print ("Dein Punktestand ist jetzt: ", punktzahl)
else:
    print (" ")
    print ("Falsch! Die Juul wäre es gewesen")
    print ("Dein Punktestand ist jetzt auf: ", punktzahl)
    
print ("Es ist zeit für die 5 und schwerste Frage")
print ("Wo macht Dario Motorrad Fahrstunden?")
print ("1)In einer normalen Fahrschule")
print ("2)Bei Fahrschule Eddy")
print ("3)Garnicht weil er garnicht darf")

print (" ")
antwort = input ("Gebe deine Antwort ein: ")
if antwort == "2":
    punktzahl = punktzahl + 1
    print (" ")
    print ("Anfragen an Eddys Fahrschule nur auf instagram: @eddy47eddy")
    print ("Dein Punktestand ist jetzt: ", punktzahl, "nicht schlecht!")
else:
    print (" ")
    print ("Es wäre Eddys Fahrschule gewesen! Die beste überhaupt")
    print ("Dein Punktestand ist jetzt: ", punktzahl)
print (" ")

print ("Wollt ihr noch ein Paar Zusatz Fragen auf Level expert? ja oder nein?")

antwort = input (" ")

if antwort =="ja":
    print ("Super! dann mach dich gefasst! Achtung jetzt gibt es doppelte Punkte für die Richtige Antwort und -2 Punkte für eine Falsche Antwort!")

else:
    print ("schade :(")
    print ("Dein entgültiger Punktestand war", punktzahl)
    exit()
    
print ("Frage numero 6")
print ("Wie oft steppt eddy auf die toilette?")
print ("1)Oft")
print ("2)Sehr oft")
print ("3)Sehr sehr oft")

antwort = input ("Gebe deine Antwort ein: ")

if antwort == "3":
    print ("ja richtig :D ")
    punktzahl = punktzahl +2
    print (" deine Puktzahl ist" , punktzahl)
    
else:
    print ("Falsch! Das gibt minus 2 Punkte")
    punktzahl = punktzahl -2
    print ("Dein Punktestand ist jetzt auf: ", punktzahl)
    
print ("Frage 7, die vorletztze Frage! Achtung schwer!")
print ("Wie hört es sich an wenn Dario redet")
print ("1)Als würde er halb schlafen")
print ("2)Normal")
print ("3)Als würde er sich die Nase zuhalten")

antwort = input ("Wir wissen es insgeheim alle: ")

if antwort == "2":
    print ("Nicht schlecht!:) ")
    punktzahl = punktzahl +2
    print (" deine Puktzahl ist" , punktzahl)
    
else:
    print ("Falsch! Er hat immer die Nase zu xD")
    punktzahl = punktzahl -2
    print ("Dein Punktestand ist jetzt: ", punktzahl)
    

print ("Jetzt die SCHWERSTE Frage")
print ("Welche Note bekommt Eddy und Dario auf diesen Vortrag")
print ("1)Nichts weil sie nicht abgeben")
print ("2)Eine 6")
print ("3)Eine 5")
print ("4)Eine 4")
print ("5)Eine 3")
print ("6)Eine 2")
print ("7)HOFFENTLICH EINE 1 WEIL DAS WAR DAS BESTE QUIZ WAS ES GIBT")

antwort = input ("Gebe deine Antwort ein: ")

if antwort == "7":
    print ("Danke du bist ein Gönner! ")
    punktzahl = punktzahl +3
    print (" deine Puktzahl ist" , punktzahl)
    
else:
    print ("Nichtsgönner ")
    punktzahl = punktzahl -1000
    print ("Dein Punktestand ist jetzt: ", punktzahl , "Das wars wohl mit der hohen punktzahl :(")

print (" Das war das ULTIMATIVE Quiz über Eddy und Dario")

if (punktzahl > 5):
    print (" du kennst Eddy und Dario nicht wirklich gut, du kannst dich aber gerne mit den beiden anfreunden sind tolle typen")
    
elif (punktzahl < 5):
    print (" Gute Leistung du kennst die beiden echt gut!")

    
exit()
