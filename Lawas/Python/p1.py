data1=[None]*2
for i in range(2):
    data1[i]=[None]*2
for x in range(2):
    for y in range(2):
        data1[x][y]=int(input());
print(data1)

data2=[None]*2
for i in range(2):
    data2[i]=[None]*2
for x in range(2):
    for y in range(2):
        data2[x][y]=int(input());
print(data2)

a=data2[0][0]
b=(data2[0][1])
c=(data2[1][0])
d=data2[1][1]
det=a*d-b*c
b=-(b)
c=-(c)
e=[[d,b],[c,a]]

if det==0:
    print ("Maaf determinan tidak boleh sama dengan 0" )
    exit("coba lagi")
print ("karena pembagian maka matriks 2 harus kita inverskan terlebih dahulu") 
print (e)

hasil=[]

for x in range(len(data1)):
    isi = []
    for y in range(len(data1[0])):
        total = 0
        for z in range(len(data1)):
            total = total + (data1[x][z] * e [z][y]) / det
        isi.append(total)
    hasil.append(isi)
print ("Jadi hasil matriks 1 / matriks 2 adalah :")
for jadi in hasil:
    print (jadi)

