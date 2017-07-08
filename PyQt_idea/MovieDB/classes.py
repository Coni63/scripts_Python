from PyQt4 import QtGui, QtCore
import sys
import os
import PyGuiModeles.mainModele as Interface
import PyGuiModeles.settingModele as Properties

class Properties_window(Properties.Ui_Form):
    def __init__(self, Widget):
        super(Properties_window, self).__init__()
        self.widget_window = Widget
        Properties.Ui_Form.setupUi(self, Widget)
        Widget.setWindowTitle("Properties")


class Window(Interface.Ui_MainWindow):
    def __init__(self, MainWindow):
        super(Window, self).__init__()
        self.main_window = MainWindow
        Interface.Ui_MainWindow.setupUi(self, MainWindow)
        MainWindow.setWindowTitle('Movie Database')
        self.add_connectivity()

    def add_connectivity(self):
        self.menubar.hovered.connect(self.handleMenuHovered)
        self.actionNew.triggered.connect(self.new_db)
        self.actionLoad.triggered.connect(self.open_db)
        self.actionSave.triggered.connect(self.save_db)
        self.actionSave_As.triggered.connect(self.save_db_as)
        self.actionProperties.triggered.connect(self.properties)
        self.actionQuit.triggered.connect(QtGui.qApp.quit)

    def handleMenuHovered(self, action):
        QtGui.QToolTip.showText(QtGui.QCursor.pos(), action.toolTip(), self.menubar, self.menubar.actionGeometry(action))

    def new_db(self):
        self.statusbar.showMessage("new", 3000)

    def open_db(self):
        self.statusbar.showMessage("open", 3000)

    def save_db(self):
        self.statusbar.showMessage("save", 3000)

    def save_db_as(self):
        self.statusbar.showMessage("save as", 3000)

    def properties(self):
        self.statusbar.showMessage("properties", 3000)
        self.prop_Dialog = QtGui.QDialog()
        ui2 = Properties_window(self.prop_Dialog)
        self.prop_Dialog.show()