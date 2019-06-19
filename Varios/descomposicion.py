import sys
contador = 1

if len(sys.argv) == 2:
    numero = sys.argv[1]
    lnumero = len(numero)

    for numero_de_repeticion in range(lnumero):
        largo = lnumero - numero_de_repeticion
        valor = int(numero[largo-1])
        v = valor * contador
        print("{V:0{lnumero}d}".format(V = v,lnumero = lnumero))
        contador *= 10

else:
    print('la has liado')