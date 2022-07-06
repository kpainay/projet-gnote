# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 21:03:32 2022

@author: lawre
"""

import sys
import PyQt5
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUi


class strange(QMainWindow):
    def __iniy__(self, parent=None):
        super().__init__(parent)
        loadUi("C:\\Users\\lawre\\OneDrive - INP-HB\\Desktop\\LOKI\\THOR\\Strange Indeed\\strange.ui", self)

        self.pushButton_16.clicked.connect(self.click)

    def click(self):
        pass


def main():
    app = QApplication(sys.argv)
    win = strange()
    win.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
