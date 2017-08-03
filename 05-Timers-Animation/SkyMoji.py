"""
An example of animation using timers.

This program defines a custom widget that can read in Skype
resource images representing animated emoticons. The widget will
display and animate the emoticon.

Skype represents its emoticons as single png images, with each frame of
the emoticon animation appearing below the previous one. All emoticons
in skype are perfect squares (width=height)

References:
http://doc.qt.io/qt-5/qpainter.html
http://doc.qt.io/qt-5/qpixmap.html
http://doc.qt.io/qt-5/qrect.html
"""

from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPixmap, QPainter
from PyQt5.QtCore import QRect
import sys

class SkyMoji(QWidget):
    def __init__(self, imgpath, parent=None):
        super(SkyMoji, self).__init__(parent)
        self.currentFrame = 0
        self.setPixmap(QPixmap(imgpath))
        self.startTimer(1000 / 15) # animate at 15 fps

    def setPixmap(self, pix):
        self.pixmap = pix
        self.frameWidth = pix.rect().width()
        self.frameHeight = self.frameWidth # Skype emoticons are perfect squares
        self.numFrames = pix.rect().height() / self.frameHeight # Calculate number of frames in the animation
        self.resize(self.frameWidth, self.frameHeight)

    def paintEvent(self, event):
        qp = QPainter(self)
        ypos = self.frameHeight * self.currentFrame # which part of the image to display
        sourceRect = QRect(0, ypos, self.frameWidth, self.frameHeight)
        qp.drawPixmap(self.rect(), self.pixmap, sourceRect) # copy the part of the image in sourceRect to the canvas, scaling if necessary

    def timerEvent(self, event):
        self.currentFrame += 1
        if self.currentFrame == self.numFrames:
            self.currentFrame = 0 # start the animation back at frame 0
        self.update() # force the widget to redraw itself

if __name__ == '__main__':
    app = QApplication(sys.argv)
    filepath = "skype/img/fingerscrossed_anim@2x.png"
    mywidget = SkyMoji(filepath)
    mywidget.setGeometry(50, 50, 200, 200)
    mywidget.setWindowTitle("Fingers Crossed")
    mywidget.show()
    sys.exit(app.exec_())
