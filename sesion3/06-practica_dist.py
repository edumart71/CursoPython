
class coordenadas:
    x=0
    y=0
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def distancia(self,obj):
        xdif=(self.x-obj.x)**2
        ydif=(self.y-obj.y)**2

        return (xdif+ydif)**0.5

def main():
    obj1=coordenadas(-1,-3)
    obj2=coordenadas(1,-6)
    print("La distancia de los puntos es: {}".format(obj1.distancia(obj2)))

if __name__=="__main__":
    main()