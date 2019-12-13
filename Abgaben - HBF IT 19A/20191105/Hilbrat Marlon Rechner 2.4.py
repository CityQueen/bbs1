Z1= int(input('Bitte geben sie die erste Zahl ein'))
Z2= int(input('Bitte geben sie die zweite Zahl ein'))
R= int(input('Bitte geben sie die Art der Berechnung ein (1) Addition (2) Subtraktion (3)Multiplikation (4) Division'))
if (R==1)or(R==2)or(R==3)or(R==4):
 if R==1:
     E1=Z1+Z2
     print('Das Ergebnis ist', (E1))
 if R==2:
     E2=Z1-Z2
     print('Das Ergebnis ist', (E2))
 if R==3:
     E3=Z1*Z2
     print('Das Ergebnis ist', (E3))
 if R==4:
     E4=Z1/Z2
     print('Das Ergebnis ist', (E4))
 