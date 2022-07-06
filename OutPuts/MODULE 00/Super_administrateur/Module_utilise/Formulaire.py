from tkinter import*

class formulaire(Tk):
    def __init__(self):
        Tk.__init__(self)


#Ecole
    def Ecole(self):

        self.config(background="Green")
        self.geometry("600x420")

        Titre=Label(self,borderwidth=3,relief=SUNKEN,text="CREATION D'ECOLE",font=("Sans Serif",15),background="orange",
        foreground="White").place(x=100,y=0,width=400)
        id_ecole=Label(self,text="Identifiant",)
        nom=Label(self,text="Nom")
        adresse=Label(self,text="Adresse D'Ecole")
        descrip=Label(self,text="Description")
        var1=StringVar()
        var2=StringVar()
        var3=StringVar()
        var4=StringVar()
        champ_id=Entry(self,bg="orange",text=var1,font=("Arial",14),foreground="White")

        champ_nom=Entry(self,bg="orange",text=var2,font=("Arial",14),foreground="White")

        champ_adr=Entry(self,bg="orange",text=var3,font=("Arial",14),foreground="White")

        champ_descrip=Entry(self,bg="orange",text=var4,font=("Arial",14),foreground="White")

        id_ecole.place(x=100,y=100,width=100)
        champ_id.place(x=250,y=100,width=150)
        nom.place(x=150,y=150,width=50)
        champ_nom.place(x=300,y=150,width=150)
        adresse.place(x=100,y=200,width=100)
        champ_adr.place(x=300,y=200,width=150)
        descrip.place(x=100,y=250,width=100)
        champ_descrip.place(x=350,y=250,width=100)
        self.mainloop()
#Directeur d'etudes
    def Compte_directeur_ecole(self):
    
        self.config(background="Green")
        self.geometry("600x600")

        Titre=Label(self,borderwidth=3,relief=SUNKEN,text="CREATION Du COMPTE DIRECTEUR D'ECOLE",font=("Sans Serif",15),background="orange",
        foreground="White").place(x=90,y=0,width=500)
     
        matricule=Label(self,text="Matricule")
        nom=Label(self,text="Nom")
        sex=Label(self,text="SEX")
        prenom=Label(self,text="prenom")
        login=Label(self,text="Login")
        mot_pass=Label(self,text="Mot de Passe")
        numero=Label(self,text="Numero du Directeur")
        id_son_ecole=Label(self,text="Identifiant de son ecole")

        var1=StringVar()
        var2=StringVar()
        var3=StringVar()
        var4=StringVar()
        var5=StringVar()
        var6=StringVar()
        var7=StringVar()
        var8=StringVar()

        champ_matri=Entry(self,bg="orange",text=var1,font=("Arial",14),foreground="White")

        champ_nom=Entry(self,bg="orange",text=var2,font=("Arial",14),foreground="White")

        champ_pre=Entry(self,bg="orange",text=var3,font=("Arial",14),foreground="White")

        champ_sex=Entry(self,bg="orange",text=var4,font=("Arial",14),foreground="White")

        champ_login=Entry(self,bg="orange",text=var4,font=("Arial",14),foreground="White")

        champ_mot_pass=Entry(self,bg="orange",text=var4,font=("Arial",14),foreground="White")

        champ_num=Entry(self,bg="orange",text=var4,font=("Arial",14),foreground="White")

        champ_id_son_ecole=Entry(self,bg="orange",text=var4,font=("Arial",14),foreground="White")

        matricule.place(x=100,y=100,width=100)
        champ_matri.place(x=250,y=100,width=150)
        nom.place(x=150,y=150,width=50)
        champ_nom.place(x=300,y=150,width=150)
        prenom.place(x=100,y=200,width=100)
        champ_pre.place(x=300,y=200,width=150)
        sex.place(x=100,y=250,width=100)
        champ_sex.place(x=350,y=250,width=100)
        champ_login.place(x=350,y=300,width=100)
        login.place(x=100,y=300,width=100)
        champ_mot_pass.place(x=370,y=350,width=100)
        mot_pass.place(x=100,y=350,width=100)
        champ_num.place(x=400,y=380,width=100)
        numero.place(x=100,y=390,width=150)
        champ_id_son_ecole.place(x=300,y=420)
        id_son_ecole.place(x=100,y=420,width=150)
        b=Button(self,text="VALIDER",width=20,height=2).place(x=200,y=500)


        self.mainloop()

