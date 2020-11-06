class RumusFisika:
    def DayaListrik(self, usaha, waktu):
        return usaha / waktu

    def HambatanListrik(self, volt, ampere):
        return volt / ampere

    def Gaya(self, massa, percepatan):
        return massa * percepatan


class RumusMatematika:
    def VolumeBalok(self, panjang, lebar):
        return panjang * lebar

    def LuasBalok(self, panjang, lebar):
        return 2 * (panjang * lebar + panjang * lebar + panjang * lebar)

    def VolumeKubus(self, sisi):
        return sisi * sisi * sisi

    def LuasKubus(self, sisi):
        return 6 * (sisi * sisi)

    def VolumeBola(self, jari):
        return (4 / 3 * 3.14 * (jari * jari * jari))

    def LuasBola(self, jari):
        return (4 * 3.14 * (jari * jari))


from random import randint as rand

daftarPujian = ["k-fear", "goblok", "awtis"]
daftarSambutan = ["Hai", "Halooo", "Welkam to mobel lejen"]
fisika = RumusFisika()
matematika = RumusMatematika()
print(daftarSambutan[rand(0, len(daftarSambutan) - 1)] + " Segawon " + daftarPujian[rand(0, len(daftarPujian) - 1)])
print("Pilihan Mata Pelajaran: "
      "\n1.Rumus Fisika"
      "\n2.Rumus Matematika"
      "\nMasukkan pilihan dengan angka: ")
mataPelajaran = int(input())
if (mataPelajaran==1):
    print(
        "Pilih Rumus: "
        "\n1.Daya Listrik"
        "\n2.Hambatan Listrik"
        "\n3.Gaya"
        "\nMasukkan pilihan dengan angka: ")
    rumus = int(input())
    if (rumus==1):
        print(fisika.DayaListrik(
            int(input("Masukkan usaha: ")),
            int(input("Masukka waktu: "))
        ))
    elif(rumus==2):
        print(fisika.HambatanListrik(
            int(input("Masukkan volt: ")),
            int(input("Masukkan ampere: "))
        ))
    elif(rumus==3):
        print(fisika.Gaya(
            int(input("Masukkan massa: ")),
            int(input("Masukkan percepatan: "))
        ))
    else:
        print("Inputan salah")
elif(mataPelajaran==2):
    print(
        "Pilih Rumus: "
        "\n1.Volume Balok"
        "\n2.Luas Balok"
        "\n3.Volume Kubus"
        "\n4.Luas Kubus"
        "\n5.Volume Bola"
        "\n6.Luas Bola"
        "\nMasukkan pilihan dengan angka: ")
    rumus = int(input())
    if (rumus==1):
        print(matematika.VolumeBalok(
            int(input("Masukkan Panjang: ")),
            int(input("Masukkan Lebar: "))
        ))
    elif(rumus==2):
        print(matematika.LuasBalok(
            int(input("Masukkan Panjang: ")),
            int(input("Masukkan Lebar: "))
        ))
    elif(rumus==3):
        print(matematika.VolumeKubus(
            int(input("Masukkan Sisi: "))
        ))
    elif(rumus==4):
        print(matematika.LuasKubus(
            int(input("Masukkan Sisi: "))
        ))
    elif(rumus==5):
        print(matematika.VolumeBola(
            int(input("Masukkan Jari-Jari: "))
        ))
    elif(rumus==6):
        print(matematika.LuasBola(
            int(input("Masukkan Jari-Jari: "))
        ))
    else:
        print("Inputan salah")
else:
    print("Inputan salah")
