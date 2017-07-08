from PyQt4 import QtGui, QtCore
import sys
import urllib.request
import time
import pickle
#import pymysql.cursors
#import threading
#import multiprocessing


import PyGuiModeles.testModele as Interface

url1 = "http://dorercbdd.esy.es/checkrc.php"
url2 = "http://dorercbdd.esy.es/checkre.php"
url3 = "http://dorercbdd.esy.es/clean.php"
url4 = "http://dorercbdd.esy.es/graph.php"

INTERVAL_RE_RC = 30
INTERVAL_GRAPH = 86400
INTERVAL_CLEAN = 30

class A_Dallas():
    def __init__(self):
        self.last_clean = None
        self.last_update_graph = None
        self.last_update_re = None
        self.last_update_rc = None
        self.interval = 15*60 # 15 min en secondes
        self.duration = 20 #20s de script duration
        self.is_started = False

    def run_script(self):
        if self.last_clean == None or time.time()-self.last_clean > INTERVAL_CLEAN:
            ui.print_console("Starting Cleanup")
            # launch cleanup
            self.open_connection(url3)
            self.last_clean = time.time()
            ui.txt_last_clean.setText(time.ctime(self.last_clean))
        if self.last_update_graph == None or time.time()-self.last_update_graph > INTERVAL_GRAPH:
            ui.print_console("Updating Graphes")
            # launch cleanup
            self.open_connection(url4)
            self.last_update_graph = time.time()
            ui.txt_last_graphe.setText(time.ctime(self.last_update_graph))
        if self.last_update_rc  == None or time.time()-self.last_update_rc > INTERVAL_RE_RC:
            ui.print_console("Starting Research of RC")
            #launch check rc
            self.open_connection(url1)
            self.last_update_rc = time.time()
            ui.txt_last_rc.setText(time.ctime(self.last_update_rc))
        if self.last_update_re == None or time.time()-self.last_update_re > INTERVAL_RE_RC:
            ui.print_console("Starting Research of RE")
            #launch check re
            self.open_connection(url2)
            self.last_update_re = time.time()
            ui.txt_last_re.setText(time.ctime(self.last_update_re))

    def open_connection(self, url):
        print("opening", url, "@", time.ctime())
        self.filehandler = urllib.request.urlopen(url, timeout=30)
        print(self.filehandler.getcode())
        #self.filehandler.open(url)

    def exporter(self):
        wrapper = { "last_clean":self.last_clean,
                    "last_update_graph":self.last_update_graph,
                    "last_update_re":self.last_update_re,
                    "last_update_rc":self.last_update_rc,
                    "interval":self.interval,
                    "duration":self.duration,
                    "is_started":self.is_started
                }
        return wrapper

    def importer(self, wrapper):
        print(wrapper)
        self.last_clean = wrapper["last_clean"]
        self.last_update_graph = wrapper["last_update_graph"]
        self.last_update_re = wrapper["last_update_re"]
        self.last_update_rc = wrapper["last_update_rc"]
        self.interval = wrapper["interval"]
        self.duration = wrapper["duration"]
        self.is_started = wrapper["is_started"]
        ui.spin_duration.setValue(self.duration)
        ui.spin_interval.setValue(self.interval/60)
        if self.last_update_re != None : ui.txt_last_re.setText(time.ctime(self.last_update_re))
        if self.last_update_rc != None : ui.txt_last_rc.setText(time.ctime(self.last_update_rc))
        if self.last_clean != None : ui.txt_last_clean.setText(time.ctime(self.last_clean))
        if self.last_update_graph != None : ui.txt_last_graphe.setText(time.ctime(self.last_update_graph))

class Mon_IHM(Interface.Ui_MainWindow):
    def __init__(self, MainWindow, parent=None):
        self.MainWindow = MainWindow
        Interface.Ui_MainWindow.setupUi(self, MainWindow)
        self.data = A_Dallas()
        self.add_connections()
        self.is_loaded = False

    def add_connections(self):
        self.btn_start.clicked.connect(self.start)
        self.btn_load.clicked.connect(self.load_values)
        self.btn_save.clicked.connect(self.save_values)
        #QtCore.QObject.connect(self.btn_start, QtCore.SIGNAL('clicked()'), self.start)
        #QtCore.QObject.connect(self.btn_load, QtCore.SIGNAL('clicked()'), self.load_values)
        #QtCore.QObject.connect(self.btn_save, QtCore.SIGNAL('clicked()'), self.save_values)
        self.spin_interval.valueChanged.connect(self.update_values)
        self.spin_duration.valueChanged.connect(self.update_values)
        #QtCore.QObject.connect(self.spin_interval, QtCore.SIGNAL('valueChanged()'), self.update_values)
        #QtCore.QObject.connect(self.spin_duration, QtCore.SIGNAL('valueChanged()'), self.test)

    def update_values(self):
        spinbox = self.MainWindow.sender()
        if spinbox is self.spin_interval:
            self.data.interval=60*spinbox.value()
        elif spinbox is self.spin_duration:
            self.data.duration=spinbox.value()

    def load_values(self):
        self.print_console("Loading save.p ...")
        try:
            setup = pickle.load( open( "save.p", "rb" ))
            self.print_console("Datas Loaded !")
            self.print_console("Parsing data...")
            self.data.importer(setup)
            self.print_console("Datas parsed !")
        except:
            self.print_console("Error, no file found :(")
        self.is_loaded = True

    def save_values(self):
        self.print_console("Saving setup in save.p")
        setup = self.data.exporter()
        pickle.dump(setup, open( "save.p", "wb" ))
        self.print_console("Datas Saved")

    def start(self):
        if self.is_loaded:
            if self.btn_start.text() == "Start":
                self.btn_start.setText("Stop")
                self.data.is_started = True
                self.print_console("Go")
                self.data.run_script()
            else:
                self.btn_start.setText("Start")
                self.data.is_started = False
                self.save_values()
        else:
            self.load_values()
            self.start()

    def print_console(self, text):
        self.console.appendPlainText('>> '+text)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Mon_IHM(MainWindow)
    MainWindow.setWindowTitle('DO auto updates')
    MainWindow.show()
    sys.exit(app.exec_())