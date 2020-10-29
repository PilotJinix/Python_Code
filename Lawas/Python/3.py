data = [1,2,3,4,5,6,7,8,9]
awal=0
akhir=len(data)
while (awal<batas):
    tengah = int ((awal+batas)/2)
    if cari == data[tengah]:
        print('Data yang anda cari', tengah + 1 )
        break
    elif cari > data[tengah]:
        awal = tengah + 1
        
