import random
print ("=== SELAMAT DATANG DI APLIKASI JODOH METER ===")
loop = True
while loop:
    cowok =input("nama cowok : " )
    cewek1 =input("nama cewek 1: ")
    cewek2 =input("nama cewek 2: ")
    print ("============================")
    print ("nama pria : ",cowok)
    print ("nama cewek : ",cewek1)
    print ("nama cewek : ",cewek2)
    confir = input("apakah nama yang dimasukkan sudah benar ? y/n: ")
    if confir=='y':
        loop = False
match = random.randrange(0,100)
print ("match meter",match, '%')
if match > 80 :
    print (" ndang rabi")
elif match >60:
    print (" pikir- pikir")
elif match >40:
    print ("yakin? ")
elif match > 20 :
    print (" cari lagi ")
else:
    print ("putusin aja")
