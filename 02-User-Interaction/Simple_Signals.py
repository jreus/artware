"""
A simple app with a text field and two buttons. The program illustrates the basics
of using Qt's signals and slots system to design an interactive interface.

One button prints whatever is in the text field to the terminal.
The other button clears the text field.

Useful references:
QFont:
"""

from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton
from PyQt5.QtGui import QFont
import sys

class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0,0,300,150)
        self.setWindowTitle('MyApp')
        self.text = QLineEdit(self)
        self.text.setGeometry(10,10,280,50)
        self.text.setFont(QFont("Times", 30, QFont.Bold, True))
        self.text.setText("Type Something")
        self.but1 = QPushButton("Print", self)
        self.but1.setGeometry(0,70,150,80)
        self.but1.clicked.connect(self.printText)
        self.but2 = QPushButton("Clear", self)
        self.but2.setGeometry(150,70,150,80)
        self.but2.clicked.connect(self.text.clear)
        self.show()

    def printText(self):
        print self.text.text()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mywin = MyWindow()
    sys.exit(app.exec_())
