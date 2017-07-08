# noinspection
#@PydevCodeAnalysisIgnore
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '..\UI\Form_task.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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
        Form.resize(636, 542)
        self.buttonBox = QtGui.QDialogButtonBox(Form)
        self.buttonBox.setGeometry(QtCore.QRect(450, 510, 156, 23))
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Apply|QtGui.QDialogButtonBox.Cancel)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.formLayoutWidget = QtGui.QWidget(Form)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 20, 601, 461))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_3 = QtGui.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_3)
        self.input_description = QtGui.QLineEdit(self.formLayoutWidget)
        self.input_description.setObjectName(_fromUtf8("input_description"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.input_description)
        self.label = QtGui.QLabel(self.formLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label)
        self.input_due_date = QtGui.QCalendarWidget(self.formLayoutWidget)
        self.input_due_date.setObjectName(_fromUtf8("input_due_date"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.input_due_date)
        self.label_2 = QtGui.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_2)
        self.input_repetition = QtGui.QComboBox(self.formLayoutWidget)
        self.input_repetition.setObjectName(_fromUtf8("input_repetition"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.input_repetition)
        self.testbtn = QtGui.QPushButton(Form)
        self.testbtn.setGeometry(QtCore.QRect(40, 480, 546, 23))
        self.testbtn.setObjectName(_fromUtf8("testbtn"))

        self.retranslateUi(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label_3.setText(_translate("Form", "TextLabel", None))
        self.label.setText(_translate("Form", "TextLabel", None))
        self.label_2.setText(_translate("Form", "TextLabel", None))
        self.testbtn.setText(_translate("Form", "PushButton", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

