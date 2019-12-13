Cent = int(input('wie viel Cent haben wir?: '))
Euro = Cent//100
rest1 = Cent - Euro*100
Cent50 = rest1//50
rest2 = rest1 - Cent50*50
Cent20 = rest2//20
rest3 = rest2 - Cent20*20
Cent10 = rest3//10
rest4 = rest3 - Cent10*10
Cent5 = rest4//5
rest5 = rest4 - Cent5*5
Cent2 = rest5//2
Cent1 = rest5 - Cent2*2
print(Euro, ':Euro |', Cent50, ':50 Cent |', Cent20, ':20 Cent |', Cent10, ':10 Cent |', Cent5, ':5 Cent |', Cent2,':2 Cent |', Cent1, ':1 ent Stücke.')