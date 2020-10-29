a=int(input('masukkan baris'))
b=int(input('masukkan kolom'))
data=[]

for i in range (1,a+1):
    for o in range (1,b+1):
        print("Masukkan angka di baris ke ",i," kolom ",o,)
        h=int(input())
        data.append(h)
print(data,end=' ')
