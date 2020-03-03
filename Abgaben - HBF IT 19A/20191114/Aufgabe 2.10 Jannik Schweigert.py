Guthaben = float(input('Wie viel geld haben sie noch auf dem konto?'))
Abheben = float(input('Wie viel geld wollen sie abheben?'))
print('Ist ihr bisheriges Zahlungsverhalten einwandfrei?')
ZVer = input('Ja / Nein')

if Abheben < Guthaben:
    print('Sie erfüllen die bedingungen und können somit ihr geld abheben.')
elif Abheben < Guthaben + 300:
    print('Sie erfüllen die bedingungen und können somit ihr geld abheben.')
elif Abheben > Guthaben + 300 and ZVer == 'Ja':
    print('Sie erfüllen die bedingungen und können somit ihr geld abheben.')
else:
    print('ihnen kann kein geld ausgezahlt werden')