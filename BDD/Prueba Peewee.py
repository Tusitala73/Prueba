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


#class añadir():
#    us = Usuario()
#    us.Nombre = 'Jose'      
#    us.Contraseña = '1234'
#    us.Correo = 'jose@gmail.com'
#    us.save()
    


if __name__ == "__main__":
    
    Usuario.create_table

    

       
    