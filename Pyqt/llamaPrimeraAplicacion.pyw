import sys
from PrimeraAplicacion import *

class MiFormulario(QtGui.QDialog):
    QtGui.QWidget.__init__(self, parent)
    self.ui = ui_Dialog()
    self.ui.setupUi(self)

if __name__ == '__main__':
    app = QtGui.Qappilcation(sys.argv)
    myapp = MiFormulario()
    myapp.show()
    sys.exit(app.exec_())


