import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QLabel
from PyQt5.QtGui import QPixmap

class MyWindow(QWidget):
    def __init__(self, color="white", xpos=0, ypos=0):
        super(MyWindow, self).__init__()
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
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywin1 = MyWindow("white")
    mywin2 = MyWindow("inv", 360, 0)
    mywin3 = MyWindow("white", 0, 350)
    mywin4 = MyWindow("inv", 360, 350)
    sys.exit(app.exec_())
