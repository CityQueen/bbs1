from collections import namedtuple
import random

#gemacht von Sharmarke und Emmeline

#-Sharmarke-
#Fragen bereitstellen
Question = namedtuple("Question", "frage prompt answer joker antwortAusgabe")

questions = [
            Question("Was bedeutet das aus dem Altgriechischen stammende Wort 'Oktopus'?","1. Achtfuß \n2. Sibenbein\n3. Neunarm\n4. Sechshand ","1","1. Achtfuß\n2. Sibenbein","Achtfuß"),
            Question("Welche Politikerin wurde auch 'Eiserne Lady' genannt?","1. Theresa May\n2. Hillary Clinton\n3. Margaret Thatcher\n4. Rosa Luxemburg ","3","1. Theresa May\n3. Margaret Thatcher","Theresa May"),
            Question("Wie wurde eine der bekanntesten Waffen des ersten Weltkriegs genannt?","1. Runde Roswitha \n2. Dicke Bertha \n3. Starke Susanne\n4. Taffe Trudi ","2","1. Runde Roswitha \n2. Dicke Bertha ","Dicke Bertha"),
            Question("An welchem Fluss liegt Prag?","1. Rhein \n2. Wolga \n3. Loire \n4. Moldau ","4","1. Rhein \n4. Moldau","Moldau"),
            Question("Welcher Planet unseres Sonnensystems ist am weitesten von der Sonne entfernt?","1. Uranus \n2. Neptun \n3. Jupiter \n4. Saturn ","2", "1. Uranus \n2. Neptun ","Neptun"),
            Question("Wie viele Einwohner muss eine Stadt mindestens haben, um als Metropole zu gelten?","1. 100.000 \n2. 500.000 \n3. 1.000.000 \n4. 10.000.000 ","3","3. 1.000.000\n4. 10.000.000 ","1.000.000"),
            Question("Wie heißt die Hauptstadt von Kasachstan?","1. Nursultan \n2. Duschanbe \n3. Taschkent \n4. Minsk ","1","1. Nursultan \n2. Duschanbe ","Nursultan"),
            Question("Wer war zuletzt auf dem 10-DM-Schein abgebildet?","1. Albert Einstein \n2. Carl Friedrich Gauß \n3. Alexander von Humboldt \n4. Konrad Adenauer ","2","2. Carl Friedrich Gauß \n3. Alexander von Humboldt","Carl Friedrich Gauß"),
            Question("Wer sind Architekti, Forschi und Gimpli?","1. Pokémon \n2. Teletubbies \n3. Einwohner von Entenhausen \n4. Schlümpfe ","4","2. Teletubbies\n4. Schlümpfe ","Schlümpfe"),         
            Question("Wie heißt keine Figur im Eiskunstlauf?","1. Lutz \n2. Heinrich \n3. Euler \n4. Axel ","2","2. Heinrich \n3. Euler","Heinrich"),
            Question("Welcher Knochen befindet sich im Fuß?","1. Zentralfußknochen \n2. Interfußknochen \n3. Mittelfußknochen \n4. Innerfußknochen ","3","2. Interfußknochen \n3. Mittelfußknochen","Mittelfußknochen"),
            Question("Wie viele Kugeln gibt es in einem Poolbillardspiel (ohne den weißen Spielball)?","1. 21 \n2. 19 \n3. 13 \n4. 15 ","4","2. 19\n4. 15","15"),
            Question("Rose DeWitt Bukater und Jack Dawson sind die Protagonisten von welchem Filmklassiker?","1. Avatar – Aufbruch nach Pandora \n2. Titanic \n3. Jurassic Park \n4. Inception ","2","2. Titanic \n3. Jurassic Park","Titanic"),
            Question("Wie viele Knochen hat der Körper eines Erwachsenen?","1. 53 Knochen \n2. 164 Knochen \n3. 206 Knochen ","3","2. 164 Knochen \n3. 206 Knochen ","206 Knochen "),
            Question("Wie heißt die Landeshauptstadt von Rheinland-Pfalz?","1. Koblenz \n2. Mainz \n3. Heidelberg \n4. Ludwigshafen ","2","2. Mainz \n3. Heidelberg ","Mainz"),
            Question("Welches der folgenden Tiere hält keinen Winterschlaf?","1. Igel \n2. Eichhörnchen \n3. Murmeltier ","2","2. Eichhörnchen \n3. Murmeltier ","Eichhörnchen"),
            Question("Wie viele Jahre widmete Johann Wolfgang von Goethe seiner Arbeit am 'Faust'?","1. 14 \n2. 64 \n3. 35 ","3","1. 14\n3. 35 ","35"),
            Question("Was bekämpfen Antibiotika?","1. Viren \n2. Bakterien \n3. Akne ","2","1. Viren \n2. Bakterien","Bakterien"),
            Question("Wie oft wurde England bereits Fußball-Weltmeister?","1. 1 Mal \n2. 2 Mal \n3. 3 Mal ","1","1. 1 Mal \n2. 2 Mal ","1 Mal"),
            Question("Wie viele Tasten hat üblicherweise ein Klavier?","1. 66 \n2. 77 \n3. 88 ","3","2. 77 \n3. 88","88"),
            Question("Ein passendes Synonym für 'echauf­fie­ren' lautet...","1. schmunzeln \n2. sich ärgern \n3. jemanden begleiten ","2","1. schmunzeln \n2. sich ärgern ","sich ärgern"),
            Question("Wie viele Planeten gehören zu unserem Sonnensystem?","1. 3 \n2. 8 \n3. 10 ","2","2. 8 \n3. 10 ","8"),
            
]


