from io import open
 
personas = open('p.txt', 'r', encoding="utf8")
lpersonas = personas.readlines()
personas.close()

listapersona = []
for p in lpersonas:
    campos = p.replace("\n", "").split(";")
    persona = {"id":campos[0], "nombre":campos[1], "apellido":campos[2], "nacimiento":campos[3]}
    listapersona.append(persona)

for per in listapersona:
    print("id{}  {} {} nacicido en {}".format(per["id"], per["nombre"], per["apellido"], per["nacimiento"]))
