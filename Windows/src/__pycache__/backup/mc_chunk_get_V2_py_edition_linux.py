#!/usr/bin/env python3
#region Imports
import sys, platform, logging, re
try: from functions import *
except: sys.exit('Module \'functions\' not found.')
from PyQt5.QtWidgets import (QWidget, QMainWindow, QLineEdit,
    QPushButton, QApplication, QLabel, QDesktopWidget)
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIntValidator, QKeyEvent, QIcon # , QMouseEvent
from PyQt5.Qt import QClipboard
#endregion Imports
#region Init testing
logging.basicConfig(format='%(levelname)s : %(message)s', level=logging.DEBUG)
working=lambda:logging.info('Working so far...')
working()
#endregion Init Testing
#region Build Gui
class MainGui(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainGui, self).__init__(*args, **kwargs)
        self.setWindowTitle('MC Chunk Get')
        self.setFixedWidth(480)
        try: self.setWindowIcon(QIcon('mc_chunk_get.ico'))
        except: pass
#region Style & Theme
        self.style={
            'fonts':{
                'main':'Ubuntu,San Francisco,Segoe UI, \
                    Helvetica,Helvetica Neue,Arial,Lucida Grande,monospace',
            },
            'buttons':{
                'main':'QPushButton {border: 1px solid rgba(223,223,223,1);background-color: rgba(255,255,255,1);border-radius: 16px;font-weight:300;} \
                    QPushButton::hover {border: 1px solid rgba(159,159,159,1);background-color: rgba(223,223,223,1);} \
                    QPushButton::pressed {border: 1px solid rgba(0,0,223,1);background-color: rgba(0,0,223,0.1);color: rgba(0,0,223,1);}',
            },
            'edits':{
                'main':'QLineEdit {border: 1px solid rgba(191,191,191,1);border-radius: 16px;font-size: 14px;color: #0000DF; background-color: rgba(223,223,223,1);} \
                    QLineEdit::hover {border: 1px solid rgba(223,223,223,1);background-color: rgba(255,255,255,1);} \
                    QLineEdit::pressed {border: 1px solid rgba(223,223,223,1);background-color: rgba(255,255,255,1);}',
            },
        }
#endregion Style & Theme
#region Widget Data
        self.widget={}
        self.widget_object  =   {
            'LabelMain' :   {
                'Type':QLabel(self),
                'Text':'Provide x, z coordinates within a '\
                    'chunk to get that chunks boundaries in Minecraft.',
                'Geometry':{'x':8,'y':8,'w':464,'h':32},
                'WordWrap':True,
                'Align':Qt.AlignCenter,
                'Style':'QLabel {font-size: 16px;}'
            },
            'LabelX' :   {
                'Type':QLabel(self),
                'Text':'X',
                'Geometry':{'x':8,'y':48,'w':32,'h':32},
                'Align':Qt.AlignCenter,
                'Style':'QLabel {font-size: 18px;}'
            },
            'EditX' :   {
                'Type':QLineEdit(self),
                'Text':'',
                'Geometry':{'x':40,'y':48,'w':117,'h':32},
                'Align':Qt.AlignCenter,
                'Style':self.style['edits']['main'],
                'Validator':QIntValidator(),
            },
            'LabelZ' :   {
                'Type':QLabel(self),
                'Text':'Z',
                'Geometry':{'x':165,'y':48,'w':32,'h':32},
                'Align':Qt.AlignCenter,
                'Style':'QLabel {font-size: 18px;}'
            },
            'EditZ' :   {
                'Type':QLineEdit(self),
                'Text':'',
                'Geometry':{'x':197,'y':48,'w':117,'h':32},
                'Align':Qt.AlignCenter,
                'Style':self.style['edits']['main'],
                'Validator':QIntValidator(),
            },
            'ButtonClear' :   {
                'Type':QPushButton(self),
                'Text':'&Clear',
                'Geometry':{'x':322,'y':48,'w':149,'h':32},
                'Style':self.style['buttons']['main'],
                'ToolTip':'Alt+c to clear all...', 
                'Connect':lambda:self.clear_func(),
            },
            'LabelOutputInit' :  {
                'Type':QLabel(self),
                'Text':'Chunk boundaries of ',
                'Geometry':{'x':8,'y':88,'w':94,'h':32},
                'WordWrap':True,
                'Align':Qt.AlignCenter|Qt.AlignHCenter,
                'Style':'QLabel {font-size: 12px;}'
            },
            'LabelX2' :   {
                'Type':QLabel(self),
                'Text':'',
                'Geometry':{'x':103,'y':88,'w':94,'h':32},
                'Align':Qt.AlignCenter|Qt.AlignHCenter,
                'Style':'QLabel {color: rgba(0,0,223,1);font-size: 14px;}',
            },
            'LabelTo' :   {
                'Type':QLabel(self),
                'Text':'To',
                'Geometry':{'x':198,'y':88,'w':32,'h':32},
                'Align':Qt.AlignCenter|Qt.AlignHCenter,
                'Style':'QLabel {font-size: 16px;}',
            },
            'LabelZ2' :   {
                'Type':QLabel(self),
                'Text':'',
                'Geometry':{'x':231,'y':88,'w':94,'h':32},
                'Align':Qt.AlignCenter|Qt.AlignHCenter,
                'Style':'QLabel {color: rgba(0,0,223,1);font-size: 14px;}',
            },
            'ButtonCopy' :   {
                'Type':QPushButton(self),
                'Text':'Co&py',
                'Geometry':{'x':322,'y':88,'w':149,'h':32},
                'ToolTip':'Alt+p to copy...',
                'Style':self.style['buttons']['main'],
                'Connect':lambda:self.toClipboard(),
            },
            'LabelResult' :   {
                'Type':QLabel(self),
                'Text':'',
                'Geometry':{'x':8,'y':128,'w':468,'h':32},
                'Style':'QLabel {color: rgba(223,0,0,1);font-size: 18px;}',
            },
        }
