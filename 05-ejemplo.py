import os

def funcion1():
    os.system('cls')
    print("Dame dos Numeros:")
    print('')
    num1=input('Numero1: ')

    num2=input('Numero2: ')

    res = int(num1) + int(num2)

    print('las suma de {} + {} = {}'.format(num1,num2,res))

def funcion2():
    print('ejecuta la funcion 2')

def run():
    os.system('cls')
    print(' Metodo principal: ')
    print('1.funcion1')
    print('')
    print('2.funcon2')
    op=int(input('Dame la opcion:'))

    if op == 1:
        funcion1()
    if op == 2:
        funcion2()
    
if __name__ == "__main__":
    run()
