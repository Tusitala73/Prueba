from peewee import *
import datetime

db = SqliteDatabase('Tabla_peewee.db')

class Usuario(Model):
    Nombre = CharField(unique=True, max_length=50, index=True)
    Contraseña = CharField(max_length=50)
    Correo = CharField(max_length=50, null = True)
    Activo = BooleanField(default=True)
    Fecha_creacion = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db
        db_table = 'usuarios'
    def __str__(self):
        return self.Nombre

    


def agregar_1():
    if not Usuario.table_exists():
        Usuario.create_table()

    user = Usuario()
    user.Nombre = 'jose'      
    user.Contraseña = '1234'
    user.Correo = 'jose@gmail.com'
    user.save()
    
   #1º metodo para añadir datos a la talba 
   #creamos una instancia del objeto 'user' referenciando a la clase 'Usuario'
   #para que poder grabrar los datos usamos el metodo "save"

def agregar_2():
    if not Usuario.table_exists():
        Usuario.create_table()
   
    user = Usuario()
    user.save()
    user = Usuario(Nombre='Paco', Contraseña='1456', Correo='pp@gmail') 

    #2ª aqui hacemos exatamete lo mismo pero le pasamos directamente los valores en el constructor

def agregar_3():
    if not Usuario.table_exists():
        Usuario.create_table()
    
    user = {'Nombre':'Juan', 'Contraseña':'789'} #creamos el dicionario
    user = Usuario(**user) #le pasamos a la clase el diccionario como parametro
    user.save()

#3º ahora le vamos a pasar los valores a peewee atraves de un diccionario

def agregar_4():
    if not Usuario.table_exists():
        Usuario.create_table()

    user = Usuario.create(Nombre = 'Antonio', Contraseña = '4566', Correo = ' antonio@gmail.com')

#4º Usamos un metododo de clase 'Create' para crear nuevos registros

def agregar_5():
    if not Usuario.table_exists():
        Usuario.create_table()


    user = Usuario.insert(Nombre = 'Perico', Contraseña = '4566', Correo = ' antonio@gmail.com')
    user.execute()

#5 ºUsando el metodo de clase 'Insert' necesita parta salvasrse el metodo 'execute'

def buscar_modificar():
    userbuscado = Usuario.get(Usuario.id == 5) #metodo de busqueda
    print(userbuscado)

    userbuscado.Activo = False #metodo para modificar un registro
    userbuscado.save()