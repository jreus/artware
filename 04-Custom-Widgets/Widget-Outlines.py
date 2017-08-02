"""
Illustration of QRect used in worksheet.

References:
https://doc.qt.io/qt-5/qbrush.html
https://doc.qt.io/qt-5/qpen.html
https://doc.qt.io/qt-5/qpainter.html
https://doc.qt.io/qt-5/qwidget.html
https://doc.qt.io/qt-5/qrect.html
"""

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QBrush, QPen, QColor, QFont, QPainter
import sys

class Outline(QWidget):
    def __init__(self, parent):
        super(Outline, self).__init__(parent)
        self.brush = QBrush(QColor(255, 184, 0), Qt.DiagCrossPattern)
        self.pen = QPen(Qt.DashLine)
        self.pen.setWidth(5.5)
        self.font = QFont("Arial", 18, QFont.Medium)
        self.text = ""

    # This method gets called every time an Outline needs to draw itself
    # to the screen.
    def paintEvent(self, event):
        outline = self.rect()
        qp = QPainter(self)
        qp.setPen(self.pen)
        qp.setBrush(self.brush)
        qp.setFont(self.font)
        qp.drawRect(outline) # draw a rectangle on the bounding box of this widget
        # Compose a string with the width and height of the outline
        text = "width, height\n(%d, %d)"
        text = text % (outline.width(), outline.height())
        qp.drawText(outline, Qt.AlignCenter, text) # draw the text inside the widget

class MyWin(QWidget):
    def __init__(self):
        super(MyWin, self).__init__()
        self.initGUI()

    def initGUI(self):
        self.setWindowTitle("Widget Outlines")
        height = 200
        width = 500
        self.setGeometry(0,0, width, height)
        widget1 = Outline(self)
        widget1.setGeometry(5, 5, width-10, height/2-10)
        widget2 = Outline(self)
        widget2.setGeometry(5, height/2, (width-20)/3, height/2-10)
        widget3 = Outline(self)
        widget3.setGeometry(width / 3 + 5, height/2, (width-20)/3, height/2-10)
        widget4 = Outline(self)
        widget4.setGeometry((width / 3)*2 + 5, height/2, (width-20)/3, height/2-10)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mywin = MyWin()
    sys.exit(app.exec_())
