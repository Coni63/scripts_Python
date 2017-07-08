# noinspection
#@PydevCodeAnalysisIgnore
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '..\UI\test.ui'
#
# Created: Wed Apr 13 19:02:14 2016
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
        MainWindow.resize(582, 388)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.btn_start = QtGui.QPushButton(self.centralwidget)
        self.btn_start.setGeometry(QtCore.QRect(20, 10, 75, 23))
        self.btn_start.setObjectName(_fromUtf8("btn_start"))
        self.btn_load = QtGui.QPushButton(self.centralwidget)
        self.btn_load.setGeometry(QtCore.QRect(20, 40, 75, 23))
        self.btn_load.setObjectName(_fromUtf8("btn_load"))
        self.btn_save = QtGui.QPushButton(self.centralwidget)
        self.btn_save.setGeometry(QtCore.QRect(20, 70, 75, 23))
        self.btn_save.setObjectName(_fromUtf8("btn_save"))
        self.console = QtGui.QPlainTextEdit(self.centralwidget)
        self.console.setGeometry(QtCore.QRect(333, 10, 231, 341))
        self.console.setObjectName(_fromUtf8("console"))
        self.spin_interval = QtGui.QSpinBox(self.centralwidget)
        self.spin_interval.setGeometry(QtCore.QRect(190, 25, 42, 22))
        self.spin_interval.setMinimum(5)
        self.spin_interval.setProperty("value", 15)
        self.spin_interval.setObjectName(_fromUtf8("spin_interval"))
        self.spin_duration = QtGui.QSpinBox(self.centralwidget)
        self.spin_duration.setGeometry(QtCore.QRect(190, 55, 42, 22))
        self.spin_duration.setMinimum(10)
        self.spin_duration.setMaximum(30)
        self.spin_duration.setProperty("value", 20)
        self.spin_duration.setObjectName(_fromUtf8("spin_duration"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 30, 71, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(120, 60, 61, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.txt_last_re = QtGui.QLineEdit(self.centralwidget)
        self.txt_last_re.setGeometry(QtCore.QRect(140, 110, 113, 20))
        self.txt_last_re.setObjectName(_fromUtf8("txt_last_re"))
        self.txt_last_rc = QtGui.QLineEdit(self.centralwidget)
        self.txt_last_rc.setGeometry(QtCore.QRect(140, 140, 113, 20))
        self.txt_last_rc.setObjectName(_fromUtf8("txt_last_rc"))
        self.txt_last_graphe = QtGui.QLineEdit(self.centralwidget)
        self.txt_last_graphe.setGeometry(QtCore.QRect(140, 170, 113, 20))
        self.txt_last_graphe.setObjectName(_fromUtf8("txt_last_graphe"))
        self.txt_last_clean = QtGui.QLineEdit(self.centralwidget)
        self.txt_last_clean.setGeometry(QtCore.QRect(140, 200, 113, 20))
        self.txt_last_clean.setObjectName(_fromUtf8("txt_last_clean"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 110, 81, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 140, 81, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 170, 101, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(30, 200, 91, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 582, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.btn_start.setText(_translate("MainWindow", "Start", None))
        self.btn_load.setText(_translate("MainWindow", "Load", None))
        self.btn_save.setText(_translate("MainWindow", "Save", None))
        self.label.setText(_translate("MainWindow", "interval (min)", None))
        self.label_2.setText(_translate("MainWindow", "duration (s)", None))
        self.label_3.setText(_translate("MainWindow", "Last update RE", None))
        self.label_4.setText(_translate("MainWindow", "Last update RC", None))
        self.label_5.setText(_translate("MainWindow", "Last update graphes", None))
        self.label_6.setText(_translate("MainWindow", "Last cleanup", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

