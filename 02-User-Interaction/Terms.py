"""
A more interesting use of signals and slots, here instead of using built-in
slots we use our own custom functions.

For more information on Box Layouts: https://doc.qt.io/qt-5/qboxlayout.html

"""


from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import sys
from random import randint

class MyWin(QWidget):
    width = 500
    height = 600

    def __init__(self):
        super(MyWin, self).__init__()
        self.initGUI()

    def initGUI(self):
        self.buttons = []

        self.scrollText = QTextEdit()
        self.viewterms = QPushButton("View the Terms and Conditions")
        self.viewterms.clicked.connect(self.loadTerms)

        # Set up the layouts
        vbox = QVBoxLayout()
        vbox.addWidget(self.scrollText)
        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.addWidget(self.viewterms, alignment=Qt.AlignLeft)
        vbox.addLayout(self.buttonLayout)
        self.setLayout(vbox)

        self.setGeometry(0,0, self.width, self.height)
        self.setWindowTitle('What Would you Like to Do?')
        self.show()

    def loadTerms(self):
        # Load the terms & conditions HTML into the QTextEdit widget
        fp = open("terms.html", 'r')
        filetext = fp.read()
        self.scrollText.setHtml(filetext)
        fp.close()

        # Set up the new buttons
        self.viewterms.setVisible(False)
        accept = QPushButton("Accept")
        accept.clicked.connect(self.acceptPush)
        deny = QPushButton("Don't Accept")
        deny.clicked.connect(self.denyPush)
        self.buttonLayout.addWidget(accept, alignment=Qt.AlignLeft)
        self.buttonLayout.addWidget(deny, alignment=Qt.AlignLeft)
        self.buttonLayout.addStretch(1)
        self.setWindowTitle("Do You Accept the Terms and Conditions?")

    def scatter(self):
        for but in self.buttons:
            but.move(randint(50, self.width - 100), randint(50, self.height - 50))

    def acceptPush(self):
        for i in range(3):
            newbut = QPushButton(self)
            newbut.setText("Accept")
            newbut.clicked.connect(self.acceptPush)
            newbut.setVisible(True)
            self.buttons.append(newbut)
        self.scatter()

    def denyPush(self):
        for i in range(3):
            newbut = QPushButton(self)
            newbut.setText("Don't Accept")
            newbut.setMinimumWidth(120) # this button is a little bigger
            newbut.clicked.connect(self.denyPush)
            newbut.setVisible(True)
            self.buttons.append(newbut)
        self.scatter()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyWin()
    sys.exit(app.exec_())
