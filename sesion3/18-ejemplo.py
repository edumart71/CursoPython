from io import open

fichero = open('fichero.txt','a')
fichero.write('\nOtra linea mas abajo de todo')
fichero.close()