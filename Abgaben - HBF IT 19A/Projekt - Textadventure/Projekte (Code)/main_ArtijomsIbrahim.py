# Autors:Artjom, Ibrahim, David


import time

loop = True
cmd = "NULL"
name = "NULL"
skills = [0, 0, 0]
ending = 0
endings = [0, 0, 0, 0, 0, 0]
ends_achieved = 0
game = True


desc_1 = {
    "1": "\nEin neuer langweiliger Tag in der Schule. Sie erscheinen wieder zu spät zum Unterricht, schlecht ausgeschlafen und unmotiviert. "
         "So haben Sie sich für eine Minute auf dem Tisch gelegt um einen kurzen Schlaf zu haben…",
    "2": "\nAuf einmal wachen Sie auf. Da merken Sie, dass der Klassenraum komplett anders aussieht. "
         "Keiner war da. Der Klassenraum sah so aus, als sie im Mittelalter gelandet sind.",
    "3": "\n„Ist das ein Traum?..“. Diese Gedanken tauchen in ihrem Kopf auf. Sie gehen schnell zum Waschbecken um Ihr Gesicht zu waschen. "
         "Sie merken aber, dass statt normalem Waschbecken da ist irgendein Kugel ist, der komplett aus Wasser entsteht und einfach so in der Luft levitiert. "
         "Sie stecken Ihr Gesicht in den Kugel rein und direkt raus. Das kalte Wasser hat sie frisch gemacht und jetzt sind Sie sicher, dass es kein Traum ist…",
    "4": "\nSie gehen aus dem leeren Klassenraum raus. Das Gebäude ist vom Struktur her genauso gleich, aber seht einfach wie im Mittelalter aus. "
         "Sie entscheiden sich runter zu gehen, weil Sie Geräusche dort hören. So kommen Sie zum Pausenhof. Der Pausenhof war voll, an jeder "
         "Ecke war ein Schüler, aber Sie haben schnell bemerkt, dass alle Schüler anders aussehen. Manche sind wie Elfen, mansche sind wie Goblins. "
         "Sie waren der einzige Mensch da, alle andere hatten irgendeine Rase aus Fantasy Spiele oder Storys.",
    "5": "\nSie glauben immer noch nicht, dass es kein Traum ist, aber plötzlich kommt ein Elf auf Sie zu. Der hat spitze, lange Ohren genau wie in "
         "Filmen oder Spiele, aber sein Schnurrbart hat gar nicht zu ihm gepasst."
}
desc_2 = {
    "1": "\nSie haben sich entschieden noch ein bisschen Pause zu machen. Und das wäre eine gute Idee, aber alles ist schief gelaufen als "
         "Sie ausversehen ein Goblin mit Schulter geschupst haben. Der Goblin hat sofort angefangen zu schreien und sich 'breit' zu machen.",
    "2": "\n... schreit der Goblin und versucht Sie zu schupsen, aber genau in diesem Moment macht Johannes ein magisches Schield vor Ihnen. "
         "Goblin versteht, dass Johannes zu stark ist und rennt weg.",
    "3": "\nDas war das Letzte was er gesagt hat. Danach hat man ihm nicht mehr gesehen.",
    "4": "\nNach dieser Situation haben Sie sich doch entschieden in den Klassenraum zu gehen. Treppen waren voll mit Schüler, die sich geschupst haben und "
         "in diesem Moment haben Sie bereuht, dass Sie nicht früher Hoch gegangen sind. Nach 5 Minuten von dieser Hölle, haben Sie den Klassenraum erreicht."
}
desc_3 = {
    "1": "\nSie und Johannes gehen langsam hoch, bevor es nicht zu voll wird. Als Sie in den Klassenraum gekommen sind, hat Johannes sich zu Ihnen gesetzt.",
    "2": "\nAls die Klasse zum hälfte voll war, weil voll viele Schuelers heute nicht da waren, kamm es die Lehrerin rhein. Es gabs nur eine Problem.",
    "3": "\nDie Lehrerin war eine riesige Wespe. Aber was kann man tun, das ist doch Fantasy Welt. Die Lehrerin hatt sofort Sie bemerkt und hat freundlich geläschelt."
}
desc_4 = {
    "1": "\nNach dem kurzen Geschpräch, die Lehrerin hat weiter den Unterricht gemacht.",
    "2": "\nMan konnte schon verstehen, das es da kein Technik gibts. Natürlich darüber nach zu denken ist keine lösung. "
         "Zeit ging langsam und sogar in dieser Welt war die Schule langweilig."
}
desc_5 = {
    "1": "\nWährend des Unterricht hatten Sie kein bock mehr zu sitzen da. Die perfekte entscheidung Währe es in “Lecker Becker” zu gehen. "
         "Das kommisches war, das Essen dort genau so gleich war. Sie haben ein Döner Pizza gekauft und wollten in ruhe draussen Essen, "
         "aber plötzlich ist ein Orc zu Sie gekommen.",
    "2": "\nSie haben angefangen mit dem Orc zu kampfen, aber sie haben damit nicht gerechnet, das der Orc physicalisch viel starker ist. "
         "Nach dem der mit ihrem Gesicht Dreck von boden sauber gemacht hat, ist der mir dem Döner Pizza weg gegangen. Sie sind demotiviert.",
    "3": "\nDer Orc nimmt eure Pizza weg und schtreichelt ihre Kopf. Als der weg war, sind Sie in Klassenraum gegangen. Hungrig und traurig.",
    "4": "\nDer Orc geht so schnell weg, wie es möglich ist. Sie essen ihre Pizza zu ende und zufrieden gehen zuruck in ihre Klasse.",
    "5": "\nAls Orc das gehört hatt, hatt der sein Mund mit Jacke zugedect und ist schnell weg gerannt. Zum glück gibt es solche dumme Leute.",

    "6": "\nAls sie zurück in Klassenraum kammen, hat keiner etwas gemerkt. Es ist noch einbischen übrig bis zu dem Pause geblieben.",

    "7": "\nDie Doppelstunde ist vorbei und es war Zeit für noch eine Pause. Aber plötzlich kamm es noch zwei andere Personen dazu. Ein hübsches Mädchen, "
         "die auch ein Elf war und…ein Mensch? Wirklig ein andere Mensch genau wie Sie. Johannes war auch dabei.",

    "8": "\nSie haben sich entschieden mit Johannes zu gehen. Komplete Weg lang hat er nichts gesagt. "
         "Sie haben ihm verfolgt und nach paar minute kammen Sie in ein Klassenraum.",
    "9": "\nNach zwanzig Minuten haben Sie geschafft, alles zu erklären. Johannes hat alles schnell verstanden, der war echt schlau.",

    "10": "\nSie sind mit diese Elfin gegangen. Das waren beste 15 Minuten in ihres Leben. Sie haben gelacht, spass gehabt und waren einfach glücklich. "
          "Sie und Elfin, haben letzte Doppelstunde geschwenzt, damit ihr bischen mehr Zeit zusammen hatten. Und jetzt, nach Schule Sie und Elfin standen vor Schule. "
          "Sie haben Johannes gesehen, der sofort zu Sie gegangen ist.",
    "11": "\nJohannes ist Weg gegangen, aber das hat Sie garnicht interresiert. Sie kucken auf die Elfin und sind glücklich, "
          "das sie jetzt mit sie bleiben. Es ist perfecte Zeit uhm ihre gefühle zu zeigen.",

    "12": "\nSie sind mit dem anderen Mensch gegangen. Der hat sich sofort in irgend eine Ecke versteckt. "
          "Sie kucken dem an als ob der probleme mit Kopf hat (hat er doch).",
    "13": "\nSie geben den Handy zu diesem Mensch. Der hohlt aus sein Tasche ein Ladekabel raus.",
    "14": "\nSie und der komische Mensch haben angefangen zu Programmieren und nach 15 minuten Sie waren fertig mit dem Code. "
          "Auf einmall alles hat sich angefangen zu endern und Sie und der Mensch waren in eurem Welt, vor Schule.",
    "15": "\nSo haben Sie sich und diese Mensch gerätet. Keine hat natürlich geglaubt in diese Story, aber mindestens Sie wussten, das Sie was guttes getan haben.",

    "end_j_neutral": "\nSie haben nicht geschaft zu ende zu sagen. Vor ihren Augen war jetzt ihre Welt mit ganz normalle Schule. Alles war wie früher. "
                     "Erst jetzt haben sie realisiert, das es Plan von Johannes war. Alles was passiert ist. Es war schon Abend. Sie sind langsam nach Hause gegangen. "
                     "Wegen Sie ist wahrscheinlich andere Welt ausgestorben und mit diese Gedanken wurden sie ihre kommplete Leben lang bleiben…",
    "end_j_bad": "\nAuf ein mall hohlt Johannes ganz schnell ein Messer raus. Sie schaffen nicht mall zu realisieren, was passiert ist. "
                 "Alles ist auf ein mall dunkel. Sie wachen auf in Klassenraum, wo Sie am ganz anfang eingeschlaffen sind. Aber es ist keiner da. "
                 "Klassenraum ist leer und in Fenstern konnen Sie starken licht sehen. So sieht das Ende aus…",

    "end_e_good": "\nSie umarmen die Elfin und danach küsst ihr sich. So haben Sie eine schöne, neue Leben angefangen. Sie haben diese Elfin geheiratet "
                  "und zwei Kinder mit die gehabt. Und so waren Sie glücklich bis ende des Lebens. Happy End.",
    "end_e_bad": "\nDie Elfin ist ganz schnell weg gerannt zum ihre Freund. Mit gebrochene Herz Sie sind ganz allein in diese Welt geblieben. Ganz…allein…",

    "end_m_good": "\nSo haben Sie sich und diese Mensch gerätet. Keine hat natürlich geglaubt in diese Story, "
                  "aber mindestens Sie wussten, das Sie was Gutes getan haben.",
    "end_m_bad": "\nAuf einmall fängt alles an zu verschwinden, bis es nicht nur der helles Licht bleibt. Sie schauen die Umgebung um und merken, "
                 "dass Sie sich in eine Kammer für Menschen mit psychische Krankheiten befinden. Das was echt nicht der Realität…"
}
dialogs = {
    "j-1": "\nJOHANNES:     Oh, da bist du ja! Ich dachte schon, dass du gestorben bist. Schau mal. "
           "Ich verstehe was du fühlst. Lass mir kurz erklären, was da alles abläuft. Mein Name ist Johannes. "
           "Ich bin der schlauste hier und genau wegen mir bist du da. Ich hab Experimente mit Teleportationsmagie geführt und "
           "wahrscheinlich hab ich dich ausversehen in unsere Welt geholt. Ich kann dich zurück in deine Welt bringen, aber meine Mana ist leer. "
           "Die regeneriert sich zum Ende des Schultags voll, aber bis es passiert, muss du irgendwie da überleben. So… Hast du Fragen?",

    "j-2": "\nJOHANNES:     Dein ernst? Du kommst in irgendeine unbekannte für dich Welt und hast kein Fragen? Du bist echt ein Depp.",
    "j-3": "\nJOHANNES:     Wir tun es so, als ob ich das nicht gehört habe.",
    "j-4": "\nJOHANNES:     Im Prinzip… Schon.",
    "j-5": "\nJOHANNES:     Sei nicht so böse. Wann wirst du noch eine Gelegenheit haben in eine andere Welt zu reisen?",
    "j-6": "\nJOHANNES:     Genauso hab ich mir das vorgestellt. Wenn es dich interessiert, kann ich dir später paar geilen Sachen zeigen. "
           "Wollen wir hochgehen oder willst du noch auf dem Schulhof bleiben?",

    "g-1": "\nGOBLIN:   Pass auf wo gehst du, amk!",
    "g-2": "\nGOBLIN:   Ich hol mein Bruders, wart!",

    "j-7": "\nJOHANNES:     Jetzt wirklig nicht mehr.",

    "l-1": "\nLEHRERIN:     Sind Sie der neue Schüler?",
    "l-2": "\nLEHRERIN:     Wie ist ihr Name?",
    "l-3": "\nLEHRERIN:     Ouh… Das ist ein seltener Name. Erzählen sie etwas über Sie. Was sind ihre stärke?",
    "l-4": "\nLEHRERIN:     Das ist schön. Nicht viele sind gut in Mathe.",
    "l-5": "\nLEHRERIN:     Es sieht leider nicht so aus aber ich glaube Ihnen.",
    "l-6": "\nLEHRERIN:     Eh... Okay...",

    "o-1": "\nORC:          Ey, das war das letzte Döner Pizza bei “Lecker Becker”. Gib sie zu mir oder ich schlag dich.",
    "o-2": "\nORC:          Das waren deine letzte Worte.",
    "o-3": "\nORC:          Schlaue Entscheidung.",
    "o-4": "\nORC:          Sorry, Sorry, chill Bruder.",

    "j-8": "\nJOHANNES:     Schau mall. Egal was diese zwei sagen, höhr auf dem nicht zu und komm mit mir. "
           "Ich brauch kurzes Hilfe und wenn das klappt, du kommst zurück in dein Welt jetzt.",
    "e-1": "\nELFIN: Hey, misch dich nicht ein, du Pedo. Ich will einfach neue Schuler kenn lernen. Also komm mit mir, geh nicht mit Johannes.",
    "m-1": "\nANDERER JUNGE:Du kannst nur mir Vertrauen. Ich bin auch ein Mensch, genau wie du. Die lügen dir alle, komm mit mir, ich erkläre dir Alles.",

    "j-9": "\nJOHANNES:     Es egal. Kuck mall. Du hast gesagt, das du gutt Mathe kannst. Richtig?",
    "j-10": "\nJOHANNES:    Kannst du mir paar sachen erklären? Unsere Mathematic ist einfacher als in eurem Welt. Eigentlich ganze Magie hat etwas mit Mathe zu tun, "
            "deswegen wenn du mir hilfst, ich kann dich in dein Welt zurück bringen.",
    "j-11": "\nJOHANNES:    So... Endlich hab ich es geschafft.",
    "j-12": "\nJOHANNES:    Mit diese Mathe Kenntnise kann ich die ganze Welt zerstören…",
    "j-13": "\nJOHANNES:    Danke dir. Endlich hab ich ein normallen Mensch aus anderem Welt geholt. Und weil du mir so gut geholfen hast, ich tote dich nicht. Chuss.",
    "j-14": "\nJOHANNES:    So…dein Zeit ist gekommen. Sorry noch mall fur das. Warte kurz, ich bringe dich zurück in dein Welt.",
    "j-15": "\nJOHANNES:    Okay... Dann, viel Glück.",

    "j-16": "\nJOHANNES:    Schade... Das heisst, ich hab keinen anderen Wahl...",

    "j-17": "\nJOHANNES:    So…dein Zeit ist gekommen. Sorry noch mall fur das. Warte kurz, ich bringe dich zurück in dein Welt.",

    "e-2": "\nELFIN:        Warte!",
    "e-3": "\nELFIN:        Bitte bleib da! Ich…ich liebe dich!",

    "e-4": "\nELFIN:        Ja? Was ist?",
    "e-5": "\nELFIN:        Oh, da ist mein Boyfriend. Sorry das ich dich unterbreche, ich hab kein Zeit mehr. Tschuss.",

    "m-2": "\nMENSCH:       Junge, wir sind am Arsch. Checks du nicht, wo du gelandet bist?",
    "m-3": "\nMENSCH:       Du denkst wahrscheinlich das es parallel Universum ist, aber alles ist noch schlimmer. Wir sind in ein Computer Spiel!",
    "m-4": "\nMENSCH:       Irgendein Schuler programmiert grade dieses Spiel und macht das sehr wahrscheinlich Falsch. "
           "Wir konnen wegen nur ein Fehler in Code sterben! So will ich meine Lebe nicht endern.",
    "m-5": "\nMENSCH:       Du hast gesagt, das du gut programmieren kannst. Hast du dein Handy? Meine Handy hat ein Goblin geklaut.",
    "m-6": "\nMENSCH:       Ich muss mich mit diesem Welt verbinden.",

    "m-7": "\nMENSCH:       Jetzt wir schreiben Code, das wir aus diesem Spiel raus gehen. Schnell bevor der Ersteller nicht gecheckt hatt.",
    "m-8": "\nMENSCH:       Wir haben geschaft! Ja woll! Ich war in diese Spiel schon 10 Jahre lang, jetzt bin ich endlich Frei!",

    "m-9": "\nMENSCH:       Oder vieleicht hast du Probleme?",
    "m-10": "\nMENSCH:      Du bist krank mit Kopf. Das alles kann nicht wirklig passieren."
}
answers = {
    "j-1": "            1. Nein.",
    "j-2": "            2. Warum hast du so komisches Schnurrbart?",
    "j-3": "            3. Also willst du sagen, dass ich jetzt wegen dir einen unentschuldigten Fehltag kriege?",
    "j-4": "            4. Ist das okay wenn ich mit dir bleibe? Ich kenn da keine sonnst. Logisch.",

    "j-5": "            1. Fick dich",

    "j-6": "            1. Hmm... Da hast du recht.",

    "j-7": "            1. Ja, lass uns hochgehen.",
    "j-8": "            2. Lass uns noch ein bisschen draußen bleiben.",

    "j-9": "            1. Ich dachte du hattest keine Mana mehr.",

    "l-1": "            1. Wenn man logisch denkt, dann Mathe. (+ Skill für Mathe)",
    "l-2": "            2. Ich bin gut überall. (+ Skill für Rede)",
    "l-3": "            3. Programmieren. Ich bin ein Hacker. (+ Skill für Programmieren.)",

    "l-4": "            1. Vergessen Sie",

    "o-1": "            1. Komm hier, ich fick dich!",
    "o-2": "            2. E-eh…okay, okay, here nimm, aber bitte schlag mich nicht…",
    "o-3": "            3. Mein Vater arbeitet als Polizist und mein Bruder ist Weltmeisteir in Kickboxen. Willst du weiter reden? (dafür brauchen Sie Redeskills)",
    "o-4": "            4. Ich hab Corona.",

    "d-1": "            1. Mit Johannes gehen. (dafür brauchen Matheskills)",
    "d-2": "            2. Mit Elfin gehen. (dafür brauchen Redeskills)",
    "d-3": "            3. Mit Mensch gehen. (dafür brauchen Programmieren Skills.)",

    "j-10": "           1. Mussen wir nicht auf dem Schulhof?",
    "j-11": "           2. Eh… Nein. Du kannst so in Theorie ein riesigen Kraft kriegen und mich anlügen.",

    "e-1": "            1. Nein. Ich will da bleiben.",
    "e-2": "            2. Ja, die Zeit ist gekommen",

    "m-1": "            1. Eh… Hast du Paranoja?",
    "m-2": "            2. Scheiß drauf, ich gehe zurück zum Johannes.",

    "m-3": "            1. Ja… Hier.",
    "m-4": "            2. Nein man. Ich gib dir mein Handy nicht. Ich glaub du hast echt Probleme."

}
system = {
    "err_decision": "   Bitte geben Sie eine richtige Antwort ein!",
    "name": "   Geben sie Ihr Name ein: ",
    "skills": "Sie können noch ein Skill auswählen"
}
intro = {
    "intro-0": "\n\n\n\n\n",
    "intro-1": "          POINT G PRODUCTIONS",
    "intro-2": "              presents...",
    "intro-3": "            WORLD OF BBS1"
}


