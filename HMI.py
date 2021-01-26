# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HMI.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from opcua import Client
from opcua import ua
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QInputDialog, QLineEdit, QWidget
#from funcionalidades import *
#from mock_funcionalidades import Funcionalidades as func
#from variables import Variables

from POU import POU

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.desplegable = QtWidgets.QComboBox(self.centralwidget)
        self.desplegable.setGeometry(QtCore.QRect(150, 160, 291, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.desplegable.setFont(font)
        self.desplegable.setObjectName("desplegable")
        self.desplegable.addItem("")
        self.desplegable.addItem("")
        self.desplegable.addItem("")
        self.desplegable.addItem("")
        self.texto = QtWidgets.QLabel(self.centralwidget)
        self.texto.setGeometry(QtCore.QRect(150, 100, 311, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.texto.setFont(font)
        self.texto.setObjectName("texto")
        self.botonEncender = QtWidgets.QPushButton(self.centralwidget)
        self.botonEncender.setGeometry(QtCore.QRect(540, 100, 171, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.botonEncender.setFont(font)
        self.botonEncender.setObjectName("botonEncender")
        self.botonReset = QtWidgets.QPushButton(self.centralwidget)
        self.botonReset.setGeometry(QtCore.QRect(540, 170, 171, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.botonReset.setFont(font)
        self.botonReset.setObjectName("botonReset")
        self.botonApagar = QtWidgets.QPushButton(self.centralwidget)
        self.botonApagar.setGeometry(QtCore.QRect(540, 310, 171, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.botonApagar.setFont(font)
        self.botonApagar.setObjectName("botonApagar")
        self.botonPosicion = QtWidgets.QPushButton(self.centralwidget)
        self.botonPosicion.setGeometry(QtCore.QRect(90, 260, 171, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.botonPosicion.setFont(font)
        self.botonPosicion.setObjectName("botonPosicion")
        self.botonVelocidad = QtWidgets.QPushButton(self.centralwidget)
        self.botonVelocidad.setGeometry(QtCore.QRect(310, 260, 171, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.botonVelocidad.setFont(font)
        self.botonVelocidad.setObjectName("botonVelocidad")
        self.botonParar = QtWidgets.QPushButton(self.centralwidget)
        self.botonParar.setGeometry(QtCore.QRect(540, 240, 171, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.botonParar.setFont(font)
        self.botonParar.setObjectName("botonParar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.botonParar.clicked.connect(self.func_parar)
        #self.botonEncender.clicked.connect(self.func_encender)
        self.botonEncender.clicked.connect(POU.encender())
        self.botonApagar.clicked.connect(self.func_apagar)
        self.botonVelocidad.clicked.connect(self.func_leeVel)
        self.botonPosicion.clicked.connect(self.func_leePos)
        self.botonReset.clicked.connect(self.func_resetear)
        self.desplegable.currentIndexChanged.connect(self.popup_desplegable)


    def popup_desplegable(self):
        index = self.desplegable.currentIndex()
        if index == 0:
            self.solicita_vel()
            func.movimiento_cte()
        elif index == 1:
            self.solicita_Nvueltas()
            func.movimiento_relativo()
        elif index == 2:
            self.solicita_posicion()
            func.movimiento_absoluto()
    """
    TODO:
    def solicita_vel(self):
        text, ok = QtWidgets.QInputDialog.getText(self, 'Input Dialog', 'Enter text:')
        if ok:
            le.setText(str(text))
    """
        
    def func_parar(self):
        POU.parar()

    def func_encender(self):
        POU.encender()

    def func_apagar(self):
        POU.apagar()

    def func_leePos(self):
        func.posicion_actual()

    def func_leeVel(self):
        func.velocidad_actual()

    def func_resetear(self):
        func.resetear()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.desplegable.setItemText(0, _translate("MainWindow", "Mover a velocidad constante"))
        self.desplegable.setItemText(1, _translate("MainWindow", "Mover N vueltas"))
        self.desplegable.setItemText(2, _translate("MainWindow", "Mover a posición"))
        self.texto.setText(_translate("MainWindow", "Seleccione modo de funcionamiento:"))
        self.botonEncender.setText(_translate("MainWindow", "Encender motor"))
        self.botonReset.setText(_translate("MainWindow", "Resetear"))
        self.botonApagar.setText(_translate("MainWindow", "Apagar motor"))
        self.botonPosicion.setText(_translate("MainWindow", "Consultar posición"))
        self.botonVelocidad.setText(_translate("MainWindow", "Consultar velocidad"))
        self.botonParar.setText(_translate("MainWindow", "Parar motor"))

    def show_popup(self, index):
        msg = QMessageBox()
        msg.setWindowTitle("Tutorial on PyQt5")
        msg.setText("This is the main text")
        msg.setIcon(QMessageBox.Question)
        msg.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
        msg.setInformativeText("Informative text here")
        QMainWindow.line = QLineEdit

        msg.setDetailedText("details")

        msg.buttonClicked.connect(self.popup_button)
 
        x = msg.exec_()

    def popup_button(self, i):
        print(i.text())

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
