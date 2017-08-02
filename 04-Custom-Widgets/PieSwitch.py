"""
This program creates a custom 3-state Pie Switch widget.
The custom widget includes a custom signal called "changed",
that triggers whenever the user changes the selected pie segment.
The signal emits an integer representing which pie segment was
selected.

References:
http://pyqt.sourceforge.net/Docs/PyQt5/signals_slots.html
https://doc.qt.io/qt-5/qpainter.html
"""

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QObject, QPoint, QRect, pyqtSignal
from PyQt5.QtGui import QBrush, QPen, QColor, QFont, QPainter
import sys
import math

# Converts a QPoint to a point in polar coordinates
# Returns a tuple of (radius, theta(degrees))
def toPolar(point):
    x = point.x()
    y = point.y()
    radius = math.hypot(x,y)
    angle = math.degrees(math.atan(float(y) / x))
    if x < 0:
        angle += 180
    elif y < 0:
        angle += 360
    return radius, angle

class PieSwitch(QWidget):
    changed = pyqtSignal(int)

    def __init__(self, parent=None):
        super(PieSwitch, self).__init__(parent)
        self.selectedSlice = -1
        self.setMinimumSize(200, 200)
        self.setMaximumSize(200, 200)
        self.unselectedBrush = QBrush(Qt.gray)
        self.selectedBrush = QBrush(Qt.red)

    def setSlice(self, slicenumber):
        if slicenumber == 0 or slicenumber == 1 or slicenumber == 2:
            if self.selectedSlice != slicenumber:
                self.selectedSlice = slicenumber
                self.changed.emit(self.selectedSlice) # notify all listeners
                self.update() # redraw the widget

    def paintEvent(self, event):
        qp = QPainter(self)
        bounds = self.rect()
        qp.setBrush(self.unselectedBrush)
        if self.selectedSlice is 0:
            qp.setBrush(self.selectedBrush)
        qp.drawPie(bounds, 0, -120*16)
        qp.setBrush(self.unselectedBrush)
        if self.selectedSlice is 1:
            qp.setBrush(self.selectedBrush)
        qp.drawPie(bounds, -120*16, -120*16)
        qp.setBrush(self.unselectedBrush)
        if self.selectedSlice is 2:
            qp.setBrush(self.selectedBrush)
        qp.drawPie(bounds, -2*120*16, -120*16)


    def mousePressEvent(self, event):
        w = self.rect().width()
        h = self.rect().height()
        # Convert the x,y position of the mouse to a point on the circle
        circleCenter = QPoint(w / 2, h / 2)
        radius, angle = toPolar(event.pos() - circleCenter)
        if radius < 100:
            # The mouse is inside the circle, divide by 120 to get the pie piece
            pie = int(angle / 120)
            self.setSlice(pie)

class MyWin(QWidget):
    def __init__(self):
        super(MyWin, self).__init__()
        self.initGUI()

    def initGUI(self):
        self.setWindowTitle("Pie Switch")
        switch = PieSwitch()
        spinbox = QSpinBox()
        spinbox.setMaximum(2)
        spinbox.setStyleSheet("QSpinBox {font-size: 72px;font-weight: bold;}")
        switch.changed.connect(spinbox.setValue)
        spinbox.valueChanged.connect(switch.setSlice)
        layout = QVBoxLayout()
        layout.addWidget(switch)
        layout.addWidget(spinbox)
        self.setLayout(layout)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mywin = MyWin()
    sys.exit(app.exec_())
