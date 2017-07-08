from PyQt4 import QtGui, QtCore
from functions import *
from Classes import Account, New_Simulation
import matplotlib.pyplot as plt
import pickle
import PyGuiModeles.mainModele as interface
import PyGuiModeles.about_meModele as aboutme
import json

class AboutMe(QtGui.QWidget, aboutme.Ui_Form):
    def __init__(self, dialog):
        self.dialog = dialog
        aboutme.Ui_Form.setupUi(self, self.dialog)
        self.dialog.show()


class IHM(QtGui.QMainWindow, interface.Ui_MainWindow):
    def __init__(self, mainwindow, app):
        super(IHM, self).__init__()
        self.MainWindow = mainwindow
        self.application = app
        self.selected_save = None
        interface.Ui_MainWindow.setupUi(self, mainwindow)
        self.account = Account()
        self.output_filename = None
        self.add_actions()
        self.MainWindow.show()
        self.print_status("Ready !")

    def add_actions(self):
        self.pushButton.clicked.connect(self.calculate)
        #self.pushButton_2.clicked.connect(self.plot2)
        self.actionNew.triggered.connect(self.new_save)
        self.actionSave.triggered.connect(self.save)
        self.actionSave_As.triggered.connect(self.save_as)
        self.actionLoad.triggered.connect(self.load)
        self.actionAbout_Me.triggered.connect(self.dialog_about_me)
        self.actionQuit.triggered.connect(self.quit)
        self.comboBox_setup.currentIndexChanged.connect(self.update_combobox)
        self.comboBox_event.currentIndexChanged.connect(self.show_result)
        self.actionImport_2.triggered.connect(self.import_from_site)
        for child in self.MainWindow.findChildren(QtGui.QLineEdit):
            if child.objectName()[:3] != "qt_":  # to remove spinboxes
                validator = QtGui.QRegExpValidator(QtCore.QRegExp("\d+"))
                child.setValidator(validator)
                child.editingFinished.connect(self.update_account)
                child.textChanged.connect(self.update_tooltip)
        self.qte_diams.valueChanged.connect(self.update_account)

    def import_from_site(self):
        self.print_status("Import from site ...")
        text, ok = QtGui.QInputDialog.getText(self, 'Paste your Raw Data', 'Paste your raw data here:')
        if ok:
            self.raw_data = json.loads(str(text))
            for each in self.raw_data["resources"]:
                if each["resourceName"]== "oil":
                    self.account.pet = int(each["amount"])
                    self.qte_pet.setText(str(self.account.pet))
                if each["resourceName"] == "cerosin":
                    self.account.kero = int(each["amount"])
                    self.qte_kero.setText(str(self.account.kero))
                if each["resourceName"] == "diesel":
                    self.account.diesel = int(each["amount"])
                    self.qte_diesel.setText(str(self.account.diesel))
                if each["resourceName"] == "ammunition":
                    self.account.muni = int(each["amount"])
                    self.qte_muni.setText(str(self.account.muni))
                if each["resourceName"] == "money":
                    self.account.money = int(each["amount"])
                    self.qte_money.setText(str(self.account.money))
                if each["resourceName"] == "gold":
                    self.account.gold = int(each["amount"])
                    self.qte_gold.setText(str(self.account.gold))
                if each["resourceName"] == "diamonds":
                    self.account.diams = int(each["amount"])
                    self.qte_diams.setValue(int(self.account.diams))

    def print_status(self, txt, time=3000):
        self.statusbar.showMessage(txt, time)

    def calculate(self):
        self.print_status("Calculating values ...")
        self.account.account_value()
        self.out_account_value.setText("{:,}".format(self.account.acc))
        self.out_account_value.setToolTip(convert(self.account.acc))
        step = 100 // (self.max_diams.value() - self.min_diams.value())
        self.simu = []
        self.comboBox_setup.clear()
        self.comboBox_setup.addItem("Select...")
        for i in range(self.min_diams.value(), self.max_diams.value() + 1):
            simulate = New_Simulation(self.account, self)
            simulate.run(i)
            self.comboBox_setup.addItem("%s diams" % i)
            self.simu.append(simulate)
            self.progressBar.setValue(self.progressBar.value() + step)
        self.progressBar.setValue(100)
        self.print_status("Ready !")

    def update_combobox(self):
        self.comboBox_event.clear()
        index = self.comboBox_setup.currentIndex()
        if index != 0:
            for each in self.simu[index-1].result_loop:
                self.comboBox_event.addItem(str(each))

    def show_result(self):
        index = self.comboBox_setup.currentIndex()
        event = self.comboBox_event.currentIndex()
        self.out_acc.setText(str(self.simu[index-1].result_acc[event]))
        self.out_acc.setToolTip(convert(int(self.simu[index-1].result_acc[event])))
        self.out_diams.setText(str(self.simu[index-1].result_diams[event]))
        self.out_diams.setToolTip(convert(int(self.simu[index - 1].result_diams[event])))
        self.out_gain.setText(str(self.simu[index-1].result_gain[event]))
        self.out_gain.setToolTip(convert(int(self.simu[index - 1].result_gain[event])))
        self.out_kero.setText(str(self.simu[index-1].result_kero[event]))
        self.out_kero.setToolTip(convert(int(self.simu[index - 1].result_kero[event])))
        self.out_money.setText(str(self.simu[index-1].result_money[event]))
        self.out_money.setToolTip(convert(int(self.simu[index - 1].result_money[event])))

    def update_account(self):
        sender = self.MainWindow.sender()
        if sender != self.qte_diams and sender.text() != "":
            value = int(sender.text())
            if sender == self.qte_diams:
                self.account.diams = value
            elif sender == self.qte_kero:
                self.account.kero = value
            elif sender == self.qte_diesel:
                self.account.diesel = value
            elif sender == self.qte_pet:
                self.account.pet = value
            elif sender == self.qte_gold:
                self.account.gold = value
            elif sender == self.qte_muni:
                self.account.muni = value
            elif sender == self.qte_money:
                self.account.money = value
        elif sender == self.qte_diams:
            self.account.diams = sender.value()
        self.account.account_value()

    def update_tooltip(self):
        sender = self.MainWindow.sender()
        if sender.text() != "":
            cresus_style = convert(int(sender.text()))
            sender.setToolTip(cresus_style)

    def new_save(self):
        self.print_status("Create a new file")
        self.account.reset_account()
        dico = self.account.return_as_object()
        self.update_line_edit()
        self.output_filename = QtGui.QFileDialog.getSaveFileName(self.MainWindow, "Select Directory", "", "Saves (*.p)")
        pickle.dump(dico, open(self.output_filename, "wb"))
        self.print_status("Saved")

    def save(self):
        if self.output_filename is None:
            self.print_status("Saving ...")
            dico = self.account.return_as_object()
            pickle.dump(dico, open(self.output_filename, "wb"))
            self.print_status("Saved")
        else:
            self.save_as()

    def save_as(self):
        self.print_status("Saving ...")
        self.output_filename = QtGui.QFileDialog.getSaveFileName(self.MainWindow, "Select Directory", "", "Saves (*.p)")
        dico = self.account.return_as_object()
        pickle.dump(dico, open(self.output_filename, "wb"))
        self.print_status("Saved")

    def load(self, file):
        self.print_status("Loading ...")
        self.output_filename = QtGui.QFileDialog.getOpenFileName(self.MainWindow, "Open File", "", "Saves (*.p)")
        dico = pickle.load(open(self.output_filename, "rb"))
        self.account.update(dico)
        self.update_line_edit()
        self.print_status("Loaded")

    def dialog_about_me(self):
        self.New_Dialog = QtGui.QDialog()
        Ui2 = AboutMe(self.New_Dialog)

    def quit(self):
        result = QtGui.QMessageBox.question(self,
                                            "Confirm Exit...",
                                            "Are you sure you want to exit ?",
                                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)

        if result == QtGui.QMessageBox.Yes:
            QtCore.QCoreApplication.quit()

    def update_line_edit(self):
        self.qte_diesel.setText(str(self.account.diesel))
        self.qte_money.setText(str(self.account.money))
        self.qte_muni.setText(str(self.account.muni))
        self.qte_gold.setText(str(self.account.gold))
        self.qte_pet.setText(str(self.account.pet))
        self.qte_kero.setText(str(self.account.kero))
        self.qte_diams.setValue(self.account.diams)

    def plot(self):
        if hasattr(self.account, 'setup'):
            # for i in range(self.min_diams.value(), self.max_diams.value()+1) :
            i = 1
            abcisse = self.account.setup[i].keys()
            arr_money = [self.account.setup[i][k]["money"] for k in abcisse]
            arr_acc = [self.account.setup[i][k]["acc"] for k in abcisse]
            arr_kero = [self.account.setup[i][k]["kero"] for k in abcisse]
            arr_gain = [self.account.setup[i][k]["gain"] for k in abcisse]
            print(len(abcisse), len(arr_money), len(arr_acc), len(arr_kero), len(arr_gain))

            f, axarr = plt.subplots(4, sharex=True)
            axarr[0].plot(abcisse, arr_money)
            axarr[0].set_title('Sharing X axis')
            axarr[1].scatter(abcisse, arr_acc)
            axarr[2].scatter(abcisse, arr_kero)
            axarr[3].scatter(abcisse, arr_gain)
        else:
            self.print_status("You have to calculate first")

    def plot2(self):
        if hasattr(self, 'simu'):
            for sim in self.simu:
                x = sim.result_loop
                f, axarr = plt.subplots(4, sharex=True)
                axarr[0].plot(x, sim.result_pet)
                axarr[0].set_title('Sharing X axis')
                axarr[1].scatter(x, sim.result_kero)
                axarr[2].scatter(x, sim.result_acc)
                axarr[3].scatter(x, sim.result_gain)
                plt.show()
        else:
            print("nok")