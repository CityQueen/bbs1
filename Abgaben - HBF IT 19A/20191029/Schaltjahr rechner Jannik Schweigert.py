Jahr = int(input('Geben sie ein Jahr ein:'))
z1 = Jahr % 4
if z1 > 0:
    print(Jahr, 'ist kein Schaltjahr')
elif z1 == 0:
    z2 = Jahr % 400
    if z2 == 0:
        print(Jahr, 'ist ein Schaltjahr')
    elif z2 > 0:
        z3 = Jahr % 100
        if z3 == 0:
            print(Jahr, 'ist kein Schaltjahr')
        elif z3 > 0:
            print(Jahr, 'ist ein Schaltjahr')
        else:
            print('ERROR')
    else:
        print('ERROR')
else:
    print('ERROR')