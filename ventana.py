# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_venPrincipal(object):
    def setupUi(self, venPrincipal):
        venPrincipal.setObjectName("venPrincipal")
        venPrincipal.resize(1278, 1009)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(venPrincipal.sizePolicy().hasHeightForWidth())
        venPrincipal.setSizePolicy(sizePolicy)
        venPrincipal.setMinimumSize(QtCore.QSize(1150, 0))
        venPrincipal.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(venPrincipal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_7.setObjectName("gridLayout_7")
        spacerItem = QtWidgets.QSpacerItem(20, 120, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_7.addItem(spacerItem, 2, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem1, 1, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 31, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_7.addItem(spacerItem2, 0, 4, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 754, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem3, 1, 6, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(1000, 700))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.panelCli = QtWidgets.QWidget()
        self.panelCli.setObjectName("panelCli")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.panelCli)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.gridFormabajo = QtWidgets.QGridLayout()
        self.gridFormabajo.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.gridFormabajo.setObjectName("gridFormabajo")
        self.chkTar = QtWidgets.QCheckBox(self.panelCli)
        self.chkTar.setObjectName("chkTar")
        self.grpbtnPay = QtWidgets.QButtonGroup(venPrincipal)
        self.grpbtnPay.setObjectName("grpbtnPay")
        self.grpbtnPay.setExclusive(False)
        self.grpbtnPay.addButton(self.chkTar)
        self.gridFormabajo.addWidget(self.chkTar, 0, 7, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(310, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridFormabajo.addItem(spacerItem4, 0, 3, 1, 1)
        self.rbtFem = QtWidgets.QRadioButton(self.panelCli)
        self.rbtFem.setObjectName("rbtFem")
        self.grpbtnSex = QtWidgets.QButtonGroup(venPrincipal)
        self.grpbtnSex.setObjectName("grpbtnSex")
        self.grpbtnSex.addButton(self.rbtFem)
        self.gridFormabajo.addWidget(self.rbtFem, 0, 1, 1, 1)
        self.chkTrans = QtWidgets.QCheckBox(self.panelCli)
        self.chkTrans.setObjectName("chkTrans")
        self.grpbtnPay.addButton(self.chkTrans)
        self.gridFormabajo.addWidget(self.chkTrans, 0, 8, 1, 1)
        self.lblSexo = QtWidgets.QLabel(self.panelCli)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblSexo.setFont(font)
        self.lblSexo.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lblSexo.setObjectName("lblSexo")
        self.gridFormabajo.addWidget(self.lblSexo, 0, 0, 1, 1)
        self.chkEfec = QtWidgets.QCheckBox(self.panelCli)
        self.chkEfec.setObjectName("chkEfec")
        self.grpbtnPay.addButton(self.chkEfec)
        self.gridFormabajo.addWidget(self.chkEfec, 0, 6, 1, 1)
        self.rbtMasc = QtWidgets.QRadioButton(self.panelCli)
        self.rbtMasc.setObjectName("rbtMasc")
        self.grpbtnSex.addButton(self.rbtMasc)
        self.gridFormabajo.addWidget(self.rbtMasc, 0, 2, 1, 1)
        self.lblPago = QtWidgets.QLabel(self.panelCli)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblPago.setFont(font)
        self.lblPago.setObjectName("lblPago")
        self.gridFormabajo.addWidget(self.lblPago, 0, 5, 1, 1)
        self.gridLayout_8.addLayout(self.gridFormabajo, 3, 0, 1, 1)
        self.gridFormdatos = QtWidgets.QGridLayout()
        self.gridFormdatos.setObjectName("gridFormdatos")
        self.lblNome = QtWidgets.QLabel(self.panelCli)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblNome.sizePolicy().hasHeightForWidth())
        self.lblNome.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblNome.setFont(font)
        self.lblNome.setObjectName("lblNome")
        self.gridFormdatos.addWidget(self.lblNome, 0, 3, 1, 1)
        self.lblApel = QtWidgets.QLabel(self.panelCli)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblApel.sizePolicy().hasHeightForWidth())
        self.lblApel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblApel.setFont(font)
        self.lblApel.setObjectName("lblApel")
        self.gridFormdatos.addWidget(self.lblApel, 0, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridFormdatos.addItem(spacerItem5, 0, 2, 1, 1)
        self.editNome = QtWidgets.QLineEdit(self.panelCli)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editNome.sizePolicy().hasHeightForWidth())
        self.editNome.setSizePolicy(sizePolicy)
        self.editNome.setStyleSheet("background-color: rgb(255, 255, 229);")
        self.editNome.setObjectName("editNome")
        self.gridFormdatos.addWidget(self.editNome, 0, 4, 1, 1)
        self.editApel = QtWidgets.QLineEdit(self.panelCli)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editApel.sizePolicy().hasHeightForWidth())
        self.editApel.setSizePolicy(sizePolicy)
        self.editApel.setMaximumSize(QtCore.QSize(1000, 16777215))
        self.editApel.setStyleSheet("background-color: rgb(255, 255, 229);")
        self.editApel.setObjectName("editApel")
        self.gridFormdatos.addWidget(self.editApel, 0, 1, 1, 1)
        self.gridLayout_8.addLayout(self.gridFormdatos, 1, 0, 1, 1)
        self.gridFormdir = QtWidgets.QGridLayout()
        self.gridFormdir.setObjectName("gridFormdir")
        self.lblDir = QtWidgets.QLabel(self.panelCli)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblDir.sizePolicy().hasHeightForWidth())
        self.lblDir.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblDir.setFont(font)
        self.lblDir.setObjectName("lblDir")
        self.gridFormdir.addWidget(self.lblDir, 0, 0, 1, 1)
        self.cmbProv = QtWidgets.QComboBox(self.panelCli)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmbProv.sizePolicy().hasHeightForWidth())
        self.cmbProv.setSizePolicy(sizePolicy)
        self.cmbProv.setSizeIncrement(QtCore.QSize(30, 0))
        self.cmbProv.setObjectName("cmbProv")
        self.gridFormdir.addWidget(self.cmbProv, 0, 5, 1, 1)
        self.editDir = QtWidgets.QLineEdit(self.panelCli)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editDir.sizePolicy().hasHeightForWidth())
        self.editDir.setSizePolicy(sizePolicy)
        self.editDir.setStyleSheet("background-color: rgb(255, 255, 229);")
        self.editDir.setObjectName("editDir")
        self.gridFormdir.addWidget(self.editDir, 0, 1, 1, 1)
        self.lblProv = QtWidgets.QLabel(self.panelCli)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblProv.sizePolicy().hasHeightForWidth())
        self.lblProv.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblProv.setFont(font)
        self.lblProv.setObjectName("lblProv")
        self.gridFormdir.addWidget(self.lblProv, 0, 3, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(96, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridFormdir.addItem(spacerItem6, 0, 2, 1, 1)
        self.gridLayout_8.addLayout(self.gridFormdir, 2, 0, 1, 1)
        self.gridFormsup = QtWidgets.QGridLayout()
        self.gridFormsup.setObjectName("gridFormsup")
        self.lblValidar = QtWidgets.QLabel(self.panelCli)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblValidar.sizePolicy().hasHeightForWidth())
        self.lblValidar.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lblValidar.setFont(font)
        self.lblValidar.setText("")
        self.lblValidar.setObjectName("lblValidar")
        self.gridFormsup.addWidget(self.lblValidar, 2, 3, 1, 1)
        self.lblDNI = QtWidgets.QLabel(self.panelCli)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblDNI.sizePolicy().hasHeightForWidth())
        self.lblDNI.setSizePolicy(sizePolicy)
        self.lblDNI.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblDNI.setFont(font)
        self.lblDNI.setStyleSheet("")
        self.lblDNI.setObjectName("lblDNI")
        self.gridFormsup.addWidget(self.lblDNI, 2, 0, 1, 1)
        self.editDni = QtWidgets.QLineEdit(self.panelCli)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editDni.sizePolicy().hasHeightForWidth())
        self.editDni.setSizePolicy(sizePolicy)
        self.editDni.setStyleSheet("background-color: rgb(255, 255, 229);")
        self.editDni.setObjectName("editDni")
        self.gridFormsup.addWidget(self.editDni, 2, 2, 1, 1)
        self.lblClialta = QtWidgets.QLabel(self.panelCli)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblClialta.sizePolicy().hasHeightForWidth())
        self.lblClialta.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblClialta.setFont(font)
        self.lblClialta.setObjectName("lblClialta")
        self.gridFormsup.addWidget(self.lblClialta, 2, 14, 1, 1)
        self.btnCalendar = QtWidgets.QPushButton(self.panelCli)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnCalendar.sizePolicy().hasHeightForWidth())
        self.btnCalendar.setSizePolicy(sizePolicy)
        self.btnCalendar.setMaximumSize(QtCore.QSize(32, 32))
        self.btnCalendar.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/calendar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCalendar.setIcon(icon)
        self.btnCalendar.setIconSize(QtCore.QSize(30, 30))
        self.btnCalendar.setObjectName("btnCalendar")
        self.gridFormsup.addWidget(self.btnCalendar, 2, 18, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(500, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridFormsup.addItem(spacerItem7, 2, 6, 1, 1)
        self.editClialta = QtWidgets.QLineEdit(self.panelCli)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editClialta.sizePolicy().hasHeightForWidth())
        self.editClialta.setSizePolicy(sizePolicy)
        self.editClialta.setMinimumSize(QtCore.QSize(0, 0))
        self.editClialta.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.editClialta.setStyleSheet("background-color: rgb(255, 255, 229);")
        self.editClialta.setAlignment(QtCore.Qt.AlignCenter)
        self.editClialta.setObjectName("editClialta")
        self.gridFormsup.addWidget(self.editClialta, 2, 15, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(37, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridFormsup.addItem(spacerItem8, 2, 1, 1, 1)
        self.lblCodCli = QtWidgets.QLabel(self.panelCli)
        self.lblCodCli.setText("")
        self.lblCodCli.setObjectName("lblCodCli")
        self.gridFormsup.addWidget(self.lblCodCli, 2, 4, 1, 1)
        self.gridLayout_8.addLayout(self.gridFormsup, 0, 0, 1, 1)
        self.gridBoton = QtWidgets.QGridLayout()
        self.gridBoton.setObjectName("gridBoton")
        self.line_2 = QtWidgets.QFrame(self.panelCli)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridBoton.addWidget(self.line_2, 4, 0, 1, 1)
        self.tableCli = QtWidgets.QTableWidget(self.panelCli)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableCli.sizePolicy().hasHeightForWidth())
        self.tableCli.setSizePolicy(sizePolicy)
        self.tableCli.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tableCli.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableCli.setAutoScroll(True)
        self.tableCli.setAlternatingRowColors(True)
        self.tableCli.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tableCli.setGridStyle(QtCore.Qt.DotLine)
        self.tableCli.setObjectName("tableCli")
        self.tableCli.setColumnCount(3)
        self.tableCli.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableCli.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableCli.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableCli.setHorizontalHeaderItem(2, item)
        self.tableCli.horizontalHeader().setDefaultSectionSize(300)
        self.tableCli.horizontalHeader().setMinimumSectionSize(20)
        self.tableCli.verticalHeader().setStretchLastSection(False)
        self.gridBoton.addWidget(self.tableCli, 0, 0, 1, 1)
        self.groupbox = QtWidgets.QGroupBox(self.panelCli)
        self.groupbox.setObjectName("groupbox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupbox)
        self.gridLayout.setContentsMargins(10, 1, 10, -1)
        self.gridLayout.setObjectName("gridLayout")
        self.btnSalir = QtWidgets.QPushButton(self.groupbox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnSalir.sizePolicy().hasHeightForWidth())
        self.btnSalir.setSizePolicy(sizePolicy)
        self.btnSalir.setObjectName("btnSalir")
        self.gridLayout.addWidget(self.btnSalir, 1, 5, 1, 1)
        self.btnAltaCli = QtWidgets.QPushButton(self.groupbox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnAltaCli.sizePolicy().hasHeightForWidth())
        self.btnAltaCli.setSizePolicy(sizePolicy)
        self.btnAltaCli.setObjectName("btnAltaCli")
        self.gridLayout.addWidget(self.btnAltaCli, 1, 0, 1, 1)
        self.btnLimpiarCli = QtWidgets.QPushButton(self.groupbox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnLimpiarCli.sizePolicy().hasHeightForWidth())
        self.btnLimpiarCli.setSizePolicy(sizePolicy)
        self.btnLimpiarCli.setObjectName("btnLimpiarCli")
        self.gridLayout.addWidget(self.btnLimpiarCli, 1, 3, 1, 1)
        self.btmBajaCli = QtWidgets.QPushButton(self.groupbox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btmBajaCli.sizePolicy().hasHeightForWidth())
        self.btmBajaCli.setSizePolicy(sizePolicy)
        self.btmBajaCli.setObjectName("btmBajaCli")
        self.gridLayout.addWidget(self.btmBajaCli, 1, 2, 1, 1)
        self.btnModifCli = QtWidgets.QPushButton(self.groupbox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnModifCli.sizePolicy().hasHeightForWidth())
        self.btnModifCli.setSizePolicy(sizePolicy)
        self.btnModifCli.setObjectName("btnModifCli")
        self.gridLayout.addWidget(self.btnModifCli, 1, 4, 1, 1)
        self.gridBoton.addWidget(self.groupbox, 3, 0, 1, 1)
        self.gridLayout_8.addLayout(self.gridBoton, 4, 0, 1, 1)
        self.tabWidget.addTab(self.panelCli, "")
        self.panelFac = QtWidgets.QWidget()
        self.panelFac.setObjectName("panelFac")
        self.label = QtWidgets.QLabel(self.panelFac)
        self.label.setGeometry(QtCore.QRect(380, 340, 351, 101))
        self.label.setObjectName("label")
        self.tabWidget.addTab(self.panelFac, "")
        self.panelPro = QtWidgets.QWidget()
        self.panelPro.setObjectName("panelPro")
        self.tabWidget.addTab(self.panelPro, "")
        self.gridLayout_7.addWidget(self.tabWidget, 1, 2, 1, 4)
        venPrincipal.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(venPrincipal)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1278, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuArchivo = QtWidgets.QMenu(self.menuBar)
        self.menuArchivo.setObjectName("menuArchivo")
        venPrincipal.setMenuBar(self.menuBar)
        self.statusbar = QtWidgets.QStatusBar(venPrincipal)
        self.statusbar.setObjectName("statusbar")
        venPrincipal.setStatusBar(self.statusbar)
        self.actionSalir = QtWidgets.QAction(venPrincipal)
        self.actionSalir.setObjectName("actionSalir")
        self.menuArchivo.addAction(self.actionSalir)
        self.menuBar.addAction(self.menuArchivo.menuAction())

        self.retranslateUi(venPrincipal)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(venPrincipal)

    def retranslateUi(self, venPrincipal):
        _translate = QtCore.QCoreApplication.translate
        venPrincipal.setWindowTitle(_translate("venPrincipal", "Proyecto Uno"))
        self.chkTar.setText(_translate("venPrincipal", "Tarjeta"))
        self.rbtFem.setText(_translate("venPrincipal", "Femenino"))
        self.chkTrans.setText(_translate("venPrincipal", "Transferencia"))
        self.lblSexo.setText(_translate("venPrincipal", "Sexo:  "))
        self.chkEfec.setText(_translate("venPrincipal", "Efectivo"))
        self.rbtMasc.setText(_translate("venPrincipal", "Masculino"))
        self.lblPago.setText(_translate("venPrincipal", "Métodos de Pago:  "))
        self.lblNome.setText(_translate("venPrincipal", "Nombre: "))
        self.lblApel.setText(_translate("venPrincipal", "Apellidos: "))
        self.lblDir.setText(_translate("venPrincipal", "Dirección: "))
        self.lblProv.setText(_translate("venPrincipal", "Provincia:"))
        self.lblDNI.setText(_translate("venPrincipal", "DNI: "))
        self.lblClialta.setText(_translate("venPrincipal", "Fecha de Alta:"))
        item = self.tableCli.horizontalHeaderItem(0)
        item.setText(_translate("venPrincipal", "DNI"))
        item = self.tableCli.horizontalHeaderItem(1)
        item.setText(_translate("venPrincipal", "APELLIDOS"))
        item = self.tableCli.horizontalHeaderItem(2)
        item.setText(_translate("venPrincipal", "NOMBRE"))
        self.btnSalir.setText(_translate("venPrincipal", "Salir"))
        self.btnAltaCli.setText(_translate("venPrincipal", "Grabar"))
        self.btnLimpiarCli.setText(_translate("venPrincipal", "Limpiar"))
        self.btmBajaCli.setText(_translate("venPrincipal", "Eliminar"))
        self.btnModifCli.setText(_translate("venPrincipal", "Modificar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.panelCli), _translate("venPrincipal", "Clientes"))
        self.label.setText(_translate("venPrincipal", "PANEL DE FACTURACIÓN"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.panelFac), _translate("venPrincipal", "Facturación"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.panelPro), _translate("venPrincipal", "Productos"))
        self.menuArchivo.setTitle(_translate("venPrincipal", "Archivo"))
        self.actionSalir.setText(_translate("venPrincipal", "Salir"))
        self.actionSalir.setShortcut(_translate("venPrincipal", "Alt+S"))
import logo_rc
