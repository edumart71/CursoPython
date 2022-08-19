import os

def pedirNumeros():
    os.system('cls')
    print("Dame valor de a: ")
    a=int(input('a: '))
    print("Dame valor de b: ")
    b=int(input('b: '))

    x=1
    tem=0

    while x <= b:
        print("{0} + ".format(a))
        tem=tem+a
        
        x+=1
    print("a x b = {}".format(tem))

def main():
    pedirNumeros()


if __name__ == "__main__":
    main()