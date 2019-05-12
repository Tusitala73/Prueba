from Operaciones import * 

a, b, c, d = (10, 5, 0, "Hola")


try:   
    
    print( "{} + {} = {}".format(a, b, suma(a, b) ) )
    

except TypeError:
        print("Debe introducir solo numeros") 
        
try:   
    
    print( "{} - {} = {}".format(b, d, resta(b, d) ) )
   

except TypeError:
        print("Debe introducir solo numeros") 
        
try:   
    
    print( "{} * {} = {}".format(b, b, producto(b, b) ) ) 

except TypeError:
        print("Debe introducir solo numeros") 
        
try:   
    
    print( "{} / {} = {}".format(a, c, division(a, c) ) )

except TypeError:
        print("Debe introducir solo numeros") 
        
except ZeroDivisionError:
    print("no se puede dividir por cero")   