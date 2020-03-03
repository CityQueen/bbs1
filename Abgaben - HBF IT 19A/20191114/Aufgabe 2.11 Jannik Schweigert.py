n1 = int (input("Geben Sie eine Zahl vür n1 ein:"))
n2 = int (input("Geben Sie eine Zahl vür n2 ein:"))
n3 = int (input("Geben Sie eine Zahl vür n3 ein:"))
n4 = int (input("Geben Sie eine Zahl vür n4 ein:"))
n5 = int (input("Geben Sie eine Zahl vür n5 ein:"))
max = 17;
# 1)
if n1 < 0:
    n1 = 0
# 2)
if n2 > 0:
    z2 = (n2 / 100)*10
    n2 = n2 + z2
    print('Der wert von n2 ist jetzt gleich', n2)
# 3)
if n3 % 2 == 0:
    n3_1 = n3 / 2
else:
    n3_1 = n3 * 2
# 4)
z3 = n3 // 2
rest = n3 - z3 * 2
if rest == 0:
    n3_2 = n3 / 2
else:
    n3_2 = n3 / 2
# 5)
z1 = min(n1,n2)
z2 = max(n1,n2)
print(z1, z2)
# 6)
if n1 == 0:
elif n1 > 0:
    n1 = n1 - 1
elif n1 < 0:
    n1 = n1 + 1
# 7)
if n2 == 0:
else:
    n2 = n2 - 1
# 8)
Max = max(n1,n2,n3)
# 9)
Max = max(n1,n2,n3,n4,n5)