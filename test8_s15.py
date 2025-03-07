a = [1, 2, 3, 4, 5]
b = [5, 4, 3, 2, 1]
print(a==b)

a = {1, 2, 3, 4, 5}
b = {5, 4, 3, 2, 1}
print(a==b)#l’ordre des éléments est ignoré

a = {1, 2, 3, 4, 5,2,4}#les doublons sont automatiquement éliminés (pas de duplication d’éléments)
b = {2, 3, 4, 5, 1}
print(a==b)#l’ordre des éléments est ignoré
