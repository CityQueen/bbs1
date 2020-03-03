# Bankautomat Basti,Leon,Sabira
# Sie haben drei Versuche ihren Code richtig einzugeben um Zugriff auf ihr Geld zu erlangen)
Code = ("1234") 
print("Geben sie ihren Code ein")
versuch = 2
eintritt = False
while versuch >-1 and eintritt == False:
    eingabe = input("Bitte Passwort eingeben: ")
    if eingabe == Code:
        print("Wie viel Geld wollen sie abheben?")
        break
    else:
       print("Falsches Passwort. Sie haben noch ", versuch, " Versuche")
       versuch -=1
       print("Schönen Tag noch")
 
 

 
