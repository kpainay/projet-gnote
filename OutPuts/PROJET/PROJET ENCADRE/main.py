# projet encadré d'informatique
from tkinter import *
from tkinter.font import *
from sqlite3 import *
from tkinter import messagebox
from tkinter import ttk
from time import *



"""les differentes fontions et class"""
class etudt:
    def __init__(self, mat, nom, prenom, tel, login,password):
        self.mat = mat
        self.nom = nom
        self.prenom = prenom
        self.tel = tel
        self.login = login
        self.password = password

    def afficher_info(self):
        print(self.mat)
    def afficher1(self):
        print(self.nom)
    def afficher2(self):
        print(self.login)
    def afficher3(self):
        print(self.prenom)
    def afficher4(self):
        print(self.tel)

class Inspecteur_de_filiere():
    def __init__(self, matricule, nom, prenom,numero, login , password):
        self.matricule = matricule
        self.nom= nom
        self.prenom = prenom
        self.numero = numero
        self.login = login
        self.password =password

    def interpeler_DE(self, message, mat_DE):
        connectons = connect("gnote_base.db")
        cursseur = connectons.cursor()

        date = strftime("%d/%m/%Y")
        heure = strftime("%H H %I")

        valeur = [(message, date, heure, "", "", mat_DE, "")]
        cursseur.executemany("""INSERT INTO Notification (libéllé_notif, date_notif, heure_notif, Matricule_etudiant, Matricule_directeur_d_ecole, identifant_DE, Matricule_Professeur) VALUES (?,?,?,?,?,?,?)""",valeur)

        connectons.commit()
        connectons.close()
        messagebox.showinfo("INFORMATION", " L'interpellation a été envoyé avec succes")

    def justifier(self, id_absence):
        connexion = connect("gnote_base.db")
        cursseur = connexion.cursor()

        cursseur.execute("""SELECT * FROM ABSENCE""")
        resultats1 = cursseur.fetchall()
        absence1 = []
        for resultat1 in resultats1:
            if str(resultat1[0]) == id_absence:
                absence1 = resultat1

        if absence1[7] == "NJNV":
            cursseur.execute("""UPDATE ABSENCE SET id_etat = "JNV" WHERE Idetifiant_absence_ =?""", (id_absence,))

        connexion.commit()
        connexion.close()
        messagebox.showinfo("INFORMATION", " L'absence a été justifié")

class professeur:
    def __init__(self, matricule, nom, prenom,numero, mail, login , password):
        self.matricule = matricule
        self.nom= nom
        self.prenom = prenom
        self.numero = numero
        self.mail = mail
        self.login = login
        self.password =password


    def ajouter_abs(self,heure_d, heure_f, mat_etu):

        connexion = connect("gnote_base.db")
        cursseur = connexion.cursor()
        date = strftime("%d/%m/%Y")
        id_etat = "NJNV"
        req1 = """SELECT*FROM ETUDIANT"""
        req2 = """SELECT * FROM CLASSE"""
        req3 = """SELECT * FROM DIRECTEUR_D_ETUDE"""
        req4 = """SELECT * FROM Inspecteur"""
        cursseur.execute(req1)
        r1 = cursseur.fetchall()
        cursseur.execute(req2)
        r2 = cursseur.fetchall()
        cursseur.execute(req3)
        r3 = cursseur.fetchall()
        cursseur.execute(req4)
        r4 = cursseur.fetchall()
        nom_classe = ""
        matri_ins = ""
        num_filiere = ""
        id_DE = ""
        for i in r1:
            if i[0] == mat_etu:
                nom_classe = i[11]
        for i in r2:
            if i[0] == nom_classe:
                num_filiere = i[2]
        for i in r3:
            if i[1] == num_filiere:
                id_DE = i[0]
        for i in r4:
            if i[7] == num_filiere:
                matri_ins = i[0]


        valeur =[(date, heure_d, heure_f,matri_ins, self.matricule, mat_etu, id_etat, id_DE )]
        cursseur.executemany("""INSERT INTO ABSENCE (date_d_absence_, Heure_de_debut, Heure_de_fin,Matricule_inspecteur, Matricule_Professeur, Matricule_etudiant, id_etat, identifant_DE) VALUES (?,?,?,?,?,?,?,?) """,valeur)

        connexion.commit()
        connexion.close()
        messagebox.showinfo("INFORMATION", " L'absence a été enregistré")

class DE(professeur):
    def __init__(self, matricule, nom, prenom,numero, mail, login , password, id_DE, num_fil):
        professeur.__init__(self, matricule, nom, prenom, numero, mail, login, password)
        self.id_DE = id_DE
        self.num_filiere = num_fil

    def ajouter_notif(self, message , mat_etu):
        connexion = connect("gnote_base.db")
        cursseur = connexion.cursor()

        date = strftime("%d/%m/%Y")
        heure = strftime("%H H %I")

        valeur = [(message, date, heure, mat_etu, "", "", "")]
        cursseur.executemany("""INSERT INTO Notification (libéllé_notif, date_notif, heure_notif, Matricule_etudiant, Matricule_directeur_d_ecole, identifant_DE, Matricule_Professeur) VALUES (?,?,?,?,?,?,?)""",valeur)

        connexion.commit()
        connexion.close()
        messagebox.showinfo("INFORMATION", " L'avertissement a été envoyé avec succes")
    def valider_absence(self, id_absence):
        connexion = connect("gnote_base.db")
        cursseur = connexion.cursor()

        cursseur.execute("""SELECT * FROM ABSENCE""")
        resultats1 = cursseur.fetchall()
        absence1 = []
        print(id_absence)
        for resultat1 in resultats1:
            if str(resultat1[0]) == id_absence:
                absence1 = resultat1

        if absence1[7] == "NJNV":
            cursseur.execute(""" UPDATE ABSENCE SET id_etat = "NJV" WHERE Idetifiant_absence_ = ?""", (id_absence,))
        if absence1[7] == "JNV":
            cursseur.execute(""" UPDATE ABSENCE SET id_etat = "JV" WHERE Idetifiant_absence_ = ?""", (id_absence,))

        connexion.commit()
        connexion.close()
        messagebox.showinfo("INFORMATION", " L'absence a été validé")


#Gestion des etudiants ----------------------------------------------------------------------------------------------------------------

