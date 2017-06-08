"""
This program gives an example of using the built-in timer functionality of
all QObjects. Qt provides this because it's such a common need to have an interval
timer running in GUI elements. e.g. for animation (think: emojis) or to run background
tasks like updating an interface from a network resource.

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

"""

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QBrush, QPainter
from random import randint
import sys

class ColorBox(QWidget):
    def __init__(self, parent=None):
        super(ColorBox, self).__init__(parent)
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
        self.box1 = ColorBox()
        self.box2 = ColorBox()
        self.box3 = ColorBox()
        self.slider1 = QSlider()
        self.slider1.valueChanged.connect(self.box1.setSpeed)
        self.slider1.setRange(1, 100)
        self.slider1.setValue(50)
        self.slider1.setOrientation(Qt.Horizontal)
        self.slider2 = QSlider()
        self.slider2.valueChanged.connect(self.box2.setSpeed)
        self.slider2.setRange(1, 100)
        self.slider2.setValue(50)
        self.slider2.setOrientation(Qt.Horizontal)
        self.slider3 = QSlider()
        self.slider3.valueChanged.connect(self.box3.setSpeed)
        self.slider3.setRange(1, 100)
        self.slider3.setValue(50)
        self.slider3.setOrientation(Qt.Horizontal)

        lay = QGridLayout()
        lay.setSpacing(0)
        lay.setContentsMargins(0,0,0,0)
        lay.addWidget(self.box1,    0,0)
        lay.addWidget(self.box2,    0,1)
        lay.addWidget(self.box3,    0,2)
        lay.addWidget(self.slider1, 1,0)
        lay.addWidget(self.slider2, 1,1)
        lay.addWidget(self.slider3, 1,2)
        self.setLayout(lay)

        title = ""
        for i in range(200):
            title += "RGB"
        self.setWindowTitle(title)
        self.setGeometry(0,0,700, 300)
        self.show()

    def resizeEvent(self, event):
        dim = self.rect().width() / 3
        self.box1.resize(dim, dim)
        self.box2.resize(dim, dim)
        self.box3.resize(dim, dim)

    def sliderChanged(self):
        val = self.slider.value()
        self.lightbox.setSpeed(int(val))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet("""
        QWidget {
            background-color: white;
        }
        ColorBox {
            margin-bottom: 10px;
        }
        QSlider {
            min-width: 100px;
        }
    """)
    mywin = MyWin()
    sys.exit(app.exec_())
