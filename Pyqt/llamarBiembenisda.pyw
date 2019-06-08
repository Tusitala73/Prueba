from mibienbenida import *#Ui_Dialog  # importing our generated file
 
import sys
 
class mywindow(QtWidgets.QDialog): 
    def __init__(self, parent=None):    
        super().__init__(parent)    
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.ButtonPulsar, QtCore.SIGNAL('clicked()'), self.mostrarmensaje)
    
    def mostrarmensaje(self):
        self.ui.LabelMensaje.setTex('Hola '+ self.ui.lineNombreUsuario.text())

app = QtWidgets.QApplication([]) 
application = mywindow() 
application.show() 
sys.exit(app.exec())