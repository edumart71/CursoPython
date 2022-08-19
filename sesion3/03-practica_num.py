import os

def pedirNumeros(a):
    os.system('cls')
    numeros=[]
    for i in range(1,a+1):
        print("numero{}".format(i))
        numeros.append(int(input()))

    return numeros

def clasifica(lst):
    par=[]
    imp=[]

    for i in lst:
        if i % 2:
            imp.append(i)
        else:
            par.append(i)
    
    print('Los numeros impares son :')
    print(imp)
    print('Los numeros pares son: ')
    print(par)

def main():
    os.system('cls')
    print('Captura de Numeros')
    n= int(input('Dame cuantos Numeros: '))
    tem=pedirNumeros(n)
    clasifica(tem)

if __name__=="__main__":
    main()