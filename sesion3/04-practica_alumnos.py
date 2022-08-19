import os

def pedirAlumnos(n):
    os.system('cls')
    lista_alumnos={}
    alumnos=[]
    cal=[]

    for i in range(1,n+1):
        print("Nombre de Alumno{}: ".format(i))
        alumnos.append(input())
    
    print(alumnos)

    for i in range(1,n+1):
        print("Califica a Alumno{}: ".format(i))
        cal.append(float(input()))
    
    print(cal)

    lista_alumnos={alumnos:cal for (alumnos,cal) in zip(alumnos,cal) }

    print(lista_alumnos)

def main():
    os.system('cls')
    print('Captura el Numero de Alumnos')
    n=int(input('Dame n:'))
    pedirAlumnos(n)

if __name__=="__main__":
    main()