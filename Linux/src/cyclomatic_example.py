#!/usr/bin/env python3
# region Refactor Done
import sys
import platform
import re
try:
    from functions import *
except:
    sys.exit('Module \'functions\' not found.')
from PyQt5.QtWidgets import (
    QWidget, QMainWindow, QLineEdit, QPushButton, QApplication, QLabel, QDesktopWidget)
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIntValidator, QKeyEvent, QIcon
from PyQt5.Qt import QClipboard


class MainGui(QMainWindow):
    def __init__(self):
        super(MainGui, self).__init__()
        self.setWindowTitle('MC Chunk Get')
        self.setFixedWidth(480)
        try:
            self.setWindowIcon(QIcon('mc_chunk_get.ico'))
        except:
            pass
        self.style = {
            'fonts': {
                'main': 'Ubuntu,San Francisco,Segoe UI, \
                    Helvetica,Helvetica Neue,Arial,Lucida Grande,monospace'
            },
            'buttons': {
                'main': 'QPushButton {border: 1px solid rgba(223,223,223,1);background-color: rgba(255,255,255,1);border-radius: 16px;font-weight:300;} \
                    QPushButton::hover {border: 1px solid rgba(159,159,159,1);background-color: rgba(223,223,223,1);} \
                    QPushButton::pressed {border: 1px solid rgba(0,0,223,1);background-color: rgba(0,0,223,0.1);color: rgba(0,0,223,1);}'
            },
            'edits': {
                'main': 'QLineEdit {border: 1px solid rgba(191,191,191,1);border-radius: 16px;font-size: 14px;color: rgba(0,0,223,1); background-color: rgba(223,223,223,1);} \
                    QLineEdit::hover {border: 1px solid rgba(223,223,223,1);background-color: rgba(255,255,255,1);} \
                    QLineEdit::pressed {border: 1px solid rgba(223,223,223,1);background-color: rgba(255,255,255,1);}'
            },
        }

        self.setStyleSheet('* {background-color: rgba(239,239,239,1);\
            color: rgba(16,16,16,1);font-size: 14px;\
            font-family:' + self.style['fonts']['main'] + ';} \
            QMainWindow {border: 1px solid rgba(63,63,63,0.25);}')
