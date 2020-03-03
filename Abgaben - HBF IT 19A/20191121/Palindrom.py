text = input("Bitte geben sie ein Wort ein")
textlow = text.lower()
textclean = textlow.replace(" ", "")
if textclean[::-1] == textclean[::]:
    print(text, " ist ein Palindrom")
else:
    print(text," ist kein Palindrom")