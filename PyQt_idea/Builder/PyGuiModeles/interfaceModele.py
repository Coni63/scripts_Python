# noinspection
#@PydevCodeAnalysisIgnore
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '..\UI\interface.ui'
#
# Created: Mon Apr 18 17:32:47 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(367, 485)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 191, 151))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.Btn_Install = QtGui.QPushButton(self.groupBox)
        self.Btn_Install.setGeometry(QtCore.QRect(20, 20, 151, 23))
        self.Btn_Install.setObjectName(_fromUtf8("Btn_Install"))
        self.Btn_Update = QtGui.QPushButton(self.groupBox)
        self.Btn_Update.setGeometry(QtCore.QRect(20, 50, 151, 23))
        self.Btn_Update.setObjectName(_fromUtf8("Btn_Update"))
        self.version = QtGui.QLabel(self.groupBox)
        self.version.setGeometry(QtCore.QRect(30, 100, 141, 20))
        self.version.setObjectName(_fromUtf8("version"))
        self.Line_Input = QtGui.QLineEdit(self.centralwidget)
        self.Line_Input.setGeometry(QtCore.QRect(160, 190, 181, 20))
        self.Line_Input.setObjectName(_fromUtf8("Line_Input"))
        self.Line_Output = QtGui.QLineEdit(self.centralwidget)
        self.Line_Output.setGeometry(QtCore.QRect(160, 220, 181, 20))
        self.Line_Output.setObjectName(_fromUtf8("Line_Output"))
        self.Btn_Compile = QtGui.QCommandLinkButton(self.centralwidget)
        self.Btn_Compile.setGeometry(QtCore.QRect(120, 350, 101, 41))
        self.Btn_Compile.setObjectName(_fromUtf8("Btn_Compile"))
        self.Btn_Input = QtGui.QPushButton(self.centralwidget)
        self.Btn_Input.setGeometry(QtCore.QRect(34, 190, 111, 23))
        self.Btn_Input.setObjectName(_fromUtf8("Btn_Input"))
        self.Btn_Output = QtGui.QPushButton(self.centralwidget)
        self.Btn_Output.setGeometry(QtCore.QRect(34, 220, 111, 23))
        self.Btn_Output.setObjectName(_fromUtf8("Btn_Output"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 260, 46, 13))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 290, 46, 13))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 320, 61, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.Inp_Name = QtGui.QLineEdit(self.centralwidget)
        self.Inp_Name.setGeometry(QtCore.QRect(160, 260, 113, 20))
        self.Inp_Name.setInputMask(_fromUtf8(""))
        self.Inp_Name.setText(_fromUtf8(""))
        self.Inp_Name.setObjectName(_fromUtf8("Inp_Name"))
        self.Inp_Version = QtGui.QLineEdit(self.centralwidget)
        self.Inp_Version.setGeometry(QtCore.QRect(160, 290, 113, 20))
        self.Inp_Version.setToolTip(_fromUtf8(""))
        self.Inp_Version.setObjectName(_fromUtf8("Inp_Version"))
        self.Inp_Description = QtGui.QLineEdit(self.centralwidget)
        self.Inp_Description.setGeometry(QtCore.QRect(160, 320, 113, 20))
        self.Inp_Description.setText(_fromUtf8(""))
        self.Inp_Description.setObjectName(_fromUtf8("Inp_Description"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 367, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.groupBox.setTitle(_translate("MainWindow", "Pip", None))
        self.Btn_Install.setText(_translate("MainWindow", "Install CxFreeze", None))
        self.Btn_Update.setText(_translate("MainWindow", "Check for updates", None))
        self.version.setText(_translate("MainWindow", "Current version : None", None))
        self.Btn_Compile.setText(_translate("MainWindow", "Compile", None))
        self.Btn_Input.setText(_translate("MainWindow", "Input (script py)", None))
        self.Btn_Output.setText(_translate("MainWindow", "Output (fichier exe)", None))
        self.label.setText(_translate("MainWindow", "Nom:", None))
        self.label_2.setText(_translate("MainWindow", "Version:", None))
        self.label_3.setText(_translate("MainWindow", "Description :", None))
        self.Inp_Name.setPlaceholderText(_translate("MainWindow", "Name you program", None))
        self.Inp_Version.setText(_translate("MainWindow", "1.0", None))
        self.Inp_Version.setPlaceholderText(_translate("MainWindow", "set your version", None))
        self.Inp_Description.setPlaceholderText(_translate("MainWindow", "Short description", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