def etudiant():
    def Etudiant():
        Label(Gabsence).place(x=0, y=0, relwidth=1, relheight=1)
        Label(Gabsence, text="ETUDIANT", font=Font(family="Aharoni", size=40, underline=2,weight="bold"), width=155).place(x=0, y=0, relwidth = 1)
        p1 = PanedWindow(Gabsence, orient=HORIZONTAL)
        p1.add(Label(p1, background='orange', anchor=CENTER, padx=230))
        p1.add(Label(p1, background='white', anchor=CENTER, padx=230))
        p1.add(Label(p1, background='green', anchor=CENTER, padx=230))
        p1.place(x = 0, y = 100, relwidth = 1)

        Button(Gabsence, text="MES HEURES D'ABSENCES", command=Absence, font=("arial", 15), width=100, cursor="hand2").place(x=110, y=190)
        Button(Gabsence, text="NOTIFICATIONS", command=Notif, font=("arial", 15), width=100, cursor="hand2").place(x=110,y=270)
        Button(Gabsence, text="QUITTER", font=("arial", 15), width=50, cursor="hand2", command=Gabsence.quit).place(x=420, y=510)
        p2 = PanedWindow(Gabsence, orient=HORIZONTAL)
        p2.add(Label(p2, text="UNION", font=("arial", 15), background='orange', anchor=CENTER, padx=180))
        p2.add(Label(p2, text="DISCIPLINE", font=("arial", 15), background='white', anchor=CENTER, padx=190))
        p2.add(Label(p2, text="TRAVAIL", font=("arial", 15), background='green', anchor=CENTER, padx=180))
        p2.place(x=0, y=650)
        Button(Gabsence, image=retour, command=accueil, border=0,cursor="hand2").place(x=0, y=0)


    def Absence():

        con = connect("gnote_base.db")

        curseur = con.cursor()

        req1 = '''SELECT* from ABSENCE '''
        curseur.execute(req1)
        resultats = curseur.fetchall()

        req2 = '''SELECT * FROM PROFESSEUR'''
        curseur.execute(req2)
        resultats2 = curseur.fetchall()

        Label(Gabsence).place(x=0, y=0, relwidth=1, relheight=1)
        my_tree = ttk.Treeview(Gabsence, column=(1, 2, 3, 4, 5), show="headings")
        my_tree['columns'] = (1, 2, 3, 4,5)

        my_tree.column(1, width=120, anchor="center")
        my_tree.column(2, width=200, anchor="center")
        my_tree.column(3, width=120, anchor="center")
        my_tree.column(4, width=120, anchor="center")
        my_tree.column(5, width=120, anchor="center")

        my_tree.heading(4, text="NOM DU PROFESSEUR")
        my_tree.heading(1, text="DATE D'ABSENCE")
        my_tree.heading(2, text="HEURE DE DEBUT")
        my_tree.heading(3, text="HEURE DE FIN")
        my_tree.heading(5, text="ETAT DE L'ABSENCE")

        for i in resultats:
            for j in resultats2:
                if j[0] == i[5]:
                    enter = [i[1], i[2], i[3],"M. "+ j[1], i[7]]
                    if i[6] == etudiants.mat:
                        my_tree.insert('', END, values=enter)

        my_tree.place(x = 0, y =0, relwidth = 1, relheight = 1)
        Button(Gabsence, image = retour, command = Etudiant, border = 0).place(x = 0, y = 700)


    def Notif():

        con = connect("gnote_base.db")

        curseur = con.cursor()

        req1 = '''SELECT* from Notification '''
        curseur.execute(req1)
        resultats = curseur.fetchall()

        h = Label(Gabsence).place(x=0, y=0, relwidth=1, relheight=1)
        my_tree = ttk.Treeview(Gabsence, column=(1, 2, 3, 4), show="headings")
        my_tree['columns'] = (1, 2, 3, 4)
        my_tree.column(1, anchor="center", width=80)
        my_tree.column(2, anchor="center", width=200)
        my_tree.column(3, anchor="center", width=150)
        my_tree.column(4, anchor="center", width=120)

        my_tree.heading(1, text="ID")
        my_tree.heading(2, text="LIBELLE")
        my_tree.heading(3, text="DATE")
        my_tree.heading(4, text = "HEURE")

        for i in resultats:
            enter = [i[0], i[1], i[2], i[3]]
            if i[4] == etudiants.mat:
                my_tree.insert('', END, values=enter)

        def item_selected(event):
            record = []
            for selected_item in my_tree.selection():
                item = my_tree.item(selected_item, 'value')
                record.append(item)

            messagebox.showinfo(title='Information', message=record)

        my_tree.bind('<<TreeviewSelect>>', item_selected)

        my_tree.place(x = 0, y =0, relwidth = 1, relheight = 1)
        Button(Gabsence, image=retour, command=Etudiant, border=0).place(x=0, y=700)

    Etudiant()


#Gestion des directeurs des etudes------------------------------------------------------------------------------------------------------

