# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Form_Memoria.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form_Memoria(object):
    def setupUi(self, Form_Memoria):
        Form_Memoria.setObjectName("Form_Memoria")
        Form_Memoria.resize(1024, 576)
        Form_Memoria.setMinimumSize(QtCore.QSize(1024, 576))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(57, 57, 57))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(57, 57, 57))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(57, 57, 57))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(57, 57, 57))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(57, 57, 57))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(57, 57, 57))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(57, 57, 57))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(57, 57, 57))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(57, 57, 57))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        Form_Memoria.setPalette(palette)
        Form_Memoria.setWindowTitle("Simulador de Sistema Operativo")
        Form_Memoria.setAutoFillBackground(False)
        Form_Memoria.setStyleSheet("background-color: rgb(57, 57, 57);")
        Form_Memoria.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.pushButton_Importar = QtWidgets.QPushButton(Form_Memoria)
        self.pushButton_Importar.setGeometry(QtCore.QRect(930, 240, 81, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 123, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 123, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 123, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 123, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 123, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 123, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 123, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 123, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 123, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.pushButton_Importar.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("12 MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_Importar.setFont(font)
        self.pushButton_Importar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_Importar.setStyleSheet("background-color: rgb(0, 123, 255);\n"
"color: rgb(0, 0, 0);")
        self.pushButton_Importar.setAutoDefault(False)
        self.pushButton_Importar.setObjectName("pushButton_Importar")
        self.pushButton_Generar = QtWidgets.QPushButton(Form_Memoria)
        self.pushButton_Generar.setGeometry(QtCore.QRect(930, 360, 81, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Generar.setFont(font)
        self.pushButton_Generar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_Generar.setStyleSheet("background-color: rgb(0, 123, 255);\n"
"color: rgb(0, 0, 0);")
        self.pushButton_Generar.setObjectName("pushButton_Generar")
        self.pushButton_Guardar = QtWidgets.QPushButton(Form_Memoria)
        self.pushButton_Guardar.setGeometry(QtCore.QRect(930, 300, 81, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Guardar.setFont(font)
        self.pushButton_Guardar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_Guardar.setStyleSheet("background-color: rgb(0, 123, 255);\n"
"color: rgb(0, 0, 0);")
        self.pushButton_Guardar.setObjectName("pushButton_Guardar")
        self.tableWidget_Procesos = QtWidgets.QTableWidget(Form_Memoria)
        self.tableWidget_Procesos.setGeometry(QtCore.QRect(190, 130, 731, 391))
        self.tableWidget_Procesos.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tableWidget_Procesos.setFont(font)
        self.tableWidget_Procesos.setAutoFillBackground(False)
        self.tableWidget_Procesos.setStyleSheet("gridline-color: rgb(0,0, 0);\n"
"color: rgb(0,0,0);\n"
"background-color: rgb(255,255,255);")
        self.tableWidget_Procesos.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.tableWidget_Procesos.setLineWidth(1)
        self.tableWidget_Procesos.setMidLineWidth(0)
        self.tableWidget_Procesos.setAlternatingRowColors(True)
        self.tableWidget_Procesos.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableWidget_Procesos.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tableWidget_Procesos.setShowGrid(True)
        self.tableWidget_Procesos.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget_Procesos.setCornerButtonEnabled(False)
        self.tableWidget_Procesos.setRowCount(0)
        self.tableWidget_Procesos.setObjectName("tableWidget_Procesos")
        self.tableWidget_Procesos.setColumnCount(7)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Procesos.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Procesos.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Procesos.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Procesos.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Procesos.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Procesos.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Procesos.setHorizontalHeaderItem(6, item)
        self.tableWidget_Procesos.horizontalHeader().setVisible(True)
        self.tableWidget_Procesos.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_Procesos.horizontalHeader().setHighlightSections(True)
        self.tableWidget_Procesos.verticalHeader().setHighlightSections(True)
        self.label_AsignacionDeMemoria = QtWidgets.QLabel(Form_Memoria)
        self.label_AsignacionDeMemoria.setGeometry(QtCore.QRect(360, 20, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_AsignacionDeMemoria.setFont(font)
        self.label_AsignacionDeMemoria.setStyleSheet("color: rgb(0, 123, 255);")
        self.label_AsignacionDeMemoria.setObjectName("label_AsignacionDeMemoria")
        self.pushButton_Siguiente = QtWidgets.QPushButton(Form_Memoria)
        self.pushButton_Siguiente.setGeometry(QtCore.QRect(950, 10, 61, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 123, 255, 150))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 123, 255, 150))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 123, 255, 150))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 123, 255, 150))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 123, 255, 150))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 123, 255, 150))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 123, 255, 150))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 123, 255, 150))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 123, 255, 150))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.pushButton_Siguiente.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_Siguiente.setFont(font)
        self.pushButton_Siguiente.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_Siguiente.setToolTip("")
        self.pushButton_Siguiente.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.pushButton_Siguiente.setStyleSheet("background-color: rgb(0, 123, 255,150);\n"
"color: rgb(0, 0, 0);")
        self.pushButton_Siguiente.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Recursos/Siguiente.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Siguiente.setIcon(icon)
        self.pushButton_Siguiente.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_Siguiente.setObjectName("pushButton_Siguiente")
        self.pushButton_Atras = QtWidgets.QPushButton(Form_Memoria)
        self.pushButton_Atras.setEnabled(True)
        self.pushButton_Atras.setGeometry(QtCore.QRect(10, 10, 61, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 123, 255, 150))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 123, 255, 150))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 123, 255, 150))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 123, 255, 150))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 123, 255, 150))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 123, 255, 150))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 123, 255, 150))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 123, 255, 150))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 123, 255, 150))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.pushButton_Atras.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("12 MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_Atras.setFont(font)
        self.pushButton_Atras.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_Atras.setToolTip("")
        self.pushButton_Atras.setStyleSheet("background-color: rgb(0, 123, 255,150);\n"
"color: rgb(0, 0, 0);")
        self.pushButton_Atras.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Recursos/Atras.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Atras.setIcon(icon1)
        self.pushButton_Atras.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_Atras.setAutoDefault(False)
        self.pushButton_Atras.setObjectName("pushButton_Atras")
        self.graphicsView = QtWidgets.QGraphicsView(Form_Memoria)
        self.graphicsView.setGeometry(QtCore.QRect(10, 210, 171, 311))
        self.graphicsView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.graphicsView.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.graphicsView.setObjectName("graphicsView")
        self.radioButton_PartFijas = QtWidgets.QRadioButton(Form_Memoria)
        self.radioButton_PartFijas.setGeometry(QtCore.QRect(20, 110, 121, 17))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.radioButton_PartFijas.setFont(font)
        self.radioButton_PartFijas.setToolTip("")
        self.radioButton_PartFijas.setStyleSheet("color: rgb(255, 255, 255);")
        self.radioButton_PartFijas.setObjectName("radioButton_PartFijas")
        self.radioButton_PartVariables = QtWidgets.QRadioButton(Form_Memoria)
        self.radioButton_PartVariables.setGeometry(QtCore.QRect(20, 140, 141, 17))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.radioButton_PartVariables.setFont(font)
        self.radioButton_PartVariables.setToolTip("")
        self.radioButton_PartVariables.setStyleSheet("color: rgb(255, 255, 255);")
        self.radioButton_PartVariables.setObjectName("radioButton_PartVariables")
        self.spinBox_Tamano = QtWidgets.QSpinBox(Form_Memoria)
        self.spinBox_Tamano.setGeometry(QtCore.QRect(110, 70, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.spinBox_Tamano.setFont(font)
        self.spinBox_Tamano.setStyleSheet("color: rgb(255, 255, 255);")
        self.spinBox_Tamano.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_Tamano.setMaximum(9999)
        self.spinBox_Tamano.setSingleStep(10)
        self.spinBox_Tamano.setObjectName("spinBox_Tamano")
        self.label_Tamano = QtWidgets.QLabel(Form_Memoria)
        self.label_Tamano.setGeometry(QtCore.QRect(10, 70, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_Tamano.setFont(font)
        self.label_Tamano.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_Tamano.setObjectName("label_Tamano")
        self.pushButton_AnadirPart = QtWidgets.QPushButton(Form_Memoria)
        self.pushButton_AnadirPart.setGeometry(QtCore.QRect(20, 170, 141, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 123, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 123, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 123, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 123, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 123, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 123, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 123, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 123, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 123, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.pushButton_AnadirPart.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("12 MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_AnadirPart.setFont(font)
        self.pushButton_AnadirPart.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_AnadirPart.setToolTip("")
        self.pushButton_AnadirPart.setStyleSheet("background-color: rgb(0, 123, 255);\n"
"color: rgb(0, 0, 0);")
        self.pushButton_AnadirPart.setAutoDefault(False)
        self.pushButton_AnadirPart.setObjectName("pushButton_AnadirPart")
        self.radioButton_BestFit = QtWidgets.QRadioButton(Form_Memoria)
        self.radioButton_BestFit.setGeometry(QtCore.QRect(310, 100, 71, 17))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.radioButton_BestFit.setFont(font)
        self.radioButton_BestFit.setToolTip("")
        self.radioButton_BestFit.setStyleSheet("color: rgb(255, 255, 255);")
        self.radioButton_BestFit.setObjectName("radioButton_BestFit")
        self.radioButton_WorstFit = QtWidgets.QRadioButton(Form_Memoria)
        self.radioButton_WorstFit.setGeometry(QtCore.QRect(310, 100, 81, 17))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.radioButton_WorstFit.setFont(font)
        self.radioButton_WorstFit.setToolTip("")
        self.radioButton_WorstFit.setStyleSheet("color: rgb(255, 255, 255);")
        self.radioButton_WorstFit.setObjectName("radioButton_WorstFit")
        self.radioButton_FirstFit = QtWidgets.QRadioButton(Form_Memoria)
        self.radioButton_FirstFit.setGeometry(QtCore.QRect(210, 100, 71, 17))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.radioButton_FirstFit.setFont(font)
        self.radioButton_FirstFit.setToolTip("")
        self.radioButton_FirstFit.setStyleSheet("color: rgb(255, 255, 255);")
        self.radioButton_FirstFit.setObjectName("radioButton_FirstFit")
        self.pushButton_Importar.raise_()
        self.pushButton_Generar.raise_()
        self.pushButton_Guardar.raise_()
        self.tableWidget_Procesos.raise_()
        self.label_AsignacionDeMemoria.raise_()
        self.pushButton_Siguiente.raise_()
        self.pushButton_Atras.raise_()
        self.graphicsView.raise_()
        self.radioButton_PartFijas.raise_()
        self.radioButton_PartVariables.raise_()
        self.label_Tamano.raise_()
        self.spinBox_Tamano.raise_()
        self.pushButton_AnadirPart.raise_()
        self.radioButton_BestFit.raise_()
        self.radioButton_WorstFit.raise_()
        self.radioButton_FirstFit.raise_()

        self.retranslateUi(Form_Memoria)
        QtCore.QMetaObject.connectSlotsByName(Form_Memoria)
        Form_Memoria.setTabOrder(self.tableWidget_Procesos, self.pushButton_Importar)
        Form_Memoria.setTabOrder(self.pushButton_Importar, self.pushButton_Guardar)
        Form_Memoria.setTabOrder(self.pushButton_Guardar, self.pushButton_Generar)
        Form_Memoria.setTabOrder(self.pushButton_Generar, self.pushButton_Siguiente)
        Form_Memoria.setTabOrder(self.pushButton_Siguiente, self.pushButton_Atras)

    def retranslateUi(self, Form_Memoria):
        _translate = QtCore.QCoreApplication.translate
        self.pushButton_Importar.setToolTip(_translate("Form_Memoria", "<html><head/><body><p>Importar carga de trabajo</p></body></html>"))
        self.pushButton_Importar.setText(_translate("Form_Memoria", "Importar"))
        self.pushButton_Generar.setToolTip(_translate("Form_Memoria", "<html><head/><body><p>Generar una carga de trabajo aleatoria</p></body></html>"))
        self.pushButton_Generar.setText(_translate("Form_Memoria", "Generar"))
        self.pushButton_Guardar.setToolTip(_translate("Form_Memoria", "<html><head/><body><p>Guardar la carga de trabajo actual</p></body></html>"))
        self.pushButton_Guardar.setText(_translate("Form_Memoria", "Guardar"))
        self.tableWidget_Procesos.setSortingEnabled(False)
        item = self.tableWidget_Procesos.horizontalHeaderItem(0)
        item.setText(_translate("Form_Memoria", "Tiempo de Arribo"))
        item = self.tableWidget_Procesos.horizontalHeaderItem(1)
        item.setText(_translate("Form_Memoria", "CPU"))
        item = self.tableWidget_Procesos.horizontalHeaderItem(2)
        item.setText(_translate("Form_Memoria", "Entrada"))
        item = self.tableWidget_Procesos.horizontalHeaderItem(3)
        item.setText(_translate("Form_Memoria", "CPU"))
        item = self.tableWidget_Procesos.horizontalHeaderItem(4)
        item.setText(_translate("Form_Memoria", "Salida"))
        item = self.tableWidget_Procesos.horizontalHeaderItem(5)
        item.setText(_translate("Form_Memoria", "CPU"))
        item = self.tableWidget_Procesos.horizontalHeaderItem(6)
        item.setText(_translate("Form_Memoria", "Memoria"))
        self.label_AsignacionDeMemoria.setText(_translate("Form_Memoria", "Asignación de Memoria"))
        self.radioButton_PartFijas.setText(_translate("Form_Memoria", "Particiones Fijas"))
        self.radioButton_PartVariables.setText(_translate("Form_Memoria", "Particiones Variables"))
        self.label_Tamano.setText(_translate("Form_Memoria", "Tamaño(KB)"))
        self.pushButton_AnadirPart.setText(_translate("Form_Memoria", "Añadir Partición"))
        self.radioButton_BestFit.setText(_translate("Form_Memoria", "Best Fit"))
        self.radioButton_WorstFit.setText(_translate("Form_Memoria", "Worst Fit"))
        self.radioButton_FirstFit.setText(_translate("Form_Memoria", "First Fit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form_Memoria = QtWidgets.QWidget()
    ui = Ui_Form_Memoria()
    ui.setupUi(Form_Memoria)
    Form_Memoria.show()
    sys.exit(app.exec_())

