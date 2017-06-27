from PyQt4 import QtGui, QtCore
import sys
import sqlite3
import pickle
import classes
import functions

if __name__ == "__main__":
    SETUP = functions.load_init()
    app = QtGui.QApplication(sys.argv)
    Main_Windows = QtGui.QMainWindow()
    ui = classes.Window(Main_Windows)
    Main_Windows.show()
    sys.exit(app.exec_())