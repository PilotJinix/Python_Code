class Sekolah:
    def __init__(self, schoolname, address):
        self.__namasekolah =  schoolname
        self.__alamat =  address

    @property
    def setalamat(self):
        pass

    @property
    def getalamat(self):
        pass

    @setalamat.setter
    def setalamat(self, input):
        self.__alamat = input

    @getalamat.getter
    def getalamat(self):
        return self.__alamat


    def setnamasekolah(self, bebas):
        self.__namasekolah = bebas

    def getnamasekolah(self):
        return self.__namasekolah

    def showsekolah(self):
        return "Sekolah = {} \nAlamat = {}".format(self.getnamasekolah(), self.getalamat)




# data = [Sekolah("SMA 1 PONROG", "PONROG"),Sekolah("SMA 2 PONROG", "PONROG 2")]
#
# for i in data :
#     print(i.showall())

# print()
# print(sekolah1.showall())


class Siswa(Sekolah):
    def __init__(self, schoolname, address, studentname, classname):
        super().__init__(schoolname, address)
        self.namasiswa = studentname
        self.namakelas = classname

    def showall(self):
        return "Data siswa \n\nNama Siswa : {}\nNama Kelas : {}\n{}".format(self.namasiswa, self.namakelas, self.showsekolah())


siswa1 = Siswa("SMA 1 ARJASA", "ARJASA", "IQBAL", "IPS 1")

sekolah1 = Sekolah("SMA 1 PATRANG", "Patrang")

print(siswa1.showall())

