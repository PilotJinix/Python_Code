'''
nama = Iqbal Al-Mahdi
nim = 182410103030
kelas = ALGO 2 (A)
'''



import csv #membuka library csv
nim = [] #mendeklarasikan array nim
nama = [] #mendeklarasikan array nama
with open('DaftarNama.csv') as csv_file: #membuka file DaftarNama.csv
    csv_reader = csv.reader(csv_file,delimiter=';') #memisahkan setiap baris menjadi 2 bagian dengan batasan ';'
    #line_count = 0 #sepertinya tidak penting
    for row in csv_reader: #membuat perulangan dengan batasan jumlah baris pada csv_reader
        nim.append(row[0]) #menambahkan data ke array nim berdasarkan data row ke 0
        nama.append(row[1]) #menambahkan data ke array nim berdasarkan data row ke 1

while True: #membuat perulangan dengan batasan selama nilai boolean True
    print ('=========================') #mencetak 
    pilihan = input('Pilih Menu:\n1.Cari Mahasiswa\n2.Tambah Mahasiswa\n3.Selesai\nPilihan: ') #membuat nilai data dari input yang diberikan
    if (pilihan=='1'): #menjalankan perintah jika nilai pilihan adalah 1
        while True: #membuat perulangan dengan batasan selama nilai boolean True
            search = input('Masukkan Nama atau Nim: ') #membuat nilai data dari input yang diberikan
            try: #memastikan file ditutup dengan baik
                if '0'<=search[0]<='9': #mengecek apakah input search merupakan angka atau string dari inisial
                    #print('1') #mengetes
                    index = nim.index(search) #mencari inputan dari array nim
                else: #jika input bukan angka
                    #print('2') #mengetes
                    index = nama.index(' '+search) #mencari inputan dari array nama, karena pada file DaftarNama.csv terdapat spasi pada awal kata, untuk menyesuaikan saya menambahkan ' '
                print('Nama:',nama[index]) #mencetak nama dengan memanggil dari array nama
                print('NIM:',nim[index]) #mencetak nim dengan memanggil dari array nim
                break #mengakhiri perulangan
            except ValueError: #jika terjadi error
                print('Sorry not found, please try again') #mencetak kata error
    elif (pilihan=='2'): #menjalankan perintah jika nilai pilihan adalah 2
        with open('DaftarNama.csv','a') as csv_file: #membuka file DaftarNama.csv
            raw_nim = input('Masukkan Nim: ') #menginputkan calon data nim
            nim.append(raw_nim) #menambahkan calon data nim ke dalam array nim
            raw_nama = input('Masukkan Nama: ') #menginputkan calon data nama
            nama.append(' '+raw_nama) #menambahkan calon data nama kedalam array nama
            new_line = '\n'+raw_nim+';'+' '+raw_nama #membuat format yang sesuai dari data calon nama dan calon nim untuk dimasukkan kedalam file DaftarNama.csv
            #print (new_line) #mengecek format yang sudah dibuat
            csv_file.write(new_line) #memasukkan data ke dalam file DaftarNama.csv berdasarkan data new_line
    elif (pilihan=='3'): #menjalankan perintah jika nilai pilihan adalah 4
        print('Program Selesai') #mencetak
        break #mengakhiri perulangan
    else: #jika input tidak sesuai dengan if manapun
        print('Input Salah, Coba lagi') #mencetak

