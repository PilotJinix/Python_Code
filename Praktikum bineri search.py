data=[5,1,7,2,9,8,10,0]
awal=0
batas=(len(data)-1)
print(data)
data.sort()

print("data diurutkan="+str(data))
cari=int(input("masukkan data yang anda cari:"))

while(awal<batas):
    print("Awal:"+str(awal),"batas:"+str(batas))
    tengah=int((awal+batas)/2)
    if (cari>data[tengah]):
        awal=tengah+1
    elif (cari<data[tengah]):
        batas=tengah-1
        print(batas)
    else:
        print("data yang anda cari ada di:",tengah)
        break
if awal == batas:
    if (data[awal] == cari):
        print("data yang anda cari ada di",awal)
    else:
        print("data yang anda cari tidak ditemukan")


