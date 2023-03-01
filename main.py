import sys
import sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem


class Show_Coffee_Widget(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.setWindowTitle('Виды кофе')
        self.con = sqlite3.connect("coffee.db")
        info = list(map(list, self.con.cursor().execute("SELECT * FROM info").fetchall()))
        self.tableWidget.setRowCount(len(info))
        self.tableWidget.setColumnCount(len(info[0]))
        for i, row in enumerate(info):
            for j, elem in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(elem)))
        self.tableWidget.setHorizontalHeaderLabels(
            ['id', 'sort', 'roasting', 'ground/grain', 'taste', 'price', 'packaging volume'])
        self.tableWidget.resizeColumnsToContents()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Show_Coffee_Widget()
    form.show()
    sys.exit(app.exec())