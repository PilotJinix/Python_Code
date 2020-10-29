data=[1,5,7,2,9,8,10]
awal=0
batas=(len(data)-1)
print(data)
data.sort()
print("data diurutkan="+str(data))
cari=int(input("masukkan data yang anda cari:"))

while(awal<=batas):
    print("Awal:"+str(awal),"batas:"+str(batas))
    tengah=int(((awal+batas)/2))
    if (data[tengah]<cari):
        awal=tengah+1
    elif (data[tengah]>cari):
        batas=tengah-1
    elif cari==data[tengah]:
        print("data yang anda cari ada di index :",tengah)
    
        


