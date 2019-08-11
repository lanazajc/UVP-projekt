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

def rezultat():
    zacetni_pozdrav("Čestitamo! Dosegli ste {} točk".format(tocke))
