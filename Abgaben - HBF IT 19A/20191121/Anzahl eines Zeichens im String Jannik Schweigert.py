Text = 'Dies ist das Kapitel ueber die Arbeit mit Zeichenketten'
Liste =[]
Liste.append(Text)
Liste.pop(0)
Liste += Text
print(Liste.count('e'))