for i in intro.values():
    print(i)
    time.sleep(2)


while game:

    print("\n\n\n\n\n")

    for i in desc_1.values():
        print(i)
        input()

    print(dialogs["j-1"])

    print(answers["j-1"])
    print(answers["j-2"])
    print(answers["j-3"])
    print(answers["j-4"])

    while loop:

        cmd = input("Ihre Antwort: ")

        if cmd == '1':
            print(dialogs["j-2"])

        elif cmd == '2':
            print(dialogs["j-3"])

        elif cmd == '3':
            print(dialogs["j-4"])
            print(answers["j-5"])
            cmd = input("Ihre Antwort: ")
            if cmd == '1':
                print(dialogs["j-5"])
                print(answers["j-6"])
                cmd = input("Ihre Antwort: ")
                if cmd != '1':
                    print(system["err_decision"])
            else:
                print(system["err_decision"])

        elif cmd == '4':
            print(dialogs["j-6"])
            print(answers["j-7"])
            print(answers["j-8"])
            loop = False

        else:
            print(system["err_decision"])

    loop = True

    while loop:

        cmd = input("Ihre Antwort: ")

        if cmd == '1':
            loop = False

        elif cmd == '2':
            input(desc_2["1"])
            input(dialogs["g-1"])
            input(desc_2["2"])
            input(dialogs["g-2"])
            input(desc_2["3"])
            print(answers["j-9"])
            cmd = input("Ihre Antwort: ")
            if cmd == '1':
                print(dialogs["j-7"])
                input(desc_2["4"])
                loop = False
            else:
                print(system["err_decision"])

        else:
            print(system["err_decision"])

    for i in desc_3.values():
        print(i)
        input()

    print(dialogs["l-2"])

    name = input(system["name"])

    print(dialogs["l-3"])

    print(answers["l-1"])
    print(answers["l-2"])
    print(answers["l-3"])

    loop = True

    while loop:

        cmd = input("Ihre Antwort: ")

        if cmd == '1':
            skills[0] = 1
            print(dialogs["l-4"])
            print(system["skills"])
            loop = False

        elif cmd == '2':
            skills[1] = 1
            print(dialogs["l-5"])
            print(system["skills"])
            loop = False

        elif cmd == '3':
            skills[2] = 1
            print(dialogs["l-6"])
            print(answers["l-4"])
            print(system["skills"])
            loop = False

        else:
            print(system["err_decision"])

    loop = True

    while loop:

        if skills[0] == 1:
            print(answers["l-2"])
            print(answers["l-3"])

            cmd = input("Ihre Antwort: ")

            if cmd == '2':
                skills[1] = 1
                print(dialogs["l-5"])
                loop = False
            elif cmd == '3':
                skills[2] = 1
                print(dialogs["l-6"])
                print(answers["l-4"])
                loop = False

        elif skills[1] == 1:
            print(answers["l-1"])
            print(answers["l-3"])

            cmd = input("Ihre Antwort: ")

            if cmd == '1':
                skills[0] = 1
                print(dialogs["l-4"])
                loop = False

            elif cmd == '3':
                skills[2] = 1
                print(dialogs["l-6"])
                print(answers["l-4"])
                loop = False

        elif skills[2] == 1:
            print(answers["l-1"])
            print(answers["l-2"])

            cmd = input("Ihre Antwort: ")

            if cmd == '1':
                skills[0] = 1
                print(dialogs["l-4"])
                loop = False

            elif cmd == '3':
                skills[2] = 1
                print(dialogs["l-6"])
                print(answers["l-4"])
                loop = False

        else:
            print(system["err_decision"])

    loop = True

    for i in desc_4.values():
        print(i)
        input()

    input(desc_5["1"])

    print(dialogs["o-1"])
    print(answers["o-1"])
    print(answers["o-2"])
    print(answers["o-3"])
    print(answers["o-4"])

    loop = True

    while loop:

        cmd = input("Ihre Antwort: ")

        if cmd == '1':
            print(dialogs["o-2"])
            print(desc_5["2"])
            loop = False

        elif cmd == '2':
            print(dialogs["o-3"])
            print(desc_5["3"])
            loop = False

        elif cmd == '3':
            if skills[1] == 1:
                print(dialogs["o-4"])
                print(desc_5["4"])
                loop = False
            else:
                print(dialogs["o-2"])
                print(desc_5["2"])
                loop = False

        elif cmd == '4':
            print(desc_5["5"])
            loop = False

        else:
            print(system["err_decision"])

    loop = True

    input(desc_5["6"])
    input(desc_5["7"])

    input(dialogs["j-8"])
    input(dialogs["e-1"])
    input(dialogs["m-1"])

    print(answers["d-1"])
    print(answers["d-2"])
    print(answers["d-3"])

    while loop:

        cmd = input()

        if cmd == '1' and skills[0] == 1:
            ending = 1
            loop = False

        elif cmd == '2' and skills[1] == 1:
            ending = 2
            loop = False

        elif cmd == '3' and skills[2] == 1:
            ending = 3
            loop = False
        else:
            print("Ihre Skills reichen nicht aus!")

    loop = True

    if ending == 1:
        input(desc_5["8"])
        print(dialogs["j-10"])
        print(answers["j-10"])
        print(answers["j-11"])

        cmd = input()

        if cmd == '1':
            input(desc_5["9"])
            input(dialogs["j-11"])
            input(dialogs["j-12"])
            input(dialogs["j-13"])
            input(dialogs["j-14"])
            input(dialogs["j-15"])
            input(desc_5["end_j_neutral"])
            endings[0] = 1
        elif cmd == '2':
            input(dialogs["j-16"])
            input(desc_5["end_j_bad"])
            endings[1] = 1
        else:
            print(system["err_decision"])

    elif ending == 2:
        input(desc_5["10"])
        input(dialogs["j-17"])
        print(answers["e-1"])
        print(answers["e-2"])

        cmd = input()

        if cmd == '1':
            input(desc_5["11"])
            print(dialogs["e-5"])
            input(desc_5["end_e_bad"])
            endings[2] = 1
        elif cmd == '2':
            input(dialogs["e-2"])
            input(dialogs["e-3"])
            input(desc_5["end_e_good"])
            endings[3] = 1
        else:
            print(system["err_decision"])

    elif ending == 3:
        input(desc_5["12"])
        input(dialogs["m-2"])
        input(dialogs["m-3"])
        input(dialogs["m-4"])
        input(dialogs["m-5"])
        input(dialogs["m-6"])
        print(answers["m-3"])
        print(answers["m-4"])

        cmd = input()

        if cmd == '1':
            input(desc_5["13"])
            input(dialogs["m-7"])
            input(desc_5["14"])
            input(dialogs["m-8"])
            input(desc_5["end_m_good"])
            endings[4] = 1
        elif cmd == '2':
            input(dialogs["m-9"])
            input(dialogs["m-10"])
            input(desc_5["end_m_bad"])
            endings[5] = 1
        else:
            print(system["err_decision"])

    input("\nEndungen freigeschaltet: {} von 6".format(endings.count(1)))
    cmd = input("\nMöchten Sie noch Mal spielen? (j/n)")

    if cmd == 'j' or cmd == 'J':
        game = True
    elif cmd == 'n' or cmd == 'N':
        game = False
        exit(0)
    else:
        print(system["err_decision"])