def de():

    #page d'accueil du DE---------------------------------------------------------------------------------------------------------------

    def accueil_de():
        etu = Label(Gabsence, bg = "#FF9F00").place(x=0, y=0, relwidth= 1, relheight = 1)
        Label(etu, image = AP_DE, bg = "#FF9F00").place(x=250, y=50, relwidth = 1, relheight = 1)
        profil =Label(Gabsence, bg= "ivory", width = 70, height = 1).place(x=0, y =0, relheight = 1)
        retour_btn = Button(etu, image=retour, command=accueil, borderwidth=0, cursor="hand2", bg="ivory")
        retour_btn.place(x=0, y=0)
        Label(profil, image = DE, bg = "ivory"). place(x = 190, y = 100)

        frame_choice = Label(profil, border = 15, width = 850, height =9,bg = "#fF9F00")
        frame_choice.place(x = 540, y = 0)

        #Choix du directeur d'etude -------------------------------------------------------------------------------------------------------------------------------

        Button(frame_choice, image=abs_NJ, text=" Voire la liste des absences non justifié", cursor="hand2", compound="top",bg = "#FF9f00",border=0, command = liste_abs_NJ).place(x= 0, y=0)
        Button(frame_choice, image = abscence, text="Valider les absences", border = 0, cursor="hand2", compound="top",bg = "#FF9f00", command = valider_abs).place(x =250, y = 0)
        Button(frame_choice, image = interpeler, text="Avertir un etudiant",border = 0, cursor="hand2", compound = "top",bg = "#FF9f00", command = averti).place(x = 450, y = 0)
        Button(frame_choice, image = notif, text = "Notification", border = 0, cursor="hand2" , compound = "top", bg = "#FF9F00", command = notifi).place(x = 600, y = 0)


        # information personnelle du directeur d'école

        Label(profil, text="Nom :", bg="ivory",font=("Aharoni", 14)).place(y=250, x=200)
        Label(profil, text="Prenoms :", bg="ivory", font=Font(family="Aharoni", size=14, underline=2)).place(y=350,x=30)
        Label(profil, text="Telephone :", bg="ivory", font=Font(family="Aharoni", size=14, underline=2)).place(y=450,x=200)
        Label(profil, text="Adresse electronique:", bg="ivory",font=Font(family="Aharoni", size=14, underline=2)).place(y=550, x=20)

        # affichage d'information personnel
        Label(profil, text=Directeur.nom, bg="ivory", font=Font(family="Aharoni", size=14)).place(y=250, x=300)
        Label(profil, text=Directeur.prenom, bg="ivory", font=Font(family="Aharoni", size=14)).place(y=350, x=130)
        Label(profil, text=Directeur.numero, bg="ivory", font=Font(family="Aharoni", size=14)).place(y=450, x=310)
        Label(profil, text=Directeur.mail, bg="ivory", font=Font(family="Aharoni", size=14)).place(y=550, x=220)

    #fonction pour affichier la liste des absence non justifier-----------------------------------------------------------------------------------------------------

    def liste_abs_NJ():
        con = connect("gnote_base.db")

        curseur = con.cursor()

        req1 = '''SELECT * from ABSENCE '''
        curseur.execute(req1)
        resultats = curseur.fetchall()

        req2 = '''SELECT * from ETUDIANT '''
        curseur.execute(req2)
        resultats2 = curseur.fetchall()

        Label(Gabsence).place(x=0, y=0, relwidth=1, relheight=1)
        my_tree = ttk.Treeview(Gabsence, column=(1, 2, 3, 4, 5,6,7), show="headings")

        my_tree.column(1, width=105, anchor="center")
        my_tree.column(2, width=130, anchor="center")
        my_tree.column(3, width=100, anchor="center")
        my_tree.column(4, width=130, anchor="center")
        my_tree.column(5, width=130, anchor="center")
        my_tree.column(6, width=130, anchor="center")
        my_tree.column(7, width=130, anchor="center")

        my_tree.heading(1, text="NOM")
        my_tree.heading(4, text="DATE DE L'ABSENCE")
        my_tree.heading(5, text="HEURE DE DEBUT")
        my_tree.heading(6, text="HEURE DE FIN")
        my_tree.heading(3, text="MATRICULE")
        my_tree.heading(7, text = "ETAT DE L'ABSENCE ")
        my_tree.heading(2, text="PRENOM")

        for i in resultats:
            for j in resultats2:
                if j[0] == i[6]:
                    enter = [j[1], j[2], j[0], i[1],i[2], i[3], i[7], i[0]]
                    if i[-1] == Directeur.id_DE:
                        if i[7] == "NJNV" or i[7] == "NJV":
                            my_tree.insert('', END, values=enter)

        my_tree.place(x=500, y=60, relheight=1)

        Label(Gabsence, text="LISTE DES ABSENCES NON JUSTIFIé", font=Font(family="Algerian", size=34, weight="bold"),bg="#FFFFFF").place(x=250, y=0, relwidth = 1)
        profil = Label(Gabsence, bg="#00FF9F", width=70, height=1).place(x=0, y=0, relheight=1)
        retour_btn = Button(Gabsence, image=retour, command=accueil_de, borderwidth=0, cursor="hand2", bg="#00FF9F")
        retour_btn.place(x=0, y=0)
        Label(profil, image=DE, bg="#00FF9F").place(x=190, y=100)

        # information personnelle du directeur d'école

        Label(profil, text="Nom :", bg="#00FF9F", font=Font(family="Aharoni", size=14, underline=2)).place(y=250, x=200)
        Label(profil, text="Prenoms :", bg="#00FF9F", font=Font(family="Aharoni", size=14, underline=2)).place(y=350,x=30)
        Label(profil, text="Telephone :", bg="#00FF9F", font=Font(family="Aharoni", size=14, underline=2)).place(y=450,x=200)
        Label(profil, text="Adresse electronique:", bg="#00FF9F", font=Font(family="Aharoni", size=14, underline=2)).place(y=550, x=20)

        # affichage d'information personnel
        Label(profil, text=Directeur.nom, bg= "#00FF9F", font=Font(family="Aharoni", size=14)).place(y=250, x=300)
        Label(profil, text=Directeur.prenom, bg="#00FF9F", font=Font(family="Aharoni", size=14)).place(y=350, x=130)
        Label(profil, text=Directeur.numero, bg="#00FF9F", font=Font(family="Aharoni", size=14)).place(y=450, x=310)
        Label(profil, text=Directeur.mail, bg="#00FF9F", font=Font(family="Aharoni", size=14)).place(y=550, x=220)

        Label(Gabsence, text="LISTE DES ABSENCES NON JUSTIFIé", font=Font(family="Algerian", size=34, weight = "bold"), bg = "#FFFFFF").place(x=550,y=0)


    #fonction pour valider les absences------------------------------------------------------------------------------------------------------------------------------

    def valider_abs():
        con = connect("gnote_base.db")

        curseur = con.cursor()

        req1 = '''SELECT * from ABSENCE '''
        curseur.execute(req1)
        resultats = curseur.fetchall()

        req2 = '''SELECT * from ETUDIANT '''
        curseur.execute(req2)
        resultats2 = curseur.fetchall()

        def chercher_etudiant(matricule_etudiant):
            con = connect("gnote_base.db")
            curseur = con.cursor()

            req1 = "SELECT * FROM ETUDIANT"
            curseur.execute(req1)
            resultats2 = curseur.fetchall()
            connexion.close()
            con.close()
            # rechercher le matricule de l'etudiant
            for resultat in resultats2:
                if resultat[0] == matricule_etudiant:
                    etu = etudt(resultat[0], resultat[1], resultat[2], resultat[3], resultat[9], resultat[10])
                    return 1, etu
            return 0,0

        Label(Gabsence).place(x=0, y=0, relwidth=1, relheight=1)
        my_tree = ttk.Treeview(Gabsence, column=(1, 2, 3, 4, 5, 6, 7), show="headings")

        my_tree.column(1, width=105, anchor="center")
        my_tree.column(2, width=130, anchor="center")
        my_tree.column(3, width=100, anchor="center")
        my_tree.column(4, width=130, anchor="center")
        my_tree.column(5, width=130, anchor="center")
        my_tree.column(6, width=130, anchor="center")
        my_tree.column(7, width=130, anchor="center")

        my_tree.heading(1, text="NOM")
        my_tree.heading(4, text="DATE DE L'ABSENCE")
        my_tree.heading(5, text="HEURE DE DEBUT")
        my_tree.heading(6, text="HEURE DE FIN")
        my_tree.heading(3, text="MATRICULE")
        my_tree.heading(7, text="ETAT DE L'ABSENCE ")
        my_tree.heading(2, text="PRENOM")

        for i in resultats:
            for j in resultats2:
                if j[0] == i[6]:
                    enter = [j[1], j[2], j[0], i[1], i[2], i[3], i[7], i[0]]
                    if i[-1] == Directeur.id_DE:
                        if i[7] == "NJNV" or i[7] == "JNV":
                            my_tree.insert('', END, values=enter)

        def item_selected(event):
            record = []
            for selected_item in my_tree.selection():
                item = my_tree.item(selected_item, 'value')
                record.append(item)

            etu = chercher_etudiant(record[0][2])
            reponse =messagebox.askyesno(title='ATTENTION', message="Voulez vous valider l'absence de l'etudiant {} {}".format(etu[1].nom, etu[1].prenom))

            if reponse == True:
                Directeur.valider_absence(record[0][-1])
                valider_abs()


        my_tree.bind('<<TreeviewSelect>>', item_selected)

        my_tree.place(x=500, y=60, relheight=1)
        Label(Gabsence, text="LISTE DES ABSENCES NON VALIDé", font=Font(family="Algerian", size=34, weight="bold"),bg="#FFFFFF").place(x=250, y=0, relwidth=1)

        profil = Label(Gabsence, bg="#00FF9F", width=70, height=1).place(x=0, y=0, relheight=1)
        retour_btn = Button(Gabsence, image=retour, command=accueil_de, borderwidth=0, cursor="hand2", bg="#00FF9F")
        retour_btn.place(x=0, y=0)
        Label(profil, image=DE, bg="#00FF9F").place(x=190, y=100)


        # information personnelle du directeur d'école

        Label(profil, text="Nom :", bg="#00FF9F", font=Font(family="Aharoni", size=14, underline=2)).place(y=250, x=200)
        Label(profil, text="Prenoms :", bg="#00FF9F", font=Font(family="Aharoni", size=14, underline=2)).place(y=350,  x=30)
        Label(profil, text="Telephone :", bg="#00FF9F", font=Font(family="Aharoni", size=14, underline=2)).place(y=450,  x=200)
        Label(profil, text="Adresse electronique:", bg="#00FF9F",font=Font(family="Aharoni", size=14, underline=2)).place(y=550, x=20)

        # affichage d'information personnel
        Label(profil, text=Directeur.nom, bg="#00FF9F", font=Font(family="Aharoni", size=14)).place(y=250, x=300)
        Label(profil, text=Directeur.prenom, bg="#00FF9F", font=Font(family="Aharoni", size=14)).place(y=350, x=130)
        Label(profil, text=Directeur.numero, bg="#00FF9F", font=Font(family="Aharoni", size=14)).place(y=450, x=310)
        Label(profil, text=Directeur.mail, bg="#00FF9F", font=Font(family="Aharoni", size=14)).place(y=550, x=220)



    #fonction pour affichier les notification du directeur d'etude---------------------------------------------------------------------------------------------------

    def notifi():
        con = connect("gnote_base.db")

        curseur = con.cursor()

        req1 = '''SELECT* from Notification '''
        curseur.execute(req1)
        resultats = curseur.fetchall()

        Label(Gabsence).place(x=0, y=0, relwidth=1, relheight=1)
        my_tree = ttk.Treeview(Gabsence, column = (1,2,3,4), show ="headings" )
        my_tree['columns'] = (1, 2, 3, 4)
        my_tree.column(1, anchor="center", width=80)
        my_tree.column(2, anchor="center", width=500)
        my_tree.column(3, anchor="center", width=150)
        my_tree.column(4, anchor="center", width=120)

        my_tree.heading(1, text="ID")
        my_tree.heading(2, text="LIBELLE")
        my_tree.heading(3, text="DATE")
        my_tree.heading(4, text="HEURE")

        for i in resultats:
            enter = [i[0], i[1], i[2],i[3]]
            if i[6] == Directeur.id_DE:
                my_tree.insert('', END, values=enter)

        #affichage des données du TREEVIEW
        def item_selected(event):
            record = []
            for selected_item in my_tree.selection():
                item = my_tree.item(selected_item, 'value')
                record.append(item)

            messagebox.showinfo(title='Information', message=record)

        my_tree.bind('<<TreeviewSelect>>', item_selected)

        my_tree.place(x=500, y=60, relheight=1)

        Label(Gabsence, text="MES NOTIFICATIONS", font=Font(family="Algerian", size=34, weight="bold"),bg="#FFFFFF").place(x=315, y=0, relwidth = 1)
        Button(Gabsence, text="Avertir un etudiant", command=averti, border=0, cursor="hand2").place(x=1250, y=700)

        profil = Label(Gabsence, bg="#00FF9F", width=70, height=1).place(x=0, y=0, relheight=1)
        retour_btn = Button(Gabsence, image=retour, command=accueil_de, borderwidth=0, cursor="hand2", bg="#00FF9F")
        retour_btn.place(x=0, y=0)
        Label(profil, image=DE, bg="#00FF9F").place(x=190, y=100)

        # information personnelle du directeur d'école

        Label(profil, text="Nom :", bg="#00FF9F", font=Font(family="Aharoni", size=14, underline=2)).place(y=250, x=200)
        Label(profil, text="Prenoms :", bg="#00FF9F", font=Font(family="Aharoni", size=14, underline=2)).place(y=350,x=30)
        Label(profil, text="Telephone :", bg="#00FF9F", font=Font(family="Aharoni", size=14, underline=2)).place(y=450, x=200)
        Label(profil, text="Adresse electronique:", bg="#00FF9F", font=Font(family="Aharoni", size=14, underline=2)).place(y=550, x=20)

        # affichage d'information personnel
        Label(profil, text=Directeur.nom, bg="#00FF9F", font=Font(family="Aharoni", size=14)).place(y=250, x=300)
        Label(profil, text=Directeur.prenom, bg="#00FF9F", font=Font(family="Aharoni", size=14)).place(y=350, x=130)
        Label(profil, text=Directeur.numero, bg="#00FF9F", font=Font(family="Aharoni", size=14)).place(y=450, x=310)
        Label(profil, text=Directeur.mail, bg="#00FF9F", font=Font(family="Aharoni", size=14)).place(y=550, x=220)



    #fonction pour avertir un etudiant-------------------------------------------------------------------------------------------------------------------------------
    def averti():
        def rechercher_etudiant(event):
            connexion = connect("gnote_base.db")
            curseur = connexion.cursor()

            req1 = "SELECT * FROM ETUDIANT"
            curseur.execute(req1)
            resultats = curseur.fetchall()
            connexion.close()
            #rechercher le matricule
            for resultat in  resultats:
                if resultat[0] == Champ_saisie.get():
                    etu = etudt(resultat[0],resultat[1],resultat[2],resultat[3],resultat[9],resultat[10])
                    return 1,etu

            return 0,0

        def action_bouton():
            def test():
                connexion = connect("gnote_base.db")
                curseur = connexion.cursor()

                req1 = "SELECT * FROM ETUDIANT"
                curseur.execute(req1)
                resultats = curseur.fetchall()
                connexion.close()
                etu = dict()
                for resultat in resultats:
                    if resultat[0] == Champ_saisie.get():
                        etu = etudt(resultat[0], resultat[1], resultat[2], resultat[3], resultat[9], resultat[10])
                        return 1, etu

                return 0,etu
            a = test()
            aff_var = StringVar()
            champ_aff = Entry(Decole, textvariable=aff_var, border=0, bg="#FFFFFF", width=40)
            champ_aff.bind("<Return>", afficher_info)
            if a[0] == 1:
                message = "VOULEZ VOUS AVERTIR L'ETUDIANT {} {}"
                reponse = messagebox.askyesno("AVERTISSEMENT",message.format(a[1].nom,a[1].prenom))
                if reponse == True:
                    libelle = "NOM: {} \nPRENOM: {} \nOBJET : AVERTISSEMENT POUR ABSENCE\n\nM/Mme cette notification est un avertissement pour vos nombreuse heures d'absence.priez etre assidus en classe.\n Merci de votre attention"
                    Directeur.ajouter_notif(libelle.format(Directeur.nom,Directeur.prenom), Champ_saisie.get())
            if a[0] == 0:
                messagebox.showinfo("INFORMATION","LE MATRICULE QUE VOUOS VENEZ D'ENTREZ N'EST PAS RECONUE PAR LE SYSTEME ")

        def afficher_info(event):
            value = rechercher_etudiant(event)
            aff_var = StringVar()
            champ_aff = Entry(Decole, textvariable = aff_var, border = 0, bg = "#FFFFFF", width = 40)
            champ_aff.bind("<Return>", afficher_info)
            if value[0] == 1:
                message = "VOULEZ VOUS AVERTIR L'ETUDIANT {} {}"
                reponse = messagebox.askyesno("AVERTISSEMENT",message.format(value[1].nom, value[1].prenom))
                if reponse == True:
                    libelle = "NOM: {} \nPRENOM: {} \nOBJET : AVERTISSEMENT POUR ABSENCE\n\nM/Mme cette notification est un avertissement pour vos nombreuse heures d'absence.priez etre assidus en classe.\n Merci de votre attention"
                    Directeur.ajouter_notif(libelle.format(Directeur.nom, Directeur.prenom), Champ_saisie.get())
            if value[0] == 0:
                messagebox.showinfo("INFORMATION", "LE MATRICULE QUE VOUOS VENEZ D'ENTREZ N'EST PAS RECONUE PAR LE SYSTEME ")

        Decole= Label(Gabsence, bg="#FFFFFF").place(x=0, y=0, relwidth=1, relheight=1)
        Label(Decole, image=BG_avert, bg="#FFFFFF").place(x=250, y=50, relwidth=1, relheight=1)
        profil = Label(Gabsence, bg="#00FF9F", width=70, height=1).place(x=0, y=0, relheight=1)
        retour_btn = Button(Decole, image=retour, command=accueil_de, borderwidth=0, cursor="hand2", bg="#00FF9F")
        retour_btn.place(x=0, y=0)
        Label(profil, image=DE, bg="#00FF9F").place(x=190, y=100)

        # information personnelle du directeur d'école

        Label(profil, text="Nom :", bg="#00FF9F", font = Font(family="Aharoni", size=14, underline=2)).place(y=250, x=200)
        Label(profil, text="Prenoms :", bg="#00FF9F", font=Font(family="Aharoni", size=14, underline=2)).place(y=350,x=30)
        Label(profil, text="Telephone :", bg="#00FF9F", font=Font(family="Aharoni", size=14, underline=2)).place(y=450, x=200)
        Label(profil, text="Adresse electronique:", bg="#00FF9F",font=Font(family="Aharoni", size=14, underline=2)).place(y=550, x=20)

        # affichage d'information personnel
        Label(profil, text=Directeur.nom, bg="#00FF9F", font=Font(family="Aharoni", size=14)).place(y=250, x=300)
        Label(profil, text=Directeur.prenom, bg="#00FF9F", font=Font(family="Aharoni", size=14)).place(y=350, x=130)
        Label(profil, text=Directeur.numero, bg="#00FF9F", font=Font(family="Aharoni", size=14)).place(y=450, x=310)
        Label(profil, text=Directeur.mail, bg="#00FF9F", font=Font(family="Aharoni", size=14)).place(y=550, x=220)

        Label(Decole, text="AVERTIR UN éTUDIANT ", font=Font(family="Algerian", size=34, weight="bold"),bg="#FFFFFF").place(x=670, y=0)
        Label(Decole, text = "Entrez le matricule de l'étudiant à avertir", font = Font(family = "serif", size = 15), bg = "#FFFFFF").place(x = 500, y =150)
        Champ_saisie_var = StringVar()
        Champ_saisie = Entry(Decole, textvariable = Champ_saisie_var, font = Font(family = "serif", size = 15), bg = "#FFFF0F")
        Button(Decole, image = rechercher, bg = "#FFFFFF", border = 0, cursor = "hand2", command = action_bouton).place(x=1200, y=140)
        Champ_saisie.bind("<Return>", afficher_info)
        Champ_saisie.place(x = 950, y = 150)


    accueil_de()

