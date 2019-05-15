from io import open
class Personas:
    def __init__ (self,n,nombre,apellido,nacimiento):
        self.n = n
        self.nombre = nombre
        self.apellido = apellido
        self.nacimiento = nacimiento
    def __str__(self):
        return "{} {} con fecha de nacimiento{} e ID {} ".format(self.nombre,apellido,nacimiento,n)

personas = open('p.txt', 'r')
lpersonas = personas.readlines()
personas.close()

for p in lpersonas:
    persona = Personas([p])

print(persona)