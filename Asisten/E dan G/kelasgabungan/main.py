class Balok:

    def __init__(self, panjang, lebar, tinggi):
        self.p = panjang
        self.l = lebar
        self.t = tinggi


    def volume(self):
        vol = self.p * self.l * self.t
        return vol

bidang1 = Balok(2,3,4)
bidang2 = Balok(5,6,7)

data = [
    [5,6,7],
    [1,2,3],
    [10,11,12]
]

for i in data:
    bidang = Balok(i[0], i[1], i[2])
    print("Panjang ", bidang.p, "lebar ", bidang.l, "tinggi ", bidang.t)

print(bidang1.__dict__)
print(bidang2.__dict__)

#print(bidang1.volume())
#print(bidang1.l,bidang1.p)
#print("======================")
#volhasil = Balok(5,6,7).volume()
#print(volhasil)