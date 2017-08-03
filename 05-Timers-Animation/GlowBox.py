"""
This program gives an example of using the built-in timer functionality of
all QObjects. Qt provides this because it's such a common need to have an interval
timer running in GUI elements. e.g. for animation (think: emojis) or to run background
tasks like updating an interface from a network resource.

Click & Drag to change the color change rate

A custom widget (ColorBox) is created that makes a solid-color window with slowly fading
background colors. The speed of the color change can be set using the setSpeed
method of the ColorBox widget. This is done by using the built-in killTimer method.

The ColorBox widget also shows how you can use Qt's drawing API (QPainter) and the
QWidget method paintEvent to draw custom shapes and images to a widget canvas.

A final built-in method of QWidget, resizeEvent is used to react to the user
resizing the window.

References for startTimer:
http://doc.qt.io/qt-5/qobject.html#startTimer
http://doc.qt.io/qt-5/timers.html

References for QPainter and the drawing API:
http://zetcode.com/gui/pyqt5/painting/
http://doc.qt.io/qt-5/qpainter-members.html

References:
http://doc.qt.io/qt-5/qdesktopwidget.html#details
http://doc.qt.io/qt-5/qwidget.html#showFullScreen

"""

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QColor, QBrush, QPainter, QKeySequence
from random import randint
import sys

class GlowBox(QWidget):
    def __init__(self, parent=None):
        super(GlowBox, self).__init__(parent)
        self.color = [randint(0,255), randint(0,255), randint(0,255)] # red green blue values
        self.changeBy = [-7, 5, 12] # red green blue change per frame
        self.frameDelayMillis = 1000 / 60  # 60 frames per second
        self.timerID = self.startTimer(self.frameDelayMillis) # start the built-in timer

    # paintEvent is the method you use to paint shapes directly to the
    # canvas of the widget
    def paintEvent(self, event):
        qp = QPainter(self) # QPainter has all the drawing commands
        rect = self.rect()
        color = QColor(self.color[0], self.color[1], self.color[2])
        brush = QBrush(color, Qt.SolidPattern)
        qp.setBrush(brush)
        qp.setPen(Qt.NoPen)
        qp.drawRect(rect)

    # This method is called when the internal timer of this QWidget times out
    def timerEvent(self, event):
        self.updateColor()
        self.update() # force the widget to redraw itself

    # Here's where the animation frame update happens
    def updateColor(self):
        for i in [0,1,2]:
            self.color[i] = self.color[i] + self.changeBy[i]
            if self.color[i] < 0:
                self.color[i] = 0
                self.changeBy[i] *= -1 # reverse direction
            elif self.color[i] > 255:
                self.color[i] = 255
                self.changeBy[i] *= -1 # reverse direction

    def setSpeed(self, frameDelay):
        self.killTimer(self.timerID)
        self.frameDelayMillis = frameDelay
        self.timerID = self.startTimer(self.frameDelayMillis)

class MyWin(QWidget):
    def __init__(self):
        super(MyWin, self).__init__()
        self.makeWindow()

    def makeWindow(self):
        self.setWindowTitle("RGB")
        h = qApp.desktop().screenGeometry().height() - 100
        w = qApp.desktop().screenGeometry().width() - 100
        self.speedFactor = w / 50
        self.setGeometry(20, 20, w, h)
        self.box = GlowBox(self)
        self.box.resize(w,h)
        self.show()

    def resizeEvent(self, event):
        self.box.resize(self.rect().width(), self.rect().height())

    def mouseMoveEvent(self, event):
        xpos = abs(event.pos().x())
        print "X Pos: ", xpos
        self.box.setSpeed(max(xpos / float(self.speedFactor), 1))

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_F:
            self.toggleFS()

    def toggleFS(self):
        if self.isFullScreen():
            self.showNormal()
        else:
            self.showFullScreen()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mywin = MyWin()
    sys.exit(app.exec_())
