# -*- coding: utf-8 -*-
"""
import

"""
import sys
sys.path.append("./")
"""
python 會先去這裡找你企圖要 import 的.py 檔案
如果再裡面沒有找到相關檔案的話就會 raise 錯誤訊息
"""

from PyQt5.QtWidgets import QDialog, QApplication
from startUI import Ui_Form    #from 你的.py檔案名稱 import Ui_Form
import selectAll
"""
main

"""
class AppWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.show()

        #綁上與點擊事件對應的function，所有東西都在ui底下！！
        self.ui.subButton.clicked.connect(self.submit)
        self.show()

    def submit(self):
        selectAll.show()

app = QApplication(sys.argv)
w = AppWindow()
w.show()
sys.exit(app.exec_())