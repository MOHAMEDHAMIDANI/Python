a=()#tuple vide ou avec le constructeur tuple()
print(a)
b=(1,2,3)#tuple contenant trois entiers (packing)
print(b)
(a,b)=(3,5)#affectation multiple (unpacking)
print(a,b)
t=(a,b)#(packing)
# t[0]=44
print(type(t))#la fonction type() retourne le type d'objet
a,b=3,5#affectation multiple (packing implicite (création d'un tuple implicite)+unpacking)
t=(a,b)#(packing)
print(type(t))#tuple
a=3,5#(packing)
print(a)
print(type(a))#tuple
print(isinstance(a,tuple))#La fonction isinstance() permet de savoir
#si un objet est bien d'un type donné
#L'opérateur "del" ne fonctionne pas sur les tuples.

