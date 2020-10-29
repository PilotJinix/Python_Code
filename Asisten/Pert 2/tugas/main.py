def rekursif(faktorial):
    temp = faktorial
    print(temp)
    if (temp == 0 or temp == 1 ):
        print( "nilai dari temp di IF = " , temp)
        return 1
    else:
        result = temp * rekursif(temp-1)
        print("nilai dari temp = ", temp)
        print("nilai dari result = ", result)
        return result

bilanganfaktorial = int(input("Masukkan bilangan untuk di faktorialkan = "))
hasil = rekursif(bilanganfaktorial)
print("Hasil Faktorial dari bilangan ",bilanganfaktorial, " adalah = " ,hasil)


def fibomethod(bilfibonanci):
    if (bilfibonanci < 2):
        return bilfibonanci
    else:
        result = fibomethod(bilfibonanci-1) + fibomethod(bilfibonanci-2)
        print(result)
        return result

bilfibonanci = int(input("Masukkan bilangan untuk mencari bilangan fibonanci = "))
hasil = fibomethod(bilfibonanci)
print("Hasil bilangan fibonanci ke ",bilfibonanci, " adalah = " ,hasil)


dataarray = [1, 2, 3, 2, 5, 7, 6, 5, 4, 4, 4, 5, 6, 3, 2, 1, 7, 8, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def cek(jumlahdata, dicari, result):
    def hasil1():
        return result+1

    def hasil0():
        return result + 0

    if jumlahdata > 0:
        if dicari == dataarray[jumlahdata - 1]:
            return cek(jumlahdata - 1, dicari, hasil1())
        else:
            return cek(jumlahdata - 1, dicari, hasil0())
    else:
        return result

pilihan = int(input("Masukkan angka 1 sd 10 yang ingin kamu cari jumlahnya = "))
# hasil = cek(len(dataarray), pilihan, 0)
print("Hasil angka yang anda cari ", pilihan, " berjumlah = ", cek(len(dataarray), pilihan, 0))









