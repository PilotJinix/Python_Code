print ("Nama: Muhammad Agung Santoso")
print ("NIM : 182410103081")
print ("Algoritma dan Pemrograman II F")

n=10
kotak=""

for i in range (n):
    for j in range (n):
        if (i==0 or i==n-1 or j==0 or j==n-1):
            kotak=kotak+"*"
        else:
            kotak=kotak+" "
    kotak=kotak+"\n"
jarak=0
while True:
    print(kotak,end="")
    for i in range (jarak):
        print("\n")
    print("==================================")
    print("Masukkan w untuk naik dan q untuk quit")
    user=input()
    if (user == "w" or user == "w"):
        jarak=jarak+1
    else:
        break
    print("\n\n\n")
