from PyQt4 import QtGui, QtCore
import sys
from Classes_UI import IHM

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    Main_Window = QtGui.QMainWindow()
    Ui = IHM(Main_Window, app)
    Main_Window.setWindowTitle('DO boost')
    Main_Window.setWindowIcon(QtGui.QIcon('icon.png'))
    sys.exit(app.exec_())

