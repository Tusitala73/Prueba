import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic

class MainWindow(QMainWindow):
    def __init__(self, *args):
        super(MainWindow, self).__init__(*args)
        uic.loadUi('MainWindow.ui', self)
        #self.setWindowTitle("Hola como estan ?")
       
app = QApplication(sys.argv)
widget = MainWindow()
widget.show()
sys.exit(app.exec_())