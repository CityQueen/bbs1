var1 = int(input('Bitte geben Sie eine Zahl ein'))
var2 = int(input('Bitte geben Sie eine Zahl ein'))

if var1 == 0:
    print('Das geht leider nicht')
if var2 == 0:
    print('Das geht leider nicht')

var3 = min(var1, var2)
var4 = max(var1, var2)

var5 = var4 / var3

print(var5)