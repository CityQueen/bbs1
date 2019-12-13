print('Dies ist ein Centrechner. Er rechnet deine Cents in Münzen um die du dann z.B. von der Bank dafür bekommen kannst')

cent = int(input("Bitte geben sie an wie viel Cent sie haben"))

euro = cent//100

cent = cent - euro*100

print(str(euro) + ' Euro ' + str(cent) + 'Cent')