import csv
nim=[]
nama=[]
with open ('DaftarNama.csv') as csv_file:
    csv_reader=csv.reader(csv_file,delimiter=';')
    line_count=0
    for row in csv_reader:
        nim.append(row[0])
        nama.append(row[1])
while True:
    menu=input()
    if menu == '1':
        search=input('masukkan nama atau nim:')
        try:
            if '0'<=(search[0])<='9':
                print('1')
                index=nim.index(search)
            else:
                print('2')
                index=nama.index('  '+search)

            print('nama:',nama[index])
            print('nim:',nama[index])
            break
        except ValueError:
            print('d')
   
  
       
        
            
            
