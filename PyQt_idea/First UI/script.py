from PyQt4 import QtGui, QtCore
import sys
import pickle
import random

import PyGuiModeles.interfaceModele as Interface
import PyGuiModeles.interface2Modele as Interface2

class MyPopup(Interface2.Ui_Dialog):
    def __init__(self, Ui_Dialog):
        super(MyPopup, self).__init__()
        self.Ui_Dialog = Ui_Dialog
        Interface2.Ui_Dialog.setupUi(self, Ui_Dialog)

class Mon_IHM(Interface.Ui_MainWindow):
    def __init__(self, MainWindow):
        super(Mon_IHM, self).__init__()
        self.MainWindow = MainWindow
        Interface.Ui_MainWindow.setupUi(self, MainWindow)
        self.value_R, self.value_G, self.value_B = 0, 0, 0
        self.list_color = [self.Inp_color_B, self.Inp_color_C, self.Inp_color_G, self.Inp_color_O, self.Inp_color_R, self.Inp_color_V, self.Inp_color_Y]
        self.list_force = [self.Inp_Dark, self.Inp_Normal, self.Inp_Light]
        self.Palette.setStyleSheet("QPlainTextEdit{ background-color: rgb(%s, %s, %s) }" % (self.value_R, self.value_G, self.value_B))
        self.setup_connections()

    def setup_connections(self):
        self.Slider_R.valueChanged.connect(self.show_color)
        self.Slider_G.valueChanged.connect(self.show_color)
        self.Slider_B.valueChanged.connect(self.show_color)
        self.Inp_random.clicked.connect(self.set_random_color)
        self.Inp_Submit.clicked.connect(self.Guess)
        self.Inp_Learn.clicked.connect(self.Learn)
        for each in self.list_color:
            each.setCheckable(True)
            each.clicked.connect(self.select_result)
        for each in self.list_force:
            each.setCheckable(True)
            each.clicked.connect(self.select_result)
        self.see_more.clicked.connect(self.doit)

    def doit(self):
        print("Opening a new popup window...")
        Dialog = QtGui.QDialog(self.MainWindow)
        ui2 = MyPopup(Dialog)
        ui2.setupUi(Dialog)
        Dialog.show()
        #self.w = MyPopup(self.MainWindow)
        #self.w.show()

    def show_color(self):
        slider = self.MainWindow.sender()
        if slider == self.Slider_R:
            self.value_R = self.Slider_R.value()
        elif slider == self.Slider_G:
            self.value_G = self.Slider_G.value()
        else:
            self.value_B = self.Slider_B.value()
        #print(self.value_R,"-",self.value_G,"-",self.value_B)
        self.Palette.setStyleSheet("QPlainTextEdit{ background-color: rgb(%s, %s, %s) }" % (self.value_R, self.value_G, self.value_B))

    def set_random_color(self):
        try:
            self.Slider_R.disconnect()
            self.Slider_G.disconnect()
            self.Slider_B.disconnect()
        except Exception:
            pass
        self.value_R = random.randint(0,255)
        self.value_G = random.randint(0,255)
        self.value_B = random.randint(0,255)
        print(self.value_R, "-", self.value_G, "-", self.value_B)
        self.Slider_R.setValue(self.value_R)
        self.Slider_G.setValue(self.value_G)
        self.Slider_B.setValue(self.value_B)
        self.Palette.setStyleSheet("QPlainTextEdit{ background-color: rgb(%s, %s, %s) }" % (self.value_R, self.value_G, self.value_B))
        self.Slider_R.valueChanged.connect(self.show_color)
        self.Slider_G.valueChanged.connect(self.show_color)
        self.Slider_B.valueChanged.connect(self.show_color)

    def select_result(self):
        button = self.MainWindow.sender()
        if button in self.list_color:
            for each_button in self.list_color:
                each_button.setChecked(False)
            button.setChecked(True)
        elif button in self.list_force:
            for each_button in self.list_force:
                each_button.setChecked(False)
            button.setChecked(True)

    def Guess(self):
        print("Je sais pas Blyat")

    def Learn(self):
        print("Ok j'apprends")

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Mon_IHM(MainWindow)
    MainWindow.setWindowTitle('Learn Color with Neural Network')
    MainWindow.show()
    sys.exit(app.exec_())