from io import open 

fichero=open('fichero.txt','r')

#texto=fichero.read()
#texto1=fichero.readline()
texto2=fichero.readlines()

fichero.close()

print(type(texto2))
print(texto2)