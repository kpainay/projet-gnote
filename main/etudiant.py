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

class etudiant(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("etudiant.ui", self)
        self.filehandle =""

        ##################################NAVIGATIONS###################################################
        self.pushButton.clicked.connect(self.notes)
        self.pushButton_2.clicked.connect(self.notifications)
        self.pushButton_3.clicked.connect(self.envoyer)
        self.pushButton_4.clicked.connect(self.close)
        self.pushButton_6.clicked.connect(self.envoyer)
        self.pushButton_14.clicked.connect(self.close)
        self.pushButton_7.clicked.connect(self.send)

    def envoyer(self):
        self.stackedWidget.setCurrentWidget(self.page_3)
        try:
            for i in cursor.execute(""" SELECT Nom_professeur, Prenom_professeur FROM PROFESSEUR """).fetchall():
                self.comboBox.addItems(i)
        except:
            pass

    def send(self):
        pass


    def notes(self):
        self.stackedWidget.setCurrentWidget(self.page)
        try:
            try:
                data = cursor.execute("""SELECT Nom_de_la_matiere, Valeur_de_la_note FROM NOTE WHERE Matricule_etudiant='20INP'""").fetchall()
            except:
                print("SQL TROUBLE")
            self.tableWidget.setRowCount(len(data))
            self.tableWidget.setColumnCount(len(data[0]))
            for i in range(len(data)):
                for j in range(len(data[0])):
                    cell = QLabel(str(data[i][j]))
                    self.tableWidget.setCellWidget(i, j, cell)
        except:
            print("Error while reading or writing data")


    def notifications(self):
        self.listWidget.clear()
        self.stackedWidget.setCurrentWidget(self.page_2)
        try:
            for i in cursor.execute("""SELECT dete_notif, libéllé_notif FROM notification""").fetchall():
                self.listWidget.addItems(i)
        except:
            print("An error occurred!")


def main():
    app=QApplication(sys.argv)
    win = etudiant()
    win.show()

    sys.exit(app.exec_())

if __name__=='__main__':
    main()