# noinspection
#@PydevCodeAnalysisIgnore
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '..\UI\interface.ui'
#
# Created: Sun Apr 17 14:02:12 2016
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
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.Inp_random = QtGui.QPushButton(self.centralwidget)
        self.Inp_random.setGeometry(QtCore.QRect(30, 120, 101, 23))
        self.Inp_random.setObjectName(_fromUtf8("Inp_random"))
        self.Console = QtGui.QPlainTextEdit(self.centralwidget)
        self.Console.setGeometry(QtCore.QRect(420, 10, 361, 541))
        self.Console.setObjectName(_fromUtf8("Console"))
        self.Inp_Submit = QtGui.QPushButton(self.centralwidget)
        self.Inp_Submit.setGeometry(QtCore.QRect(140, 120, 111, 23))
        self.Inp_Submit.setObjectName(_fromUtf8("Inp_Submit"))
        self.Palette = QtGui.QPlainTextEdit(self.centralwidget)
        self.Palette.setEnabled(True)
        self.Palette.setGeometry(QtCore.QRect(250, 30, 60, 60))
        self.Palette.setReadOnly(True)
        self.Palette.setObjectName(_fromUtf8("Palette"))
        self.formLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 30, 211, 81))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setMargin(0)
        self.formLayout.setSpacing(6)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.formLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.Slider_R = QtGui.QSlider(self.formLayoutWidget)
        self.Slider_R.setMaximum(255)
        self.Slider_R.setOrientation(QtCore.Qt.Horizontal)
        self.Slider_R.setObjectName(_fromUtf8("Slider_R"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.Slider_R)
        self.label_2 = QtGui.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.Slider_G = QtGui.QSlider(self.formLayoutWidget)
        self.Slider_G.setMaximum(255)
        self.Slider_G.setOrientation(QtCore.Qt.Horizontal)
        self.Slider_G.setObjectName(_fromUtf8("Slider_G"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.Slider_G)
        self.label_3 = QtGui.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.Slider_B = QtGui.QSlider(self.formLayoutWidget)
        self.Slider_B.setMaximum(255)
        self.Slider_B.setOrientation(QtCore.Qt.Horizontal)
        self.Slider_B.setObjectName(_fromUtf8("Slider_B"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.Slider_B)
        self.horizontalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(9, 300, 281, 230))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.Inp_color_R = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.Inp_color_R.setObjectName(_fromUtf8("Inp_color_R"))
        self.verticalLayout_2.addWidget(self.Inp_color_R)
        self.Inp_color_O = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.Inp_color_O.setObjectName(_fromUtf8("Inp_color_O"))
        self.verticalLayout_2.addWidget(self.Inp_color_O)
        self.Inp_color_Y = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.Inp_color_Y.setObjectName(_fromUtf8("Inp_color_Y"))
        self.verticalLayout_2.addWidget(self.Inp_color_Y)
        self.Inp_color_G = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.Inp_color_G.setObjectName(_fromUtf8("Inp_color_G"))
        self.verticalLayout_2.addWidget(self.Inp_color_G)
        self.Inp_color_C = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.Inp_color_C.setObjectName(_fromUtf8("Inp_color_C"))
        self.verticalLayout_2.addWidget(self.Inp_color_C)
        self.Inp_color_B = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.Inp_color_B.setObjectName(_fromUtf8("Inp_color_B"))
        self.verticalLayout_2.addWidget(self.Inp_color_B)
        self.Inp_color_V = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.Inp_color_V.setObjectName(_fromUtf8("Inp_color_V"))
        self.verticalLayout_2.addWidget(self.Inp_color_V)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.Inp_Light = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.Inp_Light.setObjectName(_fromUtf8("Inp_Light"))
        self.verticalLayout.addWidget(self.Inp_Light)
        self.Inp_Normal = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.Inp_Normal.setObjectName(_fromUtf8("Inp_Normal"))
        self.verticalLayout.addWidget(self.Inp_Normal)
        self.Inp_Dark = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.Inp_Dark.setObjectName(_fromUtf8("Inp_Dark"))
        self.verticalLayout.addWidget(self.Inp_Dark)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.Inp_Learn = QtGui.QCommandLinkButton(self.centralwidget)
        self.Inp_Learn.setGeometry(QtCore.QRect(310, 390, 81, 41))
        self.Inp_Learn.setObjectName(_fromUtf8("Inp_Learn"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(170, 270, 46, 13))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.see_more = QtGui.QPushButton(self.centralwidget)
        self.see_more.setGeometry(QtCore.QRect(90, 180, 75, 23))
        self.see_more.setObjectName(_fromUtf8("see_more"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.Inp_random.setText(_translate("MainWindow", "Set random color", None))
        self.Inp_Submit.setText(_translate("MainWindow", "Guess", None))
        self.label.setText(_translate("MainWindow", "R", None))
        self.label_2.setText(_translate("MainWindow", "G", None))
        self.label_3.setText(_translate("MainWindow", "B", None))
        self.Inp_color_R.setText(_translate("MainWindow", "Red", None))
        self.Inp_color_O.setText(_translate("MainWindow", "Orange", None))
        self.Inp_color_Y.setText(_translate("MainWindow", "Yellow", None))
        self.Inp_color_G.setText(_translate("MainWindow", "Green", None))
        self.Inp_color_C.setText(_translate("MainWindow", "Cyan", None))
        self.Inp_color_B.setText(_translate("MainWindow", "Blue", None))
        self.Inp_color_V.setText(_translate("MainWindow", "Violet", None))
        self.Inp_Light.setText(_translate("MainWindow", "Light", None))
        self.Inp_Normal.setText(_translate("MainWindow", "Normal", None))
        self.Inp_Dark.setText(_translate("MainWindow", "Dark", None))
        self.Inp_Learn.setText(_translate("MainWindow", "Teach", None))
        self.label_4.setText(_translate("MainWindow", "Teaching", None))
        self.see_more.setText(_translate("MainWindow", "PushButton", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

