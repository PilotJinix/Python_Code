print ("pilihan ")
print ("1. Encrypt")
print ("2. DEncrypt")
pilihan=int(input("masukkan nama pilihan"))
nama=input("masukkan nama nama")
result=''

print(nama)

if pilihan==1:
    operator=1
if pilihan==2:
    operator=-1

for huruf in nama :
    print(huruf)
    shift=ord(huruf)-55
    print(shift)
    result+=chr(shift)
print (shift)
