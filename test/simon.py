import sys
from PySide2.QtCore import QSize
from PySide2.QtWidgets import QApplication, QLabel, QMessageBox, QWidget, QPushButton, QGridLayout
import sys


class TicTacToe(QWidget):
    def __init__(self):
        super().__init__()
        grid_layout = QGridLayout()
        self.setGeometry(400, 400, 400, 400)
        self.setLayout(grid_layout)

        button1 = QPushButton("", self)
        button1.name = "1"
        button1.setFixedSize(QSize(125, 125))
        grid_layout.addWidget(button1, 0, 0)

        button2 = QPushButton("", self)
        button2.name = "2"
        button2.setFixedSize(QSize(125, 125))
        grid_layout.addWidget(button2, 0, 1)

        button3 = QPushButton("", self)
        button3.name = "3"
        button3.setFixedSize(QSize(125, 125))
        grid_layout.addWidget(button3, 0, 2)

        button4 = QPushButton("", self)
        button4.name = "4"
        button4.setFixedSize(QSize(125, 125))
        grid_layout.addWidget(button4, 1, 0)

        button5 = QPushButton("", self)
        button5.name = "5"
        button5.setFixedSize(QSize(125, 125))
        grid_layout.addWidget(button5, 1, 1)

        button6 = QPushButton("", self)
        button6.name = "6"
        button6.setFixedSize(QSize(125, 125))
        grid_layout.addWidget(button6, 1, 2)

        button7 = QPushButton("", self)
        button7.name = "7"
        button7.setFixedSize(QSize(125, 125))
        grid_layout.addWidget(button7, 2, 0)

        button8 = QPushButton("", self)
        button8.name = "8"
        button8.setFixedSize(QSize(125, 125))
        grid_layout.addWidget(button8, 2, 1)

        button9 = QPushButton("", self)
        button9.name = "9"
        button9.setFixedSize(QSize(125, 125))
        grid_layout.addWidget(button9, 2, 2)

        self.setWindowTitle('Simon-Tac-Toe')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TicTacToe()
    window.show()
    sys.exit(app.exec_())
