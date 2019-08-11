Ideje

Message_box Tkinter:
def prvo_obvestilo(naslov, vsebina):
    okence = tkinter.Tk()
    okence.withdraw()
    messagebox.showinfo("Pozdravljeni!", "Kviz se začenja!")
    okence.mainloop()

Ideja celotne igre: 

def igra():
    tocke = 0
    odgovorjenih = 0
    while odgovorjenih < 7:
        for vprasanje iz random uprasanje: 
            prikazi_vprasanje(vprasanja)

            v prikazi_vprasanje funkcijo je treba vkljuci se 4 gumbe 
            for event in mousedown bla bla:
                ce gumb zadane okno 
                odgovorjenih += 1
                preveri_odgovor()
                if odgovor je true:
                        tocke += 1
    rezultat()

#### Začetni meni deluje ####

Na začetku uporabnik izbere Začni ali Izhod 
Nato sledijo vprašanja: 
X vprašanj, z možnim odgovorom Da / NE ali pa možnostjo Nasledno vprašanje. 
To je enkratni bonus, torej lahko igrlec eno vprašanje zamenja. 

Vprašanja bodo dana v slovarju, ključ bo vprsšanje, vrednost pa Da / ne 
za vsak klik z misko program preveri na katerem gumbu se je kliknilo in nato naredi primerno akcijo. 
Ce kliknes na gumb naslednje vprasanje a si bonus ze izkoristil, se izpise Erroor tkinter sporocilo.

Na koncu, po zadnjem (X) vprasanju se izpisejo tocke. 