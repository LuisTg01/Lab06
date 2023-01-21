a=set([2,4,6,8,10])
b=set([1,2,3,4,5,6,7,8,9])
c=set([2,4,3,10])

print('A =',a)
print('B =',b)
print('C =',c)
print()

print('La intersección es: ')
print(a&b&c)    #Primera forma de interseccion de conjuntos
print()
print(a.intersection(b,c))  #Segunda forma de interseccion de conjuntos
print()
