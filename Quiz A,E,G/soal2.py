class Mahasiswa:
    def __init__(self, nama, nim, ipk, ukt):
        self.__nama = nama
        self.__nim = nim
        self.__ipk = ipk
        self.__ukt = ukt

    def set_nama(self, nama):
        self.__nama = nama

    def get_nama(self):
        return self.__nama

    def set_nim(self, nim):
        self.__nim = nim

    def get_nim(self):
        return self.__nim

    def set_ipk(self, ipk):
        self.__ipk = ipk

    def get_ipk(self):
        return self.__ipk

    def set_ukt(self, ukt):
        self.__ukt = ukt

    def get_ukt(self):
        return self.__ukt


daftarMahasiswa = [
    Mahasiswa("Agung", 182410103001, 3.7, 9000000),
    Mahasiswa("Dida", 182410102001, 3.4, 1000000),
    Mahasiswa("Dewangga", 182410103005, 3.0, 2500000)
]

def searchMahasiswaByNim(nim):
    for mahasiswa in daftarMahasiswa:
        if mahasiswa.get_nim() == nim:
            return mahasiswa

print("Masukkan NIM Mahasiswa: ")
mahasiswa = searchMahasiswaByNim(int(input()))

print(mahasiswa.get_nama())
print(mahasiswa.get_nim())
print(mahasiswa.get_ipk())
print(mahasiswa.get_ukt())

if (mahasiswa.get_ipk() >= 3.5):
    print('kamu memenuhi kualifikasi')
elif (mahasiswa.get_ipk() < 3.5):
    if mahasiswa.get_ukt() > 4000000:
        print("maaf kamu tidak memenuhi kualifikasi")
    else:
        print('kamu memenuhi kualifikasi')
else:
    print("maaf kamu tidak memenuhi kualifikasi")
