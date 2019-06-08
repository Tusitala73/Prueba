# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mibienbenida.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(383, 202)
        self.labelEscribeNombre = QtWidgets.QLabel(Dialog)
        self.labelEscribeNombre.setGeometry(QtCore.QRect(66, 40, 111, 20))
        self.labelEscribeNombre.setObjectName("labelEscribeNombre")
        self.labelMensaje = QtWidgets.QLabel(Dialog)
        self.labelMensaje.setGeometry(QtCore.QRect(110, 90, 151, 20))
        self.labelMensaje.setText("")
        self.labelMensaje.setObjectName("labelMensaje")
        self.lineEditNombreUsuario = QtWidgets.QLineEdit(Dialog)
        self.lineEditNombreUsuario.setGeometry(QtCore.QRect(200, 40, 113, 20))
        self.lineEditNombreUsuario.setObjectName("lineEditNombreUsuario")
        self.pushButtonPulsar = QtWidgets.QPushButton(Dialog)
        self.pushButtonPulsar.setGeometry(QtCore.QRect(150, 120, 75, 23))
        self.pushButtonPulsar.setObjectName("pushButtonPulsar")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.labelEscribeNombre.setText(_translate("Dialog", "Introduce tu Nombre"))
        self.pushButtonPulsar.setText(_translate("Dialog", "Saludo"))

