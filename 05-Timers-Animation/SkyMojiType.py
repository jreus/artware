"""
An emoticon typing app, that turns your keystrokes into skype resources.

The fanciest thing going on in this program is the decoding of Qt key constants
to emoticons inside the keyPressEvent() method.

All of the Qt key constants are actually just integers.
( see: http://doc.qt.io/qt-5/qt.html#Key-enum for a full list )
and this program takes advantage of this by translating a range of
key constants, from 0x21 to 0x5A (33-90), down to a range from 0-57
that can be used directly as list indexes.

This program also introduces a useful python module: glob
Glob lets you quickly pick out files in a directory that match a certain
naming pattern or have a specific file format. Here we use glob to get
all the png files that have "anim" in their file name. This is skype's
naming convention for animated image resources.

The program prints to the console how many animated resources it finds,
notice that we're not even using more than half. How could we use more
of them?

References:
https://docs.python.org/2/library/glob.html
http://doc.qt.io/qt-5/qkeyevent.html
http://doc.qt.io/qt-5/qt.html#Key-enum
http://doc.qt.io/qt-5/qt.html#KeyboardModifier-enum
http://doc.qt.io/qt-5/qpainter.html
"""

from PyQt5.QtWidgets import QWidget, QApplication, qApp
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen
import sys
import glob
from SkyMoji import SkyMoji

class TypingWindow(QWidget):
    charSpace = 30
    tabSize = 4

    def __init__(self):
        super(TypingWindow, self).__init__()
        self.setWindowTitle("SkyMojiType")
        h = qApp.desktop().screenGeometry().height() - 200
        w = qApp.desktop().screenGeometry().width() - 200
        self.setGeometry(w/10, h/10, w, h)
        self.lineLength = w / self.charSpace
        self.charCount = 0
        self.cursorVisible = True
        self.emojis = []
        self.allImages = glob.glob("skype/img/*anim*.png") # grab all file names containing 'anim' and ending in .png
        print "Total Animated Files Found: ", len(self.allImages)
        # Uncomment the following lines to make the typing window transparent
        #self.setWindowFlags(Qt.FramelessWindowHint) # needed to get transparent window in Windows
        #self.setAttribute(Qt.WA_TranslucentBackground)
        self.startTimer(200) # Animation timer for cursor, don't save the ID as we don't plan to kill it
        self.show()

    def timerEvent(self, event):
        if self.cursorVisible:
            self.cursorVisible = False
        else:
            self.cursorVisible = True
        self.update() # redraw yourself!

    def paintEvent(self, event):
        qp = QPainter(self)
        if self.cursorVisible:
            pen = QPen(Qt.magenta)
            pen.setWidth(5)
            qp.setPen(pen)
            xpos = (self.charCount % self.lineLength) * self.charSpace
            ypos = (self.charCount / self.lineLength) * self.charSpace
            qp.drawLine(xpos, ypos, xpos, ypos + self.charSpace)

    def keyPressEvent(self, event):
        key = event.key()
        if key == Qt.Key_Space:
            self.charCount += 1
        elif key == Qt.Key_Return or key == Qt.Key_Enter:
            self.charCount = ((self.charCount / self.lineLength) + 1) * self.lineLength
        elif key == Qt.Key_Tab:
            self.charCount += self.tabSize
        elif key >= 0x21 and key <= 0x5A:
            # Decode Key
            filepath = self.allImages[key - 0x21]
            xpos = (self.charCount % self.lineLength) * self.charSpace
            ypos = (self.charCount / self.lineLength) * self.charSpace
            emo = SkyMoji(filepath, self)
            self.emojis.append(emo)
            emo.move(xpos, ypos)
            emo.show()
            self.charCount += 1

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mywin = TypingWindow()
    sys.exit(app.exec_())
