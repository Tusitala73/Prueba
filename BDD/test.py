from peewee import *
from datetime import date

# Como se instala peewee (http://peewee.readthedocs.io)
# Desde la consola de comandos: pip install peewee
# Nota: Al instalar Peewee, por defecto se instala tambien el SGBD SQLite3, que es el empleado en este tutorial

# Base de Datos
# Se crea un fichero llamado people.db en el mismo directorio de person.py
db = SqliteDatabase('people.db')

# Un clase que se corresponde con una tabla de la Base de Datos hereda de Model
class Person(Model):
    name = CharField()
    birthday = DateField()
    is_relative = BooleanField()

    class Meta:
        database = db  # This model uses the "people.db" database.

# Un clase que se corresponde con una tabla de la Base de Datos hereda de Model
class Pet(Model):
    owner = ForeignKeyField(Person, backref='pets')
    name = CharField()
    animal_type = CharField()

    class Meta:
        database = db  # this model uses the "people.db" database

# He descargado 'Sqlite tools' (fichero sqlite-tools-win32-x86-3170000.zip)
# Contiene el fichero sqlite3.exe, que permite abrir bases de datos (Ej. people.db) con el siguiente comando (desde la linea de comandos):
# sqlite3.exe people.

def create_and_connect():
    """Conectar con la Base de Datos y Crear Tablas según Modelos"""
    db.connect()
    db.create_tables([Person, Pet], safe=True)

def initialize_database():
    """Inicializar Base de Datos"""
    query = Pet.delete()
    query.execute()
    query = Person.delete()
    query.execute()

def create_family_members():
    """Crear Registros en la tabla Person y en la tabla Pet"""
    # Persons
    uncle_tommy = Person.create(name="Tommy", birthday=date(1973, 12, 29), is_relative=True)
    grandma_ana = Person.create(name="Ana", birthday=date(1960, 1, 1), is_relative=True)
    grandma_rosa = Person.create(name="Rosa", birthday=date(1930, 1, 1), is_relative=True)

    # Pets
    tommys_dog = Pet.create(owner=uncle_tommy, name="Fido", animal_type="Dog")
    anas_cat = Pet.create(owner=grandma_ana, name="Pelusa", animal_type="Cat")

    # Modificar (Update) un atributo
    tommys_dog.name = "Firulais"
    tommys_dog.save()

def get_family_members():
    """Obtener todos los registros de personas y mascotas"""
    for person in Person.select():
        print("La persona {} tiene asignada como fecha de nacimiento el dia {}".format(person.name, person.birthday))

    for pet in Pet.select():
      print("la mascota {} pertenece a {}".format(pet.name, pet.owner.name))

#
def get_family_member(name):
    """Obtener un solo registro mediante clausula where"""
    grandma_rosa = Person.select().where(Person.name == name).get()
    print("{} cumple el día {}".format(name, grandma_rosa.birthday))


def delete_pet1(name):
    """Borrar registros con clausula Where"""
    print("Se procede a borrar la mascota {} ...".format(name))
    query = Pet.delete().where(Pet.name == name)
    deleted_entries = query.execute()
    print("{} registros borrados!".format(deleted_entries))


def delete_pet2(name):
    """Borrar registro obteniendo el objeto y eliminando"""
    print("Se procede a borrar la mascota {} ...".format(name))
    pet = Pet.get(Pet.name == name)
    deleted_entry = pet.delete_instance()
    print("{} registros borrados!".format(deleted_entry))

# Esta condición sirve para que todo lo que alla dentro se ejecute solo cuando este programa se ejecuta (Ej. python.exe person.py)
# Si no se incluye esta condición, cuando se importa este fichero en otra clase (Ej. from person.py import *), se ejecutaría tambien
if __name__ == '__main__':
    create_and_connect()
    initialize_database()
    create_family_members()
    get_family_members()
    get_family_member("Tommy")
    get_family_member("Ana")
    get_family_member("Rosa")
    delete_pet1("Pelusa")
    delete_pet1("Firulais")
