s = float(input( "bitte geben sie eine zahl ein" ))
h = float(input("bitte geben sie noch eine zahl ein"))
a= float(input(" bitte noch eine dritter zahl eingeben"))
r= s*h-a
print(r)

d= float(input("eine zahl eingeben" ))
a= float(input("noch eine zahl eingeben bitte"))
u= float(input("noch eins"))

m= d+a+u
print(m)
b=float(input("bitte eine weitere zahl eingeben"))
g= m*b
print(g)

l= float(input("bitte basis eingeben"))
m= float(input("bitte potenz eingeben"))
k= l^m
print(k)

k= float(input("gib eine zahl sofort"))
u= float(input(" noch eins"))

s=k/u
print(s)


sekunden = int(input('Wieviele Sekunden haben wir noch?'))

stunden = sekunden//3600

sekunden = sekunden - stunden * 3600

minuten = sekunden // 60

sekunden = sekunden - minuten * 60

print(stunden, 'Stunden', minuten, 'Minuten und', sekunden , 'Sekunden')


