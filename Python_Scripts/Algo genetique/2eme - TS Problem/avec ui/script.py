from PyQt5 import QtGui, QtCore, QtWidgets
import sys
import os

import PyGuiModeles.mainModele as Interface


class MainWindow(Interface.Ui_MainWindow):
    def __init__(self, Main_Window):
        super(MainWindow, self).__init__()
        Interface.Ui_MainWindow.setupUi(self, Main_Window)
        self.main_window = Main_Window
        Main_Window.setWindowTitle("Traveling Salesman Problem with GE")
        self.start.clicked.connect(self.test)
        self.stop.clicked.connect(self.test)



    def test(self):
        print("teest")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Main_Windows = QtWidgets.QMainWindow()
    ui = MainWindow(Main_Windows)
    Main_Windows.show()
    sys.exit(app.exec_())