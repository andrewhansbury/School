from PySide2.QtCore import QSize
from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QGroupBox, QGridLayout
import sys
from PySide2.QtGui import QIcon, QFont


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Grid Layout")
        self.setGeometry(300, 200, 500, 400)

        self.setIcon()

        self.createGridLayout()
        vbox = QVBoxLayout()
        vbox.addWidget(self.groupBox)
        self.setLayout(vbox)

        self.show()

    def setIcon(self):
        appIcon = QIcon("icon.png")
        self.setWindowIcon(appIcon)

    def createGridLayout(self):
        self.groupBox = QGroupBox("Tristan-Tac-Toe")
        self.groupBox.setFont(QFont("Sanserif", 13))
        gridLayout = QGridLayout()

        button = QPushButton("X", self)
        button.setFixedSize(QSize(150, 150))
        # button.setIcon(QIcon("cpp.png"))
        gridLayout.addWidget(button, 0, 0)

        button1 = QPushButton("O", self)
        button1.setFixedSize(QSize(150, 150))
        # button1.setIcon(QIcon("css.png"))
        gridLayout.addWidget(button1, 0, 1)

        button2 = QPushButton("X", self)
        button2.setFixedSize(QSize(150, 150))
        # button2.setIcon(QIcon("javascript.png"))
        gridLayout.addWidget(button2, 0, 2)

        button3 = QPushButton("O", self)
        button3.setFixedSize(QSize(150, 150))
        # button3.setIcon(QIcon("csharp.png"))
        gridLayout.addWidget(button3, 1, 0)

        button4 = QPushButton("X", self)
        button4.setFixedSize(QSize(150, 150))
        # button4.setIcon(QIcon("pythonicon.png"))
        gridLayout.addWidget(button4, 1, 1)

        button5 = QPushButton("O", self)
        button5.setFixedSize(QSize(150, 150))
        # button5.setIcon(QIcon("java.png"))
        gridLayout.addWidget(button5, 1, 2)

        button6 = QPushButton("X", self)
        button6.setFixedSize(QSize(150, 150))
        # button5.setIcon(QIcon("java.png"))
        gridLayout.addWidget(button6, 2, 0)

        button7 = QPushButton("X", self)
        button7.setFixedSize(QSize(150, 150))
        # button5.setIcon(QIcon("java.png"))
        gridLayout.addWidget(button7, 2, 1)

        button8 = QPushButton("X", self)
        button8.setFixedSize(QSize(150, 150))
        # button5.setIcon(QIcon("java.png"))
        gridLayout.addWidget(button8, 2, 2)

        self.groupBox.setLayout(gridLayout)


myapp = QApplication(sys.argv)
window = Window()


myapp.exec_()
sys.exit()
