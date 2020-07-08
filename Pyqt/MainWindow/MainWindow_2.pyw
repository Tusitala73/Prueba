import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic

#Clase heredada de QMainWindow (Constructor de ventanas)
class MainWindow(QMainWindow):
    #Método constructor de la clase
    def __init__(self, *args):
        #Iniciar el objeto QMainWindow con Super
        super().__init__(*args)
        #Cargar la configuración del archivo .ui en el objeto
        uic.loadUi('MainWindow.ui', self)
        self.setWindowTitle("Hola como estan ?")


#Instancia para iniciar una aplicación       
app = QApplication(sys.argv)
#Crear un objeto de la clase
widget = MainWindow()
#Mostra la ventana
widget.show()
#Ejecutar la aplicación
sys.exit(app.exec_())