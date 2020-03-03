gerade = [2]
ungerade = [3]
for i in range(10):
    a = int(input("Geben sie Bitte eine Ganze Zahl ein"))
    if a % 2 == 0:
        gerade.append(a)
    else:
        ungerade.append(a)
gerade.sort()
ungerade.sort()
print(gerade)
print(ungerade)
