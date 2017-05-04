"""
A slightly more interesting example of user interaction.

A window is created with a LCD display, slider, dropdown menu, button and some labels.
The slider can be used to change the x position of the window, which is displayed on
the LCD display. Different ranges for the slider can be chosen.

"""

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
import sys

class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.initUI()

    def initUI(self):
        self.setFixedWidth(300)
        self.setFixedHeight(200)
        self.move(20,20)
        self.setWindowTitle('Slippery Window')
        self.lcd = QLCDNumber(self)
        self.lcd.setGeometry(0, 0, 300, 80)
        label_pos = QLabel(self.lcd)
        label_pos.setText("X Position")
        label_pos.setFont(QFont("Mono", 16, QFont.Bold))
        label_pos.setGeometry(10, 10, 100, 25)

        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.setRange(0, 50)
        self.slider.setFixedWidth(290)
        self.slider.move(5, 80)
        self.slider.valueChanged.connect(self.sliderChanged)
        label_range = QLabel(self)
        label_range.setText("Range: ")
        self.dropdown = QComboBox(self)
        self.dropdown.addItems(["0-50", "0-200", "0-800"])
        self.dropdown.currentIndexChanged.connect(self.rangeChanged)
        label_range.move(105, 140)
        self.dropdown.move(150, 135)
        self.button = QPushButton(self)
        self.button.setText("Reset")
        self.button.clicked.connect(self.reset)
        self.button.move(150, 160)
        self.show()

    def sliderChanged(self):
        newval = self.slider.value()
        self.lcd.display(newval)
        self.move(newval, 0)

    def rangeChanged(self):
        item = self.dropdown.currentText()
        if item == "0-50":
            self.slider.setRange(0, 50)
        elif item == "0-200":
            self.slider.setRange(0, 200)
        elif item == "0-800":
            self.slider.setRange(0, 800)

    def reset(self):
        self.slider.setRange(0, 15)
        self.slider.setValue(0)
        self.dropdown.setCurrentIndex(0)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mywin = MyWindow()
    sys.exit(app.exec_())
