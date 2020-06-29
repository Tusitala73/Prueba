import sys, re # re es el modulo par la validacion de datos
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox
from PyQt5 import uic

class Dialogo(QDialog):
	def __init__(self):
		QDialog.__init__(self) 
		uic.loadUi("validacion.ui", self) 
		self.nombre.textChanged.connect(self.validar_nombre)  #hacemos que cuando ocurra el evento textChanged
		self.email.textChanged.connect(self.validar_email)    # Le pasmos  un metodo para validar si los 
		self.boton.clicked.connect(self.validar_formulario)   # carcteres son corectos
		
	def validar_nombre(self):
		nombre = self.nombre.text() #asignamos los valores de la casilla a una variable
		validar = re.match('^[a-z\sáéíóúàèìòùäëïöüñ]+$', nombre, re.I) #comrpobamos si la variable nombre  contiene ciertos valores
		if nombre == "": # si nombre esta vacio
			self.nombre.setStyleSheet("border: 1px solid yellow;")
			return False
		elif not validar: #si validar es false
			self.nombre.setStyleSheet("border: 1px solid red;")
			return False
		else:
			self.nombre.setStyleSheet("border: 1px solid green;")
			return True
			
	def validar_email(self):
		email = self.email.text()
		validar = re.match('^[a-zA-Z0-9\._-]+@[a-zA-Z0-9-]{2,}[.][a-zA-Z]{2,4}$', email, re.I)
		if email == "":
			self.email.setStyleSheet("border: 1px solid yellow;")
			return False
		elif not validar:
			self.email.setStyleSheet("border: 1px solid red;")
			return False
		else:
			self.email.setStyleSheet("border: 1px solid green;")
			return True
		
	def validar_formulario(self):
		if self.validar_nombre() and self.validar_email(): #si validar_nombre y validar_emiil son true
			QMessageBox.information(self, "Formulario correcto", "Validación correcta", QMessageBox.Discard)
		else:
			QMessageBox.warning(self, "Formulario incorrecto", "Validación incorrecta", QMessageBox.Discard)
		
		
app = QApplication(sys.argv)
dialogo = Dialogo()
dialogo.show()
app.exec_()