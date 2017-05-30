# -*- coding: utf-8 -*-
"""
Add the above line to be able to use unicode text directly in your programs.

This program shows some examples of how you can use cascading style sheets (CSS)
to style the basic Qt widgets. Many of the standard widgets in Qt can be styled
using CSS.

Useful links:
Python Format Strings: https://pyformat.info/
Stylesheet Syntax: http://doc.qt.io/qt-5/stylesheet-syntax.html
Reference: http://doc.qt.io/qt-5/stylesheet-reference.html
Stylesheet Box Model: http://doc.qt.io/qt-5/stylesheet-customizing.html#box-model
Stylesheet Examples: http://doc.qt.io/qt-5/stylesheet-examples.html
CSS: https://www.w3schools.com/css/css_font.asp
CSS Backgrounds: https://www.w3schools.com/css/css_background.asp

"""

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from random import randint
import sys

class MyWin(QMainWindow):
    def __init__(self):
        super(MyWin, self).__init__()
        self.initGUI()

    def initGUI(self):
        mainLayout = QVBoxLayout()
        centerWidget = QWidget()
        centerWidget.setObjectName("parent")
        centerWidget.setLayout(mainLayout)
        self.setCentralWidget(centerWidget)
        self.setWindowTitle("Load Styles from a .css File")

        b1 = QPushButton("Button1")
        b1.setObjectName("button1")
        b2 = QPushButton("Button2")
        b2.setObjectName("button2")
        b3 = QPushButton("Button3")
        b3.setObjectName("button3")
        b3.setStyleSheet("""
            QPushButton {
                background-color: blue;
                color: white;
                font-style: bold;
            }
            QPushButton:pressed { background-color: red; }
        """)
        layh = QHBoxLayout()
        layh.addWidget(b1)
        layh.addWidget(b2)
        layh.addWidget(b3)
        hGroupbox = QGroupBox("Buttons")
        hGroupbox.setObjectName("buttonbox")
        hGroupbox.setLayout(layh)
        mainLayout.addWidget(hGroupbox)

        self.stylePicker = QComboBox()
        self.stylePicker.addItem("System Default")
        self.stylePicker.addItem("style01.css")
        self.stylePicker.addItem("style02.css")
        self.stylePicker.setCurrentIndex(0)
        self.stylePicker.currentIndexChanged.connect(self.updateStyle)
        layForm = QFormLayout()
        layForm.addRow(QLabel("Choose a Style:"), self.stylePicker)
        layForm.addRow(QLabel("Line 1:"), QLineEdit())
        layForm.addRow(QLabel("Line 2, long text:"), QLineEdit())
        layForm.addRow(QLabel("Line 3:"), QSpinBox())
        formGroupBox = QGroupBox("Form Fields")
        formGroupBox.setObjectName("formbox")
        formGroupBox.setLayout(layForm)
        mainLayout.addWidget(formGroupBox)

    def updateStyle(self):
        newStyle = self.stylePicker.currentText()
        if(newStyle == "System Default"):
            qApp.setStyleSheet("")# remove all stylesheets
        else:
            fp = open("css/" + newStyle)
            qApp.setStyleSheet(fp.read()) # set global stylesheet of qApp
            fp.close()

if __name__=="__main__":
    app = QApplication(sys.argv)
    win = MyWin()
    win.show()
    sys.exit(app.exec_())
