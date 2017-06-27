from PyQt4 import QtGui, QtCore
import sys
import os
import subprocess
import shutil
import time

import PyGuiModeles.interfaceModele as Interface

class Window(Interface.Ui_MainWindow):
    def __init__(self, MainWindow):
        super(Window, self).__init__()
        self.MainWindow = MainWindow
        Interface.Ui_MainWindow.setupUi(self, MainWindow)
        self.add_connectivity()
        self.check_version()

    def add_connectivity(self):
        self.Btn_Compile.clicked.connect(self.compile)
        self.Btn_Input.clicked.connect(self.browse_script)
        self.Btn_Output.clicked.connect(self.save_location)
        self.Btn_Install.clicked.connect(self.install)
        self.Btn_Update.clicked.connect(self.update)

    def compile(self):
        with open('temp.py', 'w') as f:
            f.write('from cx_Freeze import setup, Executable\n\n')  # python will convert \n to os.linesep
            f.write('setup(\n')
            f.write('\tname="%s",\n' % self.Inp_Name.text())
            f.write('\tversion="%s",\n' % self.Inp_Version.text())
            f.write('\tdescription="%s",\n' % self.Inp_Description.text())
            f.write('\texecutables=[Executable("%s")],\n' % self.Line_Input.text())
            f.write(')')

        self.statusBar.showMessage("Setup file created ... Running Script", 3000)

        location = os.path.abspath("temp.py")
        address = os.path.dirname(location)
        origWD = os.getcwd()  # remember our original working directory

        os.chdir(address)
        p = subprocess.Popen("python %s build" % location)
        os.chdir(origWD)

        p.wait()

        self.statusBar.showMessage("Moving folder", 3000)
        if os.path.isdir(self.Line_Output.text()):
            shutil.move(os.path.join(address, "build"), self.Line_Output.text())
            self.statusBar.showMessage("Finish", 3000)

    def browse_script(self):
        self.input_filename = QtGui.QFileDialog.getOpenFileName(
            self.MainWindow, "Open File", "", "Script Python (*.py)")
        self.Line_Input.setText(str(self.input_filename))
        self.statusBar.showMessage("Script imported", 3000)

    def save_location(self):
        self.output_filename = QtGui.QFileDialog.getExistingDirectory(self.MainWindow, "Select Directory")
        self.Line_Output.setText(str(self.output_filename))
        self.statusBar.showMessage("Folder saved", 3000)

    def install(self):
        p=subprocess.Popen("pip install cx_Freeze", stdout=subprocess.PIPE, stdin=subprocess.PIPE)
        p.wait()
        self.statusBar.showMessage(str(p.stdout.readline()), 3000)
        sys.stdout.flush()

    def update(self):
        p=subprocess.Popen("pip install cx_Freeze --upgrade", stdout=subprocess.PIPE, stdin=subprocess.PIPE)
        p.wait()
        self.statusBar.showMessage(str(p.stdout.readline()), 3000)
        sys.stdout.flush()

    def check_version(self):
        try:
            stream = [x.split("==") for x in os.popen("pip freeze").read().split()]
            for each in stream:
                if each[0].lower() == "cx-freeze":
                    self.version.setText("Current Version : " + each[1])
                    self.statusBar.showMessage("Cx_Freeze's version found", 3000)
                    return
            self.statusBar.showMessage("No version found", 3000)
        except:
            self.statusBar.showMessage("Error :(", 3000)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    Main_Windows = QtGui.QMainWindow()
    ui = Window(Main_Windows)
    Main_Windows.setWindowTitle("Python Builder")
    Main_Windows.show()
    sys.exit(app.exec_())