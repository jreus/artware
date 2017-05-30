# -*- coding: utf-8 -*-
"""
This program creates an interface with two buttons.
The left button will randomly set some style values on the right.
"""

from PyQt5.QtWidgets import *
from random import randint, choice
import sys

class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.initGUI()

    def initGUI(self):
        self.setObjectName("main")
        # self.setStyleSheet("""
        # QWidget#main {
        #     background-color: qlineargradient(x1:0, y2:0, x2:0, y2:1,
        #                         stop: 0 #bca6c2, stop: 1 #c9ab68);
        #     padding: 20px;
        # }
        # """)
        self.setStyleSheet("""
        QWidget#main {
            background-color: lightgrey;
        }
        """)
        button1 = QPushButton("Button 1")
        button1.setStyleSheet("""
            QPushButton {
                background-color: black;
                color: white;
                border: 2px solid white;
                height: 50px;
                min-width: 100px;
                max-width: 100px;
                border-radius: 20px;
            }
            QPushButton:pressed {
                background-color: red;
            }
            QPushButton:hover {
                border: 5px solid #33AAFF;
            }
        """)
        button1.clicked.connect(self.buttonClick)
        self.button2 = QPushButton("Button 2")

        layout = QHBoxLayout()
        layout.addWidget(button1)
        layout.addWidget(self.button2)
        self.setLayout(layout)
        self.setWindowTitle("Some Styled Widgets")
        self.show()

    def buttonClick(self):
        newstyle = """
            QPushButton {
                background-color: white;
                font-size: %dpx;
                padding: %dpx;
                margin: %dpx;
                border: %dpx solid grey;
                font-family: %s;
            }
        """ % (randint(6, 48),
                randint(0, 20),
                randint(0, 20),
                randint(0, 20),
                choice(["Times New Roman","Georgia", "Monaco"]))
        self.button2.setStyleSheet(newstyle)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyWindow()
    sys.exit(app.exec_())
