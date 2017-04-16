#   Uses the more common object-oriented approach to Qt programming
#       Qt is designed with the expectation that you will extend the core
#       classes.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton

class MyMainWindow(QWidget):

    def __init__(self):
        super(MyMainWindow, self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('My App')
        self.label1 = QLabel(self)
        self.label1.setText("Hello World")
        self.button1 = QPushButton(self)
        self.button1.setText("Push Me")
        self.button1.move(0, 20)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MyMainWindow()
    win.show()
    sys.exit(app.exec_())
