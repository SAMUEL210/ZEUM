# Copyright © SAMI, SAMUEL IBOU MARONE
# Programme ZEGM (Cryptage Binaire Avancé)
# Cypte et décrypte du texte et des fichier texte avac un cyptage en binaire tres avance et evolué

# Samuel Ibou Marone // @SAMI, @THe_CHoOSen_One // @SAMI, @ThE_HAckEr_One
# @ SAMI ©

# -------------------------------------------------------------------- #
#                                @ ZEUM                                #
#                              @ By SAMI                               #
#                    @ SAMIUEL IBOU MARONE  // Sept 2018               #
# -------------------------------------------------------------------- #

from tkinter import *
from random import *
from tkinter.messagebox import *
from tkinter.filedialog import *


class Zeum():
    def __init__(self):
        self.CODE = ['²','~','\n',' ', 'i', '\t', 'U','§','j', '[','©', '}','k', '(','P', 'l', ']','D', 'm', 'S', 'n', 'o', '-', '|', '&', 'p', 'q', 'C','{', 'a', 'b', 'c', 'd', 'e','E', 'H', 'F','_', 'é', 'ç', 'ê','ô', 'â', 'J', 'K', '8', 'L', '^', 'M', '\'', 'N','\"', 'O', 'Y', 'Z', 'f', 'g', 'h', 'r', 's', 't', 'u', 'v', 'w', 'x', '0', 'y', 'z' , '1', '2','A', '4', 'W', '5','G', '6', 'I','7', ",", '@', '!', '.', '?', ';', ':', '/', "'", '*', '+', 'T', '3', 'V', 'B', '#', 'Q', 'R', 'X', ')', 'î', '9']
        self.COLORS = ['OliveDrab2', 'PaleGreen2', 'DarkOrange2','gray74', 'AntiqueWhite3', 'khaki1', 'SkyBlue1', 'brown2', 'SkyBlue1', 'snow2', 'AntiqueWhite1', 'chartreuse4', 'DarkGoldenrod3', 'lawn green', 'DarkOrange4', 'gray70', 'old lace', 'bisque3', 'CadetBlue2', 'medium spring green', 'misty rose', 'steel blue', 'LightSalmon2', 'violet red', 'khaki2', 'dark orange', 'turquoise4', 'PaleTurquoise1', 'DeepPink3', 'lime green','ghost white','light yellow', 'honeydew2', 'HotPink1', 'sandy brown', 'DarkOrange2', 'IndianRed3', 'IndianRed1', 'LightSkyBlue1']
        self.fen = Tk()
        self.fen.geometry('700x300')
        self.fen.title('ZEUM')
        self.fen.resizable(height=False, width=False)
        self.fen.config(bg='DarkOrange2')
        self.fen.iconbitmap('logo.ico')

        menubar = Menu(self.fen)

        menu1 = Menu(menubar, tearoff=0)
        menu1.add_separator()
        menu1.add_command(label='Quitter', command=self.fen.destroy)
        menubar.add_cascade(label='FENETRE', menu=menu1)

        menu2 = Menu(menubar, tearoff=0)
        menu2.add_command(label='Cryptage Texte', command=self.CryptTexte)
        menu2.add_separator()
        menu2.add_command(label='Decryptage Texte', command=self.DecryptTexte)
        menu2.add_separator()
        menu2.add_command(label='Cryptage Fichier', command=self.CryptFichier)
        menu2.add_separator()
        menu2.add_command(label='Decryptage Fichier', command=self.DecryptFichier)
        menubar.add_cascade(label='OPTIONS', menu=menu2)

        menu3 = Menu(menubar, tearoff=0)
        menu3.add_command(label='Infos App', command=self.Infos)
        menu3.add_separator()
        menu3.add_command(label='Contacter L\'aurteur', command=self.Contact)
        menubar.add_cascade(label='?', menu=menu3)

        self.fen.config(menu=menubar)
        framfram0  =Frame(self.fen, bg='DarkOrange2')
        framfram0.pack()

        fram1 = Frame(framfram0,  bg='DarkOrange2')
        fram1.pack(side=LEFT, padx=20)

        photo1 = PhotoImage(file='logo1.png')
        self.item1 = Label(fram1, image=photo1, relief=GROOVE, bg='white')
        self.item1.photo = photo1
        self.item1.pack()
        self.animation()
        
        fram2 = Frame(framfram0, relief=GROOVE, bg='DarkOrange2')
        fram2.pack(pady=20)
        Label(fram2, text='Zeum Cryptage Décrytage', font='calibri 14 bold italic', bg='DarkOrange2').pack()
        Label(fram2, text='Chiffrement Avancé', font='calibri 10 italic', bg='DarkOrange2').pack()
        Button(fram2, text='ZEUM', font='calibri 12 bold italic', command=self.Z, bg='bisque').pack(pady=10, padx=30)
        Button(fram2, text='Crypt / Décrypt Texte', font='calibri 12 bold italic', padx=4, command=self.CryptTexte, bg='bisque').pack(pady=10, padx=30)
        Button(fram2, text='Crypt / Décrypt Fichier', font='calibri 12 bold italic', command=self.CryptFichier, bg='bisque').pack(pady=10, padx=30)

        fram101 = Frame(self.fen)
        fram101.pack(side=BOTTOM, fill=X)

        marquee = Marquee(fram101, text='ZEUM\t\t\t\t\t\t\t\tCHIFFREMENT\t\t\t\t\t\t\t\tCrytage & Décryptage Avancé\t\t\t\t\t\t\t\tZEUM est une application qui exploite une méthode de chiffrement de Texte basé sur du 0b111100b1000b101000b111010b1000b1110100b100001 (RETOUR A LA BASE DE L\'INFORMATION) mais modifié avec une petite recette secrète qui renvoi un rendu en 0b111100b1000b101000b111010b1000b1110100b100001 AVANCÉ. Étant sur sa première version 1.6  Elle présente pour le moment la possibilité de chiffrer du TEXTE et DES FICHIERS TEXTE !!!\t\t\t\t\t\t\t\t\tVous remerciant de l\'intéret que vous portez à notre application, vous pouvez nous contacter pour conseille ou suggestion ou critique via notre email: hiserviceone@gmailcom\t\t\t\t\t\t\t\tAvec ZEUM l\'information est en sureté partout\t\t\t\t\tN\'ésiter pas a aller dans les options pour plus de possibilité !!!, Copyright S I MARONE, SAMI ©, Juil 2018', borderwidth=1, relief="sunken")
        marquee.pack(fill=X)   

        self.fen.mainloop()

    def animation(self):
        val = randint(0, 38)
        self.va = self.COLORS[val]
        self.item1.config(bg=self.va)
        self.item1.after(2000, self.animation)

    def affi(self):
        print(self.va)

    def Infos(self):
        showinfo('INFORMATION', 'ZEUM EST UN SYSTEME DE CHIFFREMENT DE TEXTE OU DE FICHIERS CONTENANT DU TEXTE QUI RENVOI UN RESULTAT EN BINNAIRE MAIS EN BINAIRE MODIFIER SELON UNE TECHNIQUE SECRETE INDECYPTIBLE !!!\n\nCopyright © S MARONE')

    def Contact(self):
        showinfo('CONTACT AUTEUR', 'EN CAS DE BEUG OU DE CONSEIL OU DE SUGGESTION D\'AMÉLIORATION VOUS POUVEZ CONTACTER L\'AUTEUR VIA CE EMAIL :::\nEmail : hiservicesone@gmail.com\n\nCopyright © S MARONE') 

    def Z(self):
        showinfo('ZEUM', '\t  ZEUM\n\nCryptage Décryptage Binaire Avancé\nVersion : 1.6\nAuteur : S I MARONE @SAMI \nEmail : hiservicesone@gmail.com\n\nCopyright © S MARONE, Sept. 2018') 
    
    def CryptTexte(self):
        self.enc = 10
        try:
            self.fen1.destroy()
        except:
            rien = ''
        self.fen1 = Toplevel(self.fen)
        self.fen1.grab_set()
        self.fen1.focus_set()
        self.fen1.geometry("+350+10")  
        self.fen1.title('Cryptage Texte')
        self.fen1.iconbitmap('logo.ico') 
        self.fen1.resizable(width=False,height=False)
        self.fen1.config(bg='DarkOrange2')

        menubar = Menu(self.fen1)

        menu1 = Menu(menubar, tearoff=0)
        menu1.add_separator()
        menu1.add_command(label='Quitter', command=self.fen1.destroy)
        menubar.add_cascade(label='FENETRE', menu=menu1)

        menu2 = Menu(menubar, tearoff=0)
        menu2.add_command(label='Decryptage Texte', command=self.DecryptTexte)
        menu2.add_separator()
        menu2.add_command(label='Cryptage Fichier', command=self.CryptFichier)
        menu2.add_separator()
        menu2.add_command(label='Décryptage Fichier', command=self.DecryptFichier)
        menu2.add_separator()
        menu2.add_command(label='Ajouter Une Cle   //Enlever Option', command=self.OptAjouterCle)
        menu2.add_separator()
        menu2.add_command(label='Ajouter Le niveau de Cryptage   //Enlever Option', command=self.OptNiveauCryptage)
        menu2.add_separator()
        menu2.add_command(label='Ajouter Phrase Secrète   //Enlever Option', command=self.OptAjouterPhraseSecrete)
        menubar.add_cascade(label='OPTIONS', menu=menu2)

        menu3 = Menu(menubar, tearoff=0)
        menu3.add_command(label='Infos App', command=self.Infos)
        menu3.add_separator()
        menu3.add_command(label='Contacter L\'aurteur', command=self.Contact)
        menubar.add_cascade(label='?', menu=menu3)

        self.fen1.config(menu=menubar)

        self.etatAjCle = 0
        self.etatAjNiveau = 0
        self.etatAjPhraseSecrete = 0
        
        Label(self.fen1, text='Cryptage Texte', font='algerian 45 bold italic', bg='DarkOrange2').pack()
        
        self.fram00 = Frame(self.fen1, bg='DarkOrange2')
        self.fram00.pack(padx=10, pady=5)
        Label(self.fram00, text='In', font='calibri 12 italic', bg='DarkOrange2').pack(anchor='nw')
        self.Texte0 = Text(self.fram00, height= 7, width=80, font='calibri 11 bold italic', bg='bisque')
        self.Texte0.pack(side=LEFT)
        
        scrollbar0 = Scrollbar(self.fram00, command=self.Texte0.yview)
        scrollbar0.pack(side=RIGHT, fill=Y)
        scrollbar0.configure(command=self.Texte0.yview)
        self.Texte0['yscrollcommand'] = scrollbar0.set

        self.fram0 = Frame(self.fen1, bg='DarkOrange2')
        self.fram0.pack(fill=X, padx=20, pady=5)
        
        self.fram01 = Frame(self.fram0, width=100, height=100, bg='DarkOrange2')
        self.fram01.pack()

        self.label0 = Label(self.fram01, text='Mot de passe : ', font='calibri 12 bold italic', bg='DarkOrange2')
        self.label0.pack(side=LEFT)
        self.mp = Entry(self.fram01, width=20, font='calibri 11 bold italic', bg='bisque')
        self.mp.pack(pady=5,padx=5, side=LEFT)
        
        self.ButCrypter = Button(self.fen1, text='Crypter', command=self.CrypterTexte, font='calibri 12 bold italic', padx=2,bg='bisque')
        self.ButCrypter.pack()

        self.fram11 = Frame(self.fen1, bg='DarkOrange2')
        self.fram11.pack(padx=10, pady=5)
        Label(self.fram11, text='Out', font='calibri 12 italic', bg='DarkOrange2').pack(anchor='nw')
        self.Texte1 = Text(self.fram11, height= 7, width=80, font='calibri 11 bold italic', bg='bisque')
        self.Texte1.pack(side=LEFT)
        self.Texte1.configure(state=DISABLED)
        scrollbar11 = Scrollbar(self.fram11, command=self.Texte1.yview)
        scrollbar11.pack(side=RIGHT, fill=Y)
        scrollbar11.configure(command=self.Texte1.yview)
        self.Texte1['yscrollcommand'] = scrollbar11.set

        Label(self.fen1, text='Info Cryptage', font='calibri 12 italic', bg='DarkOrange2').pack()
        self.Texteinf = Text(self.fen1, height= 3, width=41, font='calibri 11 italic bold', bg='bisque')
        self.Texteinf.pack(padx=10, pady=4)
        self.Texteinf.configure(state=DISABLED)

        self.fen1.mainloop()

    def DecryptTexte(self):
        try:
            self.fen1.destroy()
        except:
            rien = ''
        self.fen1 = Toplevel(self.fen)
        self.fen1.grab_set()
        self.fen1.focus_set()
        self.fen1.geometry("+350+10")  
        self.fen1.title('Décryptage Texte')
        self.fen1.iconbitmap('logo.ico') 
        self.fen1.resizable(width=False,height=False)
        self.fen1.config(bg='DarkOrange2')

        menubar = Menu(self.fen1)

        menu1 = Menu(menubar, tearoff=0)
        menu1.add_separator()
        menu1.add_command(label='Quitter', command=self.fen1.destroy)
        menubar.add_cascade(label='FENETRE', menu=menu1)

        menu2 = Menu(menubar, tearoff=0)
        menu2.add_command(label='Cryptage Texte', command=self.CryptTexte)
        menu2.add_separator()
        menu2.add_command(label='Décryptage Fichier', command=self.DecryptFichier)
        menu2.add_separator()
        menu2.add_command(label='Cryptage Fichier', command=self.CryptFichier)
        menu2.add_separator()
        menu2.add_command(label='Ajouter Une Cle   //Enlever Option', command=self.OptAjouterCle)
        menu2.add_separator()
        menu2.add_command(label='Ajouter Le niveau de Décryptage   //Enlever Option', command=self.OptNiveauCryptage)
        menu2.add_separator()
        menu2.add_command(label='Ajouter Phrase Secrète   //Enlever Option', command=self.OptAjouterPhraseSecrete)
        menubar.add_cascade(label='OPTIONS', menu=menu2)

        menu3 = Menu(menubar, tearoff=0)
        menu3.add_command(label='Infos App', command=self.Infos)
        menu3.add_separator()
        menu3.add_command(label='Contacter L\'aurteur', command=self.Contact)
        menubar.add_cascade(label='?', menu=menu3)

        self.fen1.config(menu=menubar)

        self.etatAjCle = 0
        self.etatAjNiveau = 0
        self.etatAjPhraseSecrete = 0
        self.enc = 10
        
        Label(self.fen1, text='Décryptage Texte', font='algerian 45 bold italic', bg='DarkOrange2').pack(padx=5)
        
        self.fram00 = Frame(self.fen1, bg='DarkOrange2')
        self.fram00.pack(padx=10, pady=5)
        Label(self.fram00, text='In', font='calibri 12 italic', bg='DarkOrange2').pack(anchor='nw')
        self.Texte0 = Text(self.fram00, height= 7, width=80, font='calibri 11 bold italic', bg='bisque')
        self.Texte0.pack(side=LEFT)
        scrollbar0 = Scrollbar(self.fram00, command=self.Texte0.yview)
        scrollbar0.pack(side=RIGHT, fill=Y)
        scrollbar0.configure(command=self.Texte0.yview)
        self.Texte0['yscrollcommand'] = scrollbar0.set
        
        self.fram0 = Frame(self.fen1, bg='DarkOrange2')
        self.fram0.pack(fill=X, padx=20, pady=5)
        
        self.fram01 = Frame(self.fram0, width=100, height=100, bg='DarkOrange2')
        self.fram01.pack()

        self.label0 = Label(self.fram01, text='Mot de passe : ', font='calibri 12 bold italic', bg='DarkOrange2')
        self.label0.pack(side=LEFT)
        self.mp = Entry(self.fram01, width=20, font='calibri 11 bold italic', bg='bisque')
        self.mp.pack(pady=5,padx=5, side=LEFT)
        
        self.ButCrypter = Button(self.fen1, text='Décrypter', command=self.DecrypterTexte, font='calibri 12 bold italic', padx=2, bg='bisque')
        self.ButCrypter.pack()

        self.fram11 = Frame(self.fen1, bg='DarkOrange2')
        self.fram11.pack(padx=10, pady=5)
        Label(self.fram11, text='Out', font='calibri 12 italic', bg='DarkOrange2').pack(anchor='nw')
        self.Texte1 = Text(self.fram11, height= 7, width=80, font='calibri 11 bold italic', bg='bisque')
        self.Texte1.pack(side=LEFT)
        self.Texte1.configure(state=DISABLED)
        scrollbar11 = Scrollbar(self.fram11, command=self.Texte1.yview)
        scrollbar11.pack(side=RIGHT, fill=Y)
        scrollbar11.configure(command=self.Texte1.yview)
        self.Texte1['yscrollcommand'] = scrollbar11.set

        self.fen1.mainloop()

    def CryptFichier(self):
        try:
            self.fen1.destroy()
        except:
            rien = ''
        self.fen1 = Toplevel(self.fen)
        self.fen1.grab_set()
        self.fen1.focus_set()
        self.fen1.geometry("+350+100")  
        self.fen1.title('Cryptage Fichier')
        self.fen1.iconbitmap('logo.ico') 
        self.fen1.resizable(width=False,height=False)
        self.fen1.config(bg='DarkOrange2')
        
        menubar = Menu(self.fen1)

        menu1 = Menu(menubar, tearoff=0)
        menu1.add_separator()
        menu1.add_command(label='Quitter', command=self.fen1.destroy)
        menubar.add_cascade(label='FENETRE', menu=menu1)
        menu2 = Menu(menubar, tearoff=0)
        menu2.add_command(label='Décryptage Fichier', command=self.DecryptFichier)
        menu2.add_separator()
        menu2.add_command(label='Cryptage Texte', command=self.CryptTexte)
        menu2.add_separator()
        menu2.add_command(label='Décryptage Texte', command=self.DecryptTexte)
        menu2.add_separator()
        menu2.add_command(label='Ajouter Une Cle   //Enlever Option', command=self.OptAjouterCle)
        menu2.add_separator()
        menu2.add_command(label='Ajouter Le niveau de Cryptage   //Enlever Option', command=self.OptNiveauCryptage)
        menu2.add_separator()
        menu2.add_command(label='Ajouter Phrase Secrète   //Enlever Option', command=self.OptAjouterPhraseSecrete)
        menubar.add_cascade(label='OPTIONS', menu=menu2)

        menu3 = Menu(menubar, tearoff=0)
        menu3.add_command(label='Infos App', command=self.Infos)
        menu3.add_separator()
        menu3.add_command(label='Contacter L\'aurteur', command=self.Contact)
        menubar.add_cascade(label='?', menu=menu3)

        self.fen1.config(menu=menubar)

        self.etatAjCle = 0
        self.etatAjNiveau = 0
        self.etatAjPhraseSecrete = 0
        self.enc = 20
        
        Label(self.fen1, text='Cryptage Fichier', font='algerian 45 bold italic', padx=10, bg='DarkOrange2').pack()
        
        Label(self.fen1, text='In', font='calibri 12 italic', bg='DarkOrange2').pack(anchor='nw', padx=10)
        self.fram00 = LabelFrame(self.fen1, relief=GROOVE, bg='DarkOrange2')
        self.fram00.pack(padx=10, pady=5)
        self.Entre0  = Entry(self.fram00, width=70, font='calibri 11 bold italic', bg='bisque', state=DISABLED)
        self.Entre0.pack(side=LEFT, pady=10, padx=5)
        self.Parc0 = Button(self.fram00, text='Parcourrir', font='calibri 12 bold italic', command=self.ParcFichCrypt, bg='bisque')
        self.Parc0.pack(side=LEFT, padx=10, pady=10)
        
        Label(self.fen1, text='Out', font='calibri 12 italic', bg='DarkOrange2').pack(anchor='nw', padx=10)
        self.fram11 = LabelFrame(self.fen1, bg='DarkOrange2')
        self.fram11.pack(padx=10, pady=5)
        self.Entre1  = Entry(self.fram11, width=70, font='calibri 11 italic', bg='bisque', state=DISABLED)
        self.Entre1.pack(side=LEFT, pady=10, padx=5)
        self.Parc1 = Button(self.fram11, text='Parcourrir', font='calibri 12 bold italic', command=self.ParcFichSauvCrypt, bg='bisque')
        self.Parc1.pack(side=LEFT, padx=10, pady=10)

        self.fram0 = Frame(self.fen1, bg='DarkOrange2')
        self.fram0.pack(fill=X, padx=20, pady=20)
        
        self.fram01 = Frame(self.fram0, width=100, height=100, bg='DarkOrange2')
        self.fram01.pack()

        self.label0 = Label(self.fram01, text='Mot de passe : ', font='calibri 12 bold italic', bg='Darkorange2')
        self.label0.pack(side=LEFT)
        self.mp = Entry(self.fram01, width=20, font='calibri 11 bold italic', bg='bisque')
        self.mp.pack(pady=5,padx=5, side=LEFT)
        
        self.ButCrypter = Button(self.fen1, text='Crypter', command=self.CrypterTexte, font='calibri 12 bold italic', padx=2, bg='bisque')
        self.ButCrypter.pack(pady=10)

        Label(self.fen1, text='Info Cryptage', font='calibri 12 italic', bg='DarkOrange2').pack()
        self.Texteinf = Text(self.fen1, height= 3, width=41, font='calibri 11 italic bold', bg='bisque')
        self.Texteinf.pack(padx=10, pady=4)
        self.Texteinf.configure(state=DISABLED)

        self.fen1.mainloop()

    def DecryptFichier(self):
        try:
            self.fen1.destroy()
        except:
            rien = ''
        self.fen1 = Toplevel(self.fen)
        self.fen1.grab_set()
        self.fen1.focus_set()
        self.fen1.geometry("+350+100")  
        self.fen1.title('Décryptage Fichier')
        self.fen1.iconbitmap('logo.ico') 
        self.fen1.resizable(width=False,height=False)
        self.fen1.config(bg='DarkOrange2')

        menubar = Menu(self.fen1)

        menu1 = Menu(menubar, tearoff=0)
        menu1.add_separator()
        menu1.add_command(label='Quitter', command=self.fen1.destroy)
        menubar.add_cascade(label='FENETRE', menu=menu1)

        menu2 = Menu(menubar, tearoff=0)
        menu2.add_command(label='Cryptage Fichier', command=self.CryptFichier)
        menu2.add_separator()
        menu2.add_command(label='Décryptage Texte', command=self.DecryptTexte)
        menu2.add_separator()
        menu2.add_command(label='Cryptage Texte', command=self.CryptTexte)
        menu2.add_separator()
        menu2.add_command(label='Ajouter Une Cle   //Enlever Option', command=self.OptAjouterCle)
        menu2.add_separator()
        menu2.add_command(label='Ajouter Le niveau de Décryptage   //Enlever Option', command=self.OptNiveauCryptage)
        menu2.add_separator()
        menu2.add_command(label='Ajouter Phrase Secrète   //Enlever Option', command=self.OptAjouterPhraseSecrete)
        menubar.add_cascade(label='OPTIONS', menu=menu2)

        menu3 = Menu(menubar, tearoff=0)
        menu3.add_command(label='Infos App', command=self.Infos)
        menu3.add_separator()
        menu3.add_command(label='Contacter L\'aurteur', command=self.Contact)
        menubar.add_cascade(label='?', menu=menu3)

        self.fen1.config(menu=menubar)

        self.etatAjCle = 0
        self.etatAjNiveau = 0
        self.etatAjPhraseSecrete = 0
        self.enc = 20
        
        Label(self.fen1, text='Décryptage Fichier', font='algerian 45 bold italic', padx=10, bg='DarkOrange2').pack()
        
        Label(self.fen1, text='In', font='calibri 12 italic', bg='DarkOrange2').pack(anchor='nw', padx=10)
        self.fram00 = LabelFrame(self.fen1, relief=GROOVE, bg='DarkOrange2')
        self.fram00.pack(padx=10, pady=5)
        self.Entre0  = Entry(self.fram00, width=70, font='calibri 11 bold italic', bg='bisque', state=DISABLED)
        self.Entre0.pack(side=LEFT, pady=10, padx=5)
        self.Parc0 = Button(self.fram00, text='Parcourrir', font='calibri 12 bold italic', command=self.ParcFichADecrypt, bg='bisque')
        self.Parc0.pack(side=LEFT, padx=10, pady=10)
        
        Label(self.fen1, text='Out', font='calibri 12 italic', bg='DarkOrange2').pack(anchor='nw', padx=10)
        self.fram11 = LabelFrame(self.fen1, bg='DarkOrange2')
        self.fram11.pack(padx=10, pady=5)
        self.Entre1 = Entry(self.fram11, width=70, font='calibri 11 italic', bg='bisque', state=DISABLED)
        self.Entre1.pack(side=LEFT, pady=10, padx=5)
        self.Parc1 = Button(self.fram11, text='Parcourrir', font='calibri 12 bold italic', command=self.ParcFichSauvDecrypt, bg='bisque')
        self.Parc1.pack(side=LEFT, padx=10, pady=10)

        self.fram0 = Frame(self.fen1, bg='DarkOrange2')
        self.fram0.pack(fill=X, padx=20, pady=20)
        
        self.fram01 = Frame(self.fram0, width=100, height=100, bg='DarkOrange2')
        self.fram01.pack()

        self.label0 = Label(self.fram01, text='Mot de passe : ', font='calibri 12 bold italic', bg='DarkOrange2')
        self.label0.pack(side=LEFT)
        self.mp = Entry(self.fram01, width=20, font='calibri 11 bold italic', bg='bisque')
        self.mp.pack(pady=5,padx=5, side=LEFT)
        
        self.ButCrypter = Button(self.fen1, text='Décrypter', command=self.DecrypterTexte, font='calibri 12 bold italic', padx=2, bg='bisque')
        self.ButCrypter.pack(pady=10)

        self.fen1.mainloop()
        
    def OptAjouterCle(self):
        if self.etatAjPhraseSecrete == 1:
            showinfo('OPTIONS', 'L\'OPTIONS PHRASE SECRÈTE EST ACTIVE CETTE OPTION NE PEUT PAS ETRE ACTIVE\nVEUILLEZ DÉSACTIVER L\'OPTION PHRASE SECRÈTE POUR UTILISER CETE OPTION !!!')
        else:
            if self.etatAjCle == 1:
                if askyesno('OPTION CLÉ DEJA ACTIVÉE', 'CETTE OPTION EST DÉJA ACTIVÉE VOULEZ VOUS LA DÉSACTIVER ?'):
                    self.fram02.destroy()
                    self.etatAjCle = 0
                else:
                    rien = ''
            else:
                self.fram02 = Frame(self.fram0, bg='DarkOrange2')
                self.fram02.pack()
                self.valeur = IntVar()
                self.checkcle = Checkbutton(self.fram02, text='Ajouter une clé : ', variable=self.valeur, command=self.AjouterCle, font='calibri 12 bold italic', bg='DarkOrange2')
                self.checkcle.pack()
                self.etatAjCle = 1
        
    def AjouterCle(self):
        if self.valeur.get() == 1:
            self.textcle = Entry(self.fram02, width=15, font='calibri 11 italic', bg='bisque')
            self.checkcle.pack(side=LEFT)
            self.textcle.pack(side= LEFT)

        else:
            self.textcle.destroy()

    def OptNiveauCryptage(self):
        if self.etatAjNiveau == 1:
            if askyesno('OPTION NIVEAU DEJA ACTIVÉE', 'CETTE OPTION EST DEJA ACTIVÉE VOULEZ VOUS LA DÉSACTIVER ?'):
                self.fram03.destroy()
                self.etatAjNiveau = 0
            else:
                rien = ''
        else:
            showinfo('INFORMATION', 'LE CRYPTAGE PAR NIVEAU REQUIERT BEAUCOUP DE PUISSANCE POUR UNE EXÉCUTION FLUIDE\nPLUS LE NIVEAU EST HAUT PLUS DE PUISSANCE SERAS REQUIS !!!')
            self.fram03 = Frame(self.fram0, bg='DarkOrange2')
            self.fram03.pack()
            self.valeurniv = IntVar()
            self.checkniveau = Checkbutton(self.fram03, text='Niveau de Cryptage : ', variable=self.valeurniv, command=self.NiveauCryptage, font='calibri 12 bold italic', bg='DarkOrange2')
            self.checkniveau.pack()
            self.etatAjNiveau = 1

    def NiveauCryptage(self):
        if self.valeurniv.get() == 1:
            self.textniv = Spinbox(self.fram03, width=2,from_=1, to=10, font='calibri 11 bold italic', bg='bisque')
            self.checkniveau.pack(side=LEFT)
            self.textniv.pack(side= LEFT)
        else:
            self.textniv.destroy()

    def OptAjouterPhraseSecrete(self):
        if self.etatAjPhraseSecrete == 1:
            if askyesno('OPTION PHRASE SECRETE DÉJA ACTIVÉE', 'CETTE OPTION EST DÉJA ACTIVÉE VOULEZ VOUS LA DÉSACTIVER ?'):
                self.fram01.destroy()
                self.fram01 = Frame(self.fram0, width=100, height=100, bg='DarkOrange2')
                self.fram01.pack()
                self.label0 = Label(self.fram01, text='Mot de passe : ', font='calibri 12 bold italic', bg='DarkOrange2')
                self.label0.pack(side=LEFT)
                self.mp = Entry(self.fram01, width=15, font='calibri 11 bold italic')
                self.mp.pack(side=LEFT, padx=5, pady=5)
                self.etatAjPhraseSecrete = 0
                self.etatAjCle = 0
            else:
                rien = ''
        else:
            if askyesno('PHRASE SECRÈTE', 'SI CETTE OPTION EST ACTIVÉE LES OPTIONS MOT DE PASSE ET CLÉ SERONT DÉSACTIVÉES !!!'):
                self.fram01.destroy()
                try:
                    self.fram02.destroy()
                except:
                    rien = ''
                self.fram01 = Frame(self.fram0, width=100, height=100, bg='DarkOrange2')
                self.fram01.pack()
                self.labelsecrete = Label(self.fram01, text='Phrase Secrète : ', font='calibri 12 bold italic', bg='DarkOrange2')
                self.labelsecrete.pack(side=LEFT)
                self.secrete = Entry(self.fram01, width=40, font='calibri 11 bold italic')
                self.secrete.pack(side=LEFT, pady=5,padx=5)
                self.etatAjPhraseSecrete = 1
                self.etatAjCle = 0
            else:
                rien = ''

    def ParcFichCrypt(self):
        self.cryptfile = askopenfilename(title='Ouvrir Fichier à crypter', filetypes=[('Text files','.txt'), ('Textos Files', '.xto')])
        self.Entre0.configure(state=NORMAL)
        self.Entre0.delete(0, 100000000)
        self.Entre0.insert(0, self.cryptfile)
        self.Entre0.configure(state=DISABLED)

    def ParcFichSauvCrypt(self):
        self.savefilecrypt = asksaveasfilename(title='Enregistrer Sous', filetypes=[('MRN files','.mrn')])
        self.Entre1.configure(state=NORMAL)
        self.Entre1.delete(0, 100000000)
        if self.savefilecrypt[-4:] == '.mrn':
            self.Entre1.insert(0, self.savefilecrypt)
        else:
            self.Entre1.insert(0, self.savefilecrypt + '.mrn')
        self.Entre1.configure(state=DISABLED)

    def ParcFichADecrypt(self):
        self.cryptfile = askopenfilename(title='Ouvrir Fichier à Décrypter', filetypes=[('MRN files','.mrn')])
        self.Entre0.configure(state=NORMAL)
        self.Entre0.delete(0, 100000000)
        self.Entre0.insert(0, self.cryptfile)
        self.Entre0.configure(state=DISABLED)

    def ParcFichSauvDecrypt(self):
        self.savefilecrypt = asksaveasfilename(title='Enregistrer Sous', filetypes=[('Text files','.txt'), ('Textos Files', '.xto')])
        self.Entre1.configure(state=NORMAL)
        self.Entre1.delete(0, 100000000)
        if self.savefilecrypt[-4:] == '.txt' or self.savefilecrypt[-4:] == '.xto':
            self.Entre1.insert(0, self.savefilecrypt)
        else:
            self.Entre1.insert(0, self.savefilecrypt + '.txt')
        self.Entre1.configure(state=DISABLED)

    def CrypterTexte(self):
        
        self.CODE = ['²','~','\n',' ', 'i', '\t', 'U','§','j', '[','©', '}','k', '(','P', 'l', ']','D', 'm', 'S', 'n', 'o', '-', '|', '&', 'p', 'q', 'C','{', 'a', 'b', 'c', 'd', 'e','E', 'H', 'F','_', 'é', 'ç', 'ê','ô', 'â', 'J', 'K', '8', 'L', '^', 'M', '\'', 'N','\"', 'O', 'Y', 'Z', 'f', 'g', 'h', 'r', 's', 't', 'u', 'v', 'w', 'x', '0', 'y', 'z' , '1', '2','A', '4', 'W', '5','G', '6', 'I','7', ",", '@', '!', '.', '?', ';', ':', '/', "'", '*', '+', 'T', '3', 'V', 'B', '#', 'Q', 'R', 'X', ')', 'î', '9']
        if self.enc == 10:
            Texte = self.Texte0.get(0.0, 1000000000000.0)
            Texte = Texte[:-1]
        elif self.enc == 20:
            with open(self.cryptfile, 'r') as f:
                Texte = f.read()
        a = 0
        b = 0
        c = 0
        d = 0
        if Texte == '' or Texte == '\n':
            showinfo('SAISIE VIDE', 'VEUILLEZ SAISIR LE TEXTE À CRYPTER !!!')
        else:
            if self.etatAjPhraseSecrete == 0:
                if self.mp.get() != '':
                    mp = self.mp.get()
                    if len(mp) > 13:
                        showinfo('ERREUR TAILLE MOT DE PASSE', 'LA TAILLE MAX DU MOT DE PASSE EST DE 13 CARRACTÈRES !!!\n\nTEXTE CRYPTÉ SANS LE MOT DE PASSE!!!')
                        self.mp.delete(0, 1000)
                        self.Texteinf.configure(state=NORMAL)
                        self.Texteinf.delete(0.0, 100000000.0)
                        self.Texteinf.configure(state=DISABLED)
                    elif len(mp) < 6:
                        showinfo('ERREUR TAILLE MOT DE PASSE', 'LA TAILLE MIN DU MOT DE PASSE EST DE 6 CARRACTÈRES !!!\n\nTEXTE CRYPTÉ SANS LE MOT DE PASSE!!!')
                        self.mp.delete(0, 1000)
                        self.Texteinf.configure(state=NORMAL)
                        self.Texteinf.delete(0.0, 100000000.0)
                        self.Texteinf.configure(state=DISABLED)
                    else:
                        mp = self.mpkey(mp)
                        if mp >= 1.0:
                            mp = mp - int(mp)
                    try:
                        shuffle(self.CODE, random=lambda:mp)
                        a = 1
                    except:
                        rien = ''
        
                if self.etatAjCle == 1:
                    if self.valeur.get() == 1:
                        cle = self.textcle.get()
                        if len(cle) > 13:
                            showinfo('ERREUR TAILLE DE LA CLÉ', 'LA TAILLE DE LA CLÉ EST DOIT ETRE 13 CARRACTÈRES !!!\n\nTEXTE CRYPTÉ SANS LA CLÉ!!!')
                            self.textcle.delete(0, 1000)
                            self.Texteinf.configure(state=NORMAL)
                            self.Texteinf.delete(0.0, 100000000.0)
                            self.Texteinf.configure(state=DISABLED)
                        elif len(cle) < 3:
                            showinfo('ERREUR TAILLE DE LA CLÉ', 'LA TAILLE MIN DE LA CLÉ EST DE 3 CARRACTÈRES !!!\n\nTEXTE CRYPTÉ SANS LA CLÉ !!!')
                            self.textcle.delete(0, 1000)
                            self.Texteinf.configure(state=NORMAL)
                            self.Texteinf.delete(0.0, 100000000.0)
                            self.Texteinf.configure(state=DISABLED)
                        else:
                            cle = self.mpkey(cle)
                            if cle >= 1.0:
                                cle = cle - int(cle)
                        try:
                            shuffle(self.CODE, random=lambda:cle)
                            b = 1
                        except:
                            rien = ''
            else:
                if self.secrete.get() != '':
                    mp =  self.secrete.get()
                    if len(mp) > 40:
                        showinfo('ERREUR TAILLE', 'LA TAILLE MAX DE LA PHRASE SECRÈTE EST DE 40 CARRACTÈRES !!!')
                        self.secrete.delete(0, 1000)
                        self.Texteinf.configure(state=NORMAL)
                        self.Texteinf.delete(0.0, 100000000.0)
                        self.Texteinf.configure(state=DISABLED)
                    elif len(mp) <15:
                        showinfo('ERREUR TAILLE', 'LA TAILLE MIN DE LA PHRASE SECRÈTE EST DE 15 CARRACTÈRES !!!')
                        self.secrete.delete(0, 1000)
                        self.Texteinf.configure(state=NORMAL)
                        self.Texteinf.delete(0.0, 100000000.0)
                        self.Texteinf.configure(state=DISABLED)
                    else:
                        mp = self.mpkey1(mp)
                        if mp >= 1.0:
                            mp = mp - int(mp)
                    try:
                        shuffle(self.CODE, random=lambda:mp)
                        d = 1
                    except:
                        rien = ''
                        
            if self.etatAjNiveau == 1:
                if self.valeurniv.get() == 1:
                    ValNiv = self.textniv.get()
                    if ValNiv.isdigit() == False:
                        showinfo('ERREUR VALEUR', 'CARRACTÈRE APHABETIQUE NON PRIS EN CHARGE !!!')
                    elif int(ValNiv) > 10 or int(ValNiv) < 1:
                        showinfo('ERREUR NIVEAU', 'LE NIVEAU RENSEIGNÉ NON PRIS EN CHARGE !!!')
                    else:
                        for i in range(int(ValNiv)):
                            Texte = self.cryptbin(Texte)
                            c = 1

            if self.enc == 10:
                self.Texte1.configure(state=NORMAL)
                self.Texte1.delete(0.0, 1000000000000.0)
                if c == 1:
                    self.Texte1.insert(0.0, Texte)
                else:
                    self.Texte1.insert(0.0, self.cryptbin(Texte))
                self.Texte1.configure(state=DISABLED)
                
                
            elif self.enc == 20:
                with open(self.savefilecrypt + '.mrn', 'w') as f:
                    if c == 1:
                        f.write(Texte)
                        showinfo('SUCCES', 'FICHIER CRYPTÉ GENERÉ AVEC SUCCES !!!')
                    else:
                        f.write(self.cryptbin(Texte))
                        showinfo('SUCCES', 'FICHIER CRYPTÉ GENERÉ AVEC SUCCES !!!')
                        
            self.Texteinf.configure(state=NORMAL)
            self.Texteinf.delete(0.0, 10000000000.0)    
            if a == 1:
                self.Texteinf.insert(END, 'MP: %s\n' % self.mp.get())
            if b == 1:
                self.Texteinf.insert(END, 'CLE: %s\n' % self.textcle.get())
            if c == 1:
                self.Texteinf.insert(END, 'NIV: %s\n' % self.textniv.get())
            if d == 1:
                self.Texteinf.insert(END, 'PS: %s\n' % self.secrete.get())
            self.Texteinf.configure(state=DISABLED)

    def DecrypterTexte(self):
        self.TexteNonZeum = 0
        self.CODE = ['²','~','\n',' ', 'i', '\t', 'U','§','j', '[','©', '}','k', '(','P', 'l', ']','D', 'm', 'S', 'n', 'o', '-', '|', '&', 'p', 'q', 'C','{', 'a', 'b', 'c', 'd', 'e','E', 'H', 'F','_', 'é', 'ç', 'ê','ô', 'â', 'J', 'K', '8', 'L', '^', 'M', '\'', 'N','\"', 'O', 'Y', 'Z', 'f', 'g', 'h', 'r', 's', 't', 'u', 'v', 'w', 'x', '0', 'y', 'z' , '1', '2','A', '4', 'W', '5','G', '6', 'I','7', ",", '@', '!', '.', '?', ';', ':', '/', "'", '*', '+', 'T', '3', 'V', 'B', '#', 'Q', 'R', 'X', ')', 'î', '9']
        if self.enc == 10:
            Texte = self.Texte0.get(0.0, 1000000000000.0)
            Texte = Texte[:-1]
        elif self.enc == 20:
            with open(self.cryptfile, 'r') as f:
                Texte = f.read()
        for i in Texte.split('0b'):
            if i != '':
                if i.isdigit() == False:
                    self.TexteNonZeum = 1
                    break
        for i in Texte.split('0b'):
            if i != '':
                for j in i:
                    if j != '0' and j != '1':
                        self.TexteNonZeum = 1
                        break
                    
        a = 0
        b = 0
        c = 0
        if Texte == '' or Texte == '\n':
            showinfo('SAISIE VIDE', 'VEUILLEZ SAISIR LE TEXTE À DÉCRYPTER !!!')
        elif self.TexteNonZeum == 1:
            showinfo('ERREUR TEXTE CRYPTÉ', 'LE TEXTE N\'EST PAS DU TEXTE CRYPTE PAR ZEUM OU EST CORROMPU !!!')
        else:
            if self.etatAjPhraseSecrete == 0:
                if self.mp.get() != '':
                    mp = self.mp.get()
                    if len(mp) > 13:
                        showinfo('ERREUR TAILLE MOT DE PASSE', 'LA TAILLE MAX DU MOT DE PASSE EST DE 13 CARRACTÈRES !!!\n\nTEXTE CRYPTÉ SANS LE MOT DE PASSE!!!')
                        self.mp.delete(0, 1000)
                    elif len(mp) < 6:
                        showinfo('ERREUR TAILLE MOT DE PASSE', 'LA TAILLE MIN DU MOT DE PASSE EST DE 6 CARRACTÈRES !!!\n\nTEXTE CRYPTÉ SANS LE MOT DE PASSE!!!')
                        self.mp.delete(0, 1000)
                    else:
                        mp = self.mpkey(mp)
                        if mp >= 1.0:
                            mp = mp - int(mp)
                    try:
                        shuffle(self.CODE, random=lambda:mp)
                        a = 1
                    except:
                        rien = ''
                    
                if self.etatAjCle == 1:
                    if self.valeur.get() == 1:
                        cle = self.textcle.get()
                        if len(cle) > 13:
                            showinfo('ERREUR TAILLE DE LA CLÉ', 'LA TAILLE MAX DE LA CLÉ EST DE 13s CARRACTÉRES !!!\n\nTEXTE CRYPTÉ SANS LA CLÉ!!!')
                            self.textcle.delete(0, 1000)
                        elif len(cle) < 3:
                            showinfo('ERREUR TAILLE DE LA CLÉ', 'LA TAILLE MIN DE LA CLÉ EST DE 3 CARRACTÉRES !!!\n\nTEXTE CRYPTÉ SANS LA CLÉ !!!')
                            self.textcle.delete(0, 1000)
                        else:
                            cle = self.mpkey(cle)
                            if cle >= 1.0:
                                cle = cle - int(cle)
                        try:
                            shuffle(self.CODE, random=lambda:cle)
                            b = 1
                        except:
                            rien = ''
            else:
                if self.secrete.get() != '':
                    mp =  self.secrete.get()
                    if len(mp) > 40:
                        showinfo('ERREUR TAILLE', 'LA TAILLE MAX DE LA PHRASE SECRÈTE EST DE 40 CARRACTÈRES !!!')
                        self.secrete.delete(0, 1000)
                    elif len(mp) <15:
                        showinfo('ERREUR TAILLE', 'LA TAILLE MIN DE LA PHRASE SECRÈTE EST DE 15 CARRACTÈRES !!!')
                        self.secrete.delete(0, 1000)
                    else:
                        mp = self.mpkey1(mp)
                        if mp >= 1.0:
                            mp = mp - int(mp)
                    try:
                        shuffle(self.CODE, random=lambda:mp)
                        d = 1
                    except:
                        rien = ''

            if self.etatAjNiveau == 1:
                if self.valeurniv.get() == 1:
                    ValNiv = self.textniv.get()
                    if ValNiv.isdigit() == False:
                        showinfo('ERREUR VALEUR', 'CARRACTÈRE APHABETIQUE NON PRIS EN CHARGE !!!')
                    elif int(ValNiv) > 10 or int(ValNiv) < 1:
                        showinfo('ERREUR NIVEAU', 'LE NIVEAU RENSEIGNÉ NON PRIS EN CHARGE !!!')
                    else:
                        for i in range(int(ValNiv)):
                            Texte = self.decryptbin(Texte)
                            c = 1
                            
            if self.enc == 10:
                self.Texte1.configure(state=NORMAL)
                self.Texte1.delete(0.0, 10000000000.0)
                if c == 1:
                    self.Texte1.insert(0.0, Texte)
                else:
                    self.Texte1.insert(0.0, self.decryptbin(Texte))
                self.Texte1.configure(state=DISABLED)

            elif self.enc == 20:
                with open(self.savefilecrypt + '.txt', 'w') as f:
                    if c == 1:
                        f.write(Texte)
                        showinfo('SUCCES', 'FICHIER DÉCRYPTÉ GENERÉ AVEC SUCCES !!!')
                    else:
                        f.write(self.decryptbin(Texte))
                        showinfo('SUCCES', 'FICHIER DÉCRYPTÉ GENERÉ AVEC SUCCES !!!')
                

    def cryptbin (self, chaine):
        liste = list(chaine)
        IN = []
        BIN = []
        for i in liste:
            if i in self.CODE:
                ind = self.CODE.index(i)
                IN.append(ind)
        for i in IN:
            BIN.append(bin(i))
        return "".join(BIN)

    def debin(self, chaine):
        chaine = list(chaine)
        chaine.reverse()
        val = 0
        tot = 0
        for i in chaine:
            if i == '1':
                tot += 2 ** val
            val += 1
        return int(tot)

    def decryptbin(self, chaine):
        valeur = []
        liste  = []
        chaine = chaine.split('0b')
        try:
            chaine.remove('')
        except:
            zero = 0
        for i in chaine:
            valeur.append(self.debin(i))
        for i in valeur:
            liste.append(self.CODE[i])
        return "".join(liste)
    
    def mpkey(self, chaine):
        CODE = ['é', 'I', 'S', 'q', 'd', '²', '\t', '8', '"', 'h', 'w', 'A', '~', '?', 'T', 'R', 'D', 'm', '\n', 'n', 'o', '-', '|', '&', 'p', ' ', 'C', '{', 'a', 'b', 'c', 'i', 'e', 'E', 'H', 'F', '_', 'U', 'ç', 'ê', 'ô', 'â', 'J', 'K', '§', 'L', '^', 'M', "'", 'N', 'j', 'O', 'Y', 'Z', 'f', 'g', '[', 'r', 's', 't', 'u', 'v', '©', 'x', '0', 'y', 'z', '1', '2', '}', '4', 'W', '5', 'G', '6', 'k', '7', ',', '@', '!', '.', '(', ';', ':', '/', "'", '*', '+', 'P', '3', 'V', 'B', '#', 'Q', 'l', 'X', ')', 'î', '9', ']']
        Val = []
        chaine = list(chaine)
        for i in chaine:
            if i in CODE:
                Val.append(str(CODE.index(i)))
        Val = ''.join(Val)
        Val = int(Val)
        return Val / 1000000000000

    def mpkey1(self, chaine):
        CODE1 = ['é', 'I', 'S', 'q', 'd', '²', '\t', '8', '"', 'h', 'w', 'A', '~', '?', 'T', 'R', 'D', 'm', '\n', 'n', 'o', '-', '|', '&', 'p', ' ', 'C', '{', 'a', 'b', 'c', 'i', 'e', 'E', 'H', 'F', '_', 'U', 'ç', 'ê', 'ô', 'â', 'J', 'K', '§', 'L', '^', 'M', "'", 'N', 'j', 'O', 'Y', 'Z', 'f', 'g', '[', 'r', 's', 't', 'u', 'v', '©', 'x', '0', 'y', 'z', '1', '2', '}', '4', 'W', '5', 'G', '6', 'k', '7', ',', '@', '!', '.', '(', ';', ':', '/', "'", '*', '+', 'P', '3', 'V', 'B', '#', 'Q', 'l', 'X', ')', 'î', '9', ']']
        Val = []
        chaine = list(chaine)
        for i in chaine:
            if i in CODE1:
                Val.append(str(CODE1.index(i)))
        Val = ''.join(Val)
        Val = int(Val)
        return Val / 10000000000000000000000000000000
    
class Marquee(Canvas):
    def __init__(self, parent, text, margin=2, borderwidth=1, relief='flat', fps=30):
        Canvas.__init__(self, parent, borderwidth=borderwidth, relief=relief)
        self.fps = fps

        text = self.create_text(0, -1000, text=text,font='calibri 14 bold italic', anchor="w", tags=("text",))
        (x0, y0, x1, y1) = self.bbox("text")
        width = (x1 - x0) + (2*margin) + (2*borderwidth)
        height = (y1 - y0) + (2*margin) + (2*borderwidth)
        self.configure(width=width, height=height)

        self.animate()
        
    def animate(self):
        (x0, y0, x1, y1) = self.bbox("text")
        if x1 < 0 or y0 < 0:
            x0 = self.winfo_width()
            y0 = int(self.winfo_height()/2)
            self.coords("text", x0, y0)
        else:
            self.move("text", -3, 0)

        self.after_id = self.after(int(1000/self.fps), self.animate)


Fenetre = Zeum() 
