# noinspection
#@PydevCodeAnalysisIgnore
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '..\UI\main.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(950, 533)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 40, 160, 131))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.points = QtWidgets.QSpinBox(self.formLayoutWidget)
        self.points.setMinimum(5)
        self.points.setMaximum(72)
        self.points.setProperty("value", 25)
        self.points.setObjectName("points")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.points)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.population_size = QtWidgets.QSpinBox(self.formLayoutWidget)
        self.population_size.setMinimum(1)
        self.population_size.setMaximum(1000)
        self.population_size.setProperty("value", 100)
        self.population_size.setObjectName("population_size")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.population_size)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.mutation_ratio = QtWidgets.QSpinBox(self.formLayoutWidget)
        self.mutation_ratio.setMaximum(100)
        self.mutation_ratio.setProperty("value", 5)
        self.mutation_ratio.setObjectName("mutation_ratio")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.mutation_ratio)
        self.crossover_ratio = QtWidgets.QSpinBox(self.formLayoutWidget)
        self.crossover_ratio.setMaximum(100)
        self.crossover_ratio.setProperty("value", 70)
        self.crossover_ratio.setObjectName("crossover_ratio")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.crossover_ratio)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.selection_ratio = QtWidgets.QSpinBox(self.formLayoutWidget)
        self.selection_ratio.setMaximum(100)
        self.selection_ratio.setProperty("value", 50)
        self.selection_ratio.setObjectName("selection_ratio")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.selection_ratio)
        self.label_11 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_11.setObjectName("label_11")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.openGLWidget = QtWidgets.QOpenGLWidget(self.centralwidget)
        self.openGLWidget.setGeometry(QtCore.QRect(290, 30, 401, 321))
        self.openGLWidget.setObjectName("openGLWidget")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 10, 151, 21))
        self.label_5.setTextFormat(QtCore.Qt.AutoText)
        self.label_5.setObjectName("label_5")
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(10, 200, 251, 121))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_6.setObjectName("label_6")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_7.setObjectName("label_7")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.label_8 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_8.setObjectName("label_8")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.label_9 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_9.setObjectName("label_9")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.best_dist = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.best_dist.setText("")
        self.best_dist.setObjectName("best_dist")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.best_dist)
        self.nb_tries = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.nb_tries.setMidLineWidth(-3)
        self.nb_tries.setObjectName("nb_tries")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.nb_tries)
        self.total_path = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.total_path.setText("")
        self.total_path.setObjectName("total_path")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.total_path)
        self.gen_best_path = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.gen_best_path.setText("")
        self.gen_best_path.setObjectName("gen_best_path")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.gen_best_path)
        self.label_16 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_16.setObjectName("label_16")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_16)
        self.current_gen = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.current_gen.setObjectName("current_gen")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.current_gen)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(10, 170, 151, 21))
        self.label_10.setTextFormat(QtCore.Qt.AutoText)
        self.label_10.setObjectName("label_10")
        self.start = QtWidgets.QPushButton(self.centralwidget)
        self.start.setGeometry(QtCore.QRect(20, 330, 75, 23))
        self.start.setObjectName("start")
        self.stop = QtWidgets.QPushButton(self.centralwidget)
        self.stop.setGeometry(QtCore.QRect(100, 330, 75, 23))
        self.stop.setObjectName("stop")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 950, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Points"))
        self.label_2.setText(_translate("MainWindow", "Population"))
        self.label_3.setText(_translate("MainWindow", "Mutation Ratio"))
        self.label_4.setText(_translate("MainWindow", "CrossOver Ratio"))
        self.label_11.setText(_translate("MainWindow", "Selection Ratio"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; text-decoration: underline;\">Inputs: </span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "Best Distance :"))
        self.label_7.setText(_translate("MainWindow", "Tries"))
        self.label_8.setText(_translate("MainWindow", "Total Paths existings"))
        self.label_9.setText(_translate("MainWindow", "Best_path found at generations :"))
        self.nb_tries.setText(_translate("MainWindow", "0"))
        self.label_16.setText(_translate("MainWindow", "Generation :"))
        self.current_gen.setText(_translate("MainWindow", "0"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; text-decoration: underline;\">Outputs: </span></p></body></html>"))
        self.start.setText(_translate("MainWindow", "Start"))
        self.stop.setText(_translate("MainWindow", "Stop"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
