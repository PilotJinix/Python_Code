class Kendaraan:

    def __init__(self, name, brand):
        self.__nama = name
        self.__merk = brand

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
        self.__nama = value

    @getnama.getter
    def getnama(self):
        return self.__nama

    @setmerk.setter
    def setmerk(self, value):
        self.__merk = value

    @getmerk.getter
    def getmerk(self):
        return self.__merk

class Truck(Kendaraan):

    def __init__(self, name,brand, dayatampung, ban):
        super().__init__(name, brand)
        self.__muatan = dayatampung
        self.__roda = ban

    @property
    def setmuatan(self):
        pass

    @property
    def getmuatan(self):
        pass

    @property
    def setroda(self):
        pass

    @property
    def getroda(self):
        pass

    @setmuatan.setter
    def setmuatan(self, value):
        self.__muatan = value

    @getmuatan.getter
    def getmuatan(self):
        return self.__muatan

    @setroda.setter
    def setroda(self, value):
        self.__roda = value

    @getroda.getter
    def getroda(self):
        return self.__roda



truck1 = Truck("Tayo", "Toyota", 30000, 6)
print(truck1.__dict__)
print("==============================")
truck1.setnama = input("Masukkan nama untuk diperbarui = ")
truck1.setmerk = input("Masukkan merk untuk diperbarui = ")
truck1.setmuatan = int(input("Masukkan jumlah muatan untuk diperbarui = "))
truck1.setroda = int(input("Masukkan jumlah roda untuk diperbarui = "))
print("==============================")
print(truck1.__dict__)

# class Hewan:
#     '''Hewan adalah class induk/ parent'''
#     def __init__(self, nama, jenis_hewan):
#         self.nama        = nama
#         self.jenis_hewan = jenis_hewan
#
#     def info(self):
#         print("Nama :", self.nama)
#         print("Motif :", self.motif)
#
# class Kucing(Hewan):
#     '''Kucing adalah class anak dari hewan'''
#     jumlah_kaki = 4
#     jumlah      = 0
#
#     def __init__(self, nama, motif, suara = "Miaw"):
#         super().__init__(nama)
#         self.motif       = motif
#         self.suara       = suara
#         Kucing.jumlah   += 1
#
#     def populasi(self):
#         return Kucing.jumlah
#
#     def bunyi(self):
#         print("Bunyi kucing:", self.jumlah)
#
#
#
# pet1 = Kucing("Tororo", "Kuning", "guk guk")
# pet2 = Kucing("Hijiki", "Belang Telon")
