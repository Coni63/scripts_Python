from PyQt4 import QtGui, QtCore
import sys
import os
import pickle
import PyGuiModeles.interfaceModele as Interface
import PyGuiModeles.Form_taskModele as Form

class Task:
    def __init__(self, title):
        self.description = title
        self.last_date = None
        self.first_date = None
        self.repetition = None
        self.current_save = None
        self.task_list = []

class Task_Form(QtGui.QWidget, Form.Ui_Form):
    def __init__(self):
        super(Task_Form, self).__init__()
        self.setupUi(self)
        self.widget_window = self
        self.add_connectivity2()

    def add_connectivity2(self):
        self.buttonBox.button(QtGui.QDialogButtonBox.Apply).setText('Create Task')
        self.buttonBox.button(QtGui.QDialogButtonBox.Cancel).setText('Cancel')
        self.buttonBox.button(QtGui.QDialogButtonBox.Apply).clicked.connect(self.create_task)
        self.buttonBox.button(QtGui.QDialogButtonBox.Cancel).clicked.connect(self.cancel)
        self.testbtn.clicked.connect(self.create_task)

    def create_task(self):
        self.buttonBox.button(QtGui.QDialogButtonBox.Apply).setText('dhse')
        print("tic")

    def cancel(self):
        self.buttonBox.button(QtGui.QDialogButtonBox.Cancel).setText('gdsh')
        print("fin")


class Window(QtGui.QMainWindow, Interface.Ui_MainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setupUi(self)
        self.MainWindow = self
        self.add_connectivity()

    def add_connectivity(self):
        self.menubar.hovered.connect(self.handleMenuHovered)
        self.actionNew.triggered.connect(self.new_save)
        self.actionLoad.triggered.connect(self.load)
        self.actionSave.triggered.connect(self.save)
        self.actionSave_As.triggered.connect(self.save_as) #save_db_as
        #self.actionProperties.triggered.connect(self.properties)
        self.actionQuit.triggered.connect(QtGui.qApp.quit)
        self.Save.clicked.connect(self.add_task)
        self.Add_task.clicked.connect(self.open_Form)

    def add_task(self):
        new_task = Task()
        self.task_list.append(new_task)
        nextIndex = self.tableWidget.rowCount()
        self.tableWidget.insertRow(nextIndex)
        self.tableWidget.setItem(nextIndex, 0, QtGui.QTableWidgetItem("Hello %s"%(nextIndex)))
        self.tableWidget.setItem(nextIndex, 1, QtGui.QTableWidgetItem("Hello"))
        self.tableWidget.setItem(nextIndex, 2, QtGui.QTableWidgetItem("Hello"))
        btn = QtGui.QPushButton("test")
        self.tableWidget.setCellWidget(nextIndex, 3, btn)
        btn.clicked.connect(self.set_task_done)

    def set_task_done(self):
        button = self.main_window.sender()
        index = self.tableWidget.indexAt(button.pos())
        currentRow = index.row()
        mydata = str(self.tableWidget.item(currentRow, 1).text())
        print(currentRow, mydata)
        self.statusbar.showMessage("BOMM", 3000)

    def handleMenuHovered(self, action):
        QtGui.QToolTip.showText(QtGui.QCursor.pos(), action.toolTip(), self.menubar, self.menubar.actionGeometry(action))

    def new_save(self):
        self.statusbar.showMessage("Create a new file", 3000)
        self.task_list = {}
        self.save_content = {"id" : "task_manager", "data" : self.task_list}
        self.output_filename = QtGui.QFileDialog.getSaveFileName(self.MainWindow, "Select Directory", "", "Saves (*.p)")
        try:
            pickle.dump(self.save_content, open(self.output_filename, "wb"))
            self.statusbar.showMessage("Saved", 3000)
        except:
            self.statusbar.showMessage("Error", 3000)

    def save(self):
        if not self.output_filename is None:
            self.statusbar.showMessage("Saving ...", 3000)
            self.save_content = {"id": "task_manager", "data": self.task_list}
            try:
                pickle.dump(self.save_content, open(self.output_filename, "wb"))
                self.statusbar.showMessage("Saved", 3000)
            except:
                self.statusbar.showMessage("Error", 3000)
        else:
            self.save_as()

    def save_as(self):
        self.statusbar.showMessage("Saving ...", 3000)
        self.output_filename = QtGui.QFileDialog.getSaveFileName(self.MainWindow, "Select Directory", "", "Saves (*.p)")
        self.save_content = {"id": "task_manager", "data": self.task_list}
        try:
            pickle.dump(self.save_content, open(self.output_filename, "wb"))
            self.statusbar.showMessage("Saved", 3000)
        except:
            self.statusbar.showMessage("Error", 3000)

    def load(self):
        self.statusbar.showMessage("Loading ...", 3000)
        self.output_filename = QtGui.QFileDialog.getOpenFileName(self.MainWindow, "Open File", "", "Saves (*.p)")
        content = pickle.load(open(self.output_filename, "rb"))
        if not content.get("id", None) is None:
            print(content.get("data", "Error"))
        else:
            self.statusbar.showMessage("Incorrect File", 3000)

    def open_Form(self):
        self.statusbar.showMessage("New Task", 3000)
        self.form_Dialog = Task_Form()
        self.form_Dialog.show()