inp = int(input('Input: '))
sec = inp
m1n = int(sec / 60)
sec = int(sec - m1n * 60)
hou = int(m1n / 60)
m1n = int(m1n - hou * 60)
day = int(hou / 24)
hou = int(hou - day * 24)
print(day,'d', hou,'h', m1n,'min', sec,'sec')