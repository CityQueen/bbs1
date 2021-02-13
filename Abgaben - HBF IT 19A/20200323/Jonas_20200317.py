list1 = [1,3,4,532,34,6,9,3,34,5,8,22,35,7,3]
list2 = [423,654,45,7,2,112,326,5,8,23,4,7,96,7,32]
list3 = [1,3,43,54,532,43,43,45,45,63,423,446,235,45,623,4]
list4 = ['a','b','c','ichbineinberlinerkrapfen','krapfenisteindoodoowort']
list5 = ['hilfe wieso bin ic hier drin aaaah','was soll das i']
list6 = ['blörns','warum','mussdassein','zy','bdkfjs']

superlist = [list1, list2, list3, list4, list5, list6]
antwort = int(input('Welche der 6 Listen wollen sie analysiert haben?(bitte 1-6 als antwort)'))
if antwort == 1 or antwort == 2 or antwort == 3:
    antwort = antwort-1
    groesstezahl = (superlist[antwort])[0]
    kleinstezahl = (superlist[antwort])[0]
    mittelwert = 0
    a = 0
    b = 0
    summe = 0

    for i in range (len(superlist[antwort])-1):
        if ((superlist[antwort])[a]) <= ((superlist[antwort])[i+1]):
            groesstezahl = (superlist[antwort])[i+1]
            a = i+1
        elif ((superlist[antwort])[b]) >= ((superlist[antwort])[i+1]):
            kleinstezahl = (superlist[antwort])[i+1]
            b = i+1
        summe = summe+(superlist[antwort])[i]
        mittelwert = summe/len(superlist[antwort])
    print (groesstezahl)
    print (kleinstezahl)
    print(mittelwert)
else:
    antwort = antwort-1
    for i in range (len(superlist[antwort])-1):
        a = 0
        groessteswort = (superlist[antwort])[0]
        groessteswort = '0'
        if (len((superlist[antwort])[a])) <= (len((superlist[antwort])[i+1])):
            groessteswort = (superlist[antwort])[i+1]
            a = i+1
    print (groessteswort)