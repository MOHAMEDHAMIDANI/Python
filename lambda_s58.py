d={'976':'Mongolia','52':'Mexico','212':'Morocco','64':'New Zealand','33':'France'}
d_trie = sorted(d.items(), key=lambda x: x[1],reverse=True) #commande « reverse» / expression ou mot-clé « lambda »
for a,b in d_trie: #Affichage
	print(a,b)
#Dans ce script, on trie les clés via les valeurs, de Z à A (ordre décroissant/descendant). 
