# class Karayawan:
#     uangTransportPerhari = 50000
#     uangMakanPerhari = 50000
#     jumlahkaryawan = 0
#
#     def __init__(self, salary, allowance, present ):
#         self.gajipokok = salary
#         self.tunjangankeluarga = allowance
#         self.kehadiran = present
#
#
#     def cek(self):
#         Karayawan.jumlahkaryawan += 1
#         totalUangTransport = Karayawan.uangTransportPerhari * self.kehadiran
#         totalUangMakan = Karayawan.uangMakanPerhari * self.kehadiran
#         total = self.gajipokok + self.tunjangankeluarga + totalUangTransport + totalUangMakan
#         return "\nGaji Karyawan {} \n - Gaji Pokok: Rp. {:,}\n - Tunjangan keluarga: Rp. {:,}\n - Uang transport: Rp. {:,}\n - Uang makan: Rp. {:,}\nTotal: Rp. {:,}".format(Karayawan.jumlahkaryawan, self.gajipokok, self.tunjangankeluarga, totalUangTransport, totalUangMakan, total)
#
# orang1 = Karayawan(2500000, 1000000, 20)
# orang2 = Karayawan(2750000, 1100000, 22)
# orang3 = Karayawan(2000000, 0, 25)
# orang4 = Karayawan(2000000, 1250000, 18)
#
# print(orang1.cek())
# print(orang2.cek())
# print(orang3.cek())
# print(orang4.cek())

class Elektronik:

    flashdisk_32_GB = 80000
    flashdisk_64_GB = 150000
    hardisk_1_TB = 1000000
    UPS_1000W = 500000
    CPU_desktop = 5000000

    def __init__(self, name, item, quantity, name1, item1, quantity1, name2="", item2=0, quantity2=0, name3="", item3=0, quantity3=0, name4="", item4=0, quantity4=0):
        self.nama = name
        self.barang = item
        self.jumlah = quantity
        self.nama1 = name1
        self.barang1 = item1
        self.jumlah1 = quantity1
        self.nama2 = name2
        self.barang2 = item2
        self.jumlah2 = quantity2
        self.nama3 = name3
        self.barang3 = item3
        self.jumlah3 = quantity3
        self.nama4 = name4
        self.barang4 = item4
        self.jumlah4 = quantity4

    def cek(self):
        totalasli = self.barang * self.jumlah + self.barang1 * self.jumlah1 +self.barang2 * self.jumlah2 +self.barang3 * self.jumlah3 +self.barang4 * self.jumlah4
        if(totalasli < 500000):
            diskon = "Diskon 0% x "
            jumlahdiskon = totalasli
            harga = totalasli - jumlahdiskon
            bonus = "-"
        elif(totalasli >= 500000 and totalasli < 1500000):
            diskon = "Diskon 1% x "
            jumlahdiskon =totalasli * 1 / 100
            harga = totalasli - jumlahdiskon
            bonus = "-"
        elif (totalasli >= 1500000 and totalasli < 5000000):
            diskon = "Diskon 4% x "
            jumlahdiskon =totalasli * 4 / 100
            harga = totalasli - jumlahdiskon
            bonus = "-"
        else:
            diskon = "Diskon 10% x "
            jumlahdiskon = totalasli * 10 / 100
            harga = totalasli - jumlahdiskon
            if(jumlahdiskon > 10000000):
                bonus = jumlahdiskon // 10000000

        return "No \t Nama Barang \t\tHarga \t\t\tJumlah \t\t\tJumlah x Harga \n1 .\t {} \t{}\t\t\t{}\t\t\t\t{}\n2 .\t {} \t{}\t\t\t{}\t\t\t\t{}\n3 .\t {} \t\t{}\t\t\t{}\t\t\t\t{}\n4 .\t {} \t\t\t\t\t{}\t\t\t\t{}\t\t\t\t{}\n5 .\t {} \t\t\t\t\t{}\t\t\t\t{}\t\t\t\t{}\n--------------------------------------------------------------------- +\n\t\t\t\t\t\t\t\t\t\t\tTotal\t\t{} \n\t\t\t\t\t\t\t\t{}{}\t\t{}\n--------------------------------------------------------------------- -\n\t\t\t\t\t\t\t\t\tTotal Dibayar\t\t{}\n\t\t\t\t\t\t\t\t\t\t\tBonus \t\t{}".format(self.nama, self.barang,self.jumlah,self.jumlah*self.barang,self.nama1, self.barang1,self.jumlah1,self.jumlah1*self.barang1,self.nama2, self.barang2,self.jumlah2,self.jumlah2*self.barang2,self.nama3, self.barang3,self.jumlah3,self.jumlah3*self.barang3,self.nama4, self.barang4,self.jumlah4,self.jumlah4*self.barang4,totalasli,diskon,totalasli,jumlahdiskon,harga,bonus)



barang = Elektronik("flashdisk_32_GB", Elektronik.flashdisk_32_GB, 5, "flashdisk_64_GB", Elektronik.flashdisk_64_GB, 4, "hardisk_1_TB", Elektronik.hardisk_1_TB, 2)

print(barang.cek())
