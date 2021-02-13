i=0
import random
print("Hallo liebe Spieler. Willkommen zum unsere Ratspiel!")
print("Wir stellen dir 10 Fragen, und du hast 3 Herze wenn du einmal falsch hast dann fängst du von erst frage an, wer alle Fragen richtig beant-wortet ist sehr Fleißig:)")
str(print('Wenn du der spiel anfangen willst, dann drück bitte auf "Lehrzeichen + Enter" '))


while input() != " ":
    if input() == " ":
        continue
while i < 3 :
    i = i+1    
    print("1. Was trinkst du wenn du durst hast?\n")
    print(" a = Wasser")
    print(" b = Piss")
    print(" c = Öl")
    if input() != "a" :
       print("Falsch, du hast ",i, "Herze veloren")
       print("Dein Score ist 0")
    else  :
        print("RICHTIG! Nächste Frage:")
        print("2.Dein Tisch ist kaputt, was brauchst du um den Tisch zu reparieren?\n")
        print(" a = PC")
        print(" b = Messer")
        print(" c = Hammer")
        if input() != "c":
           print("Falsch, du hast ",i, "Herze verloren")
           print("Dein Score ist 1")
        else:
            print("RICHTIG! Nächste Frage:")
            print("3.Wer ist der schlauste Mecnsch in der Welt?\n")
            print(" a = Albert Einstein")
            print(" b = Stephen Hawking")
            print(" c = Jonas Eggert")
            if input() != "a":
                 print("Falsch, du hast ",i, "Herze verloren Ist nicht Jonas dummkopf.")
                 print("Dein Score ist 2")
    
            else:
                print("RICHTIG! Nächste Frage:")
                print("4.Wer hat den ersten Programmiersprache entwickelt?\n")
                print(" a = Yukihiro Matsumoto")
                print(" b = John Warner Backus ")
                print(" c = Guido van Rossum")
                if input() != "b":
                   print("Falsch, du hast ",i, "Herze verloren!")
                   print("Dein Score ist 3")
                else:
                     print("RICHTIG! Nächste Frage:")
                     print("5.Was ist den ersten Programmiersprache in der Welt?\n")
                     print(" a = Fortran")
                     print(" b = JavaScript")
                     print(" c = Python")
                     if input() != "a":  
                         print("Falsch, du hast ",i, "Herze verloren!")
                         print("Dein Score ist 4")
                     else: 
                          print("RICHTIG! Nächste Frage:")
                          print("6.Wann war das erste iPhone auf dem Markt?\n")
                          print(" a = 2006 ")
                          print(" b = 2007 ")
                          print(" c = 2005 ")
                          if input() != "b":
                             print("Falsch, du hast ",i, "Herze verloren!")
                             print("Dein Score ist 5")
                          else:
                              
                              print("RICHTIG! Nächste Fragen:")
                              print("7.Wer war der Erste deutsche Bundeskanzler?\n")
                              print(" a = Konrad Adenauer")
                              print(" b = Ludwig Erhard")
                              print(" c = Kurt Georg Kiesinger")
                              if input() != "a":  
                                print("Falsch, du hast ",i, "Herze verloren!")
                                print("Dein Score ist 6")
                              else: 
                                 print("RICHTIG! Nächste Fragen:")
                                 print("8.Wer hat die erste Fussball WM gewonnen?\n")
                                 print(" a = Jugoslawien")
                                 print(" b = Argentina")
                                 print(" c = Uruguay ")
                                 if input() != "c":
                                    print("Falsch, du hast ",i, "Herze verloren!")
                                    print("Dein Score ist 7")
                                 else:
                                      print("RICHTIG! Nächste Fragen:")
                                      print("9.Wer hat der erste Flugzeug erfunden?\n")
                                      print(" a = Charles Lindbergh")
                                      print(" b = Brüder Wright")
                                      print(" c = Yuri Alekseyevich Gagarin")
                                      if input() != "b":  
                                         print("Falsch, du hast ",i, "Herze verloren!")
                                         print("Dein Score ist 8")
                                      else:
                                          print("RICHTIG! Nächste Fragen:")
                                          print("10.Wer hat den ersten Computer entwickelt?\n")
                                          print(" a = Tim Berners-Lee")
                                          print(" b = Bill Gates")
                                          print(" c = Konrad Zuse")
                                          if input() != "c":  
                                            print("Falsch, du hast ",i, "Herze verloren!")
                                            print("Dein Score ist 9")
                                          else: 
                                               print("RICHTIG! DU HAST ES GESCHAFT!")
                                               print("DU HAST GEWONNEN! Dein Score ist 10!")
                                               print("BIN STOLZ AUF DICH")
                                               break