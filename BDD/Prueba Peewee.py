from peewee import *
import datetime

db = SqliteDatabase('Tabla_peewee.db')

class Usuario(Model):
    Nombre = CharField(unique=True, max_length=50, index=True)
    Contraseña = CharField(max_length=50)
    Correo = CharField(max_length=50, null = False)
    Activo = BooleanField(default=True)
    Fecha_creacion = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db
        db_table = 'usuarios'


    


if __name__ == "__main__":
    if not Usuario.table_exists():
        Usuario.create_table()

    us = Usuario()
    us.Nombre = 'jose 2'      
    us.Contraseña = '1234'
    us.Correo = 'jose@gmail.com'
    us.save()
    

       
    