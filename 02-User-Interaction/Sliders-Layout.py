"""
More info on QSlider: https://doc.qt.io/qt-5/qslider.html#details
More info on Layouts: http://zetcode.com/gui/pyqt5/layout/

"""

from PyQt5.QtWidgets import QApplication, QWidget, QSlider, QProgressBar, QLabel, QFrame
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
import sys

class Sliders(QWidget):
    width = 550
    height = 350

    def __init__(self):
        super(Sliders, self).__init__()
        self.initGUI()

    def initGUI(self):
        slider1 = QSlider(self)
        slider2 = QSlider(self)
        slider1.setOrientation(Qt.Horizontal)
        slider2.setOrientation(Qt.Horizontal)
        progress1 = QProgressBar(self)
        progress2 = QProgressBar(self)
        label1 = QLabel(self)
        label2 = QLabel(self)
        label1.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        label1.setFont(QFont("Monaco", 32, QFont.Bold))
        label1.setNum(0)
        label2.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        label2.setFont(QFont("Monaco", 32, QFont.Bold))
        label2.setNum(0)

        # Connect signals
        slider1.valueChanged.connect(progress1.setValue)
        slider1.valueChanged.connect(label1.setNum)
        slider2.valueChanged.connect(progress2.setValue)
        slider2.valueChanged.connect(label2.setNum)

        # Position everything using layouts this time
        hbox1 = QHBoxLayout()
        hbox1.addWidget(slider1)
        hbox1.addWidget(label1)
        hbox2 = QHBoxLayout()
        hbox2.addWidget(slider2)
        hbox2.addWidget(label2)
        vbox = QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addStretch(1)
        vbox.addWidget(progress1)
        vbox.addStretch(10)
        vbox.addLayout(hbox2)
        vbox.addWidget(progress2)
        self.setLayout(vbox)

        self.setGeometry(0,0, self.width, self.height)
        self.setWindowTitle("Sliders Aplenty")
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Sliders()
    sys.exit(app.exec_())
