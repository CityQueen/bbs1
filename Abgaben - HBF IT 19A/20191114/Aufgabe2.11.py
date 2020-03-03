n1 = int(input("Geben Sie ein Zahl ein: "))
n2 = int(input("Geben Sie ein Zahl ein: "))
n3 = int(input("Geben Sie ein Zahl ein: "))
n4 = int(input("Geben Sie ein Zahl ein: "))
n5 = int(input("Geben Sie ein Zahl ein: "))
max = 17

if n1 < 0:
    n1 = 0

if n2 > 0:
    z2 = n2 * 1.1
    print("Der Wert von n2 ist jetz gleich:" , z2 , )

if n3 % 2 == 0:
    n3 = n3/2
else:
    n3 = n3*2

if n1 > n2:
    print("Der kleinere Zahl ist:", n2 ,
          " und der großere Zal ist:", n1 ,)
elif n1 < n2:
    print("Der kleinere Zahl ist:", n1)
    print("und die größere Zahl ist:", n2 ,)
    
if n1 == 0:
    n1 = 0
elif n1 > 0:
    n1 = n1-1
elif n1 < 0:
    n1 = n1+1

if n2 == 0:
    n2 = 0
else:
    n2 - 1
    
if n1 > n2 and n1 > n3 and n1 > n4 and n1 > n5:
    max = n1
elif n2 > n1 and n2 > n3 and n2 > n4 and n2 > n5:
        max = n2
elif n3 > n1 and n3 > n2 and n3 > n4 and n3 > n5:
        max = n3
elif n4 > n1 and n4 > n2 and n4 > n3 and n4 > n5:
        max = n4

elif n5 > n1 and n5 > n2 and n5 > n3 and n5 > n4:
        max = n5

