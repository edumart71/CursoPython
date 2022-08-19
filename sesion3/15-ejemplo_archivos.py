from io import open
 
texto="Una line con texto\notra line de texto"

#Ruta donde crearemos el fiechero

fichero=open('fichero.txt','w')

#Escribir en el archivo
fichero.write(texto)

cadena2="\nEsto es otra cadena"

fichero.write(cadena2)
#Cerramos el archivo
fichero.close()