## Vacation Budget calculator ##
import tkinter as tk
from tkinter import *

class Budget(object):

    def __init__(self, strosek):

        Label(root, text= "Število nočitev").grid(row = 1, column = 1, sticky = W)
      
        Label(root, text = "Število oseb").grid(row=2, column = 1, sticky = W)

        Label(root, text = "Pričakovan strošek prevoza").grid(row = 3, column = 1, sticky = W)

        Label(root, text = "Povprečen strošek nočitve").grid(row = 4, column = 1, sticky = W)

        Label(root, text = "Dnevni strošek hrane in pijače na osebo").grid(row = 5, column = 1, sticky = W)

        Label(root, text = "Dnevni strošek ogledov, atrakcij, ...").grid(row = 6, column = 1, sticky = W)

        self.stevilo_nocitev = IntVar()
        self.stevilo_oseb = IntVar()
        self.prevoz = DoubleVar()
        self.nocitev = DoubleVar()
        self.hrana_pijaca = DoubleVar()
        self.ogledi = DoubleVar()
        self.skupni_stroski = StringVar()
        self.ostali_stroski = StringVar()
        self.prevoz_nastanitev = StringVar()

        Entry(root, textvariable= self.stevilo_nocitev).grid(row = 1, column = 2)
        Entry(root, textvariable = self.stevilo_oseb).grid(row = 2, column = 2)
        Entry(root, textvariable= self.prevoz).grid(row = 3, column = 2)
        Entry(root, textvariable = self.nocitev).grid(row = 4, column = 2)
        Entry(root, textvariable= self.hrana_pijaca).grid(row = 5, column = 2)
        Entry(root, textvariable = self.ogledi).grid(row = 6, column = 2)

        izracun = Button(text = "Izračunaj", command = self.izracun_skupni_stroški).grid(row = 7, column = 2)

        Label(root, text = "Skupni strošek").grid(row = 8, column = 1, sticky = E)
        Label(root, text = "od tega prevoz in nastanitev").grid(row = 9, column = 1, sticky = E)
        Label(root, text = "ostali stroški").grid(row = 10, column = 1, sticky = E)

        skupnistroski = Label(root, textvariable = self.skupni_stroski).grid(row = 8, column = 2, sticky = E)
        prevoznastanitev = Label(root, textvariable = self.prevoz_nastanitev).grid(row = 9, column = 2, sticky = E)
        ostalistroski = Label(root, textvariable = self.ostali_stroski).grid(row = 10, column = 2, sticky = E)


    def izračun_ostali_stroški(self, osebe, hrana_in_pijaca, ogledi, dnevi):
        ostalistroski = osebe * (hrana_in_pijaca + ogledi) * dnevi
        return ostalistroski
  
  
    def izračun_prevoz_in_nastanitve(self, st_nocitev, str_nocitev, prevoz):
        prevoznastanitev = (st_nocitev * str_nocitev) + prevoz
        return prevoznastanitev
 
    def izracun_skupni_stroški(self):
        prevoznastanitev = self.izračun_prevoz_in_nastanitve(self.stevilo_nocitev.get(),self.nocitev.get(),self.prevoz.get())
        ostalistroski = self.izračun_ostali_stroški(self.stevilo_oseb.get(), self.hrana_pijaca.get(), self.ogledi.get(), self.stevilo_nocitev.get() + 1 )

        skupnistroski = prevoznastanitev + ostalistroski 

        self.skupni_stroski.set(skupnistroski)
        
        self.prevoz_nastanitev.set(prevoznastanitev)

        self.ostali_stroski.set(ostalistroski)

        
    


    




root = tk.Tk()
root.title("Stroškovnik dopusta")
stroškovnik = Budget(root)
#root.geometry("800x600")
root.mainloop()
