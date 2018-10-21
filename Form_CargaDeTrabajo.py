# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Form_CargaDeTrabajo.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form_CargaDeTrabajo(object):
    def setupUi(self, Form_CargaDeTrabajo):
        Form_CargaDeTrabajo.setObjectName("Form_CargaDeTrabajo")
        Form_CargaDeTrabajo.resize(1423, 862)
        Form_CargaDeTrabajo.setStyleSheet("")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(Form_CargaDeTrabajo)
        self.verticalLayout_5.setSpacing(15)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_9.setSpacing(5)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem)
        self.pushButton_Minimizar = QtWidgets.QPushButton(Form_CargaDeTrabajo)
        self.pushButton_Minimizar.setStyleSheet("background-image: url();")
        self.pushButton_Minimizar.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Recursos/Minimizar.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Minimizar.setIcon(icon)
        self.pushButton_Minimizar.setObjectName("pushButton_Minimizar")
        self.horizontalLayout_9.addWidget(self.pushButton_Minimizar)
        self.pushButton_Ventana = QtWidgets.QPushButton(Form_CargaDeTrabajo)
        self.pushButton_Ventana.setStyleSheet("background-image: url();")
        self.pushButton_Ventana.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Recursos/Ventana.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Ventana.setIcon(icon1)
        self.pushButton_Ventana.setObjectName("pushButton_Ventana")
        self.horizontalLayout_9.addWidget(self.pushButton_Ventana)
        self.pushButton_Cerrar = QtWidgets.QPushButton(Form_CargaDeTrabajo)
        self.pushButton_Cerrar.setStyleSheet("background-image: url();")
        self.pushButton_Cerrar.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Recursos/Cerrar.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Cerrar.setIcon(icon2)
        self.pushButton_Cerrar.setObjectName("pushButton_Cerrar")
        self.horizontalLayout_9.addWidget(self.pushButton_Cerrar)
        self.verticalLayout_5.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.label_CargaDeTrabajo = QtWidgets.QLabel(Form_CargaDeTrabajo)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_CargaDeTrabajo.setFont(font)
        self.label_CargaDeTrabajo.setStyleSheet("background-image: url();\n"
"color: rgb(139, 170, 255);\n"
"background-color: rgb(0, 0, 0, 0);")
        self.label_CargaDeTrabajo.setObjectName("label_CargaDeTrabajo")
        self.horizontalLayout_2.addWidget(self.label_CargaDeTrabajo)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(20)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem3)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.radioButton_PartFijas = QtWidgets.QRadioButton(Form_CargaDeTrabajo)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.radioButton_PartFijas.setFont(font)
        self.radioButton_PartFijas.setToolTip("")
        self.radioButton_PartFijas.setStyleSheet("background-image: url();\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0, 0);")
        self.radioButton_PartFijas.setObjectName("radioButton_PartFijas")
        self.horizontalLayout_6.addWidget(self.radioButton_PartFijas)
        self.pushButton_AnadirPart = QtWidgets.QPushButton(Form_CargaDeTrabajo)
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
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_AnadirPart.setFont(font)
        self.pushButton_AnadirPart.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_AnadirPart.setToolTip("")
        self.pushButton_AnadirPart.setStyleSheet("background-image: url();\n"
"background-color: rgb(0, 123, 255);\n"
"color: rgb(0, 0, 0);")
        self.pushButton_AnadirPart.setAutoDefault(False)
        self.pushButton_AnadirPart.setObjectName("pushButton_AnadirPart")
        self.horizontalLayout_6.addWidget(self.pushButton_AnadirPart, 0, QtCore.Qt.AlignLeft)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.radioButton_PartVariables = QtWidgets.QRadioButton(Form_CargaDeTrabajo)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.radioButton_PartVariables.setFont(font)
        self.radioButton_PartVariables.setToolTip("")
        self.radioButton_PartVariables.setStyleSheet("background-image: url();\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0, 0);")
        self.radioButton_PartVariables.setObjectName("radioButton_PartVariables")
        self.horizontalLayout_5.addWidget(self.radioButton_PartVariables)
        self.line_2 = QtWidgets.QFrame(Form_CargaDeTrabajo)
        self.line_2.setLineWidth(0)
        self.line_2.setMidLineWidth(10)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_5.addWidget(self.line_2)
        self.label_Tamano = QtWidgets.QLabel(Form_CargaDeTrabajo)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_Tamano.setFont(font)
        self.label_Tamano.setStyleSheet("background-image: url();\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0, 0);")
        self.label_Tamano.setObjectName("label_Tamano")
        self.horizontalLayout_5.addWidget(self.label_Tamano)
        self.spinBox_Tamano = QtWidgets.QSpinBox(Form_CargaDeTrabajo)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.spinBox_Tamano.setFont(font)
        self.spinBox_Tamano.setStyleSheet("background-image: url();\n"
"background-color: rgb(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.spinBox_Tamano.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_Tamano.setMaximum(9999)
        self.spinBox_Tamano.setSingleStep(10)
        self.spinBox_Tamano.setObjectName("spinBox_Tamano")
        self.horizontalLayout_5.addWidget(self.spinBox_Tamano)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.line = QtWidgets.QFrame(Form_CargaDeTrabajo)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setLineWidth(0)
        self.line.setMidLineWidth(10)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.verticalLayout_3.addWidget(self.line)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.radioButton_FirstFit = QtWidgets.QRadioButton(Form_CargaDeTrabajo)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.radioButton_FirstFit.setFont(font)
        self.radioButton_FirstFit.setToolTip("")
        self.radioButton_FirstFit.setStyleSheet("background-image: url();\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0, 0);")
        self.radioButton_FirstFit.setObjectName("radioButton_FirstFit")
        self.buttonGroup = QtWidgets.QButtonGroup(Form_CargaDeTrabajo)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.radioButton_FirstFit)
        self.horizontalLayout_4.addWidget(self.radioButton_FirstFit)
        self.radioButton_BestFit = QtWidgets.QRadioButton(Form_CargaDeTrabajo)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.radioButton_BestFit.setFont(font)
        self.radioButton_BestFit.setToolTip("")
        self.radioButton_BestFit.setStyleSheet("background-image: url();\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0, 0);")
        self.radioButton_BestFit.setObjectName("radioButton_BestFit")
        self.buttonGroup.addButton(self.radioButton_BestFit)
        self.horizontalLayout_4.addWidget(self.radioButton_BestFit)
        self.radioButton_WorstFit = QtWidgets.QRadioButton(Form_CargaDeTrabajo)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.radioButton_WorstFit.setFont(font)
        self.radioButton_WorstFit.setToolTip("")
        self.radioButton_WorstFit.setStyleSheet("background-image: url();\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0, 0);")
        self.radioButton_WorstFit.setObjectName("radioButton_WorstFit")
        self.buttonGroup.addButton(self.radioButton_WorstFit)
        self.horizontalLayout_4.addWidget(self.radioButton_WorstFit)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem4)
        self.graphicsView = QtWidgets.QGraphicsView(Form_CargaDeTrabajo)
        self.graphicsView.setStyleSheet("background-image: url();\n"
"background-color: rgb(0, 0, 0, 0);")
        self.graphicsView.setFrameShape(QtWidgets.QFrame.Box)
        self.graphicsView.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.graphicsView.setLineWidth(0)
        self.graphicsView.setMidLineWidth(4)
        self.graphicsView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.graphicsView.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout_3.addWidget(self.graphicsView)
        self.verticalLayout_3.setStretch(1, 1)
        self.verticalLayout_3.setStretch(2, 1)
        self.verticalLayout_3.setStretch(4, 1)
        self.verticalLayout_3.setStretch(6, 8)
        self.horizontalLayout_8.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_NProcesos = QtWidgets.QLabel(Form_CargaDeTrabajo)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_NProcesos.setFont(font)
        self.label_NProcesos.setStyleSheet("background-image: url();\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0, 0);")
        self.label_NProcesos.setObjectName("label_NProcesos")
        self.horizontalLayout.addWidget(self.label_NProcesos)
        self.spinBox_NProcesos = QtWidgets.QSpinBox(Form_CargaDeTrabajo)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.spinBox_NProcesos.setFont(font)
        self.spinBox_NProcesos.setStyleSheet("background-color: rgb(0, 0, 0, 0);\n"
"background-image: url();\n"
"color: rgb(255, 255, 255);")
        self.spinBox_NProcesos.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_NProcesos.setMaximum(999)
        self.spinBox_NProcesos.setSingleStep(1)
        self.spinBox_NProcesos.setObjectName("spinBox_NProcesos")
        self.horizontalLayout.addWidget(self.spinBox_NProcesos)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.tableWidget_Procesos = QtWidgets.QTableWidget(Form_CargaDeTrabajo)
        self.tableWidget_Procesos.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tableWidget_Procesos.setFont(font)
        self.tableWidget_Procesos.setAutoFillBackground(False)
        self.tableWidget_Procesos.setStyleSheet("background-image: url();\n"
"gridline-color: rgb(0,0, 0);\n"
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
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_Procesos.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_Procesos.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_Procesos.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_Procesos.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_Procesos.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_Procesos.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_Procesos.setHorizontalHeaderItem(6, item)
        self.tableWidget_Procesos.horizontalHeader().setVisible(True)
        self.tableWidget_Procesos.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_Procesos.horizontalHeader().setHighlightSections(True)
        self.tableWidget_Procesos.verticalHeader().setHighlightSections(True)
        self.verticalLayout_4.addWidget(self.tableWidget_Procesos)
        self.horizontalLayout_8.addLayout(self.verticalLayout_4)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, 35, -1, -1)
        self.verticalLayout.setSpacing(25)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_Algoritmo = QtWidgets.QGroupBox(Form_CargaDeTrabajo)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_Algoritmo.setFont(font)
        self.groupBox_Algoritmo.setStyleSheet("background-image: url();\n"
"color: rgb(0, 123, 255);\n"
"background-color: rgb(0, 0, 0, 0);")
        self.groupBox_Algoritmo.setObjectName("groupBox_Algoritmo")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_Algoritmo)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.radioButton_FCFS = QtWidgets.QRadioButton(self.groupBox_Algoritmo)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.radioButton_FCFS.setFont(font)
        self.radioButton_FCFS.setStyleSheet("background-image: url();\n"
"color: rgb(255, 255, 255);")
        self.radioButton_FCFS.setObjectName("radioButton_FCFS")
        self.verticalLayout_2.addWidget(self.radioButton_FCFS)
        self.radioButton_SJF = QtWidgets.QRadioButton(self.groupBox_Algoritmo)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.radioButton_SJF.setFont(font)
        self.radioButton_SJF.setStyleSheet("background-image: url();\n"
"color: rgb(255, 255, 255);")
        self.radioButton_SJF.setObjectName("radioButton_SJF")
        self.verticalLayout_2.addWidget(self.radioButton_SJF)
        self.radioButton_SRTF = QtWidgets.QRadioButton(self.groupBox_Algoritmo)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.radioButton_SRTF.setFont(font)
        self.radioButton_SRTF.setStyleSheet("background-image: url();\n"
"color: rgb(255, 255, 255);")
        self.radioButton_SRTF.setObjectName("radioButton_SRTF")
        self.verticalLayout_2.addWidget(self.radioButton_SRTF)
        self.radioButton_ROUNDROBIN = QtWidgets.QRadioButton(self.groupBox_Algoritmo)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.radioButton_ROUNDROBIN.setFont(font)
        self.radioButton_ROUNDROBIN.setStyleSheet("background-image: url();\n"
"color: rgb(255, 255, 255);")
        self.radioButton_ROUNDROBIN.setObjectName("radioButton_ROUNDROBIN")
        self.verticalLayout_2.addWidget(self.radioButton_ROUNDROBIN)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_Quantum = QtWidgets.QLabel(self.groupBox_Algoritmo)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_Quantum.setFont(font)
        self.label_Quantum.setStyleSheet("background-image: url();\n"
"color: rgb(255, 255, 255);")
        self.label_Quantum.setObjectName("label_Quantum")
        self.horizontalLayout_3.addWidget(self.label_Quantum)
        self.spinBox_Quantum = QtWidgets.QSpinBox(self.groupBox_Algoritmo)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.spinBox_Quantum.setFont(font)
        self.spinBox_Quantum.setStyleSheet("background-color: rgb(0, 0, 0, 0);\n"
"background-image: url();\n"
"color: rgb(255, 255, 255);")
        self.spinBox_Quantum.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_Quantum.setMaximum(99)
        self.spinBox_Quantum.setSingleStep(1)
        self.spinBox_Quantum.setObjectName("spinBox_Quantum")
        self.horizontalLayout_3.addWidget(self.spinBox_Quantum)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.horizontalLayout_3.setStretch(0, 2)
        self.horizontalLayout_3.setStretch(1, 2)
        self.horizontalLayout_3.setStretch(2, 4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout.addWidget(self.groupBox_Algoritmo)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem7)
        self.pushButton_Guardar = QtWidgets.QPushButton(Form_CargaDeTrabajo)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Guardar.setFont(font)
        self.pushButton_Guardar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_Guardar.setStyleSheet("background-image: url();\n"
"background-color: rgb(0, 123, 255);\n"
"color: rgb(0, 0, 0);")
        self.pushButton_Guardar.setObjectName("pushButton_Guardar")
        self.verticalLayout.addWidget(self.pushButton_Guardar)
        self.pushButton_Importar = QtWidgets.QPushButton(Form_CargaDeTrabajo)
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
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_Importar.setFont(font)
        self.pushButton_Importar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_Importar.setStyleSheet("background-image: url();\n"
"background-color: rgb(0, 123, 255);\n"
"color: rgb(0, 0, 0);")
        self.pushButton_Importar.setAutoDefault(False)
        self.pushButton_Importar.setObjectName("pushButton_Importar")
        self.verticalLayout.addWidget(self.pushButton_Importar)
        self.pushButton_Generar = QtWidgets.QPushButton(Form_CargaDeTrabajo)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Generar.setFont(font)
        self.pushButton_Generar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_Generar.setStyleSheet("background-image: url();\n"
"background-color: rgb(0, 123, 255);\n"
"color: rgb(0, 0, 0);")
        self.pushButton_Generar.setObjectName("pushButton_Generar")
        self.verticalLayout.addWidget(self.pushButton_Generar)
        self.verticalLayout.setStretch(0, 5)
        self.verticalLayout.setStretch(1, 6)
        self.horizontalLayout_8.addLayout(self.verticalLayout)
        self.horizontalLayout_8.setStretch(0, 2)
        self.horizontalLayout_8.setStretch(1, 8)
        self.horizontalLayout_8.setStretch(2, 2)
        self.verticalLayout_5.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem8)
        self.pushButton_CorrerSimulacion = QtWidgets.QPushButton(Form_CargaDeTrabajo)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_CorrerSimulacion.setFont(font)
        self.pushButton_CorrerSimulacion.setStyleSheet("background-image: url();")
        self.pushButton_CorrerSimulacion.setObjectName("pushButton_CorrerSimulacion")
        self.horizontalLayout_7.addWidget(self.pushButton_CorrerSimulacion)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem9)
        self.horizontalLayout_7.setStretch(0, 5)
        self.horizontalLayout_7.setStretch(1, 2)
        self.horizontalLayout_7.setStretch(2, 5)
        self.verticalLayout_5.addLayout(self.horizontalLayout_7)

        self.retranslateUi(Form_CargaDeTrabajo)
        QtCore.QMetaObject.connectSlotsByName(Form_CargaDeTrabajo)

    def retranslateUi(self, Form_CargaDeTrabajo):
        _translate = QtCore.QCoreApplication.translate
        Form_CargaDeTrabajo.setWindowTitle(_translate("Form_CargaDeTrabajo", "Simulador de Sistema Operativo"))
        self.label_CargaDeTrabajo.setText(_translate("Form_CargaDeTrabajo", "<html><head/><body><p>CARGA DE TRABAJO</p></body></html>"))
        self.radioButton_PartFijas.setText(_translate("Form_CargaDeTrabajo", "Particiones Fijas"))
        self.pushButton_AnadirPart.setText(_translate("Form_CargaDeTrabajo", "Añadir Partición"))
        self.radioButton_PartVariables.setText(_translate("Form_CargaDeTrabajo", "Particiones Variables"))
        self.label_Tamano.setText(_translate("Form_CargaDeTrabajo", "Tamaño(KB)"))
        self.radioButton_FirstFit.setText(_translate("Form_CargaDeTrabajo", "First Fit"))
        self.radioButton_BestFit.setText(_translate("Form_CargaDeTrabajo", "Best Fit"))
        self.radioButton_WorstFit.setText(_translate("Form_CargaDeTrabajo", "Worst Fit"))
        self.label_NProcesos.setText(_translate("Form_CargaDeTrabajo", "Nº de Procesos"))
        self.tableWidget_Procesos.setSortingEnabled(False)
        item = self.tableWidget_Procesos.horizontalHeaderItem(0)
        item.setText(_translate("Form_CargaDeTrabajo", "Tiempo de Arribo"))
        item = self.tableWidget_Procesos.horizontalHeaderItem(1)
        item.setText(_translate("Form_CargaDeTrabajo", "CPU"))
        item = self.tableWidget_Procesos.horizontalHeaderItem(2)
        item.setText(_translate("Form_CargaDeTrabajo", "Entrada"))
        item = self.tableWidget_Procesos.horizontalHeaderItem(3)
        item.setText(_translate("Form_CargaDeTrabajo", "CPU"))
        item = self.tableWidget_Procesos.horizontalHeaderItem(4)
        item.setText(_translate("Form_CargaDeTrabajo", "Salida"))
        item = self.tableWidget_Procesos.horizontalHeaderItem(5)
        item.setText(_translate("Form_CargaDeTrabajo", "CPU"))
        item = self.tableWidget_Procesos.horizontalHeaderItem(6)
        item.setText(_translate("Form_CargaDeTrabajo", "Memoria"))
        self.groupBox_Algoritmo.setTitle(_translate("Form_CargaDeTrabajo", "Algoritmo"))
        self.radioButton_FCFS.setToolTip(_translate("Form_CargaDeTrabajo", "First Come, First Served"))
        self.radioButton_FCFS.setText(_translate("Form_CargaDeTrabajo", "FCFS"))
        self.radioButton_SJF.setToolTip(_translate("Form_CargaDeTrabajo", "Shortest Job First"))
        self.radioButton_SJF.setText(_translate("Form_CargaDeTrabajo", "SJF"))
        self.radioButton_SRTF.setToolTip(_translate("Form_CargaDeTrabajo", "Short Remaining Time First"))
        self.radioButton_SRTF.setText(_translate("Form_CargaDeTrabajo", "SRTF"))
        self.radioButton_ROUNDROBIN.setText(_translate("Form_CargaDeTrabajo", "ROUND ROBIN"))
        self.label_Quantum.setText(_translate("Form_CargaDeTrabajo", "Quantum"))
        self.pushButton_Guardar.setToolTip(_translate("Form_CargaDeTrabajo", "<html><head/><body><p>Guardar la carga de trabajo actual</p></body></html>"))
        self.pushButton_Guardar.setText(_translate("Form_CargaDeTrabajo", "Guardar"))
        self.pushButton_Importar.setToolTip(_translate("Form_CargaDeTrabajo", "<html><head/><body><p>Importar carga de trabajo</p></body></html>"))
        self.pushButton_Importar.setText(_translate("Form_CargaDeTrabajo", "Importar"))
        self.pushButton_Generar.setToolTip(_translate("Form_CargaDeTrabajo", "<html><head/><body><p>Generar una carga de trabajo aleatoria</p></body></html>"))
        self.pushButton_Generar.setText(_translate("Form_CargaDeTrabajo", "Generar"))
        self.pushButton_CorrerSimulacion.setText(_translate("Form_CargaDeTrabajo", "Correr simulación"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form_CargaDeTrabajo = QtWidgets.QWidget()
    ui = Ui_Form_CargaDeTrabajo()
    ui.setupUi(Form_CargaDeTrabajo)
    Form_CargaDeTrabajo.show()
    sys.exit(app.exec_())

