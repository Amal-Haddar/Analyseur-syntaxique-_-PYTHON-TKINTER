from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import tkinter as tk

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem.snowball import FrenchStemmer

tokenizer = nltk.RegexpTokenizer(r'\w+')

class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title("Amal Haddar 2ING2 - Analyseur")
        self.minsize(640, 400)

        self.labelFrame = ttk.LabelFrame(self, text = "Choisir le document à traiter et la langue source")
        self.labelFrame.grid(column = 0, row = 1, padx = 20, pady = 20)

        
    #Bouton ouverture fichier
        self.button()

        

        w = tk.Label(self, text="Bienvenu !")
        w.grid(column = 0, row = 0, padx = 50, pady = 10)

        

        self.buttonFR()
        
        self.buttonExtraction()
        self.buttonElagage()
        self.buttonNormalisation()

        self.buttonAutreLangue()
                
        self.buttonExtractionAng()
        self.buttonElagageAng()
        self.buttonNormalisationAng()

    def button(self):
        self.button = ttk.Button(self.labelFrame, text = "Ouvrir fichier", command = self.fileDialog)
        self.button.grid(column = 1, row = 1)


    def fileDialog(self):
        self.filename = filedialog.askopenfilename(initialdir = "/", title = "Choisir document", filetype = (( "Fichiers text", "*.txt") , ("All Files","*.*")))
        self.label = ttk.Label(self.labelFrame, text = "")
        self.label.grid(column =1, row = 2)
        self.label.configure(text = self.filename)

    def buttonFR(self):
        self.button = ttk.Button(self.labelFrame, text = "Langue Française : ", width=30)
        self.button.grid(column = 1, row = 8)

    def buttonExtraction(self):
        self.button = ttk.Button(self.labelFrame, text = "Extraction", command = self.extraction)
        self.button.grid(column = 4, row = 8)

    def buttonElagage(self):
        self.button = ttk.Button(self.labelFrame, text = "Elagage", command = self.elagageFR)
        self.button.grid(column = 5, row = 8)

    def buttonNormalisation(self):
        self.button = ttk.Button(self.labelFrame, text = "Stemming", command = self.stemmingFR)
        self.button.grid(column = 6, row = 8)

    def buttonAutreLangue(self):
        self.button = ttk.Button(self.labelFrame, text = "Autre Langue : ", width=30)
        self.button.grid(column = 1, row = 11)

    def buttonExtractionAng(self):
        self.button = ttk.Button(self.labelFrame, text = "Extraction", command = self.extraction)
        self.button.grid(column = 4, row = 11)

    def buttonElagageAng(self):
        self.button = ttk.Button(self.labelFrame, text = "Elagage", command = self.elagageAutreLangue)
        self.button.grid(column = 5, row = 11)

    def buttonNormalisationAng(self):
        self.button = ttk.Button(self.labelFrame, text = "Stemming", command = self.StemmingAutreLangue)
        self.button.grid(column = 6, row = 11)


        
    #Extraction fr + autre langue
    def extraction(self):

        #Input Document
        Input = open(self.filename, "r")
        #Output Document
        Output = open(self.filename+"-out1.txt", "a")

        Text = Input.read()

        #Extraction
        for i in tokenizer.tokenize(Text):
            Output.write(i)
            Output.write("\n")
        
        self.label.configure(text = self.filename)    
        self.texte = Entry(self, width =20, font ="Arial 14", fg="green",  justify='center')
        self.texte.insert(END, "Succée d'extraction" )
        self.texte.grid(padx =16, pady =16)

        self.texte = Entry(self, width =70, font ="Arial 14", fg="blue", justify='center')
        self.texte.insert(END, "Vous trouvez votre fichier résulat sous le même répertoire du fichier source" )
        self.texte.grid(padx =16, pady =16)

    #Elagage Fr
    def elagageFR(self):

        #stopwords file
        stop = open("stopwords.txt", "r")
        stop_word = stop.read()

        #Input Document
        Input = open(self.filename, "r")
        extraction = Input.read()

        #Output Document
        Output = open(self.filename+"-out2.txt", "a")

        #Elagage
        for w in extraction.split():
            if w.lower() not in stop_word:
                Output.write(w)
                Output.write("\n")
                
        stop.close()
        Input.close()
        Output.close()

        self.label.configure(text = self.filename)    
        self.texte = Entry(self, width =20, font ="Arial 14", fg="green",  justify='center')
        self.texte.insert(END, "Succée d'elagage" )
        self.texte.grid(padx =16, pady =16)

        self.texte = Entry(self, width =50, font ="Arial 14", fg="blue", justify='center')
        self.texte.insert(END, "Vous trouvez votre fichier résulat sous le même répertoire" )
        self.texte.grid(padx =16, pady =16)
    
    #Stemming avec FrenshStemmer
    def stemmingFR(self):

        ps= FrenchStemmer()
        #Input Document
        Input = open(self.filename, "r")
        elagage = Input.read()

        #Output Document
        Output = open(self.filename+"-out3.txt", "a")


        #Stemming
        for w in elagage.split():
            Output.write(ps.stem(w))
            Output.write("\n")

        self.label.configure(text = self.filename)    
        self.texte = Entry(self, width =20, font ="Arial 14", fg="green",  justify='center')
        self.texte.insert(END, "Succée de Stemming" )
        self.texte.grid(padx =16, pady =16)

        self.texte = Entry(self, width =50, font ="Arial 14", fg="blue", justify='center')
        self.texte.insert(END, "Vous trouvez votre fichier résulat sous le même répertoire" )
        self.texte.grid(padx =16, pady =16)

  #Elagage en Anglais
    def elagageAutreLangue(self):

        #On peut changer la liste des stopwords
        stop_words = set(stopwords.words("english"))
        print(stop_words)

        #Input Document
        Input = open(self.filename, "r")
        extraction = Input.read()

        #Output Document
        Output = open(self.filename+"-out2.txt", "a")


        #Elagage
        for w in extraction.split():
            if w.lower() not in stop_words:
                Output.write(w)
                Output.write("\n")
        
        Input.close()
        Output.close()

        self.label.configure(text = self.filename)    
        self.texte = Entry(self, width =20, font ="Arial 14", fg="green",  justify='center')
        self.texte.insert(END, "Succée d'elagage" )
        self.texte.grid(padx =16, pady =16)

        self.texte = Entry(self, width =50, font ="Arial 14", fg="blue", justify='center')
        self.texte.insert(END, "Vous trouvez votre fichier résulat sous le même répertoire" )
        self.texte.grid(padx =16, pady =16)

    #Stemming Anglais
    def StemmingAutreLangue(self):

        ps = PorterStemmer()
        #Input Document
        Input = open(self.filename, "r")
        elagage = Input.read()

        #Output Document
        Output = open(self.filename+"-out3.txt", "a")


        #Stemming
        for w in elagage.split():
            Output.write(ps.stem(w))
            Output.write("\n")


        self.label.configure(text = self.filename)    
        self.texte = Entry(self, width =20, font ="Arial 14", fg="green",  justify='center')
        self.texte.insert(END, "Succée de Stemming" )
        self.texte.grid(padx =16, pady =16)

        self.texte = Entry(self, width =50, font ="Arial 14", fg="blue", justify='center')
        self.texte.insert(END, "Vous trouvez votre fichier résulat sous le même répertoire" )
        self.texte.grid(padx =16, pady =16)

        


        
            
if __name__ == '__main__':
    root = Root()
    root.mainloop()
