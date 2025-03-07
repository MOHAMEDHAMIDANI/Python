d={'976':'Mongolia','52':'Mexico','212':'Morocco','64':'New Zealand','33':'France'}
d_trie = sorted(d.items(), key=lambda x: x[0],reverse=True) #commande « reverse »/expression « lambda »
for a,b in d_trie: #Affichage
	print(a,b)
#Dans ce script, on trie les valeurs via les clés, de Z à A (ordre décroissant/descendant). 
print('\n')
for i in reversed(sorted(d.keys())):#si on supprime le reversed() c'est == reverse=False
	print(i,d.get(i))
print('\n')	
for i in reversed(sorted(d)):#si on supprime le reversed() c'est == reverse=False
	print(i,d.get(i))
print('\n')	
# Si on écrit reverse=False », c’est l’équivalent de : 
for i in sorted(d.keys()):#ou for i in sorted(d)
	print(i,d.get(i)) 
