import sys
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5 import uic

class Dialogo(QDialog):
	def __init__(self):
		QDialog.__init__(self)
		uic.loadUi("listwidget.ui", self)
		self.boton.clicked.connect(self.getItems)
		#Agregar un nuevo item
		#self.lenguajes.addItem("Visual Basic")
		#Eliminar un item
		#self.deleteItem("Python")
		
	def deleteItem(self, label):
		#Array para almacenar cada item objeto
		items = []
		#Recorrer item a item
		for x in range(self.lenguajes.count()):
			item = self.lenguajes.item(x)
			items.append(item)
		#este array almacena el texto de cada item
		labels = [i.text() for i in items]
		#Recorrer item a item el array labels
		for x in range(len(labels)):
			#Si el item existe
			if labels[x] == label:
				#Eliminar
				item = self.lenguajes.indexFromItem(self.lenguajes.item(x))
				self.lenguajes.model().removeRow(item.row())
		
	def getItems(self):
		items = self.lenguajes.selectedItems()
		#Array para guardar los items seleccionados
		selected = []
		for x in range(len(items)):
			selected.append(self.lenguajes.selectedItems()[x].text())
		self.labelLenguajes.setText("Seleccionados: " + "-".join(selected))
			
		
app = QApplication(sys.argv)
dialogo = Dialogo()
dialogo.show()
app.exec_()