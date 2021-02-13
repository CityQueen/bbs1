import random
schondurchsucht = 0
cache_gegenstaendeimraum = ' '
cache_raumbeschreibung = ' '
cache_gegenstaendeimraum = str(cache_gegenstaendeimraum)
cache_raumbeschreibung = str(cache_raumbeschreibung)
anzahlgegner = 0
tuerenimraum = 0
nahrungimraum = []
nahrungliste = ["Berkants Adventskalender", "eine Dönerpizza", "zwei Redbull", "ein Mozzarella Brötchen", "ein Fass Bier", "ein Erdbeermarmeladebrot mit Honig", "Dosenbier", "vankottes booty"]
scheisse = 'ja'
hp = 100
karma = 5
hunger = 100
ausdauer = 100
wahrnehmung = 5
hp = int(hp)
karma = int(karma)
hunger = int(hunger)
ausdauer = int(ausdauer)
gegenstaendeimraum = []
inventar = []
gegenstaendeliste = ["eine Arnold Schwarzenegger Actionfigur", "einen Defibrillator", "einen Spielzeug Panzer", "Stuhl", "einen Taser", "ein Nokia Tastenhandy", "die Heilige Handgranate", "die Bibel", "das Rambomesser", "die Tora", "den Koran", "Stinkende Socken", "ein paar Legosteine", "ein Laserschwert", "Blaues Licht", "Die Rote Armmee", "Eine Juul", "einen Pokéball", ]
welchergegenstand = 0
gegnerimraum = []
beschreibungliste = ["Du sieht einen haufen Regale an der Wand stehen", "Ein karger Raum mit einem Spiegel an der Wand", "Ein monströser Haufen Dinosaurierscheiße biblischen Ausmaßens liegt mitten im Raum", "Du befindest dich im Bernsteinzimmer", "Ein heruntergekommens WOhnzimmer mit Rissen in der Wand", "e"
                                                                                                                                                                                                                                                                                                                  "in riesiges Labor mit kaputten Behältern", "einen Atomsprengkopf durch die Decke hängen", "du merkst das du dich in der Wohnung von Familie Ritter befindest", "das Zimmer ähnelt der Toiletten des Mainzer Hauptbahnhofs", "du stehst in der Tür zu einem riesigen Serverraum"]
nummergegenstand = 0
gegnerliste = ["Atomfliege", "Hässliche Riesenratte", "Monsterkatze", "Godzilla", "Asozial Große Ameise", "Der Hausmeister", "Der Predator", "Ein Alien", "Die Heiligen drei Könige", "Kleinschleim"]
i = 0
anzahllueftungen = 0
def durchsuchen():
        nahrung()
        gegenstaende()


def gegenstaende():
    global wahrnehmung
    anzahlgegenstaende = random.randint(0, wahrnehmung)
    if anzahlgegenstaende <= 0:
        print('Du kannst in diesem Raum keine Gegenstände finden!')
        weitergehen()
    else:
        for i in range (anzahlgegenstaende):
            global gegenstaendeliste
            nummergegenstand = random.randint(0, len(gegenstaendeliste)-1)
            global gegenstaendeimraum
            gegenstaendeimraum.append(gegenstaendeliste[nummergegenstand])
        print('Du findest folgende Gegenstände:',*gegenstaendeimraum, sep='\n')
        antwort = input('Möchtest du einen dieser Gegenstände aufnehmen?')
        if antwort == 'ja' or antwort == 'Ja':
            aufnehmen()
        else:
            print('Scheinbar kein messi, huh, hier gibts keine Gewichtsbegrenzung....')
            neuerraum()


def aufnehmen():
    global inventar
    global gegenstaendeimraum
    global welchergegenstand
    welchergegenstand = input('Welchen Gegenstand möchtest du aufnehmen?(Bitte die Nummer e.g. 1, 2, 3 eingeben)')
    welchergegenstand = int(welchergegenstand)-1
    inventar.append(gegenstaendeimraum[welchergegenstand])
    print("Du hast ", gegenstaendeimraum[welchergegenstand], " aufgenommen und in deinem Rucksack verstaut")
    weitergehen2()




def nahrung():
    global wahrnehmung
    nahrungjanein = random.randint(0, wahrnehmung)
    global nahrungimraum
    global hunger
    if nahrungjanein == 0:
        print("Du kannst in diesem Raum keine Nahrung finden")
    else:
        for i in range (nahrungjanein):
            nahrungimraum.append(nahrungliste[i])
        print("du findest an essbarem: ", *nahrungimraum, sep = '\n')
        print('Du isst alles sofort auf was du findest und fühlst dich gestärkt')
        hunger = hunger+nahrungjanein*10
