# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'venavisos.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dlgaviso(object):
    def setupUi(self, dlgaviso):
        dlgaviso.setObjectName("dlgaviso")
        dlgaviso.resize(400, 178)
        dlgaviso.setModal(True)
        self.lblsaviso = QtWidgets.QLabel(dlgaviso)
        self.lblsaviso.setGeometry(QtCore.QRect(220, 70, 151, 16))
        self.lblsaviso.setObjectName("lblsaviso")
        self.btnAceptar = QtWidgets.QPushButton(dlgaviso)
        self.btnAceptar.setGeometry(QtCore.QRect(100, 130, 75, 23))
        self.btnAceptar.setObjectName("btnAceptar")
        self.buttonGroup = QtWidgets.QButtonGroup(dlgaviso)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.btnAceptar)
        self.btnCancelar = QtWidgets.QPushButton(dlgaviso)
        self.btnCancelar.setGeometry(QtCore.QRect(230, 130, 75, 23))
        self.btnCancelar.setObjectName("btnCancelar")
        self.buttonGroup.addButton(self.btnCancelar)

        self.retranslateUi(dlgaviso)
        QtCore.QMetaObject.connectSlotsByName(dlgaviso)

    def retranslateUi(self, dlgaviso):
        _translate = QtCore.QCoreApplication.translate
        dlgaviso.setWindowTitle(_translate("dlgaviso", "Dialog"))
        self.lblsaviso.setText(_translate("dlgaviso", "Desea realizar la operación?"))
        self.btnAceptar.setText(_translate("dlgaviso", "Aceptar"))
        self.btnCancelar.setText(_translate("dlgaviso", "Cancelar"))
