ipa=int(input("masukkan nilai ipamu ?"))
mtk=int(input("masukkan nilai mtkmu ?"))
bindo=int(input("masukkan nilai bindomu?"))
rerata=(((ipa)+(mtk)+(bindo))/3)

if ipa < 60:
    print("anda nd lulus")
if mtk < 60:
    print("anda nd lulus")
if bindo < 60:
    print("anda nd lulus")
if rerata > 70:
    print ("selamat anda lulus")
else:
    print ("nd") 
