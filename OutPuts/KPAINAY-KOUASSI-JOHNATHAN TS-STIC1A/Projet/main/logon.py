import os
import sys
import PyQt5
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.uic import *
from PyQt5.uic import loadUiType
import testFinal1
import etudiant
import proff
import directeur
import sqlite3
log, _ = loadUiType("C:\\Users\\lawre\\OneDrive - INP-HB\\Desktop\LOKI\\Projet\\logon.ui")
database =sqlite3.connect("gnote_base.db")
cursor = database.cursor()
app = QApplication(sys.argv)
currentUser = []

class logon(QMainWindow, log):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.icon = QPixmap("C:\\Users\\lawre\\OneDrive - INP-HB\\Desktop\LOKI\\Projet\\resources\\images\\home.png")
        self.enter.clicked.connect(self.switch)
        self.btnExit.clicked.connect(self.close)

    @pyqtSlot()
    def switch(self):

        try:
            loginProf = cursor.execute("""SELECT login FROM PROFESSEUR""").fetchall()
            loginEtudiant = cursor.execute("""SELECT login FROM ETUDIANT""").fetchall()
            loginDE = cursor.execute("""SELECT login FROM DIRECTEUR_D_ETUDE""").fetchall()
            loginDirecteur = cursor.execute("""SELECT login FROM DIRECTEUR_D_ECOLE""").fetchall()

            mpassProf = cursor.execute("""SELECT mot_de_pass FROM PROFESSEUR""").fetchall()
            mpassEtudiant = cursor.execute("""SELECT mot_de_passe FROM ETUDIANT""").fetchall()
            mpassDE= cursor.execute("""SELECT mot_de_passe FROM DIRECTEUR_D_ETUDE""").fetchall()
            mpassDirecteur = cursor.execute("""SELECT mot_de_passe FROM DIRECTEUR_D_ECOLE""").fetchall()

            for i in range(len(loginProf)):
                if self.user.text() in loginProf[i]:
                    for j in range(len(mpassProf)):
                        if self.pwrd.text() in mpassProf[j]:
                            self.etud = proff.professeur()
                            try:
                                currentUser = cursor.execute("""SELECT Matricule_Professeur, login, mot_de_passe FROM PROFESSEUR""").fetchall()
                                print(currentUser)
                                cursor.execute("""INSERT INTO currentUser (login, mot_de_passe, FILIERE) VALUES(?,?,?)""", (currentUser[0], currentUser[1]), currentUser[2])
                                print("Successful write to db")
                            except:
                                print("SQL Error")
                            self.etud.show()
                            self.close()

            for i in range(len(loginEtudiant)):
                if self.user.text() in loginEtudiant[i]:
                    for j in range(len(mpassEtudiant)):
                        if self.pwrd.text() in mpassEtudiant[j]:

                            self.etud = etudiant.etudiant()
                            self.etud.show()
                            self.close()

            for i in range(len(loginDirecteur)):
                if self.user.text() in loginDirecteur[i]:
                    for j in range(len(mpassProf)):
                        if self.pwrd.text() in mpassDirecteur[j]:
                            self.etud = directeur.Directeur()
                            self.etud.show()
                            self.close()

            for i in range(len(loginDE)):
                if self.user.text() in loginDE[i]:
                    for j in range(len(mpassDE)):
                        if self.pwrd.text() in mpassDE[j]:
                            self.DE = testFinal1.mainWindow()
                            self.DE.show()
                            self.close()

        except:
            self.info.setText("Mot De Passe ou Login Incorrecte!!!")






    def signon(self):

        if self.uname == str(self.user.text()):
            if self.uname == str(self.pwrd.text()):
                pass


            else:
                self.info.setText("PassWord Incorrect")
                self.info.setText(str(self.pwrd.text()) + " is not a password")



        else:
            self.info.setText("Uname Wrong")


def main():

    loginWindow= logon()
    loginWindow.show()


    sys.exit(app.exec_())

if __name__=='__main__':
    main()

