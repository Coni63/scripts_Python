from PyQt4 import QtGui, QtCore
import sys
import os

import Controller.functions as func
import Controller.classes as classes

if __name__ == "__main__":
    SETUP = func.load_init()
    app = QtGui.QApplication(sys.argv)
    Main_Windows = QtGui.QMainWindow()
    ui = classes.Window(Main_Windows, SETUP)
    Main_Windows.show()
    sys.exit(app.exec_())