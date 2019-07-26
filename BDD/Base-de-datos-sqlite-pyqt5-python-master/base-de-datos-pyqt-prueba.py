# Librerias necesarias
import sys
from PyQt5.QtSql import *
from PyQt5.QtCore import Qt, QModelIndex
from PyQt5.QtWidgets import QWidget, QApplication, QDialog, QGridLayout, QMessageBox, QTableWidget, QTableWidgetItem
from PyQt5 import uic
# Creamos la clase que heredara métodos y componentes de QWidget
class PYQT_BD(QDialog):
    def __init__(self):
        QDialog.__init__(self)        
        uic.loadUi("bdd.ui", self)
        self.btnCargar.clicked.connect(self.cargarDatos) # función al hacer click sobre el boton       
        self.btnInsertar.clicked.connect(self.insertarDatos) # función al hacer click sobre el boton        
        self.btnEliminar.clicked.connect(self.eliminarDatos)
        # Método para agregar datos a la base de datos
    def cargarDatos(self, event):
        index = 0
        query = QSqlQuery() # Intancia del Query
        # Ejecutamos el query "select * from personas"
        # El cual nos devolvera todos los datos d ela tabla "personas"
        query.exec_("select * from personas") 

        # Iteramos los datos recividos
        while query.next():
            ids = query.value(0) # ID
            nombre = query.value(1) # NOMBRE
            apellido = query.value(2) # APELLIDO

            # Ahora organizamos los datos en la tabla creada anteriormente
            self.table.setRowCount(index + 1)
            self.table.setItem(index, 0, QTableWidgetItem(str(ids)))
            self.table.setItem(index, 1, QTableWidgetItem(nombre))
            self.table.setItem(index, 2, QTableWidgetItem(apellido))

            index += 1

            # Método para insertar datos en la base de datos
    def insertarDatos(self, event): 
        # Obtenemos los valores de los campos de texto
        ids = int(self.txtID.text())
        nombre = self.txtName.text()
        apellido = self.txtApellido.text()

        query = QSqlQuery() # Instancia de Query
        # Ejecutamos una sentencia para insertar los datos 
        # De los campos de texto
        query.exec_("insert into personas values({0}, '{1}', '{2}')".format(ids, nombre, apellido))

        # Mpetodo para eliminar datos d ela base de datos
    def eliminarDatos(self, event):
        # select = fila seleccionada en la tabla
        selected = self.table.currentIndex()
        if not selected.isValid() or len(self.table.selectedItems()) < 1:
            return

        ids = self.table.selectedItems()[0] # valor de tabla
        query = QSqlQuery() # instancia de Query
        # Ejecutamos una sentencia. Eliminara toda fila cuyo
        # Valor de id sea igual al seleccionado
        query.exec_("delete from personas where id = " + ids.text())

        self.table.removeRow(selected.row()) # Removemos la fila
        self.table.setCurrentIndex(QModelIndex())

        # Método para crear la base de datos
    def db_connect(self, filename, server): # Recibe dos parametros: nombre de la base de datos, y el tipo.
        db = QSqlDatabase.addDatabase(server) # Creamos la base de datos
        db.setDatabaseName(filename) # Le asignamos un nombre
        if not db.open(): # En caso de que no se abra
            QMessageBox.critical(None, "Error al abrir la base de datos.\n\n"
                    "Click para cancelar y salir.", QMessageBox.Cancel)
            return False
        return True

        # Método para crear la tabla personas
    def db_create(self):
        query = QSqlQuery() # Instancia de Query
        #Ejecutamos la sentencia para crear la tabla personas con 3 columnas
        query.exec_("create table personas(id int primary key, "
                    "firstname varchar(20), lastname varchar(20))")
        # Agregamos algunos datos de prueba
        query.exec_("insert into personas values(101, 'Danny', 'Young')")
        query.exec_("insert into personas values(102, 'Christine', 'Holand')")
        query.exec_("insert into personas values(103, 'Lars', 'Gordon')")
        query.exec_("insert into personas values(104, 'Roberto', 'Robitaille')")
        query.exec_("insert into personas values(105, 'Maria', 'Papadopoulos')")

        # Método para ejecutar la base de datos
    def init(self, filename, server):
        import os # Importamos os
        if not os.path.exists(filename):
            self.db_connect(filename, server) # Llamamos a "db_connect"
            self.db_create() # Llamamis a "db_create"
        else:
            self.db_connect(filename, server)

if __name__ == '__main__':
    app = QApplication(sys.argv) # Creamos una instancia de "QApplication"
    ejm = PYQT_BD() # Instancia de nuestra clase "PYQT_DB"
    # Llamamos al metodo "iinit"
    # La base de datos se llamara 'personas' y sera 'SQLite'
    ejm.init('personas', 'QSQLITE') 
    ejm.show() # Ejecutamos la ventana
    sys.exit(app.exec_()) # Cerramos el proceso

