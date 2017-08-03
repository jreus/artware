"""
This program gives an example of using the built-in timer functionality of
all QObjects. Qt provides this because it's such a common need to have an interval
timer running in GUI elements. e.g. for animation (think: emojis) or to run background
tasks like updating an interface from a network resource.

Click & Drag to change the color change rates

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

"""

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QColor, QBrush, QPainter
from random import randint
import sys

class ColorCircle(QWidget):
    def __init__(self, parent=None):
        super(ColorCircle, self).__init__(parent)
        self.color = [randint(0,255), randint(0,255), randint(0,255)] # red green blue values
        self.changeBy = [-7, 5, 12] # red green blue change per frame
        self.frameDelayMillis = 50  # timer interval in millis
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
        qp.drawEllipse(rect)

    # This method is called when the internal timer of this QWidget times out
    def timerEvent(self, event):
        self.updateColor()
        self.update() # force the widget to redraw itself

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
        self.circle1 = ColorCircle(self)
        self.circle2 = ColorCircle(self)
        self.circle3 = ColorCircle(self)
        self.setWindowTitle("RGBRGBRGBRGBRGBRGBRGBRGBRGBRGBRGBRGBRGBRGBRGB")
        h = qApp.desktop().screenGeometry().height() - 100
        w = qApp.desktop().screenGeometry().width() - 100
        self.setGeometry(20, 20, w, h)
        #self.setMinimumSize(w-100, h-100)
        self.circle1.setGeometry(10, 10, w/3, w/3)
        self.circle2.setGeometry(w-w/3, 30, w/3, w/3)
        self.circle3.setGeometry(w-((2*w)/3), h-(w/3), w/3.3, w/3.3)
        self.setWindowFlags(Qt.FramelessWindowHint) # needed to get transparent window in Windows
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setMouseTracking(True) # always follow mouse movement even when not clicked, might not work on Windows
        self.show()

    def mouseMoveEvent(self, event):
        mx = event.pos().x()
        my = event.pos().y()
        self.circle1.setSpeed(mx / float(abs(my)+1)) # protect against division by 0 errors
        self.circle2.setSpeed(mx / 100.0)
        self.circle3.setSpeed(my / 100.0)
        print "Move: %f, %f" % (mx, my)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mywin = MyWin()
    sys.exit(app.exec_())
