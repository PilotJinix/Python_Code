class balok:

    def __init__(self, panjang, lebar, tinggi):
        self.p = panjang
        self.l = lebar
        self.t = tinggi

    def volume(self):
        vol=self.p * self.l * self.t
        return vol

    def keliling(self):
        kell = 4 * ( self.p + self.l + self.t)
        return kell

    def luas(self):
        luassss = 2*((self.p * self.l) + (self.l * self.t) + (self.t * self.p) )
        return luassss

balok1 = balok(2,3,4)
balok2 = balok(5,6,7)

print("================")
print("cek aja ")
hasil = balok1.volume()
print("hasil = " , hasil)
print("================")
print("cek masuk")
hasil = balok(9,9,9).volume()
print("hasil = " , hasil)
print("================")

print("Volume Balok 1")
print(balok1.volume())
print("================")
print("Keliling Balok 1")
print(balok1.keliling())
print("================")
print("luas Balok 1")
print(balok1.luas())

