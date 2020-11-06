class Barang:
    def __init__(self, namaBarang, hargaBarang):
        self.namaBarang = namaBarang
        self.hargaBarang = hargaBarang


class Toko:
    def __init__(self, namaToko, jumlahKaryawan, jamBuka, jamTutup, daftarBarang):
        self.__namaToko = namaToko
        self.__jumlahKaryawan = jumlahKaryawan
        self.__jamBuka = jamBuka
        self.__jamTutup = jamTutup
        self.__daftarBarang = daftarBarang

    def get_namaToko(self):
        return self.__namaToko

    def set_namaToko(self, namaToko):
        self.__namaToko = namaToko

    def get_jumlahKaryawan(self):
        return self.__jumlahKaryawan

    def set_jumlahKaryawan(self, jumlahKaryawan):
        self.__jumlahKaryawan = jumlahKaryawan

    def get_jamBuka(self):
        return self.__jamBuka

    def set_jamBuka(self, jamBuka):
        self.__jamBuka = jamBuka

    def get_jamTutup(self):
        return self.__jamTutup

    def set_jamTutup(self, jamTutup):
        self.__jamTutup = jamTutup

    def get_daftarBarang(self):
        return self.__daftarBarang

    def set_daftarBarang(self, daftarBarang):
        self.__daftarBarang = daftarBarang

    def tambahkanBarang(self, barang):
        self.__daftarBarang.append(barang)

    def kurangiBarang(self, indexBarang):
        self.__daftarBarang.pop(indexBarang)


# test
barangToko1 = [Barang("sepatu x", 5000), Barang("sepatu y", 7000)]
toko1 = Toko("Toko saya", 10, 9, 20, barangToko1)

print(toko1.get_namaToko())
for i in range(len(toko1.get_daftarBarang())):
    print(i, toko1.get_daftarBarang()[i].namaBarang, toko1.get_daftarBarang()[i].hargaBarang)
# end test

# main
daftarToko = [toko1]


def cekToko(indexToko):
    print("Nama Toko: ", daftarToko[indexToko].get_namaToko())
    print("Jumlah Karyawan: ", daftarToko[indexToko].get_jumlahKaryawan())
    print("Jam Buka: ", daftarToko[indexToko].get_jamBuka())
    print("Jam Tutup: ", daftarToko[indexToko].get_jamTutup())
    daftarBarang = daftarToko[indexToko].get_daftarBarang()
    print("Daftar Barang: ")

    index = 0;
    for barang in daftarBarang:
        print(index, barang.namaBarang, barang.hargaBarang)
        index += 1
    # for i in range (len(daftarNamaBarang)):
    #     print(i, daftarNamaBarang[i], daftarHargaBarang[i])


def cekSemuaToko():
    for i in range(len(daftarToko)):
        print("Index Toko: ", i)
        cekToko(i)


def tambahToko(tokoBaru):
    daftarToko.append(tokoBaru)


def kurangiToko(indexToko):
    daftarToko.remove(indexToko)


def tambahkanBarangToko(indexToko, barang):
    daftarToko[indexToko].tambahkanBarang(barang)


def kurangiBarangToko(indexToko, indexBarang):
    daftarToko[indexToko].kurangiBarang(indexBarang)


def cekBarangToko(indexToko):
    for i in range(len(daftarToko[indexToko].get_daftarBarang())):
        print(i, daftarToko[indexToko].get_daftarBarang()[i].namaBarang,
              daftarToko[indexToko].get_daftarBarang()[i].hargaBarang)


def buatDaftarBarang():
    daftarBarang = []
    while True:
        daftarBarang.append(Barang(
            input("Masukkan nama Barang: "),
            int(input("Masukkan harga barang: "))
        ))
        if (input("Apakah ingin menambahkan barang lagi? [Y/N]: ").lower() == "n"):
            break


while True:
    # Menu
    print("=================")
    print("Selamat datang di program manajemen mall, silahkan pilih menu: "
          "\n1.Cek Daftar Toko"
          "\n2.Cek Salah Satu Toko"
          "\n3.Tambah Toko"
          "\n4.Kurangi Toko"
          "\n5.Cek Barang Salah Satu Toko"
          "\n6.Tambah Barang di Salah Satu Toko"
          "\n7.Kurangi Barang di Salah Satu Toko"
          "\n8.Keluar"
          "\nMasukkan pilihan berupa angka: ")
    pilihan = int(input())
    print("=================")

    if pilihan == 1:
        cekSemuaToko()
    elif pilihan == 2:
        cekToko(int(input("Masukkan index Toko: ")))
    elif pilihan == 3:
        tambahToko(Toko(
            input("Masukkan nama toko: "),
            int(input("Masukkan jumlah karyawan: ")),
            int(input("Jam buka toko: ")),
            int(input("Jam tutup toko: ")),
            buatDaftarBarang()
        ))
    elif pilihan == 4:
        kurangiToko(int(input("Masukkan index toko yang ingin dihapus: ")))
    elif pilihan == 5:
        cekBarangToko(int(input("Masukkan index toko yang ingin dilihat daftar barangnya: ")))
    elif pilihan == 6:
        tambahkanBarangToko(
            int(input("Masukkan index toko yang ingin ditambah barangnya: ")),
            Barang(
                input("Masukkan nama Barang: "),
                int(input("Masukkan harga barang: "))
            )
        )
    elif pilihan == 7:
        kurangiBarangToko(
            int(input("Masukkan index toko yang ingin dikurangi barangnya: ")),
            int(input("Masukkan index barang yang ingin dikurangi: ")),
        )
    elif pilihan == 8:
        break
    else:
        print("Maaf inputan salah")
