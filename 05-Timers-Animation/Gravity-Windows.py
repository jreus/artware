"""
An example of using a QTimer in interval mode to do some animation.
In this program a custom subclass of QWidget is made that has its own
internal QTimer that times out repeatedly 12 times a second.

The timeout signal of the QTimer is connected to an animate method that
applies some basic gravity physics to the window (velocity & acceleration).

When the window hits the bottom boundary of the screen it plays a familiar sound.


Sounds are played using PyQt5.QtMultimedia.QSoundEffect
References on QSound and QSound:
http://pyqt.sourceforge.net/Docs/PyQt5/api/qsound.html
https://doc.qt.io/qt-5/qsound.html

References on QTimer
http://pyside.github.io/docs/pyside/PySide/QtCore/QTimer.html

"""

from PyQt5.QtWidgets import QApplication, qApp, QWidget
from PyQt5.QtCore import QTimer, QUrl
from PyQt5.QtMultimedia import QSound
import sys

class GravityWindow(QWidget):
    def __init__(self, xpos, ypos, title):
        super(GravityWindow, self).__init__()
        self.acceleration = 5.0
        self.velocity = 0.0
        self.screenHeight = qApp.desktop().availableGeometry().height() # height of the screen
        self.sound = QSound("sounds/Sosumi.wav")
        self.makeWin(xpos, ypos, title)

    def makeWin(self, xpos, ypos, title):
        self.setGeometry(xpos, ypos, 200, 100)
        self.setWindowTitle(title)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.animateFrame)
        self.timer.start(1000 / 12) # 12 frames per second

    # this function gets called 12 times per second
    def animateFrame(self):
        xpos = self.pos().x()
        ypos = self.pos().y() + self.velocity # move the ypos a little bit
        if (ypos + self.height()) > self.screenHeight:
            ypos = self.screenHeight - self.height()
            if abs(self.velocity) <= self.acceleration:  # when the velocity is very small, just set it to 0.0 to keep from infinite bouncing
                self.velocity = 0.0
            else:
                self.sound.play()
                self.velocity *= -0.5 # velocity of movement changes direction
        self.move(xpos, ypos)
        self.velocity += self.acceleration


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet("""
            GravityWindow {
                background-color: qlineargradient(x1:0,y1:0,x2:0,y2:1, stop: 0 #ffffff, stop: 1 #333333);
            }
        """)
    win1 = GravityWindow(50, 500, "Humpty")
    win2 = GravityWindow(400, 0, "Dumpty")
    win1.show()
    win2.show()
    sys.exit(app.exec_())
