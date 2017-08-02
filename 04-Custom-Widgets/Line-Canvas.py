"""
Line Drawer

References:
https://doc.qt.io/qt-5/qbrush.html
https://doc.qt.io/qt-5/qpen.html
https://doc.qt.io/qt-5/qpainter.html
https://doc.qt.io/qt-5/qwidget.html
https://doc.qt.io/qt-5/qrect.html
"""

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QLine
from PyQt5.QtGui import QBrush, QPen, QColor, QFont, QPainter
import sys

class LineDrawCanvas(QWidget):
    def __init__(self, parent=None):
        super(LineDrawCanvas, self).__init__(parent)
        self.setMinimumSize(200, 200)
        self.linePen = QPen(Qt.SolidLine)
        self.linePen.setColor(Qt.magenta)
        self.linePen.setWidth(6)
        self.drawingPen = QPen(Qt.DashLine)
        self.drawingPen.setColor(Qt.cyan)
        self.drawingPen.setWidth(3)
        self.currentLine = None
        self.lines = []

    def reset(self):
        self.lines = []
        self.update()

    def paintEvent(self, event):
        qp = QPainter(self)
        qp.setPen(QPen(Qt.black))
        qp.setBrush(QBrush(Qt.white))
        bounds = self.rect()
        qp.drawRect(0, 0, bounds.width()-1, bounds.height()-1) # draw an outline around the graph

        qp.setPen(self.linePen)
        for line in self.lines:
            qp.drawLine(line)

        if self.currentLine != None:
            qp.setPen(self.drawingPen)
            qp.drawLine(self.currentLine)

    def mousePressEvent(self, event):
        self.currentLine = QLine(event.pos(), event.pos()) # start a new line

    def mouseMoveEvent(self, event):
        if self.currentLine != None:
            self.currentLine.setP2(event.pos()) # update the second point of the line
            self.update() # redraw the widget to show the updated line

    def mouseReleaseEvent(self, event):
        if self.currentLine != None:
            # Turn the currentLine into a permanent line
            self.lines.append(self.currentLine)
            self.currentLine = None
            self.update()

class MyWin(QWidget):
    def __init__(self):
        super(MyWin, self).__init__()
        self.initGUI()

    def initGUI(self):
        self.setWindowTitle("Drag N Draw")
        layout = QVBoxLayout()
        self.setLayout(layout)
        canvas = LineDrawCanvas()
        resetButton = QPushButton("Erase")
        resetButton.setMaximumWidth(100)
        resetButton.pressed.connect(canvas.reset)
        layout.addWidget(canvas)
        layout.addWidget(resetButton)
        self.setGeometry(0,0, 600, 600)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mywin = MyWin()
    sys.exit(app.exec_())
