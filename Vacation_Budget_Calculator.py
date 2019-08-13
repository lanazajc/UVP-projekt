## Vacation Budget calculator ##
import tkinter as tk

class Budget(object):

    def __init__(self, strosek):
        self.strosek = strosek

        self.text_nocitve = tk.Label(root, text="Število nočitev")
        self.text_nocitve.place(x = 20, y = 50)
        self.text_nocitve.config(font=("Courier", 15))

        self.okno_nocitve = tk.Entry(root, width = 10)
        self.okno_nocitve.place(x = 270, y = 55)
        self.okno_nocitve.insert(0, "0")

        self.text_osebe = tk.Label(root, text="Število oseb")
        self.text_osebe.place(x = 20, y = 100)
        self.text_osebe.config(font=("Courier", 15))

        self.okno_osebe = tk.Entry(root, width = 10)
        self.okno_osebe.place(x = 270, y = 105)
        self.okno_osebe.insert(0, "0")

        self.text_prevoz = tk.Label(root, text="Pričakovan strošek prevoza")
        self.text_prevoz.place(x = 20, y = 150)
        self.text_prevoz.config(font=("Courier", 15))

        self.okno_prevoz = tk.Entry(root, width = 10)
        self.okno_prevoz.place(x = 400, y = 160)
        self.okno_prevoz.insert(0, "0")

        self.text_str_nocive = tk.Label(root, text="Povprečen strošek nočitve")
        self.text_str_nocive.place(x = 20, y = 200)
        self.text_str_nocive.config(font=("Courier", 15))

        self.okno_str_nocitve = tk.Entry(root, width = 10)
        self.okno_str_nocitve.place(x = 400, y = 205)
        self.okno_str_nocitve.insert(0, "0")

        self.text_hrana_pijača = tk.Label(root, text="Dnevni strošek hrane in pijače na osebo")
        self.text_hrana_pijača.place(x = 20, y = 250)
        self.text_hrana_pijača.config(font=("Courier", 15))
        
        self.okno_hrana_pijača = tk.Entry(root, width = 10)
        self.okno_hrana_pijača.place(x = 520, y = 255)
        self.okno_hrana_pijača.insert(0, "0")

        self.okno_fiksno_str = tk.Label(root, text='None')
        self.okno_fiksno_str.place(x= 700,  y = 500)


    def izračun_fiksni_stroški():
        self.fiksni_stroški = int(self.okno_nocitve.get()) * int(self.okno_str_nocitve.get())

        self.okno_fiksno_str = tk.Label(root, text=str(self.fiksni_stroški))
        self.okno_fiksno_str.place(x= 700,  y = 500)


    def pretvori_v_valuto():
        pass

root = tk.Tk()
root.title("Stroškovnik dopusta")
stroškovnik = Budget(root)
root.geometry("800x600")
root.after(100, stroškovnik.izračun_fiksni_stroški)
root.mainloop()