def sieg():
    print('Du hast gewonnen, Glückwunsch!')

def niederlage():
    print('Du hast verloren, rippedi, dippedi! :(')
    global ausdauer
    ausdauer = ausdauer-10



def lueftung():
    anzahllueftungen = random.randint(0, 2)
    print('Es gibt ' ,anzahllueftungen, ' Lüftungen in diesem Raum')
    global cache_raumbeschreibung
    cache_raumbeschreibung = cache_raumbeschreibung+('Es gibt ' ,anzahllueftungen, ' Lüftungen in diesem Raum')

def gegner():
    gegnerimraum.clear()
    global anzahlgegner
    ende = (karma/10)+5
    ende = int(ende)
    anzahlgegner = random.randint(0, ende)
    for i in range (anzahlgegner):
        gegnerimraum.append(gegnerliste[i])
    print('Es sind folgende Gegner in diesem Raum:','\n',*gegnerimraum, sep = '\n')
def kaempfen():
    antwort = input('Du musst dich verteidigen! Bist du bereit?!')
    global anzahlgegner
    ausgangdeskampfes = random.randint(0,anzahlgegner*10)
    global ausdauer
    global hp
    if ausgangdeskampfes >= ausdauer:
        niederlage()
    elif ausgangdeskampfes >= hp:
        gameover()
    else:
        global karma
        sieg()
        karma = karma + anzahlgegner * 10


def gameover():
    print('well shit, du bist rip!')


def anzahltueren():
    global tuerenimraum
    tuerenimraum = random.randint(1, 3)
    print('Du siehst ',tuerenimraum,' Türen vor dir')
    global cache_raumbeschreibung
    cache_raumbeschreibung = cache_raumbeschreibung+'Du siehst ',tuerenimraum,' Türen vor dir'

def raumbeschreibung():
    global beschreibungliste
    global cache_raumbeschreibung
    laenge = len(beschreibungliste)-1
    nummerbeschreibung = random.randint(0, laenge)
    beschreibung = beschreibungliste[nummerbeschreibung]
    cache_raumbeschreibung = str(cache_raumbeschreibung)
    beschreibung = str(beschreibung)
    print(beschreibung)
    cache_raumbeschreibung = cache_raumbeschreibung + beschreibung
def weitergehen2():
    input('Du hast nur Zeit diesen einen Gegenstand einzusammeln bevor deine Abenteuerlust dich übermannt und du weitergehen musst!')
    neuerraum()

def weitergehen():
    input('In diesem Raum gibt es nichts mehr für dich zu finden. Deine Abenteuerlust übermannt dich und du musst weitergehen!')
    neuerraum()


def start():
    global scheisse
    if scheisse == 'ja':
        print("Herzlich Willkommen in diesem Spiel, dies ist eine Platzhalterbeschreibung der Startsituation")
        antwort = input('Möchtest du die Tür deiner Kapsel öffnen?')
        scheisse = 'nein'
    if antwort == 'ja' or antwort == 'Ja':
        neuerraum()
    else:
        print('Ja gut dann halt nicht, du stirbt oder so, kryoschlaf, bitch')
def neuerraum():
    print("Du betrittst einen neuen Raum")
    global hp
    global ausdauer
    global hunger
    global schondurchsucht
    global karma
    if karma >= 100:
        print('Hinter dieser Tür verbirgt sich das Tageslicht. Herzlichen Glückwunsch, du hast es nach draußen geschafft!')
        quit()
    while hp >= 0 and ausdauer >= 0 and hunger >= 0:
        #aktuellerraum()
        raumbeschreibung()
        gegner()
        anzahltueren()
        lueftung()
        if schondurchsucht == 'ja':
            schondurchsucht = 'nein'
            weitergehen()
        if len(gegnerimraum) >= 1:
           kaempfen()
        antwort = input('Es gibt keine Gegner (mehr) in diesem Raum, möchtest du ihn durchsuchen oder weitergehen?')
        if antwort == 'durchsuchen' or antwort == 'Durchsuchen':
           durchsuchen()
           schondurchsucht = 'ja'
        else:
            neuerraum()

        if hp <= 0:
            print("Du bist gestorben!")
        elif ausdauer <= 0:
            print("Du bist zu erschöpft um weiterzugehen, GAME OVER!")
        elif hunger <= 0:
            print("Du hast nicht mehr genug Kraft um weiterzugehen, GAME OVER!")
        elif karma == 0:
            print("Du hast es raus geschafft wooooo")


start()