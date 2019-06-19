import sys
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5 import uic

class Dialogo(QDialog):
 def __init__(self):
  QDialog.__init__(self)
  uic.loadUi("combobox.ui", self)
  self.boton.clicked.connect(self.getItem)
  lista = ['Juan', 'Antonio', 'Pedro']
  #Agregar un nuevo item
  self.lenguajes.addItems(lista)
  
  #Eliminar un item
  #self.lenguajes.removeItem(0)
  
 def getItem(self):
  item = self.lenguajes.currentText()
  self.labelLenguajes.setText("Has seleccionado: " + item)
  
app = QApplication(sys.argv)
dialogo = Dialogo()
dialogo.show()
app.exec_()