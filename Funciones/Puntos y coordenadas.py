import math
class punto():

    def __init__(self,x = 0,y = 0):
        self.x = x
        self.y = y

    def __str__(self):
        return '({},{})'.format(self.x,self.y)

    def cuadrante(self):        
        if self.x > 0 and self.y > 0:
            print("{} pertenece al cuadrante 1".format(self))
        elif self.x < 0 and self.y > 0:
            print("{} pertenece al cuadrante 2".format(self))
        elif self.x < 0 and self.y < 0:
            print("{} pertenece al cuadrante 3".format(self))
        elif self.x > 0 and self.y < 0:
            print("{} pertenece al cuadrante 4".format(self))
        else:
            print("{}se encuentra en el origen".format(self))

    def vector(self,p):
        print ("el vetor entre {} y {} es ({},{})".format(self,p,p.x - self.x,p.y - self.y))
    
    def  distancia(self, p):
        d = math.sqrt((p.x - self.x)**2 + (p.y - self.y)**2)
        print("la distancia entre los puntos {} y {} es {}".format(self, p, d))

class Rectangulo:
    
    def __init__(self, pInicial=punto(), pFinal=punto()):
        self.pInicial = pInicial
        self.pFinal = pFinal
        
    def base(self):
        self.v_base = abs(self.pFinal.x - self.pInicial.x)
        print("La base del rectángulo es {}".format( self.v_base ) )
        
    def altura(self):
        self.v_altura = abs(self.pFinal.y - self.pInicial.y)
        print("La altura del rectángulo es {}".format( self.v_altura ) )
        
    def area(self):
        self.v_base = abs(self.pFinal.x - self.pInicial.x)
        self.v_altura = abs(self.pFinal.y - self.pInicial.y)
        self.v_area = self.v_base * self.v_altura
        print("El área del rectángulo es {}".format( self.v_area ) )    
    
    def dibujar(self):
         for f in range(self.v_altura):
            print("")
            for c in range(self.v_base):
                print(" * ", end='')

A = punto(2,3)
B = punto(5,5)
C = punto(-3,-1)
D = punto(0,0)  

A.cuadrante()
B.cuadrante()
C.cuadrante()
D.cuadrante()

A.vector(B)
B.vector(A)

A.distancia(B)
B.distancia(A)

A.distancia(D)
B.distancia(D)
C.distancia(D)

R = Rectangulo(A, D)
R.base()
R.altura()
R.area()
R.dibujar()