class Vehiculo():
    
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
        
    def __str__(self):
        return "color {}, {} ruedas".format( self.color, self.ruedas )
        
        
class Coche(Vehiculo):
    
    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)  # utilizamos super() sin self en lugar de Vehiculo
        self.velocidad = velocidad
        self.cilindrada = cilindrada
        
    def __str__(self):
        return super().__str__() + ", {} km/h, {} cc".format(self.velocidad, self.cilindrada)

    
# Completa el ejercicio aquí

class Camioneta(Coche):

    def __str__(self):
        return super().__str__()
   


class Bicicleta(Vehiculo):
    
    def __str__(self):
        return super().__str__()



class Motocicleta(Bicicleta):

    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)  # utilizamos super() sin self en lugar de Vehiculo
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return super().__str__() + ", {} km/h, {} cc".format(self.velocidad, self.cilindrada)



coche = Coche("rojo",4,180,1800)
coche = Coche("Azul",4,200,3000)
camioneta = Camioneta("blanco",6,120,2500)
bici = Bicicleta("azul",2)
moto = Motocicleta("negra",2,180,125)


lista = [coche,camioneta,bici,moto]


#def catalogar(a):
#    for v in a:
#        print(type(v).__name__,v)

def catalogar(vehiculos, ruedas=None):
      
    # Primera pasada, mostrar recuento
    if ruedas != None:
        contador = 0
        for v in vehiculos:
            if v.ruedas == ruedas: 
                contador += 1
        print("\nSe han encontrado {} vehículos con {} ruedas:".format(contador, ruedas))
    
    # Segnda pasada, mostrar vehículos
    for v in vehiculos:
        if ruedas == None:
            print(type(v).__name__, v)
        else:
            if v.ruedas == ruedas:
                print(type(v).__name__, v)
                
catalogar(lista,6)




    
