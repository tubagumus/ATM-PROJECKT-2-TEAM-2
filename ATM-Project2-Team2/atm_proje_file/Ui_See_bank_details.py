# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\yunus\OneDrive\Desktop\pythonogreniyorum\ATM-Project\atmproject - Version-2\atm_proje_file\See_bank_details.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import os

class Ui_MainWindow3(object):
         def setupUi(self, MainWindow):
            MainWindow.setObjectName("MainWindow")
            MainWindow.resize(592, 400)
            self.centralwidget = QtWidgets.QWidget(MainWindow)
            self.centralwidget.setObjectName("centralwidget")
            self.balance_label = QtWidgets.QLabel(self.centralwidget)
            self.balance_label.setGeometry(QtCore.QRect(20, 90, 191, 31))
            font = QtGui.QFont()
            font.setFamily("MS Shell Dlg 2")
            font.setPointSize(10)
            font.setBold(False)
            font.setItalic(False)
            font.setWeight(50)
            self.balance_label.setFont(font)
            self.balance_label.setStyleSheet("font: 14pt \".AppleSystemUIFont\";\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(254, 204, 102);")
            self.balance_label.setAlignment(QtCore.Qt.AlignCenter)
            self.balance_label.setObjectName("balance_label")
            self.balance_label_2 = QtWidgets.QLabel(self.centralwidget)
            self.balance_label_2.setGeometry(QtCore.QRect(20, 140, 191, 31))
            font = QtGui.QFont()
            font.setFamily("MS Shell Dlg 2")
            font.setPointSize(10)
            font.setBold(False)
            font.setItalic(False)
            font.setWeight(50)
            self.balance_label_2.setFont(font)
            self.balance_label_2.setStyleSheet("font: 14pt \".AppleSystemUIFont\";\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(254, 204, 102);")
            self.balance_label_2.setAlignment(QtCore.Qt.AlignCenter)
            self.balance_label_2.setObjectName("balance_label_2")
            self.balance_label_3 = QtWidgets.QLabel(self.centralwidget)
            self.balance_label_3.setGeometry(QtCore.QRect(20, 190, 191, 31))
            font = QtGui.QFont()
            font.setFamily("MS Shell Dlg 2")
            font.setPointSize(10)
            font.setBold(False)
            font.setItalic(False)
            font.setWeight(50)
            self.balance_label_3.setFont(font)
            self.balance_label_3.setStyleSheet("font: 14pt \".AppleSystemUIFont\";\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(254, 204, 102);")
            self.balance_label_3.setAlignment(QtCore.Qt.AlignCenter)
            self.balance_label_3.setObjectName("balance_label_3")
            self.balance_label_4 = QtWidgets.QLabel(self.centralwidget)
            self.balance_label_4.setGeometry(QtCore.QRect(20, 240, 191, 31))
            font = QtGui.QFont()
            font.setFamily("MS Shell Dlg 2")
            font.setPointSize(10)
            font.setBold(False)
            font.setItalic(False)
            font.setWeight(50)
            self.balance_label_4.setFont(font)
            self.balance_label_4.setStyleSheet("font: 14pt \".AppleSystemUIFont\";\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(254, 204, 102);")
            self.balance_label_4.setAlignment(QtCore.Qt.AlignCenter)
            self.balance_label_4.setObjectName("balance_label_4")
            self.balance_label_5 = QtWidgets.QLabel(self.centralwidget)
            self.balance_label_5.setGeometry(QtCore.QRect(20, 290, 191, 31))
            font = QtGui.QFont()
            font.setFamily("MS Shell Dlg 2")
            font.setPointSize(10)
            font.setBold(False)
            font.setItalic(False)
            font.setWeight(50)
            self.balance_label_5.setFont(font)
            self.balance_label_5.setStyleSheet("font: 14pt \".AppleSystemUIFont\";\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(254, 204, 102);")
            self.balance_label_5.setAlignment(QtCore.Qt.AlignCenter)
            self.balance_label_5.setObjectName("balance_label_5")
            self.check_button_2 = QtWidgets.QPushButton(self.centralwidget)
            self.check_button_2.setGeometry(QtCore.QRect(430, 55, 111, 71))
            font = QtGui.QFont()
            font.setPointSize(14)
            self.check_button_2.setFont(font)
            self.check_button_2.setStyleSheet("background-color: rgb(254, 204, 102);")
            self.check_button_2.setObjectName("check_button_2")
            self.insert_edit = QtWidgets.QLineEdit(self.centralwidget)
            self.insert_edit.setGeometry(QtCore.QRect(240, 90, 161, 31))
            self.insert_edit.setStyleSheet("background-color: rgb(204, 204, 204);")
            self.insert_edit.setText("")
            self.insert_edit.setObjectName("insert_edit")
            self.insert_edit_2 = QtWidgets.QLineEdit(self.centralwidget)
            self.insert_edit_2.setGeometry(QtCore.QRect(240, 140, 161, 31))
            self.insert_edit_2.setStyleSheet("background-color: rgb(204, 204, 204);")
            self.insert_edit_2.setText("")
            self.insert_edit_2.setObjectName("insert_edit_2")
            self.insert_edit_3 = QtWidgets.QLineEdit(self.centralwidget)
            self.insert_edit_3.setGeometry(QtCore.QRect(240, 190, 161, 31))
            self.insert_edit_3.setStyleSheet("background-color: rgb(204, 204, 204);")
            self.insert_edit_3.setText("")
            self.insert_edit_3.setObjectName("insert_edit_3")
            self.insert_edit_4 = QtWidgets.QLineEdit(self.centralwidget)
            self.insert_edit_4.setGeometry(QtCore.QRect(240, 240, 161, 31))
            self.insert_edit_4.setStyleSheet("background-color: rgb(204, 204, 204);")
            self.insert_edit_4.setText("")
            self.insert_edit_4.setObjectName("insert_edit_4")
            self.insert_edit_5 = QtWidgets.QLineEdit(self.centralwidget)
            self.insert_edit_5.setGeometry(QtCore.QRect(240, 290, 161, 31))
            self.insert_edit_5.setStyleSheet("background-color: rgb(204, 204, 204);")
            self.insert_edit_5.setText("")
            self.insert_edit_5.setObjectName("insert_edit_5")
            self.return2_button = QtWidgets.QPushButton(self.centralwidget)
            self.return2_button.setGeometry(QtCore.QRect(430, 240, 111, 71))
            self.return2_button.setStyleSheet("background-color: rgb(254, 204, 102);")
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("c:\\Users\\yunus\\OneDrive\\Desktop\\pythonogreniyorum\\ATM-Project\\atmproject - Version-2\\atm_proje_file\\../pythonogreniyorum/ATM-Project/atmproject/gümüst/icons/reply.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            icon.addPixmap(QtGui.QPixmap("c:\\Users\\yunus\\OneDrive\\Desktop\\pythonogreniyorum\\ATM-Project\\atmproject - Version-2\\atm_proje_file\\../pythonogreniyorum/ATM-Project/gümüst/icons/icns/reply.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
            self.return2_button.setIcon(icon)
            self.return2_button.setIconSize(QtCore.QSize(50, 50))
            self.return2_button.setObjectName("return2_button")
        
            self.balance_label_id = QtWidgets.QLabel(self.centralwidget)
            self.balance_label_id.setGeometry(QtCore.QRect(20, 40, 191, 31))
            font = QtGui.QFont()
            font.setFamily("MS Shell Dlg 2")
            font.setPointSize(10)
            font.setBold(False)
            font.setItalic(False)
            font.setWeight(50)
            self.balance_label_id.setFont(font)
            self.balance_label_id.setStyleSheet("font: 14pt \".AppleSystemUIFont\";\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(254, 204, 102);")
            self.balance_label_id.setAlignment(QtCore.Qt.AlignCenter)
            self.balance_label_id.setObjectName("balance_label_id")
            self.label = QtWidgets.QLabel(self.centralwidget)
            self.label.setGeometry(QtCore.QRect(250, 50, 141, 21))
            self.label.setText("")
            self.label.setObjectName("label")
            self.ID_box = QtWidgets.QComboBox(self.centralwidget)
            self.ID_box.setGeometry(QtCore.QRect(240, 30, 161, 51))
            self.ID_box.setCurrentText("")
            self.ID_box.setIconSize(QtCore.QSize(16, 16))
            self.ID_box.setObjectName("ID_box")
            MainWindow.setCentralWidget(self.centralwidget)
            self.menubar = QtWidgets.QMenuBar(MainWindow)
            self.menubar.setGeometry(QtCore.QRect(0, 0, 592, 21))
            self.menubar.setObjectName("menubar")
            MainWindow.setMenuBar(self.menubar)
            self.statusbar = QtWidgets.QStatusBar(MainWindow)
            self.statusbar.setObjectName("statusbar")
            MainWindow.setStatusBar(self.statusbar)

            self.retranslateUi(MainWindow)
            QtCore.QMetaObject.connectSlotsByName(MainWindow)

         def retranslateUi(self, MainWindow):
             _translate = QtCore.QCoreApplication.translate
             MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
             self.balance_label.setText(_translate("MainWindow", "Name"))
             self.balance_label_2.setText(_translate("MainWindow", "Surname"))
             self.balance_label_3.setText(_translate("MainWindow", "E-mail"))
             self.balance_label_4.setText(_translate("MainWindow", "Tax number"))
             self.balance_label_5.setText(_translate("MainWindow", "Password"))
             self.check_button_2.setText(_translate("MainWindow", "Update"))
             self.return2_button.setText(_translate("MainWindow", "RETURN MENU"))
             self.balance_label_id.setText(_translate("MainWindow", "CUSTOMER ID"))
