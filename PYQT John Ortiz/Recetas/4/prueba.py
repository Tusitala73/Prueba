import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic

class Dialogo(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi('D:\Proyectos Python\prueba\Prueba\PYQT John Ortiz\Recetas\Menu Principal.ui', self)
        



app = QApplication(sys.argv)
dialogo = Dialogo()
dialogo.show()
app.exec_()