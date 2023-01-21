a=set([2,4,6,8,10])
b=set([1,2,3,4,5,6,7,8,9])

print('A =',a)
print('B =',b)
print()

print()

#Primera forma de sacar la diferencia de conjuntos

print('Elementos que estan en A pero no en B =',a-b)
print()
print('Elementos que estan en B pero no en A =',b-a)
print()

#Segunda forma de sacar la diferencia de conjuntos

print(a.difference(b))
print()
print(b.difference(a))
print()