#Gestion de prof-------------------------------------------------------------------------------------------------------------------------------------

def prof():

    #Page d'accueil du professeur --------------------------------------------------------------------------------------------
    def accueil_prof():
        professeur = Label(Gabsence, bg="#7FAF7F").place(x=0, y=0, relwidth=1, relheight=1)
        Label(professeur, image=BG_prof, bg="#7FAF7F").place(x=250, y=0, relwidth=1, relheight=1)
        profil = Label(Gabsence, bg="ivory", width=70, height=1).place(x=0, y=0, relheight=1)
        retour_btn = Button(professeur, image=retour, command=accueil, borderwidth=0, cursor="hand2", bg="ivory")
        retour_btn.place(x=0, y=0)
        Label(profil, image=DE, bg="ivory").place(x=190, y=100)
        Button(professeur, text = "Marquer les abscences ", image = marquer, command = marque_abs,bg = "#7FAF7F", border = 0, cursor = "hand2",compound = "top").place(x = 770, y=55)

        #informations personnelles du professeur

        Label(profil, text="Nom :", bg="ivory", font=Font(family="Aharoni", size=14, underline=2)).place(y=250, x=200)
        Label(profil, text="Prenoms :", bg="ivory", font=Font(family="Aharoni", size=14, underline=2)).place(y=350,x=30)
        Label(profil, text="Telephone :", bg="ivory", font=Font(family="Aharoni", size=14, underline=2)).place(y=450,x=200)
        Label(profil, text="Adresse electronique:", bg="ivory",font=Font(family="Aharoni", size=14, underline=2)).place(y=550, x=20)

        # affichage d'information personnel
        Label(profil, text=Professeur.nom, bg="ivory", font=Font(family="Aharoni", size=14)).place(y=250, x=300)
        Label(profil, text=Professeur.prenom, bg="ivory", font=Font(family="Aharoni", size=14)).place(y=350, x=130)
        Label(profil, text=Professeur.numero, bg="ivory", font=Font(family="Aharoni", size=14)).place(y=450, x=310)
        Label(profil, text=Professeur.mail, bg="ivory", font=Font(family="Aharoni", size=14)).place(y=550, x=220)

    def marque_abs():
        professeu = Label(Gabsence, bg="#236326").place(x=0, y=0, relwidth=1, relheight=1)
        Label(professeu, image=BG_mar, bg="#236326").place(x=250, y=0, relwidth=1, relheight=1)
        profil = Label(Gabsence, bg= "#7FAF7F", width=70, height=1).place(x=0, y=0, relheight=1)
        retour_btn = Button(professeu, image=retour, command=accueil_prof, borderwidth=0, cursor="hand2", bg="#7FAF7F")
        retour_btn.place(x=0, y=0)
        Label(profil, image=DE, bg="#7FAF7F").place(x=190, y=100)
        Label(professeu, text="MARQUER LES ABSENCES", font=Font(family="Algerian", size=34, weight="bold"),bg="#236326",fg = "orange").place(x=700, y=0)

        # information personnelle du professeur

        Label(profil, text="Nom :", bg="#7FAF7F", font=Font(family="Aharoni", size=14, underline=2)).place(y=250, x=200)
        Label(profil, text="Prenoms :", bg="#7FAF7F", font=Font(family="Aharoni", size=14, underline=2)).place(y=350,x=30)
        Label(profil, text="Telephone :", bg="#7FAF7F", font=Font(family="Aharoni", size=14, underline=2)).place(y=450,x=200)
        Label(profil, text="Adresse electronique:", bg="#7FAF7F",font=Font(family="Aharoni", size=14, underline=2)).place(y=550, x=20)

        # affichage d'information personnel
        Label(profil, text=Professeur.nom, bg="#7FAF7F", font=Font(family="Aharoni", size=14)).place(y=250, x=300)
        Label(profil, text=Professeur.prenom, bg="#7FAF7F", font=Font(family="Aharoni", size=14)).place(y=350, x=130)
        Label(profil, text=Professeur.numero, bg="#7FAF7F", font=Font(family="Aharoni", size=14)).place(y=450, x=310)
        Label(profil, text=Professeur.mail, bg="#7FAF7F", font=Font(family="Aharoni", size=14)).place(y=550, x=220)



        def bouton_act():
            def test():
                connexion = connect("gnote_base.db")
                curseur = connexion.cursor()

                req1 = "SELECT * FROM ETUDIANT"
                curseur.execute(req1)
                resultats = curseur.fetchall()
                connexion.close()
                #Verifie si tous les champs sont remplis
                if Champ_saisie_mat.get() == "" or Champ_saisie_hd.get() == "" or Champ_saisie_hf.get() == "":
                    return 2,2

                #verifie si le matricule saisir appartient a la base de donnée
                for resultat in resultats:
                    if resultat[0] == Champ_saisie_mat.get():
                        etu = etudt(resultat[0], resultat[1], resultat[2], resultat[3], resultat[9], resultat[10])
                        return 1, etu

                return 0, 0

            testeur = test()
            if testeur[0] == 1:
                message = "VOULEZ VOUS MARQUER ABSENT(E) L'ETUDIANT {} {}"
                reponse = messagebox.askyesno("AVERTISSEMENT", message.format(testeur[1].nom, testeur[1].prenom))
                if reponse == True:
                    Professeur.ajouter_abs(Champ_saisie_hd.get(),Champ_saisie_hf.get(), Champ_saisie_mat.get())
                    Champ_saisie_var1.set("")
            elif testeur[0] == 0:
                messagebox.showinfo("INFORMATION", "LE MATRICULE QUE VOUS VENEZ D'ENTREZ N'EST PAS RECONUE PAR LE SYSTEME ")
            else:
                messagebox.showinfo("ATTENTION", "VEILLEZ REMPLIR TOUS LES CHAMPS")

        #Creation des champs et variables de saisir

        Champ_saisie_var1 = StringVar()
        Champ_saisie_var2 = StringVar()
        Champ_saisie_var3 = StringVar()
        Label(Gabsence, text = "ENTREZ LE MATRICULE DE L'ETUDIANT", fg = "white", bg = "#236326",font = Font(size = 16)).place(y = 150, x = 500)
        Label(Gabsence, text="ENTREZ L'HEURE DE DEBUT DE L'ABSENCE", fg = "white", bg = "#236326",font = Font(size = 16)).place(y = 250, x = 500)
        Label(Gabsence, text="ENTREZ L'HEURE DE FIN DE L'ABSENCE", fg = "white", bg = "#236326",font = Font(size = 16)).place(y = 350, x = 500)
        Champ_saisie_mat = Entry(Gabsence, textvariable=Champ_saisie_var1, font=Font(family="serif", size=15),bg="#FFFF0F")
        Champ_saisie_hd = Entry(Gabsence, textvariable=Champ_saisie_var2, font=Font(family="serif", size=15),bg="#FFFF0F")
        Champ_saisie_hf = Entry(Gabsence, textvariable=Champ_saisie_var3, font=Font(family="serif", size=15),bg="#FFFF0F")
        Champ_saisie_mat.place(x=950, y=150)
        Champ_saisie_hd.place(x=950, y=250)
        Champ_saisie_hf.place(x=950, y=350)
        Button(Gabsence, text="MARQUER L'ABSENCE", bg="#236326",font = Font(family ="aharoni", size = 17 , weight = "bold"),border=0, cursor="hand2", command=bouton_act).place(x=1000, y=440)

    accueil_prof()


