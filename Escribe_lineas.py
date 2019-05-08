import sys
if len(sys.argv) == 3:
    texto = sys.argv[1]
    repeticiones = int(sys.argv[2])
    for r in range(repeticiones):
        print(texto)
else:
    print('Error, introduce los argumentos corectos')
    print('Ejemplo: escribir_lineas.py "texto" 5')
    