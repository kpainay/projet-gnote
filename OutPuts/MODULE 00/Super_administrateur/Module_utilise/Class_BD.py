#coding -*- utf-8 -*-
import sqlite3 as s
class BD :
    """classe permettant de gérer un base de donnée"""
    ch = []
    tab = {}
    i = 0
    def __init__(self,ch):
        BD.ch.append(ch)
        self.ch = BD.ch[BD.i]
        BD.i += 1
    def cn(self) :
        """permet de se connecter à la base de donnée et de la creer si elle n'existe pas"""
        return s.connect(self.ch)
    def dc(self,connexion):
        """permet de se déconnecter de la base de donnée """
        connexion.close()
    def cur(self,connexion):
        """permet d'executer les requêtes"""
        return connexion.cursor()
    def mod(self,connexion,confirm):
        """permet d'enregistre ou de revenir en arrière sur 
        les informations enregistrées dans la bd"""
        if(confirm):
            connexion.commit()
        else:
            connexion.rollback()
    def req(self,curseur):
        """permet d'executer les requêtes de création de table"""
        p1 = """CREATE TABLE IF NOT EXISTS {}("""
        Linfo = []
        table = input("Entrer le nom de la table à créer : ")
        natt = input("combien d'attributs avez-vous dans votre table ? ")
        i = 1
        while i <= int(natt):
            if i < int(natt):
                attrib_domain = input("Entrer le nom de l'attribut suivi de ses informations : " + str(i)+" : ")
                Linfo.append(attrib_domain + ",")
            else:
                attrib_domain = input("Entrer le nom de l'attribut suivi de ses informations : " + str(i)+" : ")
                Linfo.append(attrib_domain)
            i+=1
        p1 = p1.format(table)
        i = 0
        while i < int(natt):
            p1 += "{}"
            p1 = p1.format(Linfo[i])
            if i == int(natt)-1 :
                p1 += ")"
            i+=1
        curseur.execute(p1)
    def data_insert_2 (self,curseur,donnee,table,val):
         """permet d'insérer des données dans une table"""
         table = input("Entrer le nom de la table : ")
         val = BD.tab[table]
         value = val.split(",")
         valeur = ""
         for i in value :
             if i != value[-1]:
                 valeur += "?" + ","
             else:
                 valeur += "?"
         inser = """INSERT INTO {} ({}) VALUES ({})""".format(table,BD.tab[table],valeur)
         for i in donnee :
             curseur.execute(inser,i)
    def data_insert (self,curseur,donnee):
         """permet d'insérer des données dans une table"""
         table = input("Entrer le nom de la table : ")
         val = BD.tab[table]
         value = val.split(",")
         valeur = ""
         for i in value :
             if i != value[-1]:
                 valeur += "?" + ","
             else:
                 valeur += "?"
         inser = """INSERT INTO {} ({}) VALUES ({})""".format(table,BD.tab[table],valeur)
         for i in donnee :
             curseur.execute(inser,i)
    def recup (self,curseur):
        """permet de récupérer tous les résulats d'une reqête"""
        table = input("Entrer le nom de la table : ")
        curseur.execute("""SELECT * FROM """ + table) 
        L = []
        for result in curseur:
            L.append(result)
        return L
    def chercher(self,donnee_log,donnee_passwd,table,login,paswd):
        """Permet de chercher des valeurs dans une base de donnee"""
        """donne est une liste contenat les valeurs à voir"""
        log_test = False
        passd_test= False
        connexion=self.cn()
        curseur=self.cur(connexion)
        curseur.execute("""SELECT {0} FROM """.format(login) + table)
        log = []
        for result in curseur:
            log.append(result)
        for i in log:
           for j in i:
                if j == donnee_log :
                     log_test = True
        paswd= list(paswd)
        paswd = ''.join(paswd)
        curseur.execute("""SELECT {0} FROM """.format(paswd) + table)
        Pass = []
        for result in curseur:
           Pass.append(result) 
        for i in Pass:
            for j in i:
                 if j == donnee_passwd:
                    passd_test = True
        self.dc(connexion)
        return (log_test and passd_test)
    def chercher_unique(self,tab1,tabdestinataire,destinataire,log,passd):
        connexion=self.cn()
        curseur=self.cur(connexion)
        curseur.execute("PRAGMA foreign_keys = ON") 
        log= list(log)
        log = ''.join(log)
        passd = list(passd)
        passd = ''.join(passd)
        curseur.execute("""SELECT O.Matricule_Professeur FROM {0} AS O WHERE O.login LIKE '{1}' AND O.mot_de_pass LIKE '{2}'""".format(tab1,log,passd)) 
        L1 = []
        for re in curseur :
            L1.append(re)
        if ( len(L1) != 0 ) :
            for i in L1:
                for j in i:
                    LL = list(j)
        else:
            LL =['']
        LL = ''.join(LL)
        curseur.execute("""SELECT L.{0} FROM {1} AS L WHERE L.Matricule_Professeur LIKE '{2}'""".format(destinataire,tabdestinataire,LL))
        L2 = []
        for re in curseur:
            L2.append(re)
        if len(L2) == 0:
            test = False
        else:
            test = True
        return(test)
        self.dc(connexion)
    def cherche(self):
        connexion=self.cn()
        curseur=self.cur(connexion)
        curseur.execute("""SELECT {0} FROM """.format("Nom") + "Tab")
        log=""
        for result in curseur:
            log=result
        return log
        self.dc(connexion)
    def inserer_donnee(self,donnee,table,val):
        connexion = self.cn()
        curseur = self.cur()
        self.data_insert_2(curseur,donnee,table,val)
        self.mod(connexion,True)
        self.dc()

def ajouter_table(bd,curseur,ajouter,inserer,donnee):
    """ 'donnee' est une liste de tuples des occurencees des attributs dans l'ordre"""
    if (ajouter):
       bd.req(curseur)
    if (inserer):
        bd.data_insert(curseur,donnee)
def affichage_info_table(bd,curseur):
    info_table = bd.recup(curseur)
    print(info_table)
    return info_table    