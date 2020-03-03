a = int(input('Bitte gebe die Länge a an:'))
b = int(input('Bitte gebe die Länge b an:'))



c = max(a,b)
q = min(a,b)

for i in range(3):
    
    r = (q/c)**2
    s = r / (4.0 + r)
    c = c + (2.0 * s*c)
    q = s*q
    
    
print(q)

    
