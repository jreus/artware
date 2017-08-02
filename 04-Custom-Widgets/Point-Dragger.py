"""
Illustration of QRect used in worksheet.

References:
http://pyqt.sourceforge.net/Docs/PyQt5/signals_slots.html
https://doc.qt.io/qt-5/qbrush.html
https://doc.qt.io/qt-5/qpen.html
https://doc.qt.io/qt-5/qpainter.html
https://doc.qt.io/qt-5/qwidget.html
https://doc.qt.io/qt-5/qrect.html
https://doc.qt.io/qt-5/qtwidgets-widgets-scribble-example.html
"""

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QObject, QPoint, QRect, pyqtSignal
from PyQt5.QtGui import QBrush, QPen, QColor, QFont, QPainter
import sys

class Handle(QObject):
    handleMoved = pyqtSignal(QPoint)

    def __init__(self, label, xpos, ypos, radius):
        super(Handle, self).__init__()
        self.pos = QPoint(xpos, ypos)
        self.label = label
        self.radius = radius
    def __str__(self):
        stringval = "%s (%d, %d)" % (self.label, self.pos.x(), self.pos.y())
        return stringval
    def setPos(self, newpos):
        self.pos.setX(newpos.x())
        self.pos.setY(newpos.y())
        self.handleMoved.emit(self.pos)
    def x(self):
        return self.pos.x()
    def y(self):
        return self.pos.y()
    def bounds(self):
        return QRect(self.x()-self.radius, self.y()-self.radius, self.radius * 2, self.radius * 2)

class XYGraph(QWidget):
    def __init__(self, parent=None):
        super(XYGraph, self).__init__(parent)
        self.handleBrush = QBrush(QColor(255, 184, 0))
        self.backgroundBrush = QBrush(Qt.white)
        self.linePen = QPen(Qt.SolidLine)
        self.linePen.setWidth(2)
        self.currentHandle = None
        self.dragStartPos = None
        self.setMinimumSize(400, 200)
        self.handles = [Handle('H1',70,80,5), Handle('H2',140,130,7), Handle('H3',270,60,9), Handle('H4',350,150,11)] # 4 handles each represented by a QPoint

    # This method gets called every time an Outline needs to draw itself
    # to the screen.
    def paintEvent(self, event):
        qp = QPainter(self)
        qp.setPen(self.linePen)
        qp.setBrush(self.backgroundBrush)
        qp.drawRect(self.rect()) # draw an outline around the graph
        qp.setBrush(self.handleBrush)
        lasthandle = None
        for handle in self.handles:
            qp.drawEllipse(handle.bounds())
            if lasthandle != None:
                qp.drawLine(lasthandle.x(), lasthandle.y(), handle.x(), handle.y())
            lasthandle = handle

    def mousePressEvent(self, event):
        mouseX = event.pos().x()
        mouseY = event.pos().y()
        # Check if the mouse is inside the bounds of a handle
        self.currentHandle = None
        for handle in self.handles:
            h = handle.bounds()
            if mouseX > h.left() and mouseX < h.right() and mouseY > h.top() and mouseY < h.bottom():
                # mouse is inside this handle's bounding box
                print "Start Dragging!"
                self.currentHandle = handle
                self.dragStartPos = QPoint(handle.x(), handle.y())
                break

    def mouseMoveEvent(self, event):
        if self.currentHandle != None:
            w = self.width()
            h = self.height()
            mouse = event.pos()
            if  mouse.x() > 0 and mouse.x() < w and mouse.y() > 0 and mouse.y() < h:
                self.currentHandle.setPos(mouse)
            else:
                self.currentHandle.setPos(self.dragStartPos)
                self.dragStartPos = None
                self.currentHandle = None
            self.update()


    def mouseReleaseEvent(self, event):
        if self.currentHandle != None:
            self.currentHandle = None
            print "Stop Dragging!"

class HandleLabel(QLabel):
    def __init__(self, handle):
        super(HandleLabel, self).__init__()
        self.label = handle.label
        self.updateLabel(handle.pos)
        self.setMinimumSize(100, 50)
        handle.handleMoved.connect(self.updateLabel)

    def updateLabel(self, handle):
        text = "%s: %d, %d" % (self.label, handle.x(), handle.y())
        self.setText(text)

class MyWin(QWidget):
    def __init__(self):
        super(MyWin, self).__init__()
        self.initGUI()

    def initGUI(self):
        mainlayout = QVBoxLayout()
        sublayout = QHBoxLayout()
        graph = XYGraph()
        # Make widgets for all the handles
        for handle in graph.handles:
            sublayout.addWidget(HandleLabel(handle))
        mainlayout.addWidget(graph)
        mainlayout.addLayout(sublayout)
        self.setLayout(mainlayout)
        self.setWindowTitle("Custom XY Graph Widget")
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mywin = MyWin()
    sys.exit(app.exec_())
