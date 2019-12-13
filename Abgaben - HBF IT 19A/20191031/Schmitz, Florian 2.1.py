var1 = int(input('Bitte geben Sie eine Zahl ein'))
var2 = int(input('Bitte geben Sie eine Zahl ein'))
var3 = int(input('Bitte geben Sie eine Zahl ein'))
var4 = int(input('Bitte geben Sie eine Zahl ein'))

print(min(var1, var2, var3, var4))

#Man kann es auch anders machen

var1 = int(input('Bitte geben Sie eine Zahl ein'))
var2 = int(input('Bitte geben Sie eine Zahl ein'))
var3 = int(input('Bitte geben Sie eine Zahl ein'))
var4 = int(input('Bitte geben Sie eine Zahl ein'))

if(var1 <= var2 and var1 <= var3 and var1 <= var4):
    print(var1, 'ist die kleinste Zahl')
elif(var2 <= var1 and var2 <= var3 and var2 <= var4):
    print(var2, 'ist die kleinste Zahl')
elif(var3 <= var1 and var3 <= var2 and var3 <= var4):
    print(var3, 'ist die kleinste Zahl')
else:
    print(var4, 'ist die kleinste Zahl')