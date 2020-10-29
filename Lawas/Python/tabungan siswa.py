print('selamat pagi')
print('===================================')
lama=int(input('Ingin menabung untuk berapa tahun ? '))
tabungan=0
    
for i in range (1,lama+1):
    print ('Tahun ke ',i)
    for y in range (1,13):
        for x in range (1,5):
            tabungan=50000+tabungan
        print('Tabungan Tahun ke ',i,' bulan ke ',y,'=', tabungan)
    print('===========================================')
    print ('Total Tabungan di tahun ke ',i,'=',tabungan)
    print('===========================================')
    