#endregion Widget Data
#region Build 
        self.setStyleSheet('* {background-color: #EFEFEF;\
            color: #101010;font-size: 14px;\
            font-family:' + self.style['fonts']['main'] + ';} \
            QMainWindow {border: 1px solid rgba(63,63,63,0.25);}')
        for widg in self.widget_object:
            try: self.widget[widg]=self.widget_object[widg]['Type']
            except: pass
            try: self.widget[widg].setText(self.widget_object[widg]['Text'])
            except: pass
            try:
                c=self.widget_object[widg]['Geometry']
                self.widget[widg].setGeometry(c['x'],c['y'],c['w'],c['h'])
                del c['x'], c['y'], c['w'], c['h'], c
            except: pass
            try: self.widget[widg].setWordWrap(self.widget_object[widg]['WordWrap'])
            except: pass
            try: self.widget[widg].setAlignment(self.widget_object[widg]['Align'])
            except: pass
            try: self.widget[widg].setStyleSheet(self.widget_object[widg]['Style'])
            except: pass
            try: self.widget[widg].setValidator(self.widget_object[widg]['Validator'])
            except: pass
            try: self.widget[widg].clicked.connect(self.widget_object[widg]['Connect'])
            except: pass
            try: self.widget[widg].setToolTip(self.widget_object[widg]['ToolTip'])
            except: pass
#endregion Build
#region Self Functions
    def toClipboard(self):
        try: QApplication.clipboard().setText(self.string)
        except: pass
    def resizeEvent(self, event):
        maxY=greatest_num(*[(self.widget[widget].geometry().y() +
            self.widget[widget].geometry().height())
            for widget in self.widget_object])+8
        if not (self.geometry().height() == maxY):
            self.setFixedHeight(maxY)
    def keyReleaseEvent(self, QKeyEvent):
        numX, numZ = self.widget['EditX'].text(), self.widget['EditZ'].text()
        if numX: self.widget['LabelX2'].setText(numX)
        else: self.widget['LabelX2'].setText('')
        if numZ: self.widget['LabelZ2'].setText(numZ)
        else: self.widget['LabelZ2'].setText('')
        if numX and numZ:
            if not (re.match('^[-|+]$',numX) or re.match('^[-|+]$',numZ)):
                self.string=mc_chunk_get(int(numX),int(numZ),string=True)
                self.widget['LabelResult'].setText(self.string)
        else: self.widget['LabelResult'].setText('')
    def clear_func(self):
        for widget in 'EditX','EditZ','LabelResult','LabelX2','LabelZ2':
            self.clear_text(widget)
    def clear_text(self,control):
       if self.widget[control].text():
            self.widget[control].setText('')
#endregion Self Functions            
#endregion Build Gui
#region Main
if __name__ == '__main__':
    MainApp=QApplication(sys.argv)
    MainApp.setStyle('Fusion')
    MainWindow=MainGui()
    MainWindow.show()
    # deskSize=QDesktopWidget().screenGeometry(-1)
    # MainWindow.move((deskSize.width()-MainWindow.width())-8,MainWindow.y()+90)
    sys.exit(MainApp.exec_())
#endregion Main
