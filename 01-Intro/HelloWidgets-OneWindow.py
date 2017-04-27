import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QLabel
from PyQt5.QtGui import QPixmap

class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.initGUI()

    def initGUI(self):
        self.setGeometry(0, 0, 600, 560)
        self.setWindowTitle("Safari Extension")
        w1 = MyWidget(self, "white", 0,0)
        w2 = MyWidget(self, "inv", 0,300)
        w3 = MyWidget(self, "white", 300,0)
        w4 = MyWidget(self, "inv", 300,300)
        self.show()


class MyWidget(QWidget):
    def __init__(self, parent, color="white", xpos=0, ypos=0):
        super(MyWidget, self).__init__(parent)
        self.initGUI(color, xpos, ypos)

    def initGUI(self, color, xpos, ypos):
        self.setGeometry(0, 0, 260, 260)
        self.setWindowTitle("Safari Extension")
        self.button1 = QPushButton(self)
        self.button1.setText("Help!")
        self.text1 = QLineEdit(self)
        self.text1.setText("Hello Widgets")
        if(color == "white"):
            pix1 = QPixmap("safariextz.png")
        else:
            pix1 = QPixmap("safariextz_inv.png")
        self.img1 = QLabel(self)
        self.img1.setPixmap(pix1)
        self.text1.move(20, 200)
        self.button1.move(170, 180)
        self.move(xpos, ypos)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywin = MyWindow()
    sys.exit(app.exec_())
