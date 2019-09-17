km = int(input("Wie lang is die Strecke"))
vm = int(input("Zu Fuß(1),Fahrrad(2)oder mit Auto(3)")) 
if (vm==1) or (vm== 2)or (vm==3):
    if vm== 1:
        stunden = km / 5
        print("Es dauert",km/5,"Stunden.")
    elif vm== 2:
            stunden = km / 15
            print("Es dauert",km/15,"Stunden")
    elif vm== 3:
        KmH = int(input("Wie schnell fahren Sie?"))
        stunden = km / KmH
        print("Es dauert",km/KmH,"Stunden")
        
else:
    print("Bitte nur 1,2 oder 3 Eingeben!")
    