#Gestion de l'inspecteur de filiere------------------------------------------------------------------------------------------------------------------


def If():
    def accueil_ins():
        Label(Gabsence, bg="#41B77F").place(x=0, y=0, relwidth=1, relheight=1)
        Label(Gabsence, text="cliquez sur l'ecran pour vous connecter ", font=("calibri", 20), bg='#41B77F',fg='white').place(x=0, y=0)
        inspecteur = Button(Gabsence, text="BIENVENUE \n INSPCTEUR DE FILIERE ", font=Font(family = "algerian",size = 60), border=0, bg='#41B77F',fg='white',command=LISTE_ABS)
        inspecteur.place(x=0, y=50, relwidth=1, relheight=1)
        Button(Gabsence, text = "QUTTER", command = Gabsence.quit, font = Font(family = "calibri", size = 15), bg = '#41B77F',fg = "white", cursor = "hand2").place(y = 0, x = 1270)
        Button(Gabsence, text="Retour", command=accueil, font=Font(family="calibri", size=15),bg = '#41B77F',fg = "white",cursor="hand2").place(y=0, x=1200)
    #############################################################################################################################

    def LISTE_ABS():
        con = connect("gnote_base.db")

        curseur = con.cursor()

        req1 = '''SELECT * from ABSENCE '''
        curseur.execute(req1)
        resultats = curseur.fetchall()

        req2 = '''SELECT * from ETUDIANT '''
        curseur.execute(req2)
        resultats2 = curseur.fetchall()

        Label(Gabsence, bg = "green").place(x=0, y=0, relwidth=1, relheight=1)
        my_tree = ttk.Treeview(Gabsence, column=(1, 2, 3, 4, 5, 6, 7), show="headings")

        my_tree.column(1, width=105, anchor="center")
        my_tree.column(2, width=130, anchor="center")
        my_tree.column(3, width=100, anchor="center")
        my_tree.column(4, width=130, anchor="center")
        my_tree.column(5, width=130, anchor="center")
        my_tree.column(6, width=130, anchor="center")
        my_tree.column(7, width=130, anchor="center")

        my_tree.heading(1, text="NOM")
        my_tree.heading(4, text="DATE DE L'ABSENCE")
        my_tree.heading(5, text="HEURE DE DEBUT")
        my_tree.heading(6, text="HEURE DE FIN")
        my_tree.heading(3, text="MATRICULE")
        my_tree.heading(7, text="ETAT DE L'ABSENCE ")
        my_tree.heading(2, text="PRENOM")

        my_tree.place(x = 0, y =150, relwidth = 1, relheight = 1)

        for i in resultats:
            for j in resultats2:
                if j[0] == i[6]:
                    enter = [j[1], j[2], j[0], i[1], i[2], i[3], i[7], i[0]]
                    if i[4] == Inspecteur.matricule:
                        if enter[-2] != "NJV" and enter[-2] != "JV":
                            my_tree.insert('', END, values=enter)

        def item_selected():
            record = []
            for selected_item in my_tree.selection():
                item = my_tree.item(selected_item, 'value')
                record.append(item)
            return record
            
        def interpeler():
            connecter = connect("gnote_base.db")
            cursseur = connecter.cursor()

            item = item_selected()
            req1 = """SELECT*FROM ETUDIANT"""
            req2 = """SELECT * FROM CLASSE"""
            req3 = """SELECT * FROM DIRECTEUR_D_ETUDE"""
            cursseur.execute(req1)
            r1 = cursseur.fetchall()
            cursseur.execute(req2)
            r2 = cursseur.fetchall()
            cursseur.execute(req3)
            r3 = cursseur.fetchall()
            connecter.close()
            nom_classe = ""
            num_filiere = ""
            mat_DE = ""
            try:
                for i in r1:
                    if i[0] == item[0][0]:
                        nom_classe = i[11]
                        break
                for i in r2:
                    if i[0] == nom_classe:
                        num_filiere = i[2]
                        break
                for i in r3:
                    if i[1] == num_filiere:
                        mat_DE = i[0]
                        break

                message = "VOULEZ VOUS INTERPELER SON DIRECTEUR D'ETUDE"
                reponse = messagebox.askyesno("AVERTISSEMENT", message)
                if reponse == True:
                    libelle = "NOM: {} \nPRENOM: {} \nOBJET : INTERPELATION POUR UN ETUDIANT  \n\nM/Mme je vous ecrit par rapport a l'etudiant dont le matricule suit {}, qui s'absente regulierement au cours.Merci de votre comprehension\n Merci de votre attention"
                    Inspecteur.interpeler_DE(libelle.format(Inspecteur.nom, Inspecteur.prenom, item[0][0]), mat_DE)
            except:
                messagebox.showinfo("ATTENTION", "CHOISISEZ D'ABORD UN ETUDIANT")

            

        def justifier():
            item = item_selected()
            try:
                if item[0][-2] != "JNV":
                    print(item[0][-1])
                    Inspecteur.justifier(item[0][-1])
                    LISTE_ABS()
                else:
                    messagebox.showinfo("ATTENTION", "L'ABSENCE EST DEJA JUSTIFIEE")
            except:
                messagebox.showinfo("ATTENTION", "CHOISISEZ D'ABORD UN ETUDIANT")

        #############################################################################################################################
        Label(Gabsence, text="LISTE DES ABSENCES ", font=Font(family="Aharoni", size=30 ,weight="bold"), relief=FLAT,bg="green", fg = "white").place(x= 0, y=0, relwidth = 1)
        Button(Gabsence, text="INTERPELLER LE DIRECTEUR DES ETUDES", command=interpeler, width=30).place(x=0, y=70)
        Button(Gabsence, text="JUSTIFICATION", command=justifier, width=30).place(x=300, y=70)

        bt_ret = Button(Gabsence, text="Retour", fg="blue", cursor="hand2", width=20, command=accueil_ins, bd=1,font=("Arial", 14))
        bt_ret.place(x=0, y=5)

    accueil_ins()



