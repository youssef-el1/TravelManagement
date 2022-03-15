from os import linesep
from sqlite3.dbapi2 import Cursor
import tkinter as tk
from tkinter.constants import CURRENT, DISABLED, END, W
from typing import Text
from tkinter import Frame, ttk
from tkinter import messagebox
import sqlite3

window=tk.Tk()
window.wm_title("Gestion des Agences de voyages")
window.geometry("1500x700")


m=tk.Menu(window) 
m1=tk.Menu(window) 
m2=tk.Menu(window) 
m3=tk.Menu(window) 

m.add_cascade(label="Gestion des clients",menu=m1)
m.add_cascade(label="Gestion des cicuits",menu=m2) 
m.add_cascade(label="Gestion des reservations",menu=m3)
def ajouter_client():
    cwindow=tk.Tk()
    cwindow.wm_title("Gestion des clients")
    cwindow.geometry("1500x700")
    table = ttk.Treeview(cwindow, columns = (1, 2, 3, 4, 5, 6,7), height = 5, show = "headings")
    def save():
        code=textbox7.get()
        nom=textbox1.get()
        prenom = textbox2.get()
        age = textbox3.get()
        cin = textbox4.get()
        lieu_de_naissance = textbox5.get()
        telephone = textbox6.get()
        if(code!=""and nom!=""and prenom!=""and age!=""and cin!=""and lieu_de_naissance!=""and telephone!=""):
        #Creeon la connexion
            con = sqlite3.connect('gestionvoyage.db')
            cuser = con.cursor()
            cuser.execute("insert into  user('code','nom','prenom','age','cin','lieunai','telephone') values (?,?,?,?,?,?,?);",(code,nom,prenom,age,cin,lieu_de_naissance,telephone))
            con.commit()
            con.close()
            messagebox.showinfo("client ajouter")
            con = sqlite3.connect('gestionvoyage.db')
            cuser = con.cursor()
            select = cuser.execute("select * from  user order by code desc")
            selectl = list(select)
            table.insert('',END,values = selectl[0])
            con.close()  
        else:
            messagebox.showerror("try again !!")
    def modifier():
        code=textbox7.get()
        nom = textbox1.get()
        prenom = textbox2.get()
        age = textbox3.get()
        cin = textbox4.get()
        lieu_nai = textbox5.get()
        telephone = textbox6.get()
        if(code!=""and nom!=""and prenom!=""and age!=""and cin!=""and lieu_nai!=""and telephone!=""):
        # Creeon la connexion
            con = sqlite3.connect("gestionvoyage.db")
            cuser = con.cursor()
            cuser.execute(
               "update user set nom=?,prenom=?,age=?,cin=?,lieunai=?,telephone=? where code=?",
                (nom, prenom, age, cin,lieu_nai ,telephone,code ))
            con.commit()
            con.close()
            messagebox.showinfo("client Modifier")
            con = sqlite3.connect("gestionvoyage.db")
            cuser = con.cursor()
            select = cuser.execute("select * from user order by code desc")
            selectl = list(select)
            table.insert('', END, values=selectl[0])
            con.close()
        else:
            messagebox.showerror("try again !!")
    def supprimer():
        codeSelectionner = table.item(table.selection())['values'][0]
        con = sqlite3.connect("gestionvoyage.db")
        cuser = con.cursor()
        delete  =cuser.execute("delete from user where code = {};".format(codeSelectionner))
        con.commit()
        table.delete(table.selection())   
   
    label1=tk.Label(cwindow,text="Nom") 
    label2=tk.Label(cwindow,text="Prenom")
    label3=tk.Label(cwindow,text="Age")
    label4=tk.Label(cwindow,text="CIN")
    label5=tk.Label(cwindow,text="Lieu de naissance")
    label6=tk.Label(cwindow,text="Telephone")
    label7=tk.Label(cwindow,text="Code")


    textbox1=tk.Entry(cwindow,width=25,borderwidth=5)
    textbox3=tk.Entry(cwindow,width=25,borderwidth=5)
    textbox2=tk.Entry(cwindow,width=25,borderwidth=5)
    textbox4=tk.Entry(cwindow,width=25,borderwidth=5)
    textbox5=tk.Entry(cwindow,width=25,borderwidth=5)
    textbox6=tk.Entry(cwindow,width=25,borderwidth=5)
    textbox7=tk.Entry(cwindow,width=25,borderwidth=5)

    b1=tk.Button(cwindow,command=save,text="Ajouter")
    b2=tk.Button(cwindow,command=supprimer,text="Suprimmer")
    b3=tk.Button(cwindow,command=modifier,text="Modifier")
    label1.grid(row=0,column=0)
    textbox1.grid(row=0,column=1)
    label2.grid(row=4,column=0)
    textbox2.grid(row=4,column=1)
    label3.grid(row=8,column=0)
    textbox3.grid(row=8,column=1)
    label4.grid(row=0,column=8)
    textbox4.grid(row=0,column=9)
    label5.grid(row=4,column=8)
    textbox5.grid(row=4,column=9)
    label6.grid(row=8,column=8)
    textbox6.grid(row=8,column=9)
    label7.grid(row=0,column=25)
    textbox7.grid(row=0,column=30)
    b1.grid(row=9,column=1)
    b2.grid(row=9,column=3)
    b3.grid(row=9,column=8)
    table.place(x = 200,y = 150, width = 800, height = 500)
    table.heading(1 , text = "code")
    table.heading(2 , text = "Nom")
    table.heading(3 , text = "Prenom")  
    table.heading(4 , text = "Age")
    table.heading(5 , text = "CIN")
    table.heading(6 , text = "Lieu de naissance")
    table.heading(7 , text = "TELEPHONE")

    #definir les dimentions des colonnes
    table.column(1,width = 50)
    table.column(2,width = 150)
    table.column(3,width = 150)
    table.column(4,width = 50)
    table.column(5,width = 150)
    table.column(6,width = 100)
    table.column(7,width = 100)

    # afficher les informations de la table
    con =  sqlite3.connect('gestionvoyage.db')
    cuser = con.cursor()
    select=cuser.execute('create table  if not exists user(code int primary key,nom varchar(50),prenom varchar(50),age int ,cin varchar(50),lieunai varchar(50),telephone int)')
    select = cuser.execute('select * from user')
    for row in select:
        table.insert('',END, value = row)  
    con.close()
    cwindow.mainloop()
                  