# endregion Refactor Done
# region Refactor Done

        self.LabelMain = QLabel(self)
        self.LabelMain.setText(
            "Provide x, z coordinates within a chunk to get that chunks boundaries in Minecraft.")
        self.LabelMain.setGeometry(8, 8, 464, 32)
        self.LabelMain.setWordWrap(True)
        self.LabelMain.setAlignment(Qt.AlignCenter)
        self.LabelMain.setStyleSheet('QLabel {font-size: 16px;}')

        self.LabelX = QLabel(self)
        self.LabelX.setText("X")
        self.LabelX.setGeometry(8, 48, 32, 32)
        self.LabelX.setAlignment(Qt.AlignCenter)
        self.LabelX.setStyleSheet('QLabel {font-size: 18px;}')

        self.EditX = QLineEdit(self)
        self.EditX.setText("")
        self.EditX.setGeometry(40, 48, 117, 32)
        self.EditX.setAlignment(Qt.AlignCenter)
        self.EditX.setStyleSheet(self.style['edits']['main'])
        self.EditX.setValidator(QIntValidator())

        self.LabelZ = QLabel(self)
        self.LabelZ.setText("Z")
        self.LabelZ.setGeometry(165, 48, 32, 32)
        self.LabelZ.setWordWrap(True)
        self.LabelZ.setAlignment(Qt.AlignCenter)
        self.LabelZ.setStyleSheet('QLabel {font-size: 18px;}')

        self.EditZ = QLineEdit(self)
        self.EditZ.setText("")
        self.EditZ.setGeometry(197, 48, 117, 32)
        self.EditZ.setAlignment(Qt.AlignCenter)
        self.EditZ.setStyleSheet(self.style['edits']['main'])
        self.EditZ.setValidator(QIntValidator())

        self.ButtonClear = QPushButton(self)
        self.ButtonClear.setText("&Clear")
        self.ButtonClear.setGeometry(322, 48, 149, 32)
        self.ButtonClear.setStyleSheet(self.style['buttons']['main'])
        self.ButtonClear.setToolTip("Alt+c to clear all...")
        self.ButtonClear.clicked.connect(lambda: self.clear_func())

        self.LabelOutputInit = QLabel(self)
        self.LabelOutputInit.setText("Chunk boundaries of ")
        self.LabelOutputInit.setGeometry(8, 88, 94, 32)
        self.LabelOutputInit.setWordWrap(True)
        self.LabelOutputInit.setAlignment(Qt.AlignCenter | Qt.AlignHCenter)
        self.LabelOutputInit.setStyleSheet("QLabel {font-size: 12px;}")

        self.LabelX2 = QLabel(self)
        self.LabelX2.setText("")
        self.LabelX2.setGeometry(103, 88, 94, 32)
        self.LabelX2.setAlignment(Qt.AlignCenter | Qt.AlignHCenter)
        self.LabelX2.setStyleSheet(
            "QLabel {color: rgba(0,0,223,1);font-size: 14px;}")

        self.LabelTo = QLabel(self)
        self.LabelTo.setText("To")
        self.LabelTo.setGeometry(198, 88, 32, 32)
        self.LabelTo.setAlignment(Qt.AlignCenter | Qt.AlignHCenter)
        self.LabelTo.setStyleSheet("QLabel {font-size: 16px;}")

        self.LabelZ2 = QLabel(self)
        self.LabelZ2.setText("")
        self.LabelZ2.setGeometry(231, 88, 94, 32)
        self.LabelZ2.setAlignment(Qt.AlignCenter | Qt.AlignHCenter)
        self.LabelZ2.setStyleSheet(
            "QLabel {color: rgba(0,0,223,1);font-size: 14px;}")

        self.ButtonCopy = QPushButton(self)
        self.ButtonCopy.setText("Co&py")
        self.ButtonCopy.setGeometry(322, 88, 149, 32)
        self.ButtonCopy.setStyleSheet(self.style['buttons']['main'])
        self.ButtonCopy.setToolTip("Alt+p to copy...")
        self.ButtonCopy.clicked.connect(lambda: self.toClipboard())

        self.LabelResult = QLabel(self)
        self.LabelResult.setText("")
        self.LabelResult.setGeometry(8, 128, 468, 32)
        self.LabelResult.setStyleSheet(
            "QLabel {color: rgba(223,0,0,1);font-size: 18px;}")

# endregion Refactor Done
# region Refactor Done
    def toClipboard(self):
        try:
            QApplication.clipboard().setText(self.string)
        except:
            pass

    def resizeEvent(self, event):
        maxY = greatest_num(
            *[self.LabelResult.geometry().y() + self.LabelResult.geometry().height() + 8])
        if not (self.geometry().height() == maxY):
            self.setFixedHeight(maxY)

    def keyReleaseEvent(self, QKeyEvent):
        numX, numZ = self.EditX.text(), self.EditZ.text()
        self.LabelX2.setText(
            numX) if numX else self.LabelX2.setText('')
        self.LabelZ2.setText(
            numZ) if numZ else self.LabelZ2.setText('')

        def params_correct_check(self, numX, numZ):
            if not (re.match('^[-|+]$', numX) or re.match('^[-|+]$', numZ)):
                self.string = mc_chunk_get(int(numX), int(numZ), string=True)
                self.LabelResult.setText(self.string)
        params_correct_check(self, numX, numZ) if (
            numX and numZ) else self.LabelResult.setText('')

    def clear_func(self):
        self.EditX.setText("")
        self.EditZ.setText("")
        self.LabelX2.setText("")
        self.LabelZ2.setText("")
        self.LabelResult.setText("")


if __name__ == '__main__':
    MainApp = QApplication(sys.argv)
    MainApp.setStyle('Fusion')
    MainApp.setWindowIcon(QIcon('mc_chunk_get.ico'))
    MainWindow = MainGui()
    MainWindow.show()
    sys.exit(MainApp.exec_())
# endregion Refactor Done