#Page d'accueil de Gabsence-----------------------------------------------------------------------------------------------------------------------------

def accueil():
    Label(Gabsence, image=bg).place(x=0, y=0, relwidth=1, relheight=1)
    mainframe = LabelFrame(Gabsence, text="BIENVENUE DANS G_ABSENCE", width=700, height=500, borderwidth=30)
    mainframe.place(x=300,y= 150)
    Label(mainframe, text="ETES VOUS?").pack(anchor="nw")

    #Bouton pour partis pour choisir la perssonalité-------------------------------------------------------------------------------------------------------------

    bouton1 = Button(mainframe, text="ETUDIANT", width=100, height=2, borderwidth=0, bg="orange",cursor = "hand2", command=etudiant)
    bouton2 = Button(mainframe, text="DIRECTEUR D'ETUDE", width=100, height=2, borderwidth=0,cursor = "hand2", command=de)
    bouton3 = Button(mainframe, text="PROFESSEUR", width=100, height=2, borderwidth=0, bg="green",cursor = "hand2", command=prof)
    bouton4 = Button(mainframe, text="INSPECTEUR DE FILIERE", width=100, height=2, borderwidth=0,cursor = "hand2", command=If)
    Label(Gabsence, width=100, height=8, bg="orange", borderwidth = 0).place(x=0, y= 660)
    bouton1.pack(padx=10, pady=20)
    bouton2.pack(padx=10, pady=20)
    bouton3.pack(padx=10, pady=20)
    bouton4.pack(padx=10, pady=20)
    Label(Gabsence, width = 100, height = 8 ).place(x = 450,y = 660)
    Label(Gabsence, width=75, height=8, bg="green").place(x=950, y=660)

    