def ajouter_cicuit():

    Cwindow=tk.Tk()
    Cwindow.wm_title("Gestion des Agences de voyages")
    Cwindow.geometry("1500x700")
    Ctable = ttk.Treeview(Cwindow, columns = (1, 2, 3, 4), height = 5, show = "headings")
    CEtable = ttk.Treeview(Cwindow, columns = (1, 2, 3, 4), height = 5, show = "headings")
    CPtable = ttk.Treeview(Cwindow, columns = (1, 2, 3,4), height = 5, show = "headings")
    def saveC():
        codeC=textbox1C.get()
        Vdep=textbox2C.get()
        Varr = textbox3C.get()
        prix = textbox4C.get()
        
        if(codeC!=""and Vdep!=""and Varr!="" and prix!=""):
        #Creeon la connexion
            con = sqlite3.connect('gestionvoyage.db')
            cuser = con.cursor()
            cuser.execute("insert into Cicuita('NUMC','VDEP','VARR','PRIX') values (?,?,?,?);",(codeC,Vdep,Varr,prix))
            con.commit()
            con.close()
            messagebox.showinfo("cicuit ajouter")
            con = sqlite3.connect('gestionvoyage.db')
            cuser = con.cursor()
            select = cuser.execute("select * from  Cicuita order by NUMC desc")
            selectl = list(select)
            Ctable.insert('',END,values = selectl[0])
            con.close()  

        else:
            messagebox.showerror("try again !!")
    def saveCE():
        codeC=textbox1C.get()
        ce1=textbox1CE.get()
        ce2=textbox2CE.get()
        ce3=textbox3CE.get()
        con = sqlite3.connect('gestionvoyage.db')
        cuser = con.cursor()
        cuser.execute("insert into LESETAPESa1('NUMeta','NUMC','VETAPE','NBJOURS') values (?,?,?,?);",(ce1,codeC,ce2,ce3))
        con.commit()
        con.close()
        messagebox.showinfo("etape ajouter")
        con = sqlite3.connect('gestionvoyage.db')
        cuser = con.cursor()
        select = cuser.execute("select * from  LESETAPESa1 order by NUMeta desc")
        selectl = list(select)
        CEtable.insert('',END,values = selectl[0])
        con.close()
    def saveCP():
        codeC=textbox1C.get()
        cp1=textbox1CP.get()
        cp2=textbox2CP.get()
        cp3=textbox3CP.get()
        con = sqlite3.connect('gestionvoyage.db')
        cuser = con.cursor()
        cuser.execute("insert into LESPROGRAMMATIONSa1('NUMpr','NUMC','DATEDEP','NBPLACES') values (?,?,?,?);",(cp1,codeC,cp2,cp3))
        con.commit()
        con.close()
        messagebox.showinfo("programme ajouter")
        con = sqlite3.connect('gestionvoyage.db')
        cuser = con.cursor()
        select = cuser.execute("select * from  LESPROGRAMMATIONSa1 order by NUMpr desc")
        selectl = list(select)
        CPtable.insert('',END,values = selectl[0])
        con.close()

    def supprimerC():
        print("ll")
    def modifierC():
        print("mo")
    def supprimerCE():
        print("ll")
    def modifierCE():
        print("mo")
    def supprimerCP():
        print("ll")
    def modifierCP():
        print("mo")
    Ctable.place(x = 10,y = 200, width = 350, height = 250)
    Ctable.heading(1 , text = "codeCircuit")
    Ctable.heading(2 , text = "Ville_dep")
    Ctable.heading(3 , text = "Ville_arr")  
    Ctable.heading(4 , text = "Prix")

    #definir les dimentions des colonnes
    Ctable.column(1,width = 50)
    Ctable.column(2,width = 150)
    Ctable.column(3,width = 150)
    Ctable.column(4,width = 50)
    
    CEtable.place(x = 450,y = 200, width = 350, height = 250)
    CEtable.heading(1 , text = "codeEtape")
    CEtable.heading(2 , text = "codeCircuit")
    CEtable.heading(3 , text = "V_ETAPE")
    CEtable.heading(4 , text = "NBR_SEJOUR")  
    #definir les dimentions des colonnes
    CEtable.column(1,width = 50)
    CEtable.column(2,width = 150)
    CEtable.column(3,width = 150)
    CEtable.column(4,width = 150)

    CPtable.place(x = 900,y = 200, width = 350, height = 250)
    CPtable.heading(1 , text = "codeProgramme")
    CPtable.heading(2 , text = "codeCircuit")
    CPtable.heading(3 , text = "DATE_DEP")
    CPtable.heading(4 , text = "NBR_PLACES")  

    #definir les dimentions des colonnes
    CPtable.column(1,width = 50)
    CPtable.column(2,width = 150)
    CPtable.column(3,width = 150)
    CPtable.column(4,width = 150)

    NumC=tk.Label(Cwindow,text="Num Cicuit") 
    Ville_dep=tk.Label(Cwindow,text="Ville depart")
    Ville_arr=tk.Label(Cwindow,text="Ville d'arrive")
    Prix=tk.Label(Cwindow,text="Prix")
    textbox1C=tk.Entry(Cwindow,width=25,borderwidth=5)
    textbox3C=tk.Entry(Cwindow,width=25,borderwidth=5)
    textbox2C=tk.Entry(Cwindow,width=25,borderwidth=5)
    textbox4C=tk.Entry(Cwindow,width=25,borderwidth=5)
    NumC.grid(row=0,column=0)
    textbox1C.grid(row=0,column=1)
    Ville_dep.grid(row=4,column=0)
    textbox2C.grid(row=4,column=1)
    Ville_arr.grid(row=8,column=0)
    textbox3C.grid(row=8,column=1)
    Prix.grid(row=12,column=0)
    textbox4C.grid(row=12,column=1)

    Cetape=tk.Label(Cwindow,text="code etape")
    Ville_ETAPE=tk.Label(Cwindow,text="ETAPES")
    NBR_SEJOUR=tk.Label(Cwindow,text="NOMBRE DE SEJOUR")
    textbox1CE=tk.Entry(Cwindow,width=25,borderwidth=5)
    textbox3CE=tk.Entry(Cwindow,width=25,borderwidth=5)
    textbox2CE=tk.Entry(Cwindow,width=25,borderwidth=5)
    Cetape.grid(row=0,column=6)
    textbox1CE.grid(row=0,column=7)
    Ville_ETAPE.grid(row=4,column=6)
    textbox2CE.grid(row=4,column=7)
    NBR_SEJOUR.grid(row=8,column=6)
    textbox3CE.grid(row=8,column=7)

    codecp=tk.Label(Cwindow,text="code programme")
    DATE_DEP=tk.Label(Cwindow,text="DATE D'EPPART")
    NBR_Places=tk.Label(Cwindow,text="NOMBRE DE PLACES")
    textbox1CP=tk.Entry(Cwindow,width=25,borderwidth=5)
    textbox3CP=tk.Entry(Cwindow,width=25,borderwidth=5)
    textbox2CP=tk.Entry(Cwindow,width=25,borderwidth=5)
    codecp.grid(row=0,column=13)
    textbox1CP.grid(row=0,column=14)
    DATE_DEP.grid(row=4,column=13)
    textbox2CP.grid(row=4,column=14)
    NBR_Places.grid(row=8,column=13)
    textbox3CP.grid(row=8,column=14)

    bC1=tk.Button(Cwindow,command=saveC,text="Ajouter cicuit")
    bC2=tk.Button(Cwindow,command=supprimerC,text="Suprimmer cicuit")
    bC3=tk.Button(Cwindow,command=modifierC,text="Modifier cicuit")
    bCE1=tk.Button(Cwindow,command=saveCE,text="Ajouter etape ")
    bCE2=tk.Button(Cwindow,command=supprimerCE,text="Suprimmer etape")
    bCE3=tk.Button(Cwindow,command=modifierCE,text="Modifier cetape")
    bCP1=tk.Button(Cwindow,command=saveCP,text="Ajouter programme")
    bCP2=tk.Button(Cwindow,command=supprimerCP,text="Suprimmer programme")
    bCP3=tk.Button(Cwindow,command=modifierCP,text="Modifier programme")
    bC1.grid(row=30,column=1)
    bC2.grid(row=33,column=1)
    bC3.grid(row=36,column=1)
    bCE1.grid(row=30,column=3)#ae
    bCE2.grid(row=33,column=3)#se
    bCE3.grid(row=36,column=3)#me
    bCP1.grid(row=30,column=8)
    bCP2.grid(row=33,column=8)
    bCP3.grid(row=36,column=8)
    con =  sqlite3.connect('gestionvoyage.db')
    cuser = con.cursor()
    selectc=cuser.execute('create table  if not exists Cicuita(NUMC int primary key,VDEP varchar(30),VARR varchar(30),PRIX int)')
    selectc=cuser.execute('select * from Cicuita')
    for row in selectc:
        Ctable.insert('',END, value = row)
    con =  sqlite3.connect('gestionvoyage.db')
    cuser = con.cursor()
    
    selectce=cuser.execute('create table  if not exists LESETAPESa1 (NUMeta int primery key,NUMC int, VETAPE varchar(40), NBJOURS int,FOREIGN KEY (NUMC) REFERENCES Cicuita (NUMC))')    
    selectce=cuser.execute('select * from LESETAPESa1')
    for row in selectce:
        CEtable.insert('',END, value = row)
    con =  sqlite3.connect('gestionvoyage.db')
    cuser = con.cursor()
    selectcp=cuser.execute('create table  if not exists LESPROGRAMMATIONSa1(NUMpr int primary key,NUMC int, DATEDEP date, NBPLACES int,FOREIGN KEY (NUMC) REFERENCES Cicuita (NUMC))')
    selectcp=cuser.execute('select * from LESPROGRAMMATIONSa1')
    
    for row in selectcp:
        CPtable.insert('',END, value = row) 
    con.close()
    Cwindow.mainloop()

