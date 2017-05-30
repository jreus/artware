# -*- coding: utf-8 -*-
"""
This program creates an interface with a number of the common styleable
widgets from Qt. And provides a text entry box where you can enter your own
stylesheet code and see the results in realtime.


Useful links:

Qt Stylesheets Reference, includes the list of styleable widgets
and the list of recognized CSS properties (and special Qt-only properties):
http://doc.qt.io/qt-5/stylesheet-reference.html

Qt Stylesheets Examples:
http://doc.qt.io/qt-5/stylesheet-examples.html

W3schools tutorial on CSS:
https://www.w3schools.com/css/css_font.asp

QGridLayout Reference:
http://doc.qt.io/qt-5/qgridlayout.html

QListWidget & QListWidgetItem:
http://doc.qt.io/qt-5/qlistwidget.html#details
http://doc.qt.io/qt-5/qlistwidgetitem.html

QDialog and QMessageBox Reference:
http://doc.qt.io/qt-5/qdialog.html#details
http://doc.qt.io/qt-5/qmessagebox.html


"""

from PyQt5.QtWidgets import QApplication, QMainWindow, qApp, QGridLayout, QHBoxLayout, QAbstractItemView
from PyQt5.QtWidgets import QComboBox, QSpinBox, QListWidget, QLineEdit, QPlainTextEdit, QPushButton
from PyQt5.QtWidgets import QWidget, QRadioButton, QCheckBox, QGroupBox, QProgressBar, QSlider, QMessageBox
from PyQt5.QtCore import Qt
import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.initGUI()

    def initGUI(self):
        self.dropdown = QComboBox()
        self.dropdown.addItem("Thing One")
        self.dropdown.addItem("Thing Two")
        self.dropdown.addItem("Thing Three")
        self.dropdown.addItem("Thing Four")
        spinbox = QSpinBox()
        spinbox.setMaximumSize(100, 60)

        radios_layout = QHBoxLayout()
        radios_layout.addWidget(QRadioButton("Radio 1"))
        radios_layout.addWidget(QRadioButton("Radio 2"))
        radios_layout.addWidget(QRadioButton("Radio 3"))
        radiobuttons = QGroupBox("Radio Buttons")
        radiobuttons.setLayout(radios_layout)
        radiobuttons.setMaximumSize(300, 70)

        checkbox_layout = QHBoxLayout()
        checkbox_layout.addWidget(QCheckBox("Check 1"))
        checkbox_layout.addWidget(QCheckBox("Check 2"))
        checkbox_layout.addWidget(QCheckBox("Check 3"))
        checkboxes = QGroupBox("Checkboxes")
        checkboxes.setLayout(checkbox_layout)
        checkboxes.setMaximumSize(300, 70)


        self.lineedit = QLineEdit("Type Some Text Here")
        self.listwidget = QListWidget()
        self.listwidget.addItem("List Item 1")
        self.listwidget.addItem("List Item 2")
        self.listwidget.addItem("List Item 3")
        self.listwidget.addItem("List Item 4")
        self.listwidget.addItem("List Item 5")
        self.listwidget.addItem("List Item 6")
        self.listwidget.setSelectionMode(QAbstractItemView.MultiSelection)

        progress = QProgressBar()
        slider = QSlider()
        slider.setOrientation(Qt.Horizontal)
        slider.valueChanged.connect(progress.setValue)
        self.textbox = QPlainTextEdit()
        self.textbox.setTabStopWidth(20)
        fp = open("css/default.css")
        self.textbox.setPlainText(fp.read())
        fp.close()

        dialogbutton = QPushButton("Display Dialog")
        dialogbutton.clicked.connect(self.openDialog)
        updatebutton = QPushButton("Update Styles")
        updatebutton.clicked.connect(self.updateStyle)

        grid = QGridLayout()
        grid.addWidget(checkboxes,      0, 0, 1, 2) # span 1 row, 2 columns
        grid.addWidget(radiobuttons,    0, 2, 1, 2) # span 1 row, 2 columns
        grid.addWidget(self.listwidget, 1, 0, 2, 1) # span 2 rows, 1 column
        grid.addWidget(self.dropdown,   1, 1)
        grid.addWidget(spinbox,         2, 1)
        grid.addWidget(slider,          1, 2, 1, 2)
        grid.addWidget(progress,        2, 2, 1, 2)
        grid.addWidget(self.lineedit,   3, 0, 1, 2) # span 1 row, 2 columns
        grid.addWidget(dialogbutton,    3, 2)
        grid.setRowStretch(4, 1)        # row 4 will stretch with the interface
        grid.addWidget(self.textbox,    4, 0, 1, 4) # span 1 row, 4 columns
        grid.addWidget(updatebutton,    5, 3)

        mainwidget = QWidget()
        mainwidget.setLayout(grid)
        mainwidget.setObjectName("main")
        self.setCentralWidget(mainwidget)
        self.setWindowTitle("Style Me")
        self.setGeometry(20,20, 500, 600)
        self.show()

    def updateStyle(self):
        styleSheet = self.textbox.toPlainText()
        qApp.setStyleSheet(styleSheet) # qApp is a global reference to your running QApplication, it's in PyQt5.QtWidgets

    def openDialog(self):
        thetext = "Selected List Items: "
        for item in self.listwidget.selectedItems():
            thetext = thetext + "\n    " + item.text()
        thetext = thetext + "\nSelected ComboBox Item: " + "\n     " + self.dropdown.currentText()
        thetext = thetext + "\nEntered Text: " + "\n     " + self.lineedit.text()

        message = QMessageBox()
        message.setText(thetext)
        message.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyWindow()
    sys.exit(app.exec_())