#pour l'affichage en plein ecran_-----------------------------------------------------------------------------------------

def plein_ecran():
    a = messagebox.askyesno("CHOIX", "\nVOULEZ VOUS PASSEZ EN PLEIN ECRANT\n\t\t")
    if a == True:
        Gabsence.attributes("-fullscreen", True)
        Gabsence.bind("<Escape>", lambda e: Gabsence.attributes("-fullscreen", False))
        messagebox.showinfo("INFORMATION", "Pour quitter en plein ecran appuyer sur la touche echap")
    else:
        Gabsence.attributes("-fullscreen", False)

#CONNECTION DES DIFFERENTS ACTEUR-------------------------------------------------------------------------------------------------
id1 = "08PROF006"
id2 = "10PROF034"
matricule = "20INP840"
id3 = "034INS032"

connexion = connect("gnote_base.db")
curseur = connexion.cursor()


#connexion d'un professeur pour le teste ----------------------------------------------------------------------------------------------------

req1 = 'SELECT * FROM PROFESSEUR'
curseur.execute(req1)
results = curseur.fetchall()
for result in results:
    if result[0] == id1:
        Professeur = professeur(result[0], result[1], result[3], result[2], result[4], result[6], result[7])
        break

#connexion d'un DE pour le teste ------------------------------------------------------------------------------------------------

