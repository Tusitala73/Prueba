from peewee import *
import datetime

db = SqliteDatabase('Tabla_almacen.db')

class Usuario(Model):
    nombre = CharField(unique=True, max_length=50, index=True)
    contraseña = CharField(max_length=50)
    correo = CharField(max_length=50, null = True)
    activo = BooleanField(default=True)
    fecha_creacion = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db
        db_table = 'usuarios'
    def __str__(self):
        return self.Nombre

class Almacen(Model):
    #Usuario = ForeignKeyField(Usuario, Primary_key=True) #Relacion uno a uno
    user = ForeignKeyField(Usuario, related_name='r_almacen') #Relacion muchos a muchos
    nombre = CharField(unique=True, max_length=50, index=True)
    direccion = TextField()
    activo = BooleanField(default=True)
    fecha_creacion = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db
        db_table = 'Almacenes'
    def __str__(self):
        return self.Nombre

class Producto(Model):
    alma = ForeignKeyField(Almacen, related_name='r_producto')
    nombre = CharField(unique=True, max_length=50, index=True)
    descripcion = TextField()
    precio = DecimalField()
    stock = IntegerField()
    fecha_creacion = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db
        db_table = 'productos'
    def __str__(self):
        return '{nombre} - {precio} €'.format(nombre=self.nombre, precio=self.precio)

def Crear_tablas():
    if Usuario.table_exists():
        Usuario.drop_table()  

    if Almacen.table_exists():
        Almacen.drop_table()      

    if Producto.table_exists():
        Producto.drop_table()  

    Usuario.create_table()
    Almacen.create_table()
    Producto.create_table()

def insertar_usuario():
    Usuario.create(nombre='Pepe', contraseña='1234', correo='pp@gmail.com')
    Usuario.create(nombre='Manolo', contraseña='4321', correo='manolo@gmail.com')

def insertar_almacen():
    Almacen.create(user_id=1, nombre='Cohesa', direccion='Oficina 1')
    Almacen.create(user_id=2, nombre='Rofemo', direccion='Oficina 2')

def insertar_producto():
    Producto.create(alma_id=1, nombre='cebollas', descripcion='rojal', precio='0.5',stock='20')   
    Producto.create(alma_id=1, nombre='pasteles', descripcion='de los buenos', precio='6.5',stock='50') 
    Producto.create(alma_id=1, nombre='pan', descripcion='pan integral', precio='1.5',stock='50')   

    Producto.create(alma_id=2, nombre='pintura', descripcion='azul', precio='3',stock='5')   
    Producto.create(alma_id=2, nombre='tornillos', descripcion='allen', precio='2.5',stock='150')   
    Producto.create(alma_id=2, nombre='tuecas', descripcion='cuadradas', precio='6.5',stock='75')   

def crear_schema():
    Crear_tablas()
    insertar_usuario()
    insertar_almacen()
    insertar_producto()

if __name__ == '__main__':
    #crear_schema()

    query = (
        Producto.select()
        .join(Almacen) 
        .join(Usuario)
        .where(Usuario.id == 1)
        .order_by(Producto.precio.desc())
    )
    for vproductos in query:
        print(vproductos)

# ESTE TIPO DE CONSULTA DA PROBLEMAS DE MEMORIA
'''    
   usev = Usuario.get(Usuario.id == 1)
    for almacenv in usev.r_almacen:
        for Producto in almacenv.r_producto:
            print(Producto)
'''
# El metodo corecto para hacer consultas muchos a muchos
# es usando JOINS

