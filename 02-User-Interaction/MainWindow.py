"""
Shows some of the things you can do with QMainWindow. This program makes a
QMainWindow with a QGraphicsView as its central widget.

The program shows how to have a status bar and a program menu with some menu items.
It also shows a very simple example of how you can use a QGraphicsScene to draw
custom 2D graphics.

It also shows an example of how to handle keypress events inside a QWidget.

Some useful references:

All about QMainWindow https://doc.qt.io/qt-5/qmainwindow.html#details
QMainWindow lets you create fully composed windowed applications. With more
features than a standard windowed QWidget.

What are QActions and how do you use them to build application menus?
QAction: http://doc.qt.io/qt-5/qaction.html#details

See the Qt.Key reference for all the various keyboard & modifiercodes
http://doc.qt.io/qt-5/qt.html#Key-enum
http://doc.qt.io/qt-5/qt.html#Modifier-enum

For more sophisticated signal mapping (adding data to signals), see QSignalMapper
http://doc.qt.io/qt-5/QSignalMapper.html#details
"""

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPen, QBrush, QColor, QKeySequence
from PyQt5.QtCore import Qt, QObject
import sys
from random import randint


class MyApp(QMainWindow):
    width = 500
    height = 600

    def __init__(self):
        super(MyApp, self).__init__()
        self.initApp()

    def initApp(self):
        self.graphics = QGraphicsScene()
        self.graphicsView = QGraphicsView(self.graphics)

        self.setCentralWidget(self.graphicsView)

        self.statusBar = self.statusBar() # create the status bar in this QMainWindow
        self.statusBar.showMessage("Drawing Shapes...", 10000) # status bar messages have a time limit

        self.initMenu() # set up the menu bar

        self.setGeometry(0, 0, self.width, self.height)
        self.setWindowTitle('A Main Window Application')
        self.show()

    def initMenu(self):
        self.menubar = self.menuBar() # initialize the menubar and get it so we can add actions

        # First make your actions
        squareAct = QAction('Square', self)
        squareAct.triggered.connect(self.drawSquare)    # triggered is sent when the user clicks the menu item
        squareAct.hovered.connect(self.menuHover)       # hovered is sent when the user hovers over the menu item
        squareAct.setToolTip("Draw a square")
        squareAct.setShortcuts(QKeySequence("Ctrl+S"))
        circleAct = QAction('Circle', self)
        circleAct.triggered.connect(self.drawCircle)
        circleAct.hovered.connect(self.menuHover)
        circleAct.setToolTip("Draw a circle")
        cirlceAct.setShortcuts(QKeySequence("Ctrl+C"))

        makeMenu = self.menubar.addMenu('Make')
        makeMenu.addAction(squareAct)
        makeMenu.addAction(circleAct)

    # Used when the user hovers over an interface object
    def menuHover(self):
        # sender() is a special method of QObject that tells you which object emitted the signal
        # Qt framework voodoo magic
        emitter = self.sender()
        self.statusBar.showMessage(emitter.toolTip() , 5000)


    def drawCircle(self):
        dimensions = self.graphicsView.size()
        x = randint(20, dimensions.width() - 20)
        y = randint(20, dimensions.height() - 20)
        w = randint(100, 200)
        h = randint(100, 200)
        brush = QBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
        self.graphics.addEllipse(x, y, w, h, QPen(QColor(0,0,0)), brush)

    def drawSquare(self):
        dimensions = self.graphicsView.size()
        x = randint(20, dimensions.width() - 20)
        y = randint(20, dimensions.height() - 20)
        w = randint(100, 200)
        h = randint(100, 200)
        brush = QBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
        self.graphics.addRect(x, y, w, h, QPen(QColor(0,0,0)), brush)

    def keyPressEvent(self, event):
        key = event.key()
        if key == Qt.Key_Equal:
            self.drawSquare()
        elif key == Qt.Key_Minus:
            self.drawCircle()
        else:
            print "Unmapped Key:", key




if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MyApp()
    sys.exit(app.exec_())
