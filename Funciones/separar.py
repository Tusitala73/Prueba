pares = []
impares = []

def lista_n(*args):
    for numero in args:
        if numero%2 == 0:
            pares.append(numero)
        else: 
            impares.append(numero)

 
lista_n(1,2,3,4,5,6,7,8,9)
print("los valoer impares son: ",impares)
print("los va lores pares son: ",pares)

