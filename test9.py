a="Bonjour j'aime l'USTHB"
mots=a.split()#l’espace est le délimiteur par défaut
print(type(mots))#mots est une liste (classe « list » )
#---------------------------------------------------------------------------#
x="bleu,rouge,vert"
(a,b,c)=x.split(",")#on utilise la virgule comme délimiteur
print(a+" comme le ciel "+b+" comme la tomate "+c+" comme une plante")
t=(a,b,c)
print(type(t))