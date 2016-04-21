# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'jsoncreator.ui'
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

class Ui_JsonCreator(object):
    def setupUi(self, JsonCreator):
        JsonCreator.setObjectName(_fromUtf8("JsonCreator"))
        JsonCreator.resize(552, 412)
        self.verticalLayoutWidget = QtGui.QWidget(JsonCreator)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 551, 411))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.textEdit = QtGui.QTextEdit(self.verticalLayoutWidget)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.verticalLayout.addWidget(self.textEdit)

        self.retranslateUi(JsonCreator)
        QtCore.QMetaObject.connectSlotsByName(JsonCreator)

    def retranslateUi(self, JsonCreator):
        JsonCreator.setWindowTitle(_translate("JsonCreator", "File Work", None))
        self.pushButton.setText(_translate("JsonCreator", "Create New", None))
        self.pushButton_2.setText(_translate("JsonCreator", "Add to File", None))
        self.pushButton_3.setText(_translate("JsonCreator", "Load File", None))
        self.pushButton_4.setText(_translate("JsonCreator", "Done", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    JsonCreator = QtGui.QDialog()
    ui = Ui_JsonCreator()
    ui.setupUi(JsonCreator)
    JsonCreator.show()
    sys.exit(app.exec_())

