def f(a,b,*c):#packing de 3 et 4 sur le dernier argument positionnel qui est un tuple
     print(a,b,c)
     print(type(c))#affiche <class 'tuple'>
f(*[1, 2, 3, 4])#unpacking
