"""
Shows some of the things you can do with QMainWindow. This program makes a
QMainWindow with a QGraphicsView as its central widget.

The program shows how to have a status bar and a program menu with some menu items.
It also shows a very simple example of how you can use a QGraphicsScene to draw
custom 2D graphics.

It also shows an example of getting keypress events and dealing with them.

All about QMainWindow https://doc.qt.io/qt-5/qmainwindow.html#details
QMainWindow lets you create fully composed windowed applications. With more
features than a standard windowed QWidget.

What is qApp ? http://doc.qt.io/qt-5/qapplication.html#qApp

QActions are added to menus:
QAction: http://doc.qt.io/qt-5/qaction.html#details
"""

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPen, QBrush, QColor
from PyQt5.QtCore import Qt
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
        self.statusBar.showMessage("Drawing Shapes...")

        self.initMenu() # set up the menu bar

        self.setGeometry(0, 0, self.width, self.height)
        self.setWindowTitle('A Main Window Application')
        self.show()

    def initMenu(self):
        menubar = self.menuBar() # initialize the menubar and get it so we can add actions

        # First make your actions
        squareAct = QAction('Square', self)
        squareAct.triggered.connect(self.drawSquare)    # connect the triggered signal
        circleAct = QAction('Circle', self)
        circleAct.triggered.connect(self.drawCircle)

        makeMenu = menubar.addMenu('Make')
        makeMenu.addAction(squareAct)
        makeMenu.addAction(circleAct)


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

    def newMenuClicked(self):
        print "Hello New!"

    def keyPressEvent(self, event):
        print "Hello Key", event
        key = event.key()
        if key == Qt.Key_S:
            self.drawSquare()
        elif key == Qt.Key_C:
            self.drawCircle()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MyApp()
    sys.exit(app.exec_())
