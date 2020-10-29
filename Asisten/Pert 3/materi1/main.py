class Arisan:

    jenis = "PKK "
    jumlah = 0

# y = chinta
# x = y

    def __init__(self, name, age, address):
        self.nama = name
        self.umur = age
        self.alamat = address
        Arisan.jumlah+=1

    def info(self):
        return "Nama = {} \n\t Umur = {}\n\t Alamat = {}".format(self.nama,self.umur,self.alamat)

orang1 = Arisan("Chinta", 19, "Jember")
orang2 = Arisan("yoppy", 19, "kediri")

print(orang1.__dict__)
print("===========================")
print("Nama cewe itu : ", orang1.nama)
# print(orang1.alamat)
# print("===========================")
# print(Arisan.jumlah)
print("===========================")
print(orang1.info())