#Erklärung
def erklärung():
    print("\nVor dir siehst du ein Labyrinth. ")
    print("Um durch dieses Labyrinth zu kommen musst du verschiedene Fragen beantworten um den richtigen Weg zu finden.")
    print("Du startest mit",Punkte,"Punkten und",Joker,"Joker.\nJedes mal wenn du eine Frage richtig beantwortest hast bekommst du 10 Punkte und darft weiter gehen.")
    print("Wenn die Frage falsch beantwortet wurde werden 20 Punkte abgezogen. ")
    print("Das Spiel ist beendet wenn du 10 Fragen richtig beantwortet oder keine Punkte mehr zur verfügung hast.\n")

print("--------------\n\033[1mFage-Labyrinth\033[0m\n--------------")

#-Emmeline-
weiter=1
Highscore=0
anwendungJoker=0
#LaberintSpiel
while(weiter==1):
    Punkte=100
    Joker=2
    Weg=0
    Stelle=0
    fFrage=0
    rFrage=0
    gekaufteJoker=0
    
    random.shuffle(questions)
    
    
    
    erklärung()

#Ablauf    
    while(Punkte>0 and Weg <10):
        print("Vor dir siehst du mehrere Wege. ")
        print("Finde den richtigen mit hilfe der Frage:\n ")       

#Fragen        
        while Punkte>0:
            print("\033[1m",questions[Stelle].frage,"\033[0m")
#Joker oder nicht?            
            if anwendungJoker==0:
                print(questions[Stelle].prompt)
                print("\n0. Joker")
            else:
                print(questions[Stelle].joker)
                print("")
                
            print("?. Info")
            answer = input("\n \033[1mAntwort:")
            print("\033[0m")
            
#Tipp            
            if answer == "0" and Joker > 0 and anwendungJoker!=1 :
                Joker-=1
                anwendungJoker=1
                print("\033[33mJoker eingesetzt\033[0m\n")
                continue
            elif answer == "0" and anwendungJoker==1:
                print("\033[33mDu hast für diese Frage schon einen Joker verwendet!\033[0m\n")
                continue
#Tipp kaufen                       
            elif answer == "0" and Joker == 0 and gekaufteJoker<1 and anwendungJoker!=1:
                print("Du hast keinen Joker mehr")
                print("möchtes du mit 10 Punkten einen kaufen?:")
                print("Du hast noch",Punkte,"Punkte")
                print("1. Ja\n2. Nein")
                Kauf = input ("")                            
                if Kauf == "1" and Punkte > 10 :
                    Punkte-=10
                    gekaufteJoker+=1
                    print("\n\033[33mDu hast einen Joker gekauft\033[0m")
                    print("Punkte übrig:\033[1m",Punkte,"\033[0m\n")
                    anwendungJoker=1
                    continue
                elif Kauf == "1" and Punkte < 20 :
                    print("\nDu hast nicht genug Punkte\n")
                    continue                              
                else:
                    print("\nOkay\n")
                    continue
