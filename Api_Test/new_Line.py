# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_Line.ui'
#
# Created: Sat May 21 14:16:12 2016
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

class Ui_NewLine(object):
    def setupUi(self, NewLine):
        NewLine.setObjectName(_fromUtf8("NewLine"))
        NewLine.resize(836, 642)
        self.verticalLayoutWidget_5 = QtGui.QWidget(NewLine)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(10, 10, 811, 563))
        self.verticalLayoutWidget_5.setObjectName(_fromUtf8("verticalLayoutWidget_5"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_5.setMargin(0)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.horizontalLayout_40 = QtGui.QHBoxLayout()
        self.horizontalLayout_40.setObjectName(_fromUtf8("horizontalLayout_40"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.verticalLayoutWidget_5)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.newMethod = QtGui.QLineEdit(self.verticalLayoutWidget_5)
        self.newMethod.setObjectName(_fromUtf8("newMethod"))
        self.horizontalLayout.addWidget(self.newMethod)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(self.verticalLayoutWidget_5)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.newAddress = QtGui.QLineEdit(self.verticalLayoutWidget_5)
        self.newAddress.setObjectName(_fromUtf8("newAddress"))
        self.horizontalLayout_2.addWidget(self.newAddress)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_3 = QtGui.QLabel(self.verticalLayoutWidget_5)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_3.addWidget(self.label_3)
        self.newTitle = QtGui.QLineEdit(self.verticalLayoutWidget_5)
        self.newTitle.setObjectName(_fromUtf8("newTitle"))
        self.horizontalLayout_3.addWidget(self.newTitle)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_41 = QtGui.QHBoxLayout()
        self.horizontalLayout_41.setObjectName(_fromUtf8("horizontalLayout_41"))
        self.saveForNext = QtGui.QCheckBox(self.verticalLayoutWidget_5)
        self.saveForNext.setObjectName(_fromUtf8("saveForNext"))
        self.horizontalLayout_41.addWidget(self.saveForNext)
        self.verticalLayout_4.addLayout(self.horizontalLayout_41)
        self.horizontalLayout_40.addLayout(self.verticalLayout_4)
        self.line = QtGui.QFrame(self.verticalLayoutWidget_5)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.horizontalLayout_40.addWidget(self.line)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_22 = QtGui.QLabel(self.verticalLayoutWidget_5)
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.verticalLayout.addWidget(self.label_22)
        self.horizontalLayout_28 = QtGui.QHBoxLayout()
        self.horizontalLayout_28.setObjectName(_fromUtf8("horizontalLayout_28"))
        self.label_20 = QtGui.QLabel(self.verticalLayoutWidget_5)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.horizontalLayout_28.addWidget(self.label_20)
        self.sKey = QtGui.QLineEdit(self.verticalLayoutWidget_5)
        self.sKey.setObjectName(_fromUtf8("sKey"))
        self.horizontalLayout_28.addWidget(self.sKey)
        self.verticalLayout.addLayout(self.horizontalLayout_28)
        self.horizontalLayout_29 = QtGui.QHBoxLayout()
        self.horizontalLayout_29.setObjectName(_fromUtf8("horizontalLayout_29"))
        self.label_21 = QtGui.QLabel(self.verticalLayoutWidget_5)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.horizontalLayout_29.addWidget(self.label_21)
        self.pKey = QtGui.QLineEdit(self.verticalLayoutWidget_5)
        self.pKey.setObjectName(_fromUtf8("pKey"))
        self.horizontalLayout_29.addWidget(self.pKey)
        self.verticalLayout.addLayout(self.horizontalLayout_29)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_4 = QtGui.QLabel(self.verticalLayoutWidget_5)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_4.addWidget(self.label_4)
        self.p_one_name = QtGui.QLineEdit(self.verticalLayoutWidget_5)
        self.p_one_name.setObjectName(_fromUtf8("p_one_name"))
        self.horizontalLayout_4.addWidget(self.p_one_name)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_5 = QtGui.QLabel(self.verticalLayoutWidget_5)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_5.addWidget(self.label_5)
        self.p_one_value = QtGui.QLineEdit(self.verticalLayoutWidget_5)
        self.p_one_value.setObjectName(_fromUtf8("p_one_value"))
        self.horizontalLayout_5.addWidget(self.p_one_value)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.label_6 = QtGui.QLabel(self.verticalLayoutWidget_5)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_8.addWidget(self.label_6)
        self.p_two_name = QtGui.QLineEdit(self.verticalLayoutWidget_5)
        self.p_two_name.setObjectName(_fromUtf8("p_two_name"))
        self.horizontalLayout_8.addWidget(self.p_two_name)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.label_7 = QtGui.QLabel(self.verticalLayoutWidget_5)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_9.addWidget(self.label_7)
        self.p_two_value = QtGui.QLineEdit(self.verticalLayoutWidget_5)
        self.p_two_value.setObjectName(_fromUtf8("p_two_value"))
        self.horizontalLayout_9.addWidget(self.p_two_value)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_9)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.label_8 = QtGui.QLabel(self.verticalLayoutWidget_5)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_11.addWidget(self.label_8)
        self.p_three_name = QtGui.QLineEdit(self.verticalLayoutWidget_5)
        self.p_three_name.setObjectName(_fromUtf8("p_three_name"))
        self.horizontalLayout_11.addWidget(self.p_three_name)
        self.horizontalLayout_10.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.label_9 = QtGui.QLabel(self.verticalLayoutWidget_5)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_12.addWidget(self.label_9)
        self.p_three_value = QtGui.QLineEdit(self.verticalLayoutWidget_5)
        self.p_three_value.setObjectName(_fromUtf8("p_three_value"))
        self.horizontalLayout_12.addWidget(self.p_three_value)
        self.horizontalLayout_10.addLayout(self.horizontalLayout_12)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_19 = QtGui.QHBoxLayout()
        self.horizontalLayout_19.setObjectName(_fromUtf8("horizontalLayout_19"))
        self.horizontalLayout_20 = QtGui.QHBoxLayout()
        self.horizontalLayout_20.setObjectName(_fromUtf8("horizontalLayout_20"))
        self.label_14 = QtGui.QLabel(self.verticalLayoutWidget_5)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.horizontalLayout_20.addWidget(self.label_14)
        self.p_four_name = QtGui.QLineEdit(self.verticalLayoutWidget_5)
        self.p_four_name.setObjectName(_fromUtf8("p_four_name"))
        self.horizontalLayout_20.addWidget(self.p_four_name)
        self.horizontalLayout_19.addLayout(self.horizontalLayout_20)
        self.horizontalLayout_21 = QtGui.QHBoxLayout()
        self.horizontalLayout_21.setObjectName(_fromUtf8("horizontalLayout_21"))
        self.label_15 = QtGui.QLabel(self.verticalLayoutWidget_5)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.horizontalLayout_21.addWidget(self.label_15)
        self.p_four_value = QtGui.QLineEdit(self.verticalLayoutWidget_5)
        self.p_four_value.setObjectName(_fromUtf8("p_four_value"))
        self.horizontalLayout_21.addWidget(self.p_four_value)
        self.horizontalLayout_19.addLayout(self.horizontalLayout_21)
        self.verticalLayout.addLayout(self.horizontalLayout_19)
        self.horizontalLayout_13 = QtGui.QHBoxLayout()
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        self.horizontalLayout_14 = QtGui.QHBoxLayout()
        self.horizontalLayout_14.setObjectName(_fromUtf8("horizontalLayout_14"))
        self.label_10 = QtGui.QLabel(self.verticalLayoutWidget_5)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.horizontalLayout_14.addWidget(self.label_10)
        self.p_five_name = QtGui.QLineEdit(self.verticalLayoutWidget_5)
        self.p_five_name.setObjectName(_fromUtf8("p_five_name"))
        self.horizontalLayout_14.addWidget(self.p_five_name)
        self.horizontalLayout_13.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_15 = QtGui.QHBoxLayout()
        self.horizontalLayout_15.setObjectName(_fromUtf8("horizontalLayout_15"))
        self.label_11 = QtGui.QLabel(self.verticalLayoutWidget_5)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.horizontalLayout_15.addWidget(self.label_11)
        self.p_five_value = QtGui.QLineEdit(self.verticalLayoutWidget_5)
        self.p_five_value.setObjectName(_fromUtf8("p_five_value"))
        self.horizontalLayout_15.addWidget(self.p_five_value)
        self.horizontalLayout_13.addLayout(self.horizontalLayout_15)
        self.verticalLayout.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_16 = QtGui.QHBoxLayout()
        self.horizontalLayout_16.setObjectName(_fromUtf8("horizontalLayout_16"))
        self.horizontalLayout_17 = QtGui.QHBoxLayout()
        self.horizontalLayout_17.setObjectName(_fromUtf8("horizontalLayout_17"))
        self.label_12 = QtGui.QLabel(self.verticalLayoutWidget_5)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.horizontalLayout_17.addWidget(self.label_12)
        self.p_six_name = QtGui.QLineEdit(self.verticalLayoutWidget_5)
        self.p_six_name.setObjectName(_fromUtf8("p_six_name"))
        self.horizontalLayout_17.addWidget(self.p_six_name)
        self.horizontalLayout_16.addLayout(self.horizontalLayout_17)
        self.horizontalLayout_18 = QtGui.QHBoxLayout()
        self.horizontalLayout_18.setObjectName(_fromUtf8("horizontalLayout_18"))
        self.label_13 = QtGui.QLabel(self.verticalLayoutWidget_5)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.horizontalLayout_18.addWidget(self.label_13)
        self.p_six_value = QtGui.QLineEdit(self.verticalLayoutWidget_5)
        self.p_six_value.setObjectName(_fromUtf8("p_six_value"))
        self.horizontalLayout_18.addWidget(self.p_six_value)
        self.horizontalLayout_16.addLayout(self.horizontalLayout_18)
        self.verticalLayout.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_25 = QtGui.QHBoxLayout()
        self.horizontalLayout_25.setObjectName(_fromUtf8("horizontalLayout_25"))
        self.horizontalLayout_26 = QtGui.QHBoxLayout()
        self.horizontalLayout_26.setObjectName(_fromUtf8("horizontalLayout_26"))
        self.label_18 = QtGui.QLabel(self.verticalLayoutWidget_5)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.horizontalLayout_26.addWidget(self.label_18)
        self.p_seven_name = QtGui.QLineEdit(self.verticalLayoutWidget_5)
        self.p_seven_name.setObjectName(_fromUtf8("p_seven_name"))
        self.horizontalLayout_26.addWidget(self.p_seven_name)
        self.horizontalLayout_25.addLayout(self.horizontalLayout_26)
        self.horizontalLayout_27 = QtGui.QHBoxLayout()
        self.horizontalLayout_27.setObjectName(_fromUtf8("horizontalLayout_27"))
        self.label_19 = QtGui.QLabel(self.verticalLayoutWidget_5)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.horizontalLayout_27.addWidget(self.label_19)
        self.p_seven_value = QtGui.QLineEdit(self.verticalLayoutWidget_5)
        self.p_seven_value.setObjectName(_fromUtf8("p_seven_value"))
        self.horizontalLayout_27.addWidget(self.p_seven_value)
        self.horizontalLayout_25.addLayout(self.horizontalLayout_27)
        self.verticalLayout.addLayout(self.horizontalLayout_25)
        self.horizontalLayout_22 = QtGui.QHBoxLayout()
        self.horizontalLayout_22.setObjectName(_fromUtf8("horizontalLayout_22"))
        self.horizontalLayout_23 = QtGui.QHBoxLayout()
        self.horizontalLayout_23.setObjectName(_fromUtf8("horizontalLayout_23"))
        self.label_16 = QtGui.QLabel(self.verticalLayoutWidget_5)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.horizontalLayout_23.addWidget(self.label_16)
        self.p_eight_name = QtGui.QLineEdit(self.verticalLayoutWidget_5)
        self.p_eight_name.setObjectName(_fromUtf8("p_eight_name"))
        self.horizontalLayout_23.addWidget(self.p_eight_name)
        self.horizontalLayout_22.addLayout(self.horizontalLayout_23)
        self.horizontalLayout_24 = QtGui.QHBoxLayout()
        self.horizontalLayout_24.setObjectName(_fromUtf8("horizontalLayout_24"))
        self.label_17 = QtGui.QLabel(self.verticalLayoutWidget_5)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.horizontalLayout_24.addWidget(self.label_17)
        self.p_eight_value = QtGui.QLineEdit(self.verticalLayoutWidget_5)
        self.p_eight_value.setObjectName(_fromUtf8("p_eight_value"))
        self.horizontalLayout_24.addWidget(self.p_eight_value)
        self.horizontalLayout_22.addLayout(self.horizontalLayout_24)
        self.verticalLayout.addLayout(self.horizontalLayout_22)
        self.horizontalLayout_40.addLayout(self.verticalLayout)
        self.verticalLayout_5.addLayout(self.horizontalLayout_40)
        self.line_3 = QtGui.QFrame(self.verticalLayoutWidget_5)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.verticalLayout_5.addWidget(self.line_3)
        self.horizontalLayout_39 = QtGui.QHBoxLayout()
        self.horizontalLayout_39.setObjectName(_fromUtf8("horizontalLayout_39"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_23 = QtGui.QLabel(self.verticalLayoutWidget_5)
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.verticalLayout_2.addWidget(self.label_23)
        self.comboBox = QtGui.QComboBox(self.verticalLayoutWidget_5)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.verticalLayout_2.addWidget(self.comboBox)
        self.findOne = QtGui.QLineEdit(self.verticalLayoutWidget_5)
        self.findOne.setObjectName(_fromUtf8("findOne"))
        self.verticalLayout_2.addWidget(self.findOne)
        self.findTwo = QtGui.QLineEdit(self.verticalLayoutWidget_5)
        self.findTwo.setObjectName(_fromUtf8("findTwo"))
        self.verticalLayout_2.addWidget(self.findTwo)
        self.findThree = QtGui.QLineEdit(self.verticalLayoutWidget_5)
        self.findThree.setObjectName(_fromUtf8("findThree"))
        self.verticalLayout_2.addWidget(self.findThree)
        self.horizontalLayout_39.addLayout(self.verticalLayout_2)
        self.line_2 = QtGui.QFrame(self.verticalLayoutWidget_5)
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.horizontalLayout_39.addWidget(self.line_2)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_30 = QtGui.QLabel(self.verticalLayoutWidget_5)
        self.label_30.setObjectName(_fromUtf8("label_30"))
        self.verticalLayout_3.addWidget(self.label_30)
        self.horizontalLayout_30 = QtGui.QHBoxLayout()
        self.horizontalLayout_30.setObjectName(_fromUtf8("horizontalLayout_30"))
        self.horizontalLayout_31 = QtGui.QHBoxLayout()
        self.horizontalLayout_31.setObjectName(_fromUtf8("horizontalLayout_31"))
        self.checkPrevValue_1 = QtGui.QCheckBox(self.verticalLayoutWidget_5)
        self.checkPrevValue_1.setText(_fromUtf8(""))
        self.checkPrevValue_1.setObjectName(_fromUtf8("checkPrevValue_1"))
        self.horizontalLayout_31.addWidget(self.checkPrevValue_1)
        self.label_24 = QtGui.QLabel(self.verticalLayoutWidget_5)
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.horizontalLayout_31.addWidget(self.label_24)
        self.check_one_name = QtGui.QLineEdit(self.verticalLayoutWidget_5)
        self.check_one_name.setObjectName(_fromUtf8("check_one_name"))
        self.horizontalLayout_31.addWidget(self.check_one_name)
        self.horizontalLayout_30.addLayout(self.horizontalLayout_31)
        self.horizontalLayout_32 = QtGui.QHBoxLayout()
        self.horizontalLayout_32.setObjectName(_fromUtf8("horizontalLayout_32"))
        self.label_25 = QtGui.QLabel(self.verticalLayoutWidget_5)
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.horizontalLayout_32.addWidget(self.label_25)
        self.check_one_value = QtGui.QLineEdit(self.verticalLayoutWidget_5)
        self.check_one_value.setObjectName(_fromUtf8("check_one_value"))
        self.horizontalLayout_32.addWidget(self.check_one_value)
        self.horizontalLayout_30.addLayout(self.horizontalLayout_32)
        self.verticalLayout_3.addLayout(self.horizontalLayout_30)
        self.horizontalLayout_33 = QtGui.QHBoxLayout()
        self.horizontalLayout_33.setObjectName(_fromUtf8("horizontalLayout_33"))
        self.horizontalLayout_34 = QtGui.QHBoxLayout()
        self.horizontalLayout_34.setObjectName(_fromUtf8("horizontalLayout_34"))
        self.checkPrevValue_2 = QtGui.QCheckBox(self.verticalLayoutWidget_5)
        self.checkPrevValue_2.setText(_fromUtf8(""))
        self.checkPrevValue_2.setObjectName(_fromUtf8("checkPrevValue_2"))
        self.horizontalLayout_34.addWidget(self.checkPrevValue_2)
        self.label_26 = QtGui.QLabel(self.verticalLayoutWidget_5)
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.horizontalLayout_34.addWidget(self.label_26)
        self.check_two_name = QtGui.QLineEdit(self.verticalLayoutWidget_5)
        self.check_two_name.setObjectName(_fromUtf8("check_two_name"))
        self.horizontalLayout_34.addWidget(self.check_two_name)
        self.horizontalLayout_33.addLayout(self.horizontalLayout_34)
        self.horizontalLayout_35 = QtGui.QHBoxLayout()
        self.horizontalLayout_35.setObjectName(_fromUtf8("horizontalLayout_35"))
        self.label_27 = QtGui.QLabel(self.verticalLayoutWidget_5)
        self.label_27.setObjectName(_fromUtf8("label_27"))
        self.horizontalLayout_35.addWidget(self.label_27)
        self.check_two_value = QtGui.QLineEdit(self.verticalLayoutWidget_5)
        self.check_two_value.setObjectName(_fromUtf8("check_two_value"))
        self.horizontalLayout_35.addWidget(self.check_two_value)
        self.horizontalLayout_33.addLayout(self.horizontalLayout_35)
        self.verticalLayout_3.addLayout(self.horizontalLayout_33)
        self.horizontalLayout_36 = QtGui.QHBoxLayout()
        self.horizontalLayout_36.setObjectName(_fromUtf8("horizontalLayout_36"))
        self.horizontalLayout_37 = QtGui.QHBoxLayout()
        self.horizontalLayout_37.setObjectName(_fromUtf8("horizontalLayout_37"))
        self.checkPrevValue_3 = QtGui.QCheckBox(self.verticalLayoutWidget_5)
        self.checkPrevValue_3.setText(_fromUtf8(""))
        self.checkPrevValue_3.setObjectName(_fromUtf8("checkPrevValue_3"))
        self.horizontalLayout_37.addWidget(self.checkPrevValue_3)
        self.label_28 = QtGui.QLabel(self.verticalLayoutWidget_5)
        self.label_28.setObjectName(_fromUtf8("label_28"))
        self.horizontalLayout_37.addWidget(self.label_28)
        self.check_three_name = QtGui.QLineEdit(self.verticalLayoutWidget_5)
        self.check_three_name.setObjectName(_fromUtf8("check_three_name"))
        self.horizontalLayout_37.addWidget(self.check_three_name)
        self.horizontalLayout_36.addLayout(self.horizontalLayout_37)
        self.horizontalLayout_38 = QtGui.QHBoxLayout()
        self.horizontalLayout_38.setObjectName(_fromUtf8("horizontalLayout_38"))
        self.label_29 = QtGui.QLabel(self.verticalLayoutWidget_5)
        self.label_29.setObjectName(_fromUtf8("label_29"))
        self.horizontalLayout_38.addWidget(self.label_29)
        self.check_three_value = QtGui.QLineEdit(self.verticalLayoutWidget_5)
        self.check_three_value.setObjectName(_fromUtf8("check_three_value"))
        self.horizontalLayout_38.addWidget(self.check_three_value)
        self.horizontalLayout_36.addLayout(self.horizontalLayout_38)
        self.verticalLayout_3.addLayout(self.horizontalLayout_36)
        self.horizontalLayout_39.addLayout(self.verticalLayout_3)
        self.verticalLayout_5.addLayout(self.horizontalLayout_39)
        self.closeBtn = QtGui.QPushButton(NewLine)
        self.closeBtn.setGeometry(QtCore.QRect(710, 560, 97, 60))
        self.closeBtn.setMinimumSize(QtCore.QSize(97, 60))
        self.closeBtn.setObjectName(_fromUtf8("closeBtn"))
        self.saveBtn = QtGui.QPushButton(NewLine)
        self.saveBtn.setGeometry(QtCore.QRect(600, 560, 97, 60))
        self.saveBtn.setMinimumSize(QtCore.QSize(97, 60))
        self.saveBtn.setObjectName(_fromUtf8("saveBtn"))

        self.retranslateUi(NewLine)
        QtCore.QMetaObject.connectSlotsByName(NewLine)

    def retranslateUi(self, NewLine):
        NewLine.setWindowTitle(_translate("NewLine", "New Line", None))
        self.label.setText(_translate("NewLine", "Method <GET/POST>:", None))
        self.label_2.setText(_translate("NewLine", "Address:", None))
        self.label_3.setText(_translate("NewLine", "Title:", None))
        self.saveForNext.setText(_translate("NewLine", "Save response for next check", None))
        self.label_22.setText(_translate("NewLine", "                                                            Params:", None))
        self.label_20.setText(_translate("NewLine", "Secret Key:", None))
        self.label_21.setText(_translate("NewLine", "Public Key: ", None))
        self.label_4.setText(_translate("NewLine", "Name:", None))
        self.label_5.setText(_translate("NewLine", "Value:", None))
        self.label_6.setText(_translate("NewLine", "Name:", None))
        self.label_7.setText(_translate("NewLine", "Value:", None))
        self.label_8.setText(_translate("NewLine", "Name:", None))
        self.label_9.setText(_translate("NewLine", "Value:", None))
        self.label_14.setText(_translate("NewLine", "Name:", None))
        self.label_15.setText(_translate("NewLine", "Value:", None))
        self.label_10.setText(_translate("NewLine", "Name:", None))
        self.label_11.setText(_translate("NewLine", "Value:", None))
        self.label_12.setText(_translate("NewLine", "Name:", None))
        self.label_13.setText(_translate("NewLine", "Value:", None))
        self.label_18.setText(_translate("NewLine", "Name:", None))
        self.label_19.setText(_translate("NewLine", "Value:", None))
        self.label_16.setText(_translate("NewLine", "Name:", None))
        self.label_17.setText(_translate("NewLine", "Value:", None))
        self.label_23.setText(_translate("NewLine", "                                                               Find:", None))
        self.label_30.setText(_translate("NewLine", "                                                            Check:", None))
        self.label_24.setText(_translate("NewLine", "Name:", None))
        self.label_25.setText(_translate("NewLine", "Value:", None))
        self.label_26.setText(_translate("NewLine", "Name:", None))
        self.label_27.setText(_translate("NewLine", "Value:", None))
        self.label_28.setText(_translate("NewLine", "Name:", None))
        self.label_29.setText(_translate("NewLine", "Value:", None))
        self.closeBtn.setText(_translate("NewLine", "Close", None))
        self.saveBtn.setText(_translate("NewLine", "Save to file", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    NewLine = QtGui.QDialog()
    ui = Ui_NewLine()
    ui.setupUi(NewLine)
    NewLine.show()
    sys.exit(app.exec_())

