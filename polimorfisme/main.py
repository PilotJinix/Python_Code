## Overriding
# class Person:
#     def __init__(self, name, age):
#         self.nama = name
#         self.umur = age
#
#     def show(self):
#         return "Nama {}\nUmur {}".format(self.nama,self.umur)
#
#
# class Mahasiswa(Person):
#     def __init__(self, name, age, nim):
#         super().__init__(name, age)
#         self.nim = nim
#
#     def show(self):
#         return "Nama {}\nUmur {}\nNim {}".format(self.nama, self.umur, self.nim)
#
#
# # orang = Person(input("Masukkan Nama : "), input("Masukkan Umur :"))
# orang1 = Mahasiswa(input("Masukkan Nama : "), input("Masukkan Umur :"), input("Masukkan Nim :"))
#
# print(orang1.show())


# Overloding
class Kalkulate:

    def mennghitung (X=None, Y=None, Z=None):
        result= 0
        if (X!=None and Y!=None and Z!=None ):
            result = X + Y + Z
        elif (X!=None and Y!=None):
            result = X + Y
        elif(X!=None):
            result = X
        else:
            print("Butuh P")
        return result

print(Kalkulate.mennghitung(1,2))


