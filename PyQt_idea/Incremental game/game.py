from PyQt4 import QtGui, QtCore
import Class
import sys

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    #Main_Windows = QtGui.QMainWindow()
    Main_Windows = Class.Window()
    Main_Windows.show()
    sys.exit(app.exec_())