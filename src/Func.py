#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Yee_172'
__date__ = '2017/12/03'


import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from GUI.maindialog import Ui_Dialog

app = QtWidgets.QApplication(sys.argv)
PATH = sys.path[1]
with open(PATH + '/PI/sources/raw/pi.txt', 'r') as f:
    text = f.read()


class MainWin(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self):
        super(MainWin, self).__init__()
        self.setupUi(self)
        self.showing_browser.setText(text)
        self.show()

    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == Qt.Key_Escape:
            self.close()