#directeur des etudes
    def directeur_etudes(self):
        self.config(background="Green")
        self.geometry("600x420")

        Titre=Label(self,borderwidth=3,relief=SUNKEN,text="CREATION DIRECTEUR D'ETUDE ",font=("Sans Serif",15),background="orange",
        foreground="White").place(x=100,y=0,width=400)

        Matricule=Label(self,text="Matricule")
        nom=Label(self,text="Nom")
        numero_filiere=Label(self,text="Numero de Filiere")
        matricule_prof=Label(self,text="Matricule de Professeur")
        var1=StringVar()
        var2=StringVar()
        var3=StringVar()
        var4=StringVar()

        champ_matri=Entry(self,bg="orange",text=var1,font=("Arial",14),foreground="White")

        champ_nom=Entry(self,bg="orange",text=var2,font=("Arial",14),foreground="White")

        champ_numero_filiere=Entry(self,bg="orange",text=var3,font=("Arial",14),foreground="White")

        champ_matricule_prof=Entry(self,bg="orange",text=var4,font=("Arial",14),foreground="White")

        Matricule.place(x=100,y=100,width=100)
        champ_matri.place(x=300,y=100,width=150)
        nom.place(x=150,y=150,width=50)
        champ_nom.place(x=300,y=150,width=150)
        numero_filiere.place(x=100,y=200,width=100)
        champ_numero_filiere.place(x=300,y=200,width=150)
        matricule_prof.place(x=50,y=250,width=150)
        champ_matricule_prof.place(x=300,y=250,width=150)
        b=Button(self,text="VALIDER",width=20,height=2).place(x=200,y=300)
        self.mainloop()

#Professeur
    def Professeur(self):

        self.config(background="Green")
        self.geometry("600x420")

        Titre=Label(self,borderwidth=3,relief=SUNKEN,text="CREATION DU COMPTE PROFESSEUR",font=("Sans Serif",15),background="orange",
        foreground="White").place(x=100,y=0,width=400)
        id_ecole=Label(self,text="Identifiant",)
        nom=Label(self,text="Nom")
        adresse=Label(self,text="Adresse D'Ecole")
        descrip=Label(self,text="Description")
        var1=StringVar()
        var2=StringVar()
        var3=StringVar()
        var4=StringVar()
        champ_id=Entry(self,bg="orange",text=var1,font=("Arial",14),foreground="White")

        champ_nom=Entry(self,bg="orange",text=var2,font=("Arial",14),foreground="White")

        champ_adr=Entry(self,bg="orange",text=var3,font=("Arial",14),foreground="White")

        champ_descrip=Entry(self,bg="orange",text=var4,font=("Arial",14),foreground="White")

        id_ecole.place(x=100,y=100,width=100)
        champ_id.place(x=250,y=100,width=150)
        nom.place(x=150,y=150,width=50)
        champ_nom.place(x=300,y=150,width=150)
        adresse.place(x=100,y=200,width=100)
        champ_adr.place(x=300,y=200,width=150)
        descrip.place(x=100,y=250,width=100)
        champ_descrip.place(x=350,y=250,width=100)


        self.mainloop()

#INSpecteur

    def inspecteur(self):

        self.config(background="Green")
        self.geometry("600x600")

        Titre=Label(self,borderwidth=3,relief=SUNKEN,text="CREATION DU COMPTE D'INSPECTEUR",font=("Sans Serif",15),background="orange",
        foreground="White").place(x=100,y=0,width=400)
        
        matricule=Label(self,text="Matricule")
        nom=Label(self,text="Nom")
        sex=Label(self,text="SEX")
        prenom=Label(self,text="prenom")
        login=Label(self,text="Login")
        mot_pass=Label(self,text="Mot de Passe")
        numero=Label(self,text="Numero d'Inspecteur")
        numero_filiere=Label(self,text="Numero de sa Filiere")

        var1=StringVar()
        var2=StringVar()
        var3=StringVar()
        var4=StringVar()
        var5=StringVar()
        var6=StringVar()
        var7=StringVar()
        var8=StringVar()

        champ_matri=Entry(self,bg="orange",text=var1,font=("Arial",14),foreground="White")

        champ_nom=Entry(self,bg="orange",text=var2,font=("Arial",14),foreground="White")

        champ_pre=Entry(self,bg="orange",text=var3,font=("Arial",14),foreground="White")

        champ_sex=Entry(self,bg="orange",text=var4,font=("Arial",14),foreground="White")

        champ_login=Entry(self,bg="orange",text=var5,font=("Arial",14),foreground="White")

        champ_mot_pass=Entry(self,bg="orange",text=var6,font=("Arial",14),foreground="White")

        champ_num=Entry(self,bg="orange",text=var7,font=("Arial",14),foreground="White")

        champ_numero_filiere=Entry(self,bg="orange",text=var8,font=("Arial",14),foreground="White")

        matricule.place(x=100,y=100,width=100)
        champ_matri.place(x=250,y=100,width=150)
        nom.place(x=150,y=150,width=50)
        champ_nom.place(x=300,y=150,width=150)
        prenom.place(x=100,y=200,width=100)
        champ_pre.place(x=300,y=200,width=150)
        sex.place(x=100,y=250,width=100)
        champ_sex.place(x=350,y=250,width=100)
        champ_login.place(x=350,y=300,width=100)
        login.place(x=100,y=300,width=100)
        champ_mot_pass.place(x=370,y=350,width=100)
        mot_pass.place(x=100,y=350,width=100)
        champ_num.place(x=400,y=380,width=100)
        numero.place(x=100,y=390,width=150)
        champ_numero_filiere.place(x=300,y=420)
        numero_filiere.place(x=100,y=420,width=150)
        b=Button(self,text="VALIDER",width=20,height=2).place(x=200,y=500)
        self.mainloop()