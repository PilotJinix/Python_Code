x=[]

while True:
    y=input()
    if y==("="):
        break
    x.append(y)
print(x,end=" ")
print("karana terlalu banyak inputan maka saya sarankan untuk menghapus")
print("")
print("pop untuk mengapus sengan pop")
print("remove untuk mengapus sengan remove")

z=input("mau yang mana ?")
if z==("pop"):
    print(x,end=" ")
    a=int(input("mau hapus yang mana ?"))
    x.pop(x[a])

    if z==("remove"):
        print(x,end=" ")
        a=int(input("mau hapus yang mana ?"))
        x.remove(a)
        print(x,end=" ")
      
