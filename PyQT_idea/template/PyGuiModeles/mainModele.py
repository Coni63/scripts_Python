# noinspection
#@PydevCodeAnalysisIgnore
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '..\UI\main.ui'
#
# Created: Wed Apr 20 20:33:18 2016
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
        MainWindow.resize(961, 731)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 961, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuMenu = QtGui.QMenu(self.menubar)
        self.menuMenu.setObjectName(_fromUtf8("menuMenu"))
        self.menuAbout = QtGui.QMenu(self.menubar)
        self.menuAbout.setObjectName(_fromUtf8("menuAbout"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtGui.QAction(MainWindow)
        self.actionNew.setObjectName(_fromUtf8("actionNew"))
        self.actionLoad = QtGui.QAction(MainWindow)
        self.actionLoad.setObjectName(_fromUtf8("actionLoad"))
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionSave_As = QtGui.QAction(MainWindow)
        self.actionSave_As.setObjectName(_fromUtf8("actionSave_As"))
        self.actionProperties = QtGui.QAction(MainWindow)
        self.actionProperties.setObjectName(_fromUtf8("actionProperties"))
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.menuMenu.addAction(self.actionNew)
        self.menuMenu.addAction(self.actionLoad)
        self.menuMenu.addAction(self.actionSave)
        self.menuMenu.addAction(self.actionSave_As)
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionProperties)
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionQuit)
        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu", None))
        self.menuAbout.setTitle(_translate("MainWindow", "About", None))
        self.actionNew.setText(_translate("MainWindow", "New", None))
        self.actionNew.setToolTip(_translate("MainWindow", "Create a new database", None))
        self.actionLoad.setText(_translate("MainWindow", "Load", None))
        self.actionLoad.setToolTip(_translate("MainWindow", "Load an existing database", None))
        self.actionSave.setText(_translate("MainWindow", "Save", None))
        self.actionSave.setToolTip(_translate("MainWindow", "Save this database", None))
        self.actionSave_As.setText(_translate("MainWindow", "Save As ...", None))
        self.actionSave_As.setToolTip(_translate("MainWindow", "Save As this database", None))
        self.actionProperties.setText(_translate("MainWindow", "Properties", None))
        self.actionProperties.setToolTip(_translate("MainWindow", "See Properties", None))
        self.actionQuit.setText(_translate("MainWindow", "Quit", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

