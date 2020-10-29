class Person:

    def __init__(self, name, age, gender, tb, bb):
        self.nama = name
        self.umur = age
        self.kelamin = gender
        self.tinggibadan = tb
        self.beratbadan = bb


    def datadiri(self):
        return "Nama Pasien {} \n\t Umur Pasien = {} \n\t Jenis Kelamin = {}" .format(self.nama,self.umur,self.kelamin)

    def cekideal(self):
        ideal = self.tinggibadan - 110
        if (self.beratbadan < ideal):
            print("Kamu Kurus")
        elif(self.beratbadan == ideal):
            print("Kamu Ideal")
        else:
            print("Kamu Gemuks")
        return "Karena berat badanmu = {}".format(ideal)

manusia1 = Person("Agung",20,"Male",180,70)
manusia2 = Person("Ivan",5,"Male",160,70)

print(manusia1.datadiri())
print(manusia1.cekideal())