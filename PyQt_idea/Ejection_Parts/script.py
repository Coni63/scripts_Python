from PyQt4 import QtGui, QtCore
import xml.etree.ElementTree as ET

import sys

import PyGuiModeles.interfaceModele as interface

class my_IHM(QtGui.QMainWindow, interface.Ui_MainWindow):
    def __init__(self, mainwindow, app):
        super(my_IHM, self).__init__()
        self.MainWindow = mainwindow
        self.application = app
        interface.Ui_MainWindow.setupUi(self, mainwindow)
        self.add_actions()
        self.MainWindow.show()
        self.print_status("Ready !")
        self.read_xml()
        self.update_machine_type()

    def add_actions(self):
        self.input_machine_type.currentIndexChanged.connect(self.update_generation)

    def print_status(self, txt, time=3000):
        self.statusbar.showMessage(txt, time)

    def read_xml(self):
        self.tree = ET.parse('test.xml')
        self.root = self.tree.getroot()

    def update_machine_type(self):
        self.input_machine_type.clear()
        for child in self.root:
            self.input_machine_type.addItem(child.attrib["name"])

    def update_generation(self):
        self.input_machine_generation.clear()
        print("[name=\"" + self.input_machine_type.currentText() + "\"]")
        for child in self.root.findall(".//*[@name=\"" + self.input_machine_type.currentText() + "\"]/neighbor"):
             self.input_machine_generation.addItem(child.attrib["name"])

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    Main_Window = QtGui.QMainWindow()
    Ui = my_IHM(Main_Window, app)
    Main_Window.setWindowTitle('Ejection Parts')
    #Main_Window.setWindowIcon(QtGui.QIcon('icon.png'))
    sys.exit(app.exec_())