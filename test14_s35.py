tab=[2,6,1]
for x in tab: #ou for x in range(len(tab)):
	print(x) #ou  	print(tab[x])
#-----------------------------------------------------------#
tab=['yellow','black','blue']
for x in range(len(tab)): #ou for x in tab:
	print(tab[x]) #ou         	print(x)
#-----------------------------------------------------------#
tab=[('yellow',3),('black',8),('blue',7)] # liste de 3 tuples 
for x,y in tab:
	print(x,type(y))#sinon print(x,y) pour afficher les entiers
