from io import open

fichero = open('fichero.txt','r')

texto=fichero.read(10)

print(texto)
#-----------------------------
print("segunda lectura")
fichero.seek(0)
texto=fichero.read(20)

print(texto)

fichero.close()