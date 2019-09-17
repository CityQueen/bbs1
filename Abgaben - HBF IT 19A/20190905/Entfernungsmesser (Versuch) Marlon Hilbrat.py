km = input ("Wie lange ist die Strecke in km?")
vm = input ("Zu Fuß (1) oder mit Fahrrad (2)?)
#vm = Verkehrsmittel
if (vm==1)or(vm==2)
# nur ausführen, wenn 1 oder 2 gewählt wurde
 if vm==1:
     stunden= km / 5
     msgDlg("Es dauert",stunden,"Stunden")
     elif vm==2:
         stunden=km/15
         msgDlg("Es dauert",stunden,"Stunden")
     