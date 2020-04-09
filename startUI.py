# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'start.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(399, 301)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 9, 381, 281))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.infoLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.infoLabel.setFont(font)
        self.infoLabel.setFocusPolicy(QtCore.Qt.NoFocus)
        self.infoLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.infoLabel.setObjectName("infoLabel")
        self.verticalLayout.addWidget(self.infoLabel, 0, QtCore.Qt.AlignHCenter)
        self.selectComboBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.selectComboBox.setFont(font)
        self.selectComboBox.setTabletTracking(False)
        self.selectComboBox.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.selectComboBox.setObjectName("selectComboBox")
        self.selectComboBox.addItem("")
        self.selectComboBox.addItem("")
        self.selectComboBox.addItem("")
        self.selectComboBox.addItem("")
        self.verticalLayout.addWidget(self.selectComboBox)
        self.subButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.subButton.setFont(font)
        self.subButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.subButton.setObjectName("subButton")
        self.verticalLayout.addWidget(self.subButton)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.infoLabel.setText(_translate("Form", "選擇要對資料庫進行的操作"))
        self.selectComboBox.setItemText(0, _translate("Form", "查詢"))
        self.selectComboBox.setItemText(1, _translate("Form", "新增"))
        self.selectComboBox.setItemText(2, _translate("Form", "刪除"))
        self.selectComboBox.setItemText(3, _translate("Form", "修改"))
        self.subButton.setText(_translate("Form", "確定"))

