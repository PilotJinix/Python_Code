class kesehatan:

    def __init__(self, name, age, tb, bb):
        self.nama = name
        self.umur = age
        self.tinggibadan = tb
        self.beratbadan = bb

    def datadiri(self):
        return "Nama Pasien {}\n\t Umur pasien = {}\n\t Tinggi Badan = {}\n\t Berat Badan Pasien = {}  ".format(self.nama,self.umur,self.tinggibadan,self.beratbadan)
        #print("Nama pasien = " +self.nama+ " Umur pasien = " +self.umur+ " Tinggi Badan = "+self.tinggibadan+ " Berat Badan = "+self.beratbadan+)

    def cekkesehatan(self):
        ideal = self.tinggibadan - 110
        if (self.beratbadan <= ideal):
            print("Kurus")
        elif(self.beratbadan > ideal):
            print("Gemuk")
        else:
            print("Anda Ideal")

        return ideal

manusia1 = kesehatan("Agung", 20, 180, 80)
manusia2 = kesehatan("Iqbal", 21, 160, 30)

print(manusia1.cekkesehatan())