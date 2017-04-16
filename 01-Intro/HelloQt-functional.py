# From zetcode.com tutorials: http://zetcode.com/gui/pyqt5/firstprograms/

import sys
from PyQt5.QtWidgets import QApplication, QWidget
#from PyQt5.Qt import QPoint

# Qt QtWidgets QtGui <-- most things are in these modules


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = QWidget()
    #pt1 = QPoint(300, 300)
    w.resize(250, 150)
    w.move(300, 300)
    #w.move(pt1)
    #w.move(QPoint(300, 300)) # also fine!
    w.setWindowTitle('Hello Qt')
    w.show()
    sys.exit(app.exec_())
