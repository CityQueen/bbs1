
import math
 
print("Schaltjahr Rechner, kronstone")
 
jahr=int(input("Geben Sie ein Jahr ein:"))
 
if math.fmod(jahr,400)==0:
    print(jahr, "ist EIN Schaltjahr")
elif math.fmod(jahr,100)==0:
    print(jahr, "ist KEIN Schaltjahr")
elif math.fmod(jahr,4)==0:
    print(jahr, "ist EIN Schaltjahr")
else:
    print(jahr, "ist KEIN Schaltjahr")