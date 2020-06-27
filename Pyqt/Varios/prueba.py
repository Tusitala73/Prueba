class Producto:
    def __init__(self,referencia,nombre,pvp,descripcion):
        self.referencia = referencia
        self.nombre = nombre
        self.pvp = pvp
        self.descripcion = descripcion
        
    def __str__(self):
        return """\
REFERENCIA\t{}
NOMBRE\t\t{}
PVP\t\t{}
DESCRIPCIÓN\t{}""".format(self.referencia,self.nombre,self.pvp,self.descripcion)
    

class Adorno(Producto):
    pass


class Alimento(Producto):
    productor = ""
    distribuidor = ""
    
    def __str__(self):
        return """\
REFERENCIA\t{}
NOMBRE\t\t{}
PVP\t\t{}
DESCRIPCIÓN\t{}
PRODUCTOR\t{}
DISTRIBUIDOR\t{}""".format(self.referencia,self.nombre,self.pvp,self.descripcion,self.productor,self.distribuidor)


class Libro(Producto):
    isbn = ""
    autor = ""
    
    def __str__(self):
        return """\
REFERENCIA\t{}
NOMBRE\t\t{}
PVP\t\t{}
DESCRIPCIÓN\t{}
ISBN\t\t{}
AUTOR\t\t{}""".format(self.referencia,self.nombre,self.pvp,self.descripcion,self.isbn,self.autor)