#from PyQt5 import QtWidgets
 
from Primera import *#Ui_Dialog  # importing our generated file
 
import sys
 
class mywindow(QtWidgets.QDialog): 
    def __init__(self, parent=None):    
        super().__init__(parent)    
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
 
app = QtWidgets.QApplication([]) 
application = mywindow() 
application.show() 
sys.exit(app.exec())