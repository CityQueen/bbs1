n = int(input("Note eingeben:"))
if (n > 6):
    print("Fehlerhafte Eingabe")
elif (n == 6):
    print("Ungenügend")
elif (n == 5):
    print("Mangelhaft")
elif (n == 4):
    print("Ausreichend")
elif (n == 3):
    print("Befriedigend")
elif (n == 2):
    ptint("Gut")
else:
    print("Sehr Gut")

