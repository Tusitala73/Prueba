import sys
from Primera import *

class MiFormulario(QtWidgets.QDialog):
    def __init__(self):        
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    myapp = MiFormulario()
    myapp.show()
    sys.exit(app.exec_())


