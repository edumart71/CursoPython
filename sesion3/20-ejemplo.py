
#nombre de la clase 

class prueba:
    #declaracion de propiedades de clase 
    num1=0
    num2=0
    res=0
   #contructir de la clase metodo especial
    '''def __init__(self,a,b):
        self.num1=a
        self.num2=b'''
    
    def sumar(self):
        self.res=self.num1+self.num2
        #print("La suma es: {}".format(self.res))
        return self.res
    
    def restar(self):
        self.res=self.num1-self.num2
        print("La resta es: {}".format(self.res))

def main():
    obj1=prueba()
    obj2=prueba()

    print("La suma de obj1 es: {}".format(obj1.sumar()))
    print("La resta de obj2 es:")
    obj2.restar()

if __name__=="__main__":
    main()

    