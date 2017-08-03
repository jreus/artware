"""
Basic Example of using a QTimer to call a function in the future.
Uses a one shot timer to create a digital version of Claude Shannon's "Ultimate Machine"
The interface is a single button inside a transparent window. The program triggers
a QTimer to go off 2 seconds after you've pressed the button, and unclicks it.

The button is given toggle behavior by setting its checkable property to true.

Module:
PyQt5.QtCore.QTimer

References:
https://www.youtube.com/watch?v=cZ34RDn34Ws
http://pyqt.sourceforge.net/Docs/PyQt5/api/qtimer.html
https://ralsina.me/weblog/posts/BB974.html
http://doc.qt.io/qt-5/qtimer.html

"""

from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer, Qt
import sys

class MyWindow(QWidget):
    buttonStyle = """
        QPushButton {
            font-size: 24px;
            font-weight: bold;
            background-color: grey;
            border-radius: 20px;
            border: 6px dashed lightgrey;
            margin: 30px;
            max-width: 200px;
            max-height: 100px;
        }
        QPushButton:checked {
            background-color: #a7e1e4;
        }
    """

    def __init__(self):
        super(MyWindow, self).__init__()
        self.timer = QTimer(self)
        self.timer.setSingleShot(True) # give the timer one-shot behavior
        self.timer.timeout.connect(self.unclick) #connect timeout to our unclick method
        self.makeWindow()

    def makeWindow(self):
        self.but = QPushButton("PRESS ME", self)
        self.but.setGeometry(self.rect())
        self.but.clicked.connect(self.turnOn)
        self.but.setStyleSheet(self.buttonStyle)

        self.setWindowTitle("The Ultimate Button")
        self.setWindowFlags(Qt.FramelessWindowHint) # needed to get transparent window in Windows
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.show()

    def turnOn(self):
        self.but.setText("PRESSED")
        #self.timer.start(2000) # 2 second delay
        self.but.setStyleSheet("""
            QPushButton {
                font-size: 24px;
                font-weight: bold;
                background-color: #a7e1e4;
                border-radius: 20px;
                border: 6px dashed lightgrey;
                margin: 30px;
                max-width: 200px;
                max-height: 100px;
            }
        """)

    def unclick(self):
        self.but.setText("PRESS ME")
        self.but.setChecked(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mywin = MyWindow()
    sys.exit(app.exec_())
