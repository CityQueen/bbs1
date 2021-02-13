Text = ("Willkomen, ein Virus ist ausgebrochen, doch keiner weis wer infiziert ist. Es wird empfholen große Menschen mengen zu vermeiden und auch keinen Körperlichen Kontakt aufzubauen, daher entscheiden sie wem sie die Hand geben, um die Person zu begrüßen. Wähle weise!")
print(Text)

from random import randint
z = 1
z1 = 2
z2 = 3
a = 0
a1 = 0
a2 = 0
a3 = 0
a4 = 0
b = 0
Infiziert = False
Hand = randint(1, 3)

while Infiziert == False:
    a = int(input("Wem gibts du die Hand? /[1: Dem Kind], [2: Dem Mann], [3: Der Frau]/:"))
    if a == Hand:
        Hand = randint(1, 3)
        b = b+1
        print("Save")

        a1 = int(input("Super! weiter gehts, Entscheide. /[1: Der Oma], [2: Der Katze], [3: Dem Baby]/:"))
        Hand = randint(1, 3)
        b = b+1
        print("Save")

        a2 = int(input("Nicht schlecht. /[1: Dem Opa], [2: Dem Kleinkind], [3: Der Nonne]/:"))
        Hand = randint(1, 3)
        b = b+1
        print("Save")

        a3 = int(input("Next round!!! /[1: Dem Hund], [2: Der Familie], [3: Dem Jugendlichen]/:"))
        Hand = randint(1, 3)
        b = b+1
        print("Save")

        a4 = int(input("Das Schaffst du./[1: Dem Touristen], [2: Dem Mann mit dem Hut], [3: Dem dickerem Mann]/:"))
        Hand = randint(1, 3)
        b = b+1
        print("Save")

    else:
        Infiziert = True
        print("Sie sind Infiziert!")
print("Dein Score:",b)



