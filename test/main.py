
from enum import Enum
from PySide2 import QtGui
from PySide2.QtCore import QSize
from PySide2.QtWidgets import QApplication, QLabel, QMessageBox, QWidget, QVBoxLayout, QPushButton, QGroupBox, QGridLayout
import sys
from PySide2.QtGui import QIcon, QFont


class player(Enum):
    PLAYER1 = 1
    PLAYER2 = 2


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Grid Layout")
        self.setGeometry(300, 200, 500, 400)

        self.setIcon()

        self.createGridLayout(player)
        vbox = QVBoxLayout()
        vbox.addWidget(self.groupBox)
        self.setLayout(vbox)

        self.show()

        # self.current_player = player.PLAYER1

    def setIcon(self):
        appIcon = QIcon("icon.png")
        self.setWindowIcon(appIcon)

    def lol(self, button: QPushButton):
        print("hey", button.name)

    def update_player(self, gridLayout: QGridLayout, player_label: QLabel):
        if player_label.text() == "Player 1":
            player_label.setText("Player 2")
        else:
            player_label.setText("Player 1")
        # self.display_player(gridLayout, current_player)

    def show_move(self, gridLayout: QGridLayout, button: QPushButton, player_label: QLabel):
        button.setFont(QFont('Times', 40))
        button.setDisabled(True)
        if player_label.text() == "Player 1":

            button.setText("X")
        else:
            button.setText("O")

    def reset_game(self, board: dict):

        board.clear()

        buttons = []
        buttons.append(self.button1)
        buttons.append(self.button2)
        buttons.append(self.button3)
        buttons.append(self.button4)
        buttons.append(self.button5)
        buttons.append(self.button6)
        buttons.append(self.button7)
        buttons.append(self.button8)
        buttons.append(self.button9)

        for but in buttons:
            but.setDisabled(False)
            but.setText("")
            but.setStyleSheet("")

    def check_winner(self, board: dict, pos_name, move):
        board[pos_name] = move

        print(board)

        try:
            board['1']
            board['9']

        except:
            board['1'] = ''
            board['2'] = ''
            board['3'] = ''
            board['4'] = ''
            board['5'] = ''
            board['6'] = ''
            board['7'] = ''
            board['8'] = ''
            board['9'] = ''

            board[pos_name] = move

        if board['1'] == board['2'] == board['3'] != '':
            self.button1.setStyleSheet("background-color: lightblue")
            self.button2.setStyleSheet("background-color: lightblue")
            self.button3.setStyleSheet("background-color: lightblue")
            msg = QMessageBox()
            msg.setWindowTitle("Game Over!")
            msg.setText("Game over! " + board['1'] + '\'s Win!')

            msg.setStandardButtons(QMessageBox.Retry)
            x = msg.exec_()

            self.reset_game(board)

        elif board['4'] == board['5'] == board['6'] != '':
            self.button4.setStyleSheet("background-color: lightblue")
            self.button5.setStyleSheet("background-color: lightblue")
            self.button6.setStyleSheet("background-color: lightblue")
            msg = QMessageBox()
            msg.setWindowTitle("Game Over!")
            msg.setText("Game over! " + board['4'] + '\'s Win!')
            msg.setStandardButtons(QMessageBox.Retry)
            x = msg.exec_()
            self.reset_game(board)
            board = {'1': '', '2': '', '3': '', '4': '',
                     '5': '', '6': '', '7': '', '8': '', '9': ''}
        elif board['7'] == board['8'] == board['9'] != '':
            self.button7.setStyleSheet("background-color: lightblue")
            self.button8.setStyleSheet("background-color: lightblue")
            self.button9.setStyleSheet("background-color: lightblue")
            msg = QMessageBox()
            msg.setWindowTitle("Game Over!")
            msg.setText("Game over! " + board['7'] + '\'s Win!')
            msg.setStandardButtons(QMessageBox.Retry)
            x = msg.exec_()
            self.reset_game(board)
            board = {'1': '', '2': '', '3': '', '4': '',
                     '5': '', '6': '', '7': '', '8': '', '9': ''}
        elif board['1'] == board['4'] == board['7'] != '':
            self.button1.setStyleSheet("background-color: lightblue")
            self.button4.setStyleSheet("background-color: lightblue")
            self.button7.setStyleSheet("background-color: lightblue")
            msg = QMessageBox()
            msg.setWindowTitle("Game Over!")
            msg.setText("Game over! " + board['1'] + '\'s Win!')
            msg.setStandardButtons(QMessageBox.Retry)
            x = msg.exec_()
            self.reset_game(board)
            board = {'1': '', '2': '', '3': '', '4': '',
                     '5': '', '6': '', '7': '', '8': '', '9': ''}
        elif board['7'] == board['8'] == board['9'] != '':
            self.button7.setStyleSheet("background-color: lightblue")
            self.button8.setStyleSheet("background-color: lightblue")
            self.button9.setStyleSheet("background-color: lightblue")
            msg = QMessageBox()
            msg.setWindowTitle("Game Over!")
            msg.setText("Game over! " + board['7'] + '\'s Win!')
            msg.setStandardButtons(QMessageBox.Retry)
            x = msg.exec_()
            self.reset_game(board)
            board = {'1': '', '2': '', '3': '', '4': '',
                     '5': '', '6': '', '7': '', '8': '', '9': ''}
        elif board['2'] == board['5'] == board['8'] != '':
            self.button2.setStyleSheet("background-color: lightblue")
            self.button5.setStyleSheet("background-color: lightblue")
            self.button8.setStyleSheet("background-color: lightblue")
            msg = QMessageBox()
            msg.setWindowTitle("Game Over!")
            msg.setText("Game over! " + board['2'] + '\'s Win!')
            msg.setStandardButtons(QMessageBox.Retry)
            x = msg.exec_()
            self.reset_game(board)
            board = {'1': '', '2': '', '3': '', '4': '',
                     '5': '', '6': '', '7': '', '8': '', '9': ''}
        elif board['3'] == board['6'] == board['9'] != '':
            self.button3.setStyleSheet("background-color: lightblue")
            self.button6.setStyleSheet("background-color: lightblue")
            self.button9.setStyleSheet("background-color: lightblue")
            msg = QMessageBox()
            msg.setWindowTitle("Game Over!")
            msg.setText("Game over! " + board['3'] + '\'s Win!')
            msg.setStandardButtons(QMessageBox.Retry)
            x = msg.exec_()
            self.reset_game(board)
            board = {'1': '', '2': '', '3': '', '4': '',
                     '5': '', '6': '', '7': '', '8': '', '9': ''}
        elif board['3'] == board['5'] == board['7'] != '':
            self.button3.setStyleSheet("background-color: lightblue")
            self.button5.setStyleSheet("background-color: lightblue")
            self.button7.setStyleSheet("background-color: lightblue")
            msg = QMessageBox()
            msg.setWindowTitle("Game Over!")
            msg.setText("Game over! " + board['3'] + '\'s Win!')
            msg.setStandardButtons(QMessageBox.Retry)
            x = msg.exec_()
            self.reset_game(board)
            board = {'1': '', '2': '', '3': '', '4': '',
                     '5': '', '6': '', '7': '', '8': '', '9': ''}
        elif board['1'] == board['5'] == board['9'] != '':
            self.button1.setStyleSheet("background-color: lightblue")
            self.button5.setStyleSheet("background-color: lightblue")
            self.button9.setStyleSheet("background-color: lightblue")
            msg = QMessageBox()
            msg.setWindowTitle("Game Over!")
            msg.setText("Game over! " + board['1'] + '\'s Win!')
            msg.setStandardButtons(QMessageBox.Retry)
            x = msg.exec_()
            self.reset_game(board)
            board = {'1': '', '2': '', '3': '', '4': '',
                     '5': '', '6': '', '7': '', '8': '', '9': ''}

        # RIGGHT HERE NEED TO DETERMINE IF TIE (IF ALL THE SPOTS ARE FILLED) !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

        else:
            notFilled = True
            for x in board:
                print(x)
                if board[x] != '':
                    notFilled = False
            if not notFilled:
                msg = QMessageBox()
                msg.setWindowTitle("Game Over!")
                msg.setText("Game over! It was a tie!")
                msg.setStandardButtons(QMessageBox.Retry)

    def createGridLayout(self, player: player):

        self.groupBox = QGroupBox("Tristan-Tac-Toe")
        self.groupBox.setFont(QFont("Sanserif", 13))
        gridLayout = QGridLayout()
        player_label = QLabel("Player 1")
        gridLayout.addWidget(player_label, 3, 1)

        self.board = {'1': '', '2': '', '3': '', '4': '',
                      '5': '', '6': '', '7': '', '8': '', '9': ''}

        self.button1 = QPushButton("", self)
        self.button1.name = "1"
        self.button1.setFixedSize(QSize(150, 150))
        self.button1.released.connect(
            lambda: self.show_move(gridLayout, self.button1, player_label))
        self.button1.released.connect(
            lambda: self.check_winner(self.board, self.button1.name, self.button1.text()))
        self.button1.released.connect(
            lambda: self.update_player(gridLayout, player_label))
        gridLayout.addWidget(self.button1, 0, 0)

        self.button2 = QPushButton("", self)
        self.button2.name = "2"
        self.button2.setFixedSize(QSize(150, 150))
        self.button2.released.connect(
            lambda: self.show_move(gridLayout, self.button2, player_label))
        self.button2.released.connect(
            lambda: self.check_winner(self.board, self.button2.name, self.button2.text()))
        self.button2.released.connect(
            lambda: self.update_player(gridLayout, player_label))
        gridLayout.addWidget(self.button2, 0, 1)

        self.button3 = QPushButton("", self)
        self.button3.name = "3"
        self.button3.setFixedSize(QSize(150, 150))
        self.button3.released.connect(
            lambda: self.show_move(gridLayout, self.button3, player_label))

        self.button3.released.connect(
            lambda: self.check_winner(self.board, self.button3.name, self.button3.text()))

        self.button3.released.connect(
            lambda: self.update_player(gridLayout, player_label))
        gridLayout.addWidget(self.button3, 0, 2)

        self.button4 = QPushButton("", self)
        self.button4.name = "4"
        self.button4.setFixedSize(QSize(150, 150))
        self.button4.released.connect(
            lambda: self.show_move(gridLayout, self.button4, player_label))
        self.button4.released.connect(
            lambda: self.check_winner(self.board, self.button4.name, self.button4.text()))
        self.button4.released.connect(
            lambda: self.update_player(gridLayout, player_label))
        gridLayout.addWidget(self.button4, 1, 0)

        self.button5 = QPushButton("", self)
        self.button5.name = "5"
        self.button5.setFixedSize(QSize(150, 150))
        self.button5.released.connect(
            lambda: self.show_move(gridLayout, self.button5, player_label))
        self.button5.released.connect(
            lambda: self.check_winner(self.board, self.button5.name, self.button5.text()))
        self.button5.released.connect(
            lambda: self.update_player(gridLayout, player_label))
        gridLayout.addWidget(self.button5, 1, 1)

        self.button6 = QPushButton("", self)
        self.button6.name = "6"
        self.button6.setFixedSize(QSize(150, 150))
        self.button6.released.connect(
            lambda: self.show_move(gridLayout, self.button6, player_label))
        self.button6.released.connect(
            lambda: self.check_winner(self.board, self.button6.name, self.button6.text()))
        self.button6.released.connect(
            lambda: self.update_player(gridLayout, player_label))
        gridLayout.addWidget(self.button6, 1, 2)

        self.button7 = QPushButton("", self)
        self.button7.name = "7"
        self.button7.setFixedSize(QSize(150, 150))
        self.button7.released.connect(
            lambda: self.show_move(gridLayout, self.button7, player_label))
        self.button7.released.connect(
            lambda: self.check_winner(self.board, self.button7.name, self.button7.text()))
        self.button7.released.connect(
            lambda: self.update_player(gridLayout, player_label))
        gridLayout.addWidget(self.button7, 2, 0)

        self.button8 = QPushButton("", self)
        self.button8.name = "8"
        self.button8.setFixedSize(QSize(150, 150))
        self.button8.released.connect(
            lambda: self.show_move(gridLayout, self.button8, player_label))
        self.button8.released.connect(
            lambda: self.check_winner(self.board, self.button8.name, self.button8.text()))
        self.button8.released.connect(
            lambda: self.update_player(gridLayout, player_label))
        gridLayout.addWidget(self.button8, 2, 1)

        self.button9 = QPushButton("", self)
        self.button9.name = "9"
        self.button9.setFixedSize(QSize(150, 150))
        self.button9.released.connect(
            lambda: self.show_move(gridLayout, self.button9, player_label))
        self.button9.released.connect(
            lambda: self.check_winner(self.board, self.button9.name, self.button9.text()))
        self.button9.released.connect(
            lambda: self.update_player(gridLayout, player_label))
        gridLayout.addWidget(self.button9, 2, 2)

        self.groupBox.setLayout(gridLayout)


def main():
    myapp = QApplication(sys.argv)

    board = {}

    window = Window()

    myapp.exec_()
    sys.exit()


if __name__ == "__main__":
    main()
