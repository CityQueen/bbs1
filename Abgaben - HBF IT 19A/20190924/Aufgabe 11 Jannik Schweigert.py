Geld = float(input('Geld:'))
Zinsen = float(input('Zinsen:'))
Jahre = int(input('wie viele jahre?'))
i = 0
ZinsenP = (Zinsen/100)
a = Geld*ZinsenP
if i == 0:
    while True:
        if i ==(Jahre):
            break
        else:
            i = i+1
            Geld = Geld+a
    print(Geld)
else:
    quit()