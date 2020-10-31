class Karayawan:
    uangTransportPerhari = 50000
    uangMakanPerhari = 50000
    jumlahkaryawan = 0

    def __init__(self, salary, allowance, present ):
        self.gajipokok = salary
        self.tunjangankeluarga = allowance
        self.kehadiran = present


    def cek(self):
        Karayawan.jumlahkaryawan += 1
        totalUangTransport = Karayawan.uangTransportPerhari * self.kehadiran
        totalUangMakan = Karayawan.uangMakanPerhari * self.kehadiran
        total = self.gajipokok + self.tunjangankeluarga + totalUangTransport + totalUangMakan
        return "\nGaji Karyawan {} \n - Gaji Pokok: Rp. {:,}\n - Tunjangan keluarga: Rp. {:,}\n - Uang transport: Rp. {:,}\n - Uang makan: Rp. {:,}\nTotal: Rp. {:,}".format(Karayawan.jumlahkaryawan, self.gajipokok, self.tunjangankeluarga, totalUangTransport, totalUangMakan, total)

orang1 = Karayawan(2500000, 1000000, 20)
orang2 = Karayawan(2750000, 1100000, 22)
orang3 = Karayawan(2000000, 0, 25)
orang4 = Karayawan(2000000, 1250000, 18)

print(orang1.cek())
print(orang2.cek())
print(orang3.cek())
print(orang4.cek())


