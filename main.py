import sys
from PyQt5.QtGui import *
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtWidgets
import sqlite3

if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class FirstForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.game = None

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Выбор игры')
        self.label = QLabel(self)
        self.label.setText('Для связи с разработчиком пишите по почте lumi4p@list.ru')

        self.LoL = QPushButton('League of Legends', self)
        self.LoL.move(60, 130)
        self.LoL.resize(180, 30)
        self.LoL.setFont(QFont('Comic Sans', 9, italic=True))
        self.CsGo = QPushButton('Counter Strike Global Offensive', self)
        self.CsGo.move(60, 100)
        self.CsGo.resize(180, 30)
        self.CsGo.setFont(QFont('Comic Sans', 9, italic=True))

        self.LoL.clicked.connect(self.open_second_form)
        self.CsGo.clicked.connect(self.open_second_form)

    def open_second_form(self):
        if self.sender().text() == 'League of Legends':
            self.game = 'LoL'
        elif self.sender().text() == 'Counter Strike Global Offensive':
            self.game = 'csgo'
        self.second_form = SecondForm(self, self.game)
        self.second_form.show()
        FirstForm.hide(self)


class SecondForm(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.game = args
        self.con = sqlite3.connect("content/DB.sqlite")
        uic.loadUi('content/teams.ui', self)
        self.cur = self.con.cursor()
        req = f"""SELECT TeamName FROM {self.game[1]}"""
        result = self.cur.execute(req).fetchall()
        for i in result:
            self.Combo1.addItem(i[0])
            self.Combo2.addItem(i[0])
        self.setWindowTitle('Поиск команд')
        self.finding.clicked.connect(self.found)
        self.finding_2.clicked.connect(self.found_2)

    def found(self):
        req = f"""SELECT * FROM {self.game[1]} 
               WHERE TeamName='{self.Combo1.currentText()}'"""
        result = self.cur.execute(req).fetchall()[0]
        self.label_19.setText(result[0])
        self.label_28.setText(result[1])
        self.label_29.setText(result[2])
        self.label_30.setText(result[3])
        self.label_31.setText(result[4])
        self.label_32.setText(result[5])
        self.label_33.setText(result[6])
        self.label_34.setText(result[7])


    def found_2(self):
        req = f"""SELECT * FROM {self.game[1]} 
        WHERE TeamName='{self.Combo2.currentText()}'"""
        result = self.cur.execute(req).fetchall()[0]
        self.label_20.setText(result[0])
        self.label_21.setText(result[1])
        self.label_22.setText(result[2])
        self.label_23.setText(result[3])
        self.label_24.setText(result[4])
        self.label_25.setText(result[5])
        self.label_26.setText(result[6])
        self.label_35.setText(result[7])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FirstForm()
    ex.show()
    sys.exit(app.exec())
