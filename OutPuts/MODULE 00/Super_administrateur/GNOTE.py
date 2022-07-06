from tkinter import*
import Module_utilise.Class_BD as bd
class win_connexion(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.p1 = Toplevel(self)
        self.p2 = Toplevel(self)
        self.p3 = Toplevel(self)
        self.p4 = Toplevel(self)
        self.p5 = Toplevel(self)
        self.p6 = Toplevel(self)
        self.p7 = Toplevel(self)
        self.p8 = Toplevel(self)
        self.p9 = Toplevel(self)
        self.withdraw()
        self.p2.withdraw()
        self.p3.withdraw()
        self.p4.withdraw()
        self.p5.withdraw()
        self.p6.withdraw()
        self.p7.withdraw()
        self.p8.withdraw()
        self.p9.withdraw()
#les methodes qui associent à chaque boutton de la page principale sa réalité#
#---------------------------------------------------------------------------------------------------------------------------------------------------------#
    def bouton_presse_admin(self):
        global B_name #nom du boutton pressé
        B_name = B_admin["text"]
        self.page_connexion_tous()
    def bouton_presse_directeur_ecole(self):
        global B_name #nom du boutton pressé
        B_name = B_DEC["text"]
        self.page_connexion_tous()
    def bouton_presse_directeur_etude(self):
        global B_name #nom du boutton pressé
        B_name = B_DE["text"]
        self.page_connexion_tous()
    def bouton_presse_inspecteur_filiere(self):
        global B_name #nom du boutton pressé
        B_name = B_IF["text"]
        self.page_connexion_tous()
    def bouton_presse_professeur(self):
        global B_name #nom du boutton pressé
        B_name = B_P["text"]
        self.page_connexion_tous()
    def bouton_presse_etudiant(self):
        global B_name #nom du boutton pressé
        B_name = B_E["text"]
        self.page_connexion_tous()
#---------------------------------------------------------------------------------------------------------------------------------------------------------#
#les methodes qui associent à chaque bouton de la page creation du super_administrateur leur réalité#
#---------------------------------------------------------------------------------------------------------------------------------------------------------#
        global school,prof,inspect,direct_ecole,direct_etude
    def bouton_creer_ecole(self):
        global B_name_creer #nom du boutton pressé
        B_name_creer = school["text"]
        self.fontionalite_creer_admin_tous()
    def bouton_creer_if(self):
        global B_name_creer #nom du boutton pressé
        B_name_creer = inspect["text"]
        self.fontionalite_creer_admin_tous()
    def bouton_creer_directeur_ecole(self):
        global B_name_creer #nom du boutton pressé
        B_name_creer = direct_ecole["text"]
        self.fontionalite_creer_admin_tous()
    def bouton_creer_directeur_etude(self):
        global B_name_creer #nom du boutton pressé
        B_name_creer = direct_etude["text"]
        self.fontionalite_creer_admin_tous()
    def bouton_creer_professeur(self):
        global B_name_creer #nom du boutton pressé
        B_name_creer = prof["text"]
        self.fontionalite_creer_admin_tous()
#---------------------------------------------------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------------------------------------------------#
#methode qui permet d'associer a chaque bouton de la page creer super_administrateur une fonctionnalite
    def fontionalite_creer_admin_tous(self):
        global B_name_creer
        if ( B_name_creer == "ecole") :
        	self.p4.withdraw()
        	self.Ecole()
        elif ( B_name_creer == "directeur_ecole") :
            self.p4.withdraw()
            self.Compte_directeur_ecole()
        elif ( B_name_creer == "direct_etude") :
            self.p4.withdraw()
            self.directeur_etudes()
        elif ( B_name_creer == "professeur") :
            self.p4.withdraw()
            self.Professeur()
        elif ( B_name_creer == "if") :
            self.p4.withdraw()
            self.inspecteur()
#------------ ---------------------------------------------------------------------------------------------------------------------------------------------#


#les methodes qui associent à chaque boutton de la page du super administrateur sa réalité#
#---------------------------------------------------------------------------------------------------------------------------------------------------------#
    def bouton_creer(self):
        global B_admin_name #nom du boutton pressé
        B_admin_name = creer["text"]
        self.fontionalite_admin_tous()
    def bouton_modifier(self):
        global B_admin_name #nom du boutton pressé
        B_admin_name = modif["text"]
        self.fontionalite_admin_tous()
    def bouton_supprimer(self):
        global B_admin_name #nom du boutton pressé
        B_admin_name = supr["text"]
        self.fontionalite_admin_tous()
#---------------------------------------------------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------------------------------------------------#
#methode qui permet d'associer a chaque bouton de la page super_administrateur une fonctionnalite
    def fontionalite_admin_tous(self):
        global B_admin_name
        if ( B_admin_name == "creer") :
        	self.p3.withdraw()
        	self.page_creation_admin()
        elif ( B_admin_name == "modifier") :
            pass
        elif ( B_admin_name == "supprimer") :
            pass
#------------ ---------------------------------------------------------------------------------------------------------------------------------------------#
#Methode qui permet d'aller à la page de connexion
#---------------------------------------------------------------------------------------------------------------------------------------------------------#
    def page_connexion_tous(self):
        self.p1.withdraw()
        self.page_de_connexion()
#---------------------------------------------------------------------------------------------------------------------------------------------------------#

#Methode qui permet de retourner à la page principale
#---------------------------------------------------------------------------------------------------------------------------------------------------------#    
    def page_principal_retour(self):
        self.p2.withdraw()
        self.p3.withdraw()
        self.p4.withdraw()
        self.p5.withdraw()
        self.p6.withdraw()
        self.p7.withdraw()
        self.p8.withdraw()
        self.p9.withdraw()
        self.p1.deiconify()
#---------------------------------------------------------------------------------------------------------------------------------------------------------#

#Methode qui permet de retourner de la page administrateur à la page de connexion
#---------------------------------------------------------------------------------------------------------------------------------------------------------#    
    def page_admin_connexion_retour(self):
         self.p3.withdraw()
         self.p2.deiconify()
#---------------------------------------------------------------------------------------------------------------------------------------------------------#

#Methode qui permet de quitter l'appli
#---------------------------------------------------------------------------------------------------------------------------------------------------------#    
    def Quitter(self):
        self.destroy()

#---------------------------------------------------------------------------------------------------------------------------------------------------------#
#methode pemettant de faire les requêtes sur les bases de donnees  
#---------------------------------------------------------------------------------------------------------------------------------------------------------# 
    def connexion_tous(self):
        global login
        global mot_pass
        global B_name
        login_tous = login.get()#recuperation du login
        passwd_tous= mot_pass.get()#recuperation du mot de passe
        LO = ["Login_Admin","login"]
        PA = ["Password_Admin","mot_de_passe","mot_de_pass"]
        obj = bd.BD("Base_de_donnee/gnote_base.db")#creation d'un objet permettant de chercher dans la base de donnee
        if ( B_name == "Super Administrateur" ):
            test = obj.chercher(login_tous,passwd_tous,"SA",LO[0],PA[0]) #creation d'un booleen qui permettra de savoir si l'occurence existe si test == 1 l'occurence existe sinon elle n'existe pas.
            if ( test ) :
                self.p2.withdraw()
                self.page_admin()
        elif ( B_name == "Directeur D'Ecole" ):
            test = obj.chercher(login_tous,passwd_tous,"DIRECTEUR_D_ECOLE",LO[1],PA[1])
            if (test) :
                print("c'est un directeur d'école")
            else :
                print("ce n'est pas un directeur d'école")
        elif ( B_name == "Directeur des Etudes" ):
            test = obj.chercher_unique("PROFESSEUR","DIRECTEUR_D_ETUDE","identifant_DE",login_tous,passwd_tous)
            if (test):
                print("c'est un directeur d'étude")
            else:
                print("ce n'est pas un directeur d'étude")

        elif ( B_name == "Inspecteur de filiere" ):
            test = obj.chercher(login_tous,passwd_tous,"Inspecteur",LO[1],PA[2])
            if (test):
                print("c'est un inspecteur de filière")
            else:
                print("ce n'est pas un inspecteur de filière")
        elif ( B_name == "Professeur" ):
            test = obj.chercher(login_tous,passwd_tous,"PROFESSEUR",LO[1],PA[2])
            if (test):
                print("c'est un professeur")
            else:
                print("ce n'est pas un professeur")

        elif ( B_name == "Etudiant" ):
            test = obj.chercher(login_tous,passwd_tous,"ETUDIANT",LO[1],PA[1])
            if (test):
                print("c'est un étudiant")
            else:
                print("ce n'est pas un étudiant")
#---------------------------------------------------------------------------------------------------------------------------------------------------------#
    def page_creation_admin(self):
    	global school,prof,inspect,direct_ecole,direct_etude
    	self.p4.deiconify()
    	self.p4.title("CREATION DE COMPTE")
    	self.p4.config(bg="white")
    	self.p4.geometry("1000x600")
    	self.p4.resizable(width=False,height=False)
    	frame1=Frame(self.p4,width=200,height=600,bg="white")
    	frame1.place(x=0,y=0)
    	frame2=Frame(self.p4,width=700,height=450,bg="white")
    	frame2.place(x=220,y=75)
    	frame3=Frame(self.p4,width=690,height=65,bg="white")
    	frame3.place(x=230,y=5)
    	frame4=Frame(self.p4,width=345,height=65,bg="white")
    	frame4.place(x=430,y=530)
    	image_ecole=PhotoImage(file="Image_utilisee/school.png")
    	school=Button(frame2, image=image_ecole, text = "ecole", command = self.bouton_creer_ecole)
    	school.place(x=20,y=80)
    	school_label=Label(frame2,text="ECOLE",font=("times new roman",15))
    	school_label.place(x=50,y=200)
    	image_prof=PhotoImage(file="Image_utilisee/prof.png")
    	prof=Button(frame2,image=image_prof,text = "professeur", command =self.bouton_creer_professeur)
    	prof.place(x=250,y=80)
    	prof_label=Label(frame2,text="PROFESSEUR",font=("times new roman",15))
    	prof_label.place(x=250,y=190)
    	image_insp=PhotoImage(file="Image_utilisee/inspecteur.png")
    	inspect=Button(frame2,image=image_insp,text = "if", command =self.bouton_creer_if)
    	inspect.place(x=475,y=80)
    	inspect_label=Label(frame2,text="INSPECTEUR",font=("times new roman",15))
    	inspect_label.place(x=475,y=190)
    	image_direct=PhotoImage(file="Image_utilisee/directeur_ecole.png")
    	direct_ecole=Button(frame2,image=image_direct,text = "directeur_ecole", command =self.bouton_creer_directeur_ecole)
    	direct_ecole.place(x=380,y=270)
    	direct_ecole_label=Label(frame2,text="D.ECOLE",font=("times new roman",15))
    	direct_ecole_label.place(x=380,y=390)
    	image_etud=PhotoImage(file="Image_utilisee/directeur_etudes.png")
    	direct_etude=Button(frame2,image=image_etud,text = "directeur_etude", command =self.bouton_creer_directeur_etude)
    	direct_etude.place(x=110,y=270)
    	direct_etud_label=Label(frame2,text="D.ETUDES",font=("times new roman",15))
    	direct_etud_label.place(x=110,y=390)
    	Titre=Label(frame3,text="PAGE DE CREATION ",font=("times new roman",30),bg="orange")
    	Titre.place(x=120,y=10)
    	btn_QUITTER=Button(frame4,text="QUITTER",font=("times new roman",30),bg="orange")
    	btn_QUITTER.place(x=5,y=0,width=300)
    	image_retour=PhotoImage(file="Image_utilisee/retour.png")
    	retour=Button(frame1,image=image_retour)
    	retour.place(x=10,y=300)
    	retour_label=Label(frame1,text="RETOUR",font=("times new roman",20),bg="orange")
    	retour_label.place(x=10,y=410)
    	accueil_image=PhotoImage(file="Image_utilisee/acceuil_couleurpng.png")
    	accueil=Button(frame1,image=accueil_image)
    	accueil.place(x=10,y=100)
    	accueil_label=Label(frame1,text="ACCUEIL",font=("times new roman",20),bg="orange")
    	accueil_label.place(x=10,y=50)
    	self.mainloop()
    def page_de_connexion(self):
        global login
        global mot_pass
        self.p2.deiconify()
        self.p2.config(background="Green")
        self.p2.geometry("600x420")
        self.p2.resizable(width=False,height=False)
        login_titre=Label(self.p2,borderwidth=3,relief=SUNKEN,text="FORMULAIRE DE CONNEXION",font=("Sans Serif",15),background="orange",foreground="White")
        login_titre.place(x=100,y=0,width=400)
        #Creation du champ Login
        login=Entry(self.p2,bg="orange",fg = "green") 
        login_entry=Label(self.p2,text="Login",bg = "green",font =("Sans Serif",12))
        var=StringVar()
        mot_pass=Entry(self.p2,bg="orange",text=var,show="*",font=("Arial",14),foreground="green")
        mp=Label(self.p2,text="mot de passe",bg = "green",font =("Sans Serif",12))
        login_entry.place(x=150,y=98)
        login.place(x=200,y=100,width=100)
        mp.place(x=100,y=150)
        mot_pass.place(x=200,y=150)
        connecter = Button(self.p2,text="Valider",command=self.connexion_tous)
        connecter.place(x=200,y=200)
        retour = Button(self.p2,text="Retourner au menu principal",command=self.page_principal_retour)
        retour.place(x=250,y=200)
        self.p2.mainloop()
    def placer_boutton(self):
        global B_admin,B_DEC,B_DE,B_E,B_P,B_IF
        B_admin = Button(self.p1,text="Super Administrateur",bg="green",font=("Times NEw Roman",12),command=self.bouton_presse_admin,borderwidth=10)
        B_admin.place(x=400,y=200)
        B_DEC = Button(self.p1,text="Directeur D'Ecole",bg="green",font=("Times NEw Roman",12),command=self.bouton_presse_directeur_ecole,borderwidth=10)        
        B_DEC.place(x=100,y=200)
        B_DE = Button(self.p1,text="Directeur des Etudes",bg="green",font=("Times NEw Roman",12),command=self.bouton_presse_directeur_etude,borderwidth=10)        
        B_DE.place(x=400,y=400)
        B_IF = Button(self.p1,text="Inspecteur de filiere",bg="green",font=("Times NEw Roman",12),command=self.bouton_presse_inspecteur_filiere,borderwidth=10)
        B_IF.place(x=100,y=400)
        B_P = Button(self.p1,text="Professeur",bg="green",font=("Times NEw Roman",12),command=self.bouton_presse_professeur,borderwidth=10)
        B_P.place(x=700,y=200)
        B_E = Button(self.p1,text="Etudiant",bg="green",font=("Times NEw Roman",12),command=self.bouton_presse_etudiant,borderwidth=10)
        B_E.place(x=700,y=400)
    def page_admin(self):
        global creer,supr,modif
        self.p3.deiconify()
        self.p3.config(bg="white")
        self.p3.geometry("1000x600")
        self.p3.resizable(width=False,height=False)
        frame1=Frame(self.p3,width=200,height=600,bg="white")
        frame1.place(x=0,y=0)
        frame2=Frame(self.p3,width=700,height=450,bg="white")
        frame2.place(x=220,y=75)
        frame3=Frame(self.p3,width=690,height=65,bg="white")
        frame3.place(x=230,y=5)
        frame4=Frame(self.p3,width=345,height=65,bg="white")
        frame4.place(x=430,y=530)
        #Creation de l'option Creer
        image_creer=PhotoImage(file="Image_utilisee/creer.png")
        creer=Button(frame2,image=image_creer,text="creer",command=self.bouton_creer)
        creer.place(x=10,y=100)
        creer_label=Label(frame2,text="CREER",font=("times new roman",15))
        creer_label.place(x=40,y=230)
        image_modif=PhotoImage(file="Image_utilisee/modifier.png")
        modif=Button(frame2,image=image_modif,text="modifier",command=self.bouton_modifier)
        modif.place(x=250,y=100)
        modif_label=Label(frame2,text="MODIFIER",font=("times new roman",15))
        modif_label.place(x=280,y=230)
        image_supp=PhotoImage(file="Image_utilisee/supp_orange.png")
        supr=Button(frame2,image=image_supp,text="supprimer",command =self.bouton_supprimer)
        supr.place(x=475,y=100)
        supprim_label=Label(frame2,text="SUPPRIMER",font=("times new roman",15))
        supprim_label.place(x=500,y=230)
        #Gestion du frame3
        Titre=Label(frame3,text="SUPER ADMINISTRATEUR",font=("times new roman",30),bg="orange")
        Titre.place(x=10,y=10)
        #Gestion du frame4
        btn_QUITTER=Button(frame4,text="QUITTER",font=("times new roman",30),bg="orange",command=self.Quitter)
        btn_QUITTER.place(x=150,y=0,width=200)
        #Gestion du frame1
        image_retour=PhotoImage(file="Image_utilisee/retour.png")
        retour=Button(frame1,image=image_retour,command=self.page_admin_connexion_retour)
        retour.place(x=10,y=300)
        retour_label=Label(frame1,text="RETOUR",font=("times new roman",20),bg="orange")
        retour_label.place(x=10,y=410)
        accueil_image=PhotoImage(file="Image_utilisee/acceuil_couleurpng.png")
        accueil=Button(frame1,image=accueil_image,command=self.page_principal_retour)
        accueil.place(x=10,y=100) 
        accueil_label=Label(frame1,text="ACCUEIL",font=("times new roman",20),bg="orange")
        accueil_label.place(x=10,y=50)
        self.p3.mainloop()
#Ecole
#-------------------------------------------------------------------------------------------------------------------------------------------------------#
    def Ecole(self):
    	global champ_id_ecole,champ_nom_ecole,champ_adr_ecole,champ_descrip_ecole
    	self.p5.deiconify()
    	self.p5.config(background="Green")
    	self.p5.geometry("600x420")
    	Titre=Label(self.p5,borderwidth=3,relief=SUNKEN,text="CREATION D'ECOLE",font=("Sans Serif",15),background="orange",foreground="White").place(x=100,y=0,width=400)
    	id_ecole=Label(self.p5,text="Identifiant")
    	nom=Label(self.p5,text="Nom")
    	adresse=Label(self.p5,text="Adresse D'Ecole")
    	descrip=Label(self.p5,text="Description")
    	var1=StringVar()
    	var2=StringVar()
    	var3=StringVar()
    	var4=StringVar()
    	champ_id_ecole=Entry(self.p5,bg="orange",text=var1,font=("Arial",14),foreground="White")
    	champ_nom_ecole=Entry(self.p5,bg="orange",text=var2,font=("Arial",14),foreground="White")
    	champ_adr_ecole=Entry(self.p5,bg="orange",text=var3,font=("Arial",14),foreground="White")
    	champ_descrip_ecole=Entry(self.p5,bg="orange",text=var4,font=("Arial",14),foreground="White")
    	id_ecole.place(x=100,y=100,width=100)
    	champ_id_ecole.place(x=250,y=100,width=150)
    	nom.place(x=150,y=150,width=50)
    	champ_nom_ecole.place(x=300,y=150,width=150)
    	adresse.place(x=100,y=200,width=100)
    	champ_adr_ecole.place(x=300,y=200,width=150)
    	descrip.place(x=100,y=250,width=100)
    	champ_descrip_ecole.place(x=350,y=250,width=100)
    	retour = Button(self.p5,text="Retourner au menu principal",command=self.page_principal_retour)
    	retour.place(x=300,y=300)
    	valider = Button(self.p5, text="Valider", command=self.req_ajout_tous)
    	valider.place(x=100,y=300)
    	self.p5.mainloop()
#-------------------------------------------------------------------------------------------------------------------------------------------------------#
#methode permettant de faire des requêtes d'ajout :

    def req_ajout_tous(self):
    	global B_name_creer
    	L_ecole = "Identifiant_ecole,Nom_ecole,Adresse_Ecole,Libellé_ecole"
    	L_directeur_etude = "identifiant_DE,Numero_filiere_,Matricule_Professeur"
    	L_directeur_ecole = "Matricule_directeur_d_ecole,sexe_directeur_d_ecole,Nom_directeur_d_ecole,Prenom_directeur_d_ecole,numero_directeur_d_ecole","login","mot_de_passe","Identifiant__ecole"
    	L_professeur = "Matricule_Professeur,Nom_professeur,numero_professeur,Prenom_professeur,Couriel_professeur_,Sexe_Professeur,login,mot_de_pass"
    	L_inspecteur = "Matricule_inspecteur,Nom_inspecteur,prénom_ispecteur,Sexe_inspecteur_,login,mot_de_pass,Numero_filiere_"
    	global champ_id_ecole,champ_nom_ecole,champ_adr_ecole,champ_descrip_ecole #ecole
    	global champ_matri_dir_ecole,champ_nom_dir_ecole,champ_pre_dir_ecole,champ_sex_dir_ecole,champ_login_dir_ecole,champ_mot_pass_dir_ecole,champ_num_dir_ecole,champ_id_son_ecole_dir_ecole #dir_ecole
    	global champ_matri_etude,champ_nom_etude,champ_numero_filiere_etude,champ_matricule_prof_etude
    	global champ_id_professeur,champ_nom_professeur,champ_adr_professeur,champ_descrip_professeur
    	global champ_matri_if,champ_nom_if,champ_pre_if,champ_sex_if,champ_login_if ,champ_mot_pass_if,champ_num_if,champ_numero_filiere_if
    	obj = bd.BD("Base_de_donnee/gnote_base.db")
    	if ( B_name_creer == "ecole") :
    		donne = [(champ_id_ecole.get(),champ_nom_ecole.get(),champ_adr_ecole.get(),champ_descrip_ecole.get())]
    		ime = donne[0]
    		test = [i for i in ime if len(i) != 0 ]
    		if len( test ) != 0:
    			obj.inserer_donnee(donne,"ECOLE",L_ecole)
    		else:
    			print("Veuiller remplir tous les champs")

    	elif ( B_name_creer == "directeur_ecole") :                      
    	    donne = [(champ_matri_dir_ecole.get(),champ_nom_dir_ecole.get(),champ_pre_dir_ecole.get(),champ_sex_dir_ecole.get(),champ_login_dir_ecole.get(),champ_mot_pass_dir_ecole.get(),champ_num_dir_ecole.get(),champ_id_son_ecole_dir_ecole.get())]
    	    ime = donne[0]
    	    test = [i for i in ime if len(i) != 0 ]
    	    if len( test ) != 0:
    	    	obj.inserer_donnee(donne,"DIRECTEUR_D_ECOLE",L_directeur_ecole )
    	    else:
                print("Veuiller remplir tous les champs")
    	elif ( B_name_creer == "direct_etude"):
    	    donne = [(champ_matri_etude.get(),champ_nom_etude.get(),champ_numero_filiere_etude.get(),champ_matricule_prof_etude.get())]
    	    ime = donne[0]
    	    test = [i for i in ime if len(i) != 0 ]
    	    if len( test ) != 0:
    	    	obj.inserer_donnee(donne,"DIRECTEUR_D_ETUDE",L_directeur_etude)
    	    else:
                print("Veuiller remplir tous les champs")
    	elif ( B_name_creer == "if"):
    	    donne = [(champ_matri_if.get(),champ_nom_if.get(),champ_pre_if.get(),champ_sex_if.get(),champ_login_if.get(),champ_mot_pass_if.get(),champ_num_if.get(),champ_numero_filiere_if.get())]
    	    ime = donne[0]
    	    test = [i for i in ime if len(i) != 0 ]
    	    if len( test  ) != 0:
    	    	obj.inserer_donnee(donne,"Inspecteur",L_inspecteur)
    	    else:
                print("Veuiller remplir tous les champs")
    	elif ( B_name_creer == "professeur"):
    	    donne = [(champ_id_professeur.get(),champ_nom_professeur.get(),champ_adr_professeur.get(),champ_descrip_professeur.get())]
    	    ime = donne[0]
    	    test = [i for i in ime if len(i) != 0 ]
    	    if len( test ) != 0 :
    	    	obj.inserer_donnee(donne,"PROFESSEUR",L_professeur)
    	    else:
                print("Veuiller remplir tous les champs")
#-------------------------------------------------------------------------------------------------------------------------------------------------------#
#Directeur d'etudes
    def Compte_directeur_ecole(self):
    	global champ_matri_dir_ecole,champ_nom_dir_ecole,champ_pre_dir_ecole,champ_sex_dir_ecole,champ_login_dir_ecole,champ_mot_pass_dir_ecole,champ_num_dir_ecole,champ_id_son_ecole_dir_ecole
    	self.p6.deiconify()
    	self.p6.config(background="Green")
    	self.p6.geometry("600x600")
    	Titre=Label(self.p6,borderwidth=3,relief=SUNKEN,text="CREATION Du COMPTE DIRECTEUR D'ECOLE",font=("Sans Serif",15),background="orange",foreground="White").place(x=90,y=0,width=500)
    	matricule=Label(self.p6,text="Matricule")
    	nom=Label(self.p6,text="Nom")
    	sex=Label(self.p6,text="SEX")
    	prenom=Label(self.p6,text="prenom")
    	login=Label(self.p6,text="Login")
    	mot_pass=Label(self.p6,text="Mot de Passe")
    	numero=Label(self.p6,text="Numero du Directeur")
    	id_son_ecole=Label(self.p6,text="Identifiant de son ecole")
    	var1=StringVar()
    	var2=StringVar()
    	var3=StringVar()
    	var4=StringVar()
    	var5=StringVar()
    	var6=StringVar()
    	var7=StringVar()
    	var8=StringVar()
    	champ_matri_dir_ecole=Entry(self.p6,bg="orange",text=var1,font=("Arial",14),foreground="White")
    	champ_nom_dir_ecole=Entry(self.p6,bg="orange",text=var2,font=("Arial",14),foreground="White")
    	champ_pre_dir_ecole=Entry(self.p6,bg="orange",text=var3,font=("Arial",14),foreground="White")
    	champ_sex_dir_ecole=Entry(self.p6,bg="orange",text=var4,font=("Arial",14),foreground="White")
    	champ_login_dir_ecole=Entry(self.p6,bg="orange",text=var4,font=("Arial",14),foreground="White")
    	champ_mot_pass_dir_ecole=Entry(self.p6,bg="orange",text=var4,font=("Arial",14),foreground="White")
    	champ_num_dir_ecole=Entry(self.p6,bg="orange",text=var4,font=("Arial",14),foreground="White")
    	champ_id_son_ecole_dir_ecole=Entry(self.p6,bg="orange",text=var4,font=("Arial",14),foreground="White")
    	matricule.place(x=100,y=100,width=100)
    	champ_matri_dir_ecole.place(x=250,y=100,width=150)
    	nom.place(x=150,y=150,width=50)
    	champ_nom_dir_ecole.place(x=300,y=150,width=150)
    	prenom.place(x=100,y=200,width=100)
    	champ_pre_dir_ecole.place(x=300,y=200,width=150)
    	sex.place(x=100,y=250,width=100)
    	champ_sex_dir_ecole.place(x=350,y=250,width=100)
    	champ_login_dir_ecole.place(x=350,y=300,width=100)
    	login.place(x=100,y=300,width=100)
    	champ_mot_pass_dir_ecole.place(x=370,y=350,width=100)
    	mot_pass.place(x=100,y=350,width=100)
    	champ_num_dir_ecole.place(x=400,y=380,width=100)
    	numero.place(x=100,y=390,width=150)
    	champ_id_son_ecole_dir_ecole.place(x=300,y=420)
    	id_son_ecole.place(x=100,y=420,width=150)
    	retour = Button(self.p6,text="Retourner au menu principal",command=self.page_principal_retour)
    	retour.place(x=300,y=450)
    	valider = Button(self.p6, text="Valider", command=self.req_ajout_tous)
    	valider.place(x=100,y=450)
    	self.p6.mainloop()

#directeur des etudes
    def directeur_etudes(self):
    	global champ_matri_etude,champ_nom_etude,champ_numero_filiere_etude,champ_matricule_prof_etude
    	self.p7.deiconify()
    	self.p7.config(background="Green")
    	self.p7.geometry("600x420")
    	Titre=Label(self.p7,borderwidth=3,relief=SUNKEN,text="CREATION DIRECTEUR D'ETUDE ",font=("Sans Serif",15),background="orange",foreground="White").place(x=100,y=0,width=400)
    	Matricule=Label(self.p7,text="Matricule")
    	nom=Label(self.p7,text="Nom")
    	numero_filiere=Label(self.p7,text="Numero de Filiere")
    	matricule_prof=Label(self.p7,text="Matricule de Professeur")
    	var1=StringVar()
    	var2=StringVar()
    	var3=StringVar()
    	var4=StringVar()
    	champ_matri_etude=Entry(self.p7,bg="orange",text=var1,font=("Arial",14),foreground="White")
    	champ_nom_etude=Entry(self.p7,bg="orange",text=var2,font=("Arial",14),foreground="White")
    	champ_numero_filiere_etude=Entry(self.p7,bg="orange",text=var3,font=("Arial",14),foreground="White")
    	champ_matricule_prof_etude=Entry(self.p7,bg="orange",text=var4,font=("Arial",14),foreground="White")
    	Matricule.place(x=100,y=100,width=100)
    	champ_matri_etude.place(x=300,y=100,width=150)
    	nom.place(x=150,y=150,width=50)
    	champ_nom_etude.place(x=300,y=150,width=150)
    	numero_filiere.place(x=100,y=200,width=100)
    	champ_numero_filiere_etude.place(x=300,y=200,width=150)
    	matricule_prof.place(x=50,y=250,width=150)
    	champ_matricule_prof_etude.place(x=300,y=250,width=150)
    	b=Button(self.p7,text="VALIDER",width=20,height=2).place(x=200,y=300)
    	retour = Button(self.p5,text="Retourner au menu principal",command=self.page_principal_retour)
    	retour.place(x=100,y=300)
    	self.p7.mainloop()

#Professeur
    def Professeur(self):
    	global champ_id_professeur,champ_nom_professeur,champ_adr_professeur,champ_descrip_professeur
    	self.p8.deiconify()
    	self.p8.config(background="Green")
    	self.p8.geometry("600x420")
    	Titre=Label(self.p8,borderwidth=3,relief=SUNKEN,text="CREATION DU COMPTE PROFESSEUR",font=("Sans Serif",15),background="orange",foreground="White").place(x=100,y=0,width=400)
    	id_ecole=Label(self.p8,text="Identifiant",)
    	nom=Label(self.p8,text="Nom")
    	adresse=Label(self.p8,text="Adresse D'Ecole")
    	descrip=Label(self.p8,text="Description")
    	var1=StringVar()
    	var2=StringVar()
    	var3=StringVar()
    	var4=StringVar()
    	champ_id_professeur=Entry(self.p8,bg="orange",text=var1,font=("Arial",14),foreground="White")
    	champ_nom_professeur=Entry(self.p8,bg="orange",text=var2,font=("Arial",14),foreground="White")
    	champ_adr_professeur=Entry(self.p8,bg="orange",text=var3,font=("Arial",14),foreground="White")
    	champ_descrip_professeur=Entry(self.p8,bg="orange",text=var4,font=("Arial",14),foreground="White")
    	id_ecole.place(x=100,y=100,width=100)
    	champ_id_professeur.place(x=250,y=100,width=150)
    	nom.place(x=150,y=150,width=50)
    	champ_nom_professeur.place(x=300,y=150,width=150)
    	adresse.place(x=100,y=200,width=100)
    	champ_adr_professeur.place(x=300,y=200,width=150)
    	descrip.place(x=100,y=250,width=100)
    	champ_descrip_professeur.place(x=350,y=250,width=100)
    	self.p8.mainloop()

#INSpecteur

    def inspecteur(self):
    	global champ_matri_if,champ_nom_if,champ_pre_if,champ_sex_if,champ_login_if ,champ_mot_pass_if,champ_num_if,champ_numero_filiere_if
    	self.p9.deiconify()
    	self.p9.config(background="Green")
    	self.p9.geometry("600x600")
    	Titre=Label(self.p9,borderwidth=3,relief=SUNKEN,text="CREATION DU COMPTE D'INSPECTEUR",font=("Sans Serif",15),background="orange",foreground="White").place(x=100,y=0,width=400)
    	matricule=Label(self.p9,text="Matricule")
    	nom=Label(self.p9,text="Nom")
    	sex=Label(self.p9,text="SEX")
    	prenom=Label(self.p9,text="prenom")
    	login=Label(self.p9,text="Login")
    	mot_pass=Label(self.p9,text="Mot de Passe")
    	numero=Label(self.p9,text="Numero d'Inspecteur")
    	numero_filiere=Label(self.p9,text="Numero de sa Filiere")
    	var1=StringVar()
    	var2=StringVar()
    	var3=StringVar()
    	var4=StringVar()
    	var5=StringVar()
    	var6=StringVar()
    	var7=StringVar()
    	var8=StringVar()
    	champ_matri_if=Entry(self.p9,bg="orange",text=var1,font=("Arial",14),foreground="White")
    	champ_nom_if=Entry(self.p9,bg="orange",text=var2,font=("Arial",14),foreground="White")
    	champ_pre_if=Entry(self.p9,bg="orange",text=var3,font=("Arial",14),foreground="White")
    	champ_sex_if=Entry(self.p9,bg="orange",text=var4,font=("Arial",14),foreground="White")
    	champ_login_if=Entry(self.p9,bg="orange",text=var5,font=("Arial",14),foreground="White")
    	champ_mot_pass_if=Entry(self.p9,bg="orange",text=var6,font=("Arial",14),foreground="White")
    	champ_num_if=Entry(self.p9,bg="orange",text=var7,font=("Arial",14),foreground="White")
    	champ_numero_filiere_if=Entry(self.p9,bg="orange",text=var8,font=("Arial",14),foreground="White")
    	matricule.place(x=100,y=100,width=100)
    	champ_matri_if.place(x=250,y=100,width=150)
    	nom.place(x=150,y=150,width=50)
    	champ_nom_if.place(x=300,y=150,width=150)
    	prenom.place(x=100,y=200,width=100)
    	champ_pre_if.place(x=300,y=200,width=150)
    	sex.place(x=100,y=250,width=100)
    	champ_sex_if.place(x=350,y=250,width=100)
    	champ_login.place(x=350,y=300,width=100)
    	login.place(x=100,y=300,width=100)
    	champ_mot_pass_if.place(x=370,y=350,width=100)
    	mot_pass.place(x=100,y=350,width=100)
    	champ_num_if.place(x=400,y=380,width=100)
    	numero.place(x=100,y=390,width=150)
    	champ_numero_filiere_if.place(x=300,y=420)
    	numero_filiere.place(x=100,y=420,width=150)
    	b=Button(self.p9,text="VALIDER",width=20,height=2).place(x=200,y=500)
    	self.p9.mainloop()
    def afficher(self):
        self.p1.title("GNOTE")
        self.p1.geometry("950x700")
        self.p1.config(bg = "White") 
        self.p1.resizable(width=False,height=False)
        L_bienvenue = Label(self.p1,text="Bienvenue SUR G-NOTE",bg="orange",font=("Times NEw Roman",20))
        L_bienvenue.place(x=250,y=100,width=500)
        self.placer_boutton()
        self.mainloop()
fen = win_connexion()
fen.afficher()