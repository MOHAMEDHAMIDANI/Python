texte=["pomme","pain","pomme","orange","pomme","pain"]
lettres ={}
for c in texte:
	if c not in lettres:
		lettres[c] = 0
		print(lettres,"a")
	lettres[c] +=1 
	print(lettres,"b")
for i in sorted(lettres):
	print(i,lettres.get(i))
