from io import open 


with open('fichero.txt','r') as fichero:
    for linea in fichero:
        print(linea)

#texto=fichero.readlines()

fichero.close()