def ajouter_reservation():
    Rwindow=tk.Tk()
    Rwindow.wm_title("Gestion des Agences de voyages")
    Rwindow.geometry("1500x700")
    Rtable = ttk.Treeview(Rwindow, columns = (1, 2, 3, 4), height = 5, show = "headings")
    RRtable = ttk.Treeview(Rwindow, columns = (1, 2, 3), height = 5, show = "headings")
    
    def recherche():
        t=textboxrecherchedate.get()
        con =  sqlite3.connect('gestionvoyage.db')
        cuser = con.cursor()
        selectr=cuser.execute('select * from Cicuita where NUMC IN (SELECT NUMC from LESPROGRAMMATIONSa1 where DATEDEP='+t+')')
        for row in selectr:
            Rtable.insert('',END, value = row) 
        con.close()
    Rtable.place(x = 10,y = 200, width = 600, height = 300)
    Rtable.heading(1 , text = "codeCircuit")
    Rtable.heading(2 , text = "Ville_dep")
    Rtable.heading(3 , text = "Ville_arr")  
    Rtable.heading(4 , text = "Prix")


    #definir les dimentions des colonnes
    Rtable.column(1,width = 50)
    Rtable.column(2,width = 150)
    Rtable.column(3,width = 150)
    Rtable.column(4,width = 50)
    
    RRtable.place(x = 700,y = 200, width = 600, height = 300)
    RRtable.heading(1 , text = "code cicuit")
    RRtable.heading(2 , text = "code client")
    RRtable.heading(3 , text = "DATE_reservation")  
    #definir les dimentions des colonnes
    RRtable.column(1,width = 50)
    RRtable.column(2,width = 150)
    RRtable.column(3,width = 150)
    textboxrecherchedate=tk.Entry(Rwindow,width=25,borderwidth=5)
    textboxrecherchedate.grid(row=10,column=1)
    def saveR():
        codeC=textbox1R.get()
        CODECLI=textbox2R.get()
        DATERES = textbox3R.get()
        if(codeC!=""and CODECLI!=""and DATERES!=""):
        #Creeon la connexion
            con = sqlite3.connect('gestionvoyage.db')
            cuser = con.cursor()
            cuser.execute("insert into RESERVATION('NUMC','code','DATEres') values (?,?,?);",(codeC,CODECLI,DATERES))
            con.commit()
            con.close()
            messagebox.showinfo("reservation ajouter")
            con = sqlite3.connect('gestionvoyage.db')
            cuser = con.cursor()
            select = cuser.execute("select * from  RESERVATION order by NUMC desc,code desc")
            selectl = list(select)
            RRtable.insert('',END,values = selectl[0])
            con.close()  
        else:
            messagebox.showerror("try again !!")
    def supprimerR():
        print("jk")
    def modifierR():
        print("jk")
    recherchelabel=tk.Button(Rwindow,command=recherche,text="Recherche date")
    bR1=tk.Button(Rwindow,command=saveR,text="Ajouter RESERVATION")
    bR2=tk.Button(Rwindow,command=supprimerR,text="Suprimmer RESERVATION")
    bR3=tk.Button(Rwindow,command=modifierR,text="Modifier RESERVATION")
    bR1.grid(row=20,column=10)
    bR2.grid(row=20,column=20)
    bR3.grid(row=20,column=30)
    recherchelabel.grid(row=10,column=4)
    codec=tk.Label(Rwindow,text="NUM CICUIT")
    CODEU=tk.Label(Rwindow,text="NUM CLIENT")
    DATE_RESA=tk.Label(Rwindow,text="date reservation")
    textbox1R=tk.Entry(Rwindow,width=25,borderwidth=5)
    textbox3R=tk.Entry(Rwindow,width=25,borderwidth=5)
    textbox2R=tk.Entry(Rwindow,width=25,borderwidth=5)
    codec.grid(row=0,column=13)
    textbox1R.grid(row=0,column=14)
    CODEU.grid(row=4,column=13)
    textbox2R.grid(row=4,column=14)
    DATE_RESA.grid(row=8,column=13)
    textbox3R.grid(row=8,column=14)
    con =  sqlite3.connect('gestionvoyage.db')
    cuser = con.cursor()
    selectcp=cuser.execute('create table  if not exists RESERVATION(NUMC int,code int, DATEres date,primary key(NUMC,code),FOREIGN KEY (NUMC) REFERENCES Cicuita (NUMC),FOREIGN KEY (code) REFERENCES user (code))')
    selectcp=cuser.execute('select * from RESERVATION')
    for row in selectcp:
        RRtable.insert('',END, value = row) 
    con.close()
    Rwindow.mainloop()

m1.add_cascade(label="Ajouter",command=ajouter_client)

m2.add_command(label="Ajouter",command=ajouter_cicuit)
 
m3.add_command(label="Ajouter",command=ajouter_reservation)

window.config(menu=m,width=600,height=200) 

window.mainloop()