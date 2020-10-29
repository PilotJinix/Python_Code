class Manusia:

    def __init__(self, name, Gender):
        self.__nama = name
        self.__gender = Gender


    @property
    def info(self):
        return "Nama = {} \n\t darah = {}".format(self.__nama,self.__gender)

    @property
    def setnama(self):
        pass

    @property
    def getnama(self):
        pass

    @property
    def setgender(self):
        pass

    @property
    def getgender(self):
        pass

    @getnama.getter
    def getnama(self):
        return self.__nama

    @setnama.setter
    def setnama(self,value):
        self.__nama = value


    @getgender.getter
    def getgender(self):
        return self.__gender

    @setgender.setter
    def setgender(self,value):
        self.__gender = value


orang = Manusia("lina","Perempuan")
print(orang.info)
orang.setnama =input("Masukkan nama untuk memperbarui = ")
orang.setgender =input("Masukkan nama untuk memperbarui = ")
print(orang.getnama)
print(orang.getgender)
print("Info setelah diubah \n", orang.info)




