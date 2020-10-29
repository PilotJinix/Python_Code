#import tkinter
#main_window = tkinter.Tk()
#label1=tkinter.Button(main_window, text ="label1")
#label1.pack()
#main_window.mainloop()

class Tumbuhan:
    #class variabel
    jumlah  = 0

    def __init__(self, Iname, Ihealth, IAttpower, IArmor):
        self.name = Iname
        self.health = Ihealth
        self.Attpower = IAttpower
        self.Armor = IArmor
        Tumbuhan.jumlah += 1
        print(Tumbuhan.jumlah)

    #method
    #def nama(self):
    #   print("Jenis tumbuhan " + self.name)
    #def tambahdarah(self, tambah):
    #   self.health += tambah
    #def gettambah(self):
    #   return self.health

    def serang(self, penyerang):
        print(self.name + " Menyerang " + penyerang.name)
        penyerang.diserang(self, self.Attpower)


    def diserang(self, penyerang, kekuatan):
        print(self.name + " Diserang oleh " + penyerang.name)
        self.health -= kekuatan + self.Armor

tumbuhan1 = Tumbuhan("Tumbuhan 1", 100, 10, 2)
tumbuhan2 = Tumbuhan("Tumbuhan 2", 110, 9, 2)

tumbuhan1.serang(tumbuhan2)
print(tumbuhan2.__dict__)







