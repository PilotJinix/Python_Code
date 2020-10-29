class Kendaraan:

    jumlah = 0

    def __init__(self, name, brand):
        self.__mana = name
        self.__merk = brand
        Kendaraan.jumlah +=1


    @property
    def setnama(self):
        pass

    @property
    def getnama(self):
        pass

    @property
    def setmerk(self):
        pass

    @property
    def getmerk(self):
        pass

    @setnama.setter
    def setnama(self, value):
        self.__mana = value

    @getnama.getter
    def getnama(self):
        return self.__mana

    @setmerk.setter
    def setmerk(self, value):
        self.__merk = value

    @getmerk.getter
    def getmerk(self):
        return self.__merk

    def hitungjumlah(self):
        return Kendaraan.jumlah



mobil1 = Kendaraan("Tayo", "Hino")
mobil2 = Kendaraan("Mater", "Bmw")
mobil3 = Kendaraan("muklis", "Toyota")

print(mobil1.__dict__)
print("===================")
mobil1.setnama = input("Masukkan nama yang ingin diperbarui = ")
mobil1.setmerk = input("Masukkan merk yang ingin diperbarui = ")
print("===================")
print(mobil1.__dict__)
print("===================")
print(mobil1.hitungjumlah())

