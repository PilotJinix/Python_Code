class Kendaraan:
    def __init__(self, name, brand, color):
        self.__nama = name
        self.__merk = brand
        self.__warna = color

    @property
    def setnama(self):
        pass

    @property
    def getnama(self):
        pass

    @setnama.setter
    def setnama(self, value):
        self.__nama = value

    @getnama.getter
    def getnama(self):
        return self.__nama

mobil1 = Kendaraan("Tayo", "Hino", "Biru" )
print(mobil1.__dict__)
mobil1.setnama= input("Masukkan data = ")
print(mobil1.__dict__)


# print(mobil1.getnama)
# mobil1.nama = "Rogy"
# print("=======================================")
# print(mobil1.__dict__)


