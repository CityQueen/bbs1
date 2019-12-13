t1 = int(input("Bitte gebe die Tage ein"))
s1 = int(input("Bitte gebe die Stunden ein"))
m1 = int(input("Bitte gebe die Minuten ein"))
s2 = int(input("Bitte gebe die Sekunden ein"))

e1 = t1 * 86400
e2 = s1 * 3600
e3 = m1 * 60

e4 = e1 + e2 + e3 + s2

print('Die angegebenen Tage,Stunden,Minuten und Sekunden haben',e4,'Sekunden',)