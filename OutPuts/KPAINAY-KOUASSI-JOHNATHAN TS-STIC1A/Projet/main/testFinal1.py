import sys
import PyQt5
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sqlite3
from PyQt5.uic import *
from PyQt5.uic import loadUiType

# TODO: REMOVE ALL ERROR WARNINGS PRINTED TO A TERMINAL
ui, _ = loadUiType("C:\\Users\\lawre\\OneDrive - INP-HB\\Desktop\LOKI\\Projet\\untitled.ui")

database = sqlite3.connect("gnote_base.db")
cursor = database.cursor()


class mainWindow(QMainWindow, ui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

        ###################################################NAVIGATION###################################################
        self.btnCreation.clicked.connect(self.btnCreate)
        self.btnAffichage.clicked.connect(self.btnAffiche)
        self.btnAttributions.clicked.connect(self.btnAttribute)
        self.btnNotif.clicked.connect(self.btnNotify)
        #####################################################ENREGISTREMENTS###########################################
        self.btnComfirmEt.clicked.connect(self.writeStudent)
        self.btnClassComfirm.clicked.connect(self.writeClasse)
        self.btnComfirmFiliere.clicked.connect(self.writeFiliere)
        self.btnComfirmMatiere.clicked.connect(self.writeMatiere)
        self.btnComfirmUE.clicked.connect(self.writeUE)

        self.Et_Class_ComfirmerAttr.clicked.connect(self.etudiantClass)
        self.prof_class_comfirmer.clicked.connect(self.profClass)
        self.btnMatiereProfComfirm.clicked.connect(self.profMatiere)

        self.pushButton_2.clicked.connect(self.findPhoto)

        ##################################################ANNULATIONS##############################################
        self.btnAnnulEt.clicked.connect(self.clrPageEt)
        self.btnClassAnnuler.clicked.connect(self.clrPageClass)
        self.btnAnnulerFiliere.clicked.connect(self.clrPageFiliere)
        self.btnAnnulerMatiere.clicked.connect(self.clrPageMatiere)
        self.btnAnnulerUE.clicked.connect(self.clrPageUE)
        self.AnnulerAttr_3.clicked.connect(self.clrPageMatProf)
        self.prof_class_annuler.clicked.connect(self.clrPageClassProf)
        self.Et_Class_AnnulerAttr.clicked.connect(self.clrPageEtudiantClass)
        self.comboBox.currentIndexChanged.connect(self.classList)
        box = QComboBox()
        but = QPushButton()
        tabl = QTableWidget()

    def classList(self):
        try:
            self.tableWidget.clearContents()
            classe: str = self.comboBox.currentText()

            query = """SELECT Matricule_etudiant, Nom_etudiant_, Prenom_etudiant_ FROM ETUDIANT WHERE nom_de_la_classe_= ?"""
            try:
                data = cursor.execute(query, (classe,)).fetchall()
            except:
                print("SQL ERROR")
            try:
                for j in range(len(data)):
                    for k in range(len(data[0])):
                        cel = QLabel(data[j][k])
                        self.tableWidget.setCellWidget(j, k, cel)
            except:
                self.label_6.setText("Une Erreur s'est produite!!")
        except:
            self.label_6.setText("Erreur lors de la lecture des données!!")

    def writeFile(self, data, filename):
        with open(filename, 'wb') as file:
            file.write(data)

    def writeBlob(self, filename, ):
        with open(filename, 'rb') as file:
            BLOB = file.read()

        return BLOB

    def writeStudent(self):

        sex = ""

        if self.rdBtnMale.isChecked():
            sex = "Homme"
        elif self.rdBtnFemale.isChecked():
            sex = "Femme"
        try:
            surname = ""
            name = ""
            Id = ""
            phone = ""
            dob = ""
            parentContact = ""
            tutorContact = ""
            surname = self.nomEdit.text()
            name = self.prenomEdit.text()
            Id = self.matriculeEdit.text()
            phone = self.phoneEtud.text()
            dob = self.dateEditEt.text()
            parentContact = self.lineEdit.text()
            tutorContact = self.lineEdit_2.text()
            login = self.matriculeEdit.text()
            password = self.matriculeEdit.text()
            try:
                photoName = self.lineEdit_3.text()
                photo = self.writeBlob(photoName)
            except:
                print("Image Read Error Blob could not be created")

            writeQuery = """INSERT INTO ETUDIANT ("Matricule_etudiant", "Nom_etudiant_", "Prenom_etudiant_",
            "Telephone_etudiant", Date_de_naissance_etudiant,"Numero_parent_etudiant", "photo_etd", "Numero_tuteur_etudiant_", "sexe_etudiant", login, 
            "mot_de_passe") VALUES(?,?,?,?,?,?,?,?,?,?,?) """
            try:
                if surname != "" and name != "" and str(
                        Id) != "" and sex != "" and parentContact != "" and tutorContact != "":
                    data = [(Id, surname, name, phone, dob, parentContact, photo, tutorContact, sex,)]

                    cursor.execute(writeQuery, (
                    Id, surname, name, phone, dob, parentContact, photo, tutorContact, sex, login, password))
                    database.commit()
                    print(data)
                    self.comfirmation.setText("Enregistré Avec Succès")
                else:
                    self.comfirmation.setText("Informations Incompletes!!")
            except:
                self.comfirmation.setText("SQL Error!!")

        except:
            print("an error occurred")
            self.comfirmation.setText("Une Erreur s'est Produite!!")

    def findPhoto(self):
        try:
            fname = QFileDialog.getOpenFileName(self, "Choisir une photo", 'c:\\', 'Images, Png (*.jpg, *.jpeg, *.png)')
            self.lineEdit_3.setText(fname[0])
        except:
            print("File Error!!")
        tb = QToolButton()
        try:
            self.photo = QIcon(fname[0])
            self.toolButton_2.setIcon(self.photo)

        except:
            print("Icon Error")

    def writeClasse(self):
        try:

            nomClass = self.classNomEdit.text()
            salle = self.classSalleEdit.text()
            filiere = self.comboBox_3.currentText()
            note = self.classNoteEdit.toPlainText()
            try:
                fil_id = cursor.execute("""SELECT Numero_filiere_ FROM FILIERE WHERE Nom_filiere_=?""",
                                        (filiere,)).fetchone()[0]
                print(fil_id)
            except:
                # TODO: REMOVE THIS ERROR MSG
                print("Its Not Working !!")
            data = [(nomClass, salle, filiere, note)]
            if nomClass != "" and salle != "" and fil_id != "":
                try:
                    cursor.execute("""INSERT INTO CLASSE VALUES(?,?,?,?)""", (nomClass, salle,fil_id , note))
                    database.commit()
                    self.comfirmation.setText("Enregistré Avec Succès")
                except:
                    print("SQL ERROR")
            else:
                self.comfirmation.setText("Informations Incompletes")
        except:
            print("an error occurred")
            self.comfirmation.setText("Une Erreur s'est Produite!!")

    def writeFiliere(self):

        try:
            numero = ""
            nomFiliere = ""
            libelle = ""
            note = ""

            numero = self.filiereNumeroEdit.text()
            nomFiliere = self.filiereNomEdit.text()
            libelle = self.filiereLibelleEdit.text()
            cycle = self.comboBox_2.currentText()
            note = self.filiereNoteEdit.toPlainText()
            ecole = self.comboBox_4.currentText()

            data = [(numero, nomFiliere, libelle, cycle, note)]
            if numero != "" and nomFiliere != "" and libelle != "":
                ecol = cursor.execute("""SELECT Identifiant__ecole FROM ECOLE WHERE Nom_ecole = ?""",(ecole,)).fetchone()[0]
                print(ecole)
                try:
                    print(data)
                    cursor.execute("""INSERT INTO FILIERE VALUES(?,?,?,?,?,?)""",
                                   (numero, nomFiliere, libelle, ecol, cycle, note))

                    self.comfirmation.setText("Enregistré Avec Succès")
                    database.commit()
                except:
                    print("SQL Error!!")
            else:
                self.comfirmation.setText("Informations Incompletes")
        except:
            print("an error occurred")
            self.comfirmation.setText("Une Erreur s'est Produite!!")

    def writeMatiere(self):

        try:
            CoefMatiere = ""
            nomMatiere = ""
            libelle = ""
            note = ""
            nomMatiere = self.matiereNomEdit.text()
            CoefMatiere = self.matiereCoefEdit.text()
            nom_UE = self.comboBox_5.currentText()
            note = self.matiereNoteEdit.toPlainText()

            data = [(nomMatiere, CoefMatiere, nom_UE, note)]
            if nomMatiere != "" and str(CoefMatiere) != "" and nom_UE != "":
                try:
                    cursor.execute("INSERT INTO MATIERE VALUES(?,?,?,?)", (nomMatiere, CoefMatiere, nom_UE, note,))
                    database.commit()
                    print(data)
                    self.comfirmation.setText("Enregistré Avec Succès")
                except:
                    print("SQL ERROR OCCURRED")
            else:
                self.comfirmation.setText("Informations Incompletes")
        except:
            print("an error occurred")
            self.comfirmation.setText("Une Erreur s'est Produite!!")

    def writeUE(self):
        try:
            ueNom = ""
            note = ""

            ueNom = self.ueNomEdit.text()
            note = self.ueNoteEdit.toPlainText()
            sem = self.comboBox_6.currentText()

            data = [(ueNom, note)]
            if ueNom != "":
                cursor.execute("""INSERT INTO UE VALUES(?,?,?)""", (ueNom, sem, note,))
                print(data)
                database.commit()
                self.comfirmation.setText("Enregistré Avec Succès")
            else:
                self.comfirmation.setText("Informations Incompletes")
        except:
            print("an error occurred")
            self.comfirmation.setText("Une Erreur s'est Produite!!")

    #######################################################ATTRIBUTIONS###################################################

    def etudiantClass(self):

        try:

            Matriculequery = """UPDATE ETUDIANT SET nom_de_la_classe_ =? WHERE Matricule_etudiant =?"""
            classe = self.Et_Classe_Combo.currentText()
            matr = self.Et_Classe_MatrEdit.text()

            cursor.execute(Matriculequery, (classe, matr))
            database.commit()
            self.comfirmation2.setText("Enregistré Avec Succès!")

        except:
            self.comfirmation2.setText("Erreur!!")

    def profClass(self):
        lswg = QListWidget()


        try:
            nom_prof = self.Prof_Class_Combo.currentText().split(" ")
            nom =nom_prof[0]

            matr_prof = cursor.execute("""SELECT Matricule_Professeur FROM PROFESSEUR WHERE Nom_professeur =?""", (nom,)).fetchone()[0]
            for i in range(0, self.profClassListWidget.count()):
                print(self.profClassListWidget.item(i).text())
                cursor.execute("""INSERT INTO attribution (Matricule_Professeur, nom_de_la_classe_) VALUES(?,?)""", (matr_prof, self.profClassListWidget.item(i).text(),))
            database.commit()
        except:
            self.comfirmation2.setText("Une Erreur S'est produite")

    def profMatiere(self):
        nom_prof = self.matiere_prof_Combo.currentText().split(" ")
        nom = nom_prof[0]

        matr_prof = cursor.execute("""SELECT Matricule_Professeur FROM PROFESSEUR WHERE Nom_professeur =?""", (nom,)).fetchone()[0]
        print(matr_prof)
        matiereQuery = """UPDATE attribution SET Nom_de_la_matiere =? WHERE Matricule_Professeur=?"""
        try:
            for i in range(0, self.attrMatieres1.count()):
                cursor.execute(matiereQuery, (self.attrMatieres1.item(i).text(), matr_prof))
            self.comfirmation2.setText("Succès")
            database.commit()
        except:
            self.comfirmation2.setText("Une Erreur S'est Produite, ")


    #######################################################CLEAR ALL FORMS#################################################
    def clrPageEt(self):
        try:
            self.nomEdit.setText("")
            self.prenomEdit.clear()
            self.matriculeEdit.clear()
            self.phoneEtud.clear()
            self.lineEdit.clear()
            self.lineEdit_2.clear()
            self.lineEdit_3.clear()


        except:
            print("Error!!")
            self.comfirmation.setText("Erreur!!")

    def clrPageClass(self):
        try:
            self.classNomEdit.clear()
            self.classSalleEdit.clear()
            self.classNoteEdit.clear()
            self.comboBox_3.clear()
        except:
            print("Error!!!")
            self.comfirmation.setText("Erreur!!!")

    def clrPageFiliere(self):
        try:
            self.filiereNumeroEdit.clear()
            self.filiereNomEdit.clear()
            self.filiereLibelleEdit.clear()
            self.filiereNoteEdit.clear()
        except:
            print("Error!!")
            self.comfirmation.setText("Erreur!!")

    def clrPageMatiere(self):
        try:
            self.matiereNomEdit.clear()
            self.matiereCoefEdit.clear()
            self.matiereLibelleEdit.clear()
            self.matiereNoteEdit.clear()

        except:
            print("Error!!")
            self.comfirmation.setText("Erreur!!!")

    def clrPageUE(self):
        try:
            self.ueNomEdit.clear()
            self.ueNoteEdit.clear()
        except:
            print("Error!!!")
            self.comfirmation.setText("Erreur!!!")

    def clrPageMatProf(self):
        self.attrMatieres1.clear()
        self.matiere_prof_Combo.clear()

    def clrPageClassProf(self):
        self.profClassListWidget.clear()
        self.Prof_Class_Combo.clear()

    def clrPageEtudiantClass(self):
        pass
        self.Et_Classe_MatrEdit.clear()
        self.Et_Classe_Combo.clear()

    #################################################BUTTONS POUR LES DIFF ONGLETS################################################
    def btnNotify(self):
        self.stackedWidget.setCurrentWidget(self.NOTIFICATIONS)
        self.title.setText("NOTIFICATIONS")
        # TODO display notifications whose receiver property equals to the id of the current user
        # TODO CREATE AN ITEMCLICKED ACTION ANDA ITS RECEIVER FUNCTION

    def btnAttribute(self):
        self.stackedWidget.setCurrentWidget(self.AFFECTATIONS)
        self.title.setText("ATTRIBUTIONS")
        try:
            for row in cursor.execute("SELECT nom_de_la_classe_ FROM CLASSE ").fetchall():
                self.Et_Classe_Combo.addItems(row)
        except:
            print("Error!!!!")
        try:
            for row in cursor.execute("SELECT nom_de_la_classe_ FROM CLASSE").fetchall():
                self.listWidget_2.addItems(row)
        except:
            print("Error!!!")
        try:
            for i in cursor.execute("""SELECT Nom_professeur, Prenom_professeur FROM PROFESSEUR""").fetchall():
                item = str(i[0] + " " + i[1])
                self.Prof_Class_Combo.addItem(item)
                self.matiere_prof_Combo.addItem(item)
        except:
            print("Error Here!!")

        try:
            for j in cursor.execute("SELECT Nom_de_la_matiere FROM MATIERE").fetchall():
                self.attrMatieres2.addItems(j)
        except:
            print("Error!!")

    def btnAffiche(self):
        try:
            self.stackedWidget.setCurrentWidget(self.AFFICHAGES)
            self.title.setText("AFFICHAGES")
            try:
                for i in cursor.execute("""SELECT nom_de_la_classe_ FROM CLASSE""").fetchall():
                    self.comboBox.addItems(i)
            except:
                print("Some error occurred")
        except:
            print("Error")

    def btnCreate(self):
        self.stackedWidget.setCurrentWidget(self.CREATIONS)
        self.title.setText("CREATION")
        try:
            for i in cursor.execute("""SELECT nom_filiere_ FROM FILIERE """).fetchall():
                self.comboBox_3.addItems(i)

            for j in cursor.execute("""SELECT Nom_ecole FROM ECOLE""").fetchall():
                self.comboBox_4.addItems(j)

            for k in cursor.execute("""SELECT identifiant_cycle  FROM CYCLE""").fetchall():
                self.comboBox_2.addItems(k)

            for l in cursor.execute("""SELECT Nom_de_l_UE FROM UE""").fetchall():
                self.comboBox_5.addItems(l)

        except:
            print("Error in Initial Startup")


#########################################################LOGIN SCREEN#####################################################


def main():
    app = QApplication(sys.argv)

    win = mainWindow()
    win.show()

    sys.exit(app.exec_())
    database.commit()
    database.close()


if __name__ == '__main__':
    main()
