from math import pow, sin

#for in

# for (int i=0; i<=6; ++i)
word='Python'

#for c in word :
 #   print(c)

x=range(10)
print(type(x))
print(x)

print(list(range(1,10)))

#for n in range(1,11):
 #   print("4 x {0} = {1}".format(n,(4*n)))


lista1=['Pepe','Mario','Ana','Juan']

for i in range(len(lista1)):
    print(i,lista1[i])

    

lista2="Python"
print(len(lista1))
print(len(lista2))



    a=5
    b=3

    print(pow(a,2))
    print("seno: {0:.3f}".format(sin(1)))