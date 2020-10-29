uts = int(input("masukkan nilai UTS mahasiswa ?"))
uas = int(input("masukkan nilai UAS mahasiswa ?"))
tugas = int(input("masukkan nilai Tugas mahasiswa ?"))
quiz = int(input("masukkan nilai Quiz mahasiswa ?"))
total_nilai = (uts*35/100)+(uas*35/100)+(tugas*15/100)+(quiz*15/100)
    
print (total_nilai)
if uts and uas < 65:
    print ("nilaimu auto E")
elif total_nilai<60:
    print ("nilaimu E")
elif total_nilai>=60 and total_nilai<65:
    print ("nilaimu D") 
elif total_nilai>=65 and total_nilai<70:
    print ("nialimu C")
elif total_nilai>=70 and total_nilai<80:
    print ("nilaimu B")
elif total_nilai>=80 and total_nilai<100:
    print ("nilaimu A")
