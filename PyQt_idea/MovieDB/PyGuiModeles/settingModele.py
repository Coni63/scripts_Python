# noinspection
#@PydevCodeAnalysisIgnore
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '..\UI\setting.ui'
#
# Created: Wed Apr 20 20:33:18 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(635, 461)
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 40, 46, 13))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(30, 70, 46, 13))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(30, 100, 46, 13))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.btn_save = QtGui.QPushButton(Form)
        self.btn_save.setGeometry(QtCore.QRect(40, 410, 131, 23))
        self.btn_save.setObjectName(_fromUtf8("btn_save"))
        self.btn_discard = QtGui.QPushButton(Form)
        self.btn_discard.setGeometry(QtCore.QRect(40, 380, 131, 23))
        self.btn_discard.setObjectName(_fromUtf8("btn_discard"))
        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(90, 40, 113, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(90, 70, 113, 20))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.dockWidget = QtGui.QDockWidget(Form)
        self.dockWidget.setGeometry(QtCore.QRect(510, 10, 120, 80))
        self.dockWidget.setObjectName(_fromUtf8("dockWidget"))
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.comboBox = QtGui.QComboBox(self.dockWidgetContents)
        self.comboBox.setGeometry(QtCore.QRect(30, 10, 69, 22))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.dockWidget.setWidget(self.dockWidgetContents)
        self.stackedWidget = QtGui.QStackedWidget(Form)
        self.stackedWidget.setGeometry(QtCore.QRect(390, 140, 120, 80))
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.page = QtGui.QWidget()
        self.page.setObjectName(_fromUtf8("page"))
        self.pushButton = QtGui.QPushButton(self.page)
        self.pushButton.setGeometry(QtCore.QRect(0, 40, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtGui.QWidget()
        self.page_2.setObjectName(_fromUtf8("page_2"))
        self.buttonBox_2 = QtGui.QDialogButtonBox(self.page_2)
        self.buttonBox_2.setGeometry(QtCore.QRect(20, 40, 156, 23))
        self.buttonBox_2.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox_2.setObjectName(_fromUtf8("buttonBox_2"))
        self.stackedWidget.addWidget(self.page_2)
        self.scrollArea = QtGui.QScrollArea(Form)
        self.scrollArea.setGeometry(QtCore.QRect(90, 150, 251, 201))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 249, 199))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.checkBox = QtGui.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox.setGeometry(QtCore.QRect(50, 50, 70, 17))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.buttonBox = QtGui.QDialogButtonBox(self.scrollAreaWidgetContents)
        self.buttonBox.setGeometry(QtCore.QRect(40, 190, 156, 23))
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "TextLabel", None))
        self.label_2.setText(_translate("Form", "TextLabel", None))
        self.label_3.setText(_translate("Form", "TextLabel", None))
        self.btn_save.setText(_translate("Form", "Save and Quit", None))
        self.btn_discard.setText(_translate("Form", "Discard and Quit", None))
        self.pushButton.setText(_translate("Form", "PushButton", None))
        self.checkBox.setText(_translate("Form", "CheckBox", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

