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
    def __init__(self,name, brand , tampung, ban):
        super().__init__(name,brand)
        self.__dayatampung = tampung
        self.__roda = ban

    @property
    def view(self):
        return "Nama = {} \n\t Merk = {} \n\t Daya Tampung = {} \n\t Jumlah Roda = {} ".format(self.getnama,self.getmerk,self.getdayatampung,self.getroda)

    @property
    def setdayatampung(self):
        pass

    @property
    def getdayatampung(self):
        pass

    @property
    def setroda(self):
        pass

    @property
    def getroda(self):
        pass

    @setdayatampung.setter
    def setdayatampung(self, value):
        self.__dayatampung = value

    @getdayatampung.getter
    def getdayatampung(self):
        return self.__dayatampung

    @setroda.setter
    def setroda(self, value):
        self.__roda = value

    @getroda.getter
    def getroda(self):
        return self.__roda

truck1=Truck("Hino","toyota",3000,6)
print(truck1.view)
print("==============================")
truck1.setnama = input("Masukkan nama untuk diperbarui = ")
truck1.setmerk = input("Masukkan merk untuk diperbarui = ")
truck1.setdayatampung = int(input("Masukkan daya tampung untuk diperbarui = "))
truck1.setroda = int(input("Masukkan Jumlah roda untuk diperbarui = "))
print(truck1.view)
