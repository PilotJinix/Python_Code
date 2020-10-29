data = [4,1,2,5,4,3]  
cari = int(input('masukkan angka yang kalian inginkan '))
for i in range(0,len(data)):
  print('sedang pada proses ke ',i)
  if cari==data[i]:
    print((cari),'ada di index ke ',(i))
  else:
    print('tidak ditemukan')
    
