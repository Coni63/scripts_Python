# noinspection
#@PydevCodeAnalysisIgnore
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '..\UI\interface.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 781, 541))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.todolist = QtGui.QWidget()
        self.todolist.setObjectName(_fromUtf8("todolist"))
        self.Save = QtGui.QPushButton(self.todolist)
        self.Save.setGeometry(QtCore.QRect(634, 470, 111, 23))
        self.Save.setObjectName(_fromUtf8("Save"))
        self.tableWidget = QtGui.QTableWidget(self.todolist)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 751, 451))
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setRowCount(0)
        self.tabWidget.addTab(self.todolist, _fromUtf8(""))
        self.Tasks = QtGui.QWidget()
        self.Tasks.setObjectName(_fromUtf8("Tasks"))
        self.tableWidget_2 = QtGui.QTableWidget(self.Tasks)
        self.tableWidget_2.setGeometry(QtCore.QRect(10, 10, 751, 451))
        self.tableWidget_2.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.tableWidget_2.setColumnCount(4)
        self.tableWidget_2.setObjectName(_fromUtf8("tableWidget_2"))
        self.tableWidget_2.setRowCount(0)
        self.Add_task = QtGui.QPushButton(self.Tasks)
        self.Add_task.setGeometry(QtCore.QRect(594, 472, 121, 31))
        self.Add_task.setObjectName(_fromUtf8("Add_task"))
        self.tabWidget.addTab(self.Tasks, _fromUtf8(""))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
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
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionOption = QtGui.QAction(MainWindow)
        self.actionOption.setObjectName(_fromUtf8("actionOption"))
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionLoad)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionOption)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.Save.setText(_translate("MainWindow", "Save and Update", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.todolist), _translate("MainWindow", "To do List", None))
        self.Add_task.setText(_translate("MainWindow", "Add task", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Tasks), _translate("MainWindow", "Tasks", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.actionNew.setText(_translate("MainWindow", "New", None))
        self.actionLoad.setText(_translate("MainWindow", "Load", None))
        self.actionSave.setText(_translate("MainWindow", "Save", None))
        self.actionSave_As.setText(_translate("MainWindow", "Save As...", None))
        self.actionQuit.setText(_translate("MainWindow", "Quit", None))
        self.actionOption.setText(_translate("MainWindow", "Option", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

