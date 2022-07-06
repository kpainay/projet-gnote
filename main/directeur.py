import sys
import PyQt5
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sqlite3
from PyQt5.uic import loadUi
from PyQt5.uic import loadUiType
import xlrd, openpyxl
from openpyxl import workbook, load_workbook

prof = loadUiType("professeur.ui")

database = sqlite3.connect("gnote_base.db")
cursor = database.cursor()

class Directeur(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("directeur.ui", self)
        self.filehandle =""

        self.pushButton.clicked.connect(self.Notes)
        self.pushButton_2.clicked.connect(self.Notifications)

    def Notes(self):
        self.stackedWidget.setCurrentWidget(self.page)
        try:
            dat= QTableWidget()

            data= cursor.execute("""SELECT* FROM NOTE""").fetchall()
            self.tableWidget.setRowCount(len(data))
            self.tableWidget.setColumnCount(len(data[0]))

            for i in range(len(data)):
                for j in range(len(data[0])):
                    cell = QLabel(str(data[i][j]))
                    self.tableWidget.setCellWidget(i, j, cell)

        except:
            print("Error Getting Data")

    def Notifications(self):
        self.stackedWidget.setCurrentWidget(self.page_2)
        try:
            for i in cursor.execute("SELECT * FROM notification").fetchall():
                self.listWidget.addItems(i)
        except:
            pass



def main():
    app = QApplication(sys.argv)
    win = Directeur()
    win.show()

    sys.exit(app.exec_())

if __name__=='__main__':
    main()