# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 22:23:32 2020

@author: NO_1
"""

import sys
from PyQt5.QtWidgets import QDialog, QApplication
from MyFirstUI import Ui_Form      #MyFirstUI 是你的.py檔案名字

class AppWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

       #綁上與點擊事件對應的function，所有東西都在ui底下！！
        self.ui.pushButton.clicked.connect(self.pushButton_Click)
        self.show()

    def pushButton_Click(self):
        self.ui.label.setText("Hello World")

app = QApplication(sys.argv)
w = AppWindow()
w.show()
sys.exit(app.exec_())