import os
x=10
def dibujar_tabla_del5():
    
    for i in range(10):
        print("5 * {} = {}".format(i,i*5))


def main():
    y=x+1
    print(y)
    print("Tabla del 5: ")
    dibujar_tabla_del5()

if __name__ == "__main__":
    main()