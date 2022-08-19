#lista

lista1=[1,2,3,4,5]
lista2=['uno','dos','tres','cuatro']
lista3=[1,2,3,'uno','dos','tres']

lista4=[['a','b','c'],[1,2,3,4]]

print(type(lista3))

print(lista4[0])
print(lista4[1])
print(lista4[1][1])

print(len(lista1))
lista1[len(lista1)-1]=10
print(lista1)

lista1.append(11)
print(lista1)

listaNueva=lista1+lista2
print(listaNueva)

x=[5,1,3,100,2]

y=x
print(y)
x.append(100)
#print(y)
x.sort()
print(x)
lista2.reverse()
print(lista2)

x.remove(100)
print(x)
x.clear()
print(x)