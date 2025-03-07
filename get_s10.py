texte=["pomme","pain","pomme","orange","pomme","pain"]
lettres ={}
for c in texte:
	if c in lettres:
		lettres[c] = lettres[c] + 1#ou lettres[c]+=1
		print(lettres[c],"a")#afficher la valeur
		print(lettres)
	else:
		lettres[c] = 1
		print(lettres[c],"b")#afficher la valeur
		print(lettres)
for i in sorted(lettres):
	print(i,lettres.get(i))