#Tipp kaufen teuer                           
            elif answer == "0" and Joker == 0 and gekaufteJoker>=1 and anwendungJoker!=1:
                print("Du hast keinen Joker mehr")
                print("möchtes du mit 20 Punkten einen kaufen?:")
                print("Du hast noch",Punkte,"Punkte")
                print("1. Ja\n2. Nein")
                Kauf = input ("")
                if Kauf == "1" and Punkte > 20 :
                    Punkte-=20
                    gekaufteJoker+=1
                    print("\n\033[33mDu hast einen Joker gekauft\033[0m")
                    print("Punkte übrig:\033[1m",Punkte,"\033[0m\n")
                    anwendungJoker=1
                    continue
                elif Kauf == "1" and Punkte < 30:
                    print("\nDu hast nicht genug Punkte\n")
                    continue
                else:
                    print("\nOkay\n")
                    continue
#Info
            elif answer == "?":
                print("\033[1m\033[34mInfo ?\033[0m")
                print("Punkte:",Punkte)
                print("Weg gegangen:",Weg)
                print("Joker übrig:",Joker)
                print("Fragen beantwortet:",rFrage +fFrage)
                print("Davon",fFrage,"Fragen falsch und",rFrage,"Fragen richtig.\n")
                continue
#Antwort r.        
            elif answer == questions[Stelle].answer or answer == questions[Stelle].antwortAusgabe:
                print ("Du hast den \033[32mrichtigen\033[0m Weg gewählt! \033[1m\033[32m✔\033[0m")
                print ("Damit erählst du 10 Punkte und bist ein mal weitergerückt.")
                Punkte +=10
                Weg+=1
                rFrage+=1
                anwendungJoker=0
                break
#Antwort f.        
            else:
                print ("Du hast den \033[31mfalschen\033[0m Weg gewählt! \033[1m\033[31m✘\033[0m")
                print ("Die richtige Antwort ist: \033[1m \033[31m",questions[Stelle].antwortAusgabe," \033[0m")
                print ("Damit verlierst du 20 Punkte und bist nicht weitergerückt.")
                Punkte-=20
                fFrage+=1
                anwendungJoker=0
                break
#Frage weiter
        if Stelle<len(questions)-1:
            Stelle+=1
        else:
            random.shuffle(questions)
            Stelle=0
            
            
#Auswertung            
    if Punkte==0:
        print("\n\033[31m\033[1mDu hast keine Punkte und kannst nicht mehr weitergehen\033[0m")
        print("Punkte:",Punkte)
        print("Weg gegangen:",Weg)
        print("Joker übrig:",Joker)
        print("Fragen beantwortet:",rFrage +fFrage)
        print("Davon",fFrage,"Fragen falsch und",rFrage,"Fragen richtig.")
    else:
        print("\n\033[1m\033[32mHerzlichen Glückwunsch\033[0m")
        print("Du hast es aus dem Labyrinth geschaft!")
        print("Punkte:",Punkte)
        print("Weg gegangen:",Weg)
        print("Joker übrig:",Joker)
        print("Fragen beantwortet:",rFrage +fFrage)
        print("Davon",fFrage,"Fragen falsch und",rFrage,"Fragen richtig.")
        
#Highscore        
        if Punkte>Highscore:
            Highscore=Punkte
            print("\nSuper du hast \033[1meinen neuen\033[0m Highscor aufgestellt")
            print("Highscor:\033[1m",Highscore,"\033[0m")
        else:
            print("\nSchade du hast \033[1mkeinen\033[0m neuen Highscor aufgestellt")
            print("Highscor:\033[1m",Highscore,"\033[0m")
            
#Weiter?            
    weiter=int(input("\nMöchtest du noch mal spielen?\n1. Ja\n2. Nein\n"))
    print("\n------------------------------------------------------------------------")