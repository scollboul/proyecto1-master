# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vensalir.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dlgsalir(object):
    def setupUi(self, dlgsalir):
        dlgsalir.setObjectName("dlgsalir")
        dlgsalir.resize(376, 154)
        dlgsalir.setModal(True)
        self.btnBoxSalir = QtWidgets.QDialogButtonBox(dlgsalir)
        self.btnBoxSalir.setGeometry(QtCore.QRect(120, 90, 161, 32))
        self.btnBoxSalir.setOrientation(QtCore.Qt.Horizontal)
        self.btnBoxSalir.setStandardButtons(QtWidgets.QDialogButtonBox.No|QtWidgets.QDialogButtonBox.Yes)
        self.btnBoxSalir.setCenterButtons(True)
        self.btnBoxSalir.setObjectName("btnBoxSalir")
        self.lblMensalir = QtWidgets.QLabel(dlgsalir)
        self.lblMensalir.setGeometry(QtCore.QRect(90, 40, 271, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lblMensalir.setFont(font)
        self.lblMensalir.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lblMensalir.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblMensalir.setObjectName("lblMensalir")
        self.label = QtWidgets.QLabel(dlgsalir)
        self.label.setGeometry(QtCore.QRect(30, 70, 51, 51))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/newPrefix/iconoaviso.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        self.retranslateUi(dlgsalir)
        self.btnBoxSalir.accepted.connect(dlgsalir.accept)
        self.btnBoxSalir.rejected.connect(dlgsalir.reject)
        QtCore.QMetaObject.connectSlotsByName(dlgsalir)

    def retranslateUi(self, dlgsalir):
        _translate = QtCore.QCoreApplication.translate
        dlgsalir.setWindowTitle(_translate("dlgsalir", "Salir"))
        self.lblMensalir.setText(_translate("dlgsalir", "¿Está seguro que desea salir de la aplicación?"))
import avisosalir_rc
