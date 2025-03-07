#-------------
(a,*b)=5,6,8#les valeurs 6 et 8 sont empaquetées dans une liste
print(a,b)
#-------------
(*a,b)=5,6,8#les valeurs 5 et 6 sont empaquetées dans une liste
print(a,b)
#-------------
(a,b,*c)=5,6#a prendra la valeur 5, b prendra la valeur 6 et c sera une liste vide car elle n'a pas d'éléments correspondants dans l'affectation
print(a,b,c)