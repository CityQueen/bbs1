var1 = int(input('Bitte geben Sie eine Schulnote ein'))
if (var1 == 1) or (var1 == 2) or (var1 == 3) or (var1 == 4) or (var1 == 5) or (var1 == 6):
    
    if var1 == 1:
        print('Sehr gut')
        
    if var1 == 2:
        print('Gut')
        
    if var1 == 3:
        print('Befriedigend')
        
    if var1 == 4:
        print('Ausreichend')
        
    if var1 == 5:
        print('Mangelhaft')
        
    if var1 == 6:
        print('Ungenügend')
    
else:
    print('Bitte geben Sie nur eine Zahl zwischen 1 und 6 ein')