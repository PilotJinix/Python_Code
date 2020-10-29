import csv
import re
nim = []
nama = []
with open('DaftarNama.csv') as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=';')
    line_count = 0
    for row in csv_reader:
        nim.append(row[0])
        nama.append(row[1])

while True:
    print ('=========================')
    pilihan = input('Pilih Menu:\n1.Cari Mahasiswa\n2.Tambah Mahasiswa\n3.Tampilkan Daftar Mahasiswa\n4.Selesai\nPilihan: ')
    if (pilihan=='1'):
        while True:
            search = input('Masukkan Nama atau Nim: ')
            try:
                if '0'<=search[0]<='9':
                    #print('1')
                    index = nim.index(search)
                else:
                    #print('2')
                    index = nama.index(' '+search)
                print('Nama:',nama[index])
                print('NIM:',nim[index])
                break
            except ValueError:
                print('Sorry not found, please try again')
    elif (pilihan=='2'):
        with open('DaftarNama.csv') as csv_file:
            raw_nim = input('Masukkan Nim: ')
            nim.append(raw_nim)
            raw_nama = input('Masukkan Nama: ')
            nama.append(' '+raw_nama)
            new_line = '\n'+raw_nim+';'+' '+raw_nama
            for p in csv_file:
                csv_file.write(new_line)
            ##print (new_line)
            ##csv_file.write(new_line)
    elif(pilihan=='3'):
        with open('DaftarNama.csv') as csv_file:
            csv_reader = csv.reader(csv_file,delimiter=';')
            for o in csv_reader:
                print (o)
            csv_file.close()
        
        
        
    elif (pilihan=='4'):
        print('Program Selesai')
        break
    else:
        print('Input Salah, Coba lagi')
            
                    
'''                
    elif (pilihan=='2'):
        writer = open('DaftarNama.csv','a')
        raw_nim = input('Masukkan Nim: ')
        nim.append(raw_nim)
        raw_nama = input('Masukkan Nama: ')
        nama.append(' '+raw_nama)
        new_line = '\n'+raw_nim+';'+' '+raw_nama
        print (new_line)
        writer.write(new_line)
        writer.close()
'''

