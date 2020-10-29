nama=[]
nilai=[]
banyak=int(input())

for i in range (banyak):
    nama.append(input())
    nilai.append(int(input()))
for k in range (len (nama)+1):
    for j in range (len (nama)-1):
        if nilai[j]<nilai[j+1]:
                temp=nilai[j]
                nilai[j]=nilai[j+1]
                nilai[j+1]=temp
                temp=nama[j]
                nama[j]=nama[j+1]
                nama[j+1]=temp

print (nama[0])
print (nilai[0])