req1 = 'SELECT Matricule_Professeur,Nom_professeur,  Prenom_professeur, numero_professeur,Couriel_professeur_, login,mot_de_pass, identifant_DE, Numero_filiere_ FROM DIRECTEUR_D_ETUDE LEFT JOIN PROFESSEUR ON DIRECTEUR_D_ETUDE.Matricule_Professeur1 = PROFESSEUR.Matricule_Professeur'
curseur.execute(req1)
resultats = curseur.fetchall()
for resultat in resultats:
    if resultat[0] == id2:
        Directeur = DE(resultat[0], resultat[1], resultat[2], resultat[3],resultat[4], resultat[5], resultat[6],resultat[7], resultat[8])


#connexion d'un etudiant pour le teste----------------------------------------------------------------------------------------------

req1 = "SELECT * FROM ETUDIANT"
curseur.execute(req1)
resultats = curseur.fetchall()
for resulta in resultats:
    if resulta[0] == matricule:
        etudiants = etudt(resulta[0], resulta[1], resulta[2], resulta[3], resulta[9], resulta[10])
        break

#connection de l'inspecteur de filliere pour l'exemple ---------------------------------------------------------------------------

req1 = "SELECT * FROM Inspecteur"
curseur.execute(req1)
resultats = curseur.fetchall()
for resulta in resultats:
    if resulta[0] == id3:
        Inspecteur = Inspecteur_de_filiere(resulta[0], resulta[1], resulta[2], resulta[3], resulta[5], resulta[6])
        break


connexion.close()


#Creation de la fenetre principale ------------------------------------------------------------------------------------------------

Gabsence = Tk()
Gabsence.title("Gabsence")
Gabsence.geometry("1200x800")
Gabsence.state("zoomed")
Gabsence.config(bg='#007800')
Gabsence.resizable(False,False)
Gabsence.iconbitmap("logo11.ico")

#definition des image comme variable globale ------------------------------------------------------------------------------------------


bg = PhotoImage(file ="BG_green.png")
retour = PhotoImage(file = "62069.png")
DE = PhotoImage(file = "user-interface.png")
AP_DE = PhotoImage(file = "group.png")
abscence = PhotoImage(file = "student.png")
abs_NJ = PhotoImage(file = "unprotected.png")
interpeler = PhotoImage(file = "writing-tool.png")
notif = PhotoImage(file = "notification (1).png")
BG_notif = PhotoImage(file = "notification (2).png")
BG_abs = PhotoImage(file = "student (2).png")
BG_avert = PhotoImage(file = "writing-tool (2).png")
BG_abs_NJ= PhotoImage(file = "unprotected (2).png")
rechercher = PhotoImage(file= "search ().png")
BG_prof = PhotoImage(file = "pngegg (17).png")
marquer = PhotoImage(file = "writer1.png")
BG_mar = PhotoImage(file = "writing-tool (3).png")


accueil()
plein_ecran()
#Maintenir la fenetre ------------------------------------------------------------------------------------------------------------------
Gabsence.mainloop()