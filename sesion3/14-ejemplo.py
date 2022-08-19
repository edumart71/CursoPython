
x=0

lista=[]


colores={'amarillo':'yellow','azul':'blue','rojo':'red'}

print(colores)

print(colores['amarillo'])

#agregue
colores['verde']='green'
print(colores)

#modifique
colores['amarillo']='white'
print(colores)

#borrar
del(colores['amarillo'])
print(colores)

numeros={1:'uno',2:'dos',3:'tres'}

print("Dic de numeros",numeros[2])

edades={'Pepe':22,'Juan':40,'Mario':27}

print(edades)
edades['Pepe']+=1
print(edades)

print(edades['Juan'] + edades['Mario'])

for edad in edades:
    print(edad)

for clave in edades:
    print(clave,edades[clave])

alumnos=[]

grupo1={'Nombre':'Pedro','Edad':23,'Materia':'Ingles'}
grupo2={'Nombre':'Dario','Edad':20,'Materia':'Ingles'}
grupo3={'Nombre':'Laura','Edad':29,'Materia':'Matematicas'}

alumnos.append(grupo1)
alumnos.append(grupo2)
alumnos.append(grupo3)

print(type(alumnos))
print(alumnos)