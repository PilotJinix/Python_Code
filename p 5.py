jokowi=[218665,1746764,242816,604492,491564,907453,582497,1075388,392029,374636,1033206,1962956,6242807,682758,3983439,636027,1397511,297349]
provinsi_jokowi=['Aceh','Sumatra Utara','Sumatra Barat','Riau','Jambi','Sumatra Selatan','Bengkulu','Lampung','Kepulauan Bangka Belitung','Kepulauan Riau','DKI Jakarta','Jawa Barat','Jawa Tengah','Daerah Istimewa Yogyakarta','Jawa Timur','Banten','Bali','Nusa Tenggara Timur']
prabowo=[1079176,1385034,1582166,883651,616736,1364440,585384,796912,223505,304490,912144,2419102,1865908,282594,1794932,1052782,108884,665584]
provinsi_prabowo=['Aceh','Sumatra Utara','Sumatra Barat','Riau','Jambi','Sumatra Selatan','Bengkulu','Lampung','Kepulauan Bangka Belitung','Kepulauan Riau','DKI Jakarta','Jawa Barat','Jawa Tengah','Daerah Istimewa Yogyakarta','Jawa Timur','Banten','Bali','Nusa Tenggara Timur']
x=len(jokowi)
paslon01=0
paslon02=0


for i in range (len(provinsi_jokowi)):
    for j in range (len(provinsi_jokowi)-1):
        if jokowi[j]<jokowi[j+1]:
            jokowi[j],jokowi[j+1]=jokowi[j+1],jokowi[j]
            provinsi_jokowi[j],provinsi_jokowi[j+1]=provinsi_jokowi[j+1],provinsi_jokowi[j]
for i in range (len(provinsi_prabowo)):
    for j in range (len(provinsi_prabowo)-1):
        if prabowo[j]<prabowo[j+1]:
            prabowo[j],prabowo[j+1]=prabowo[j+1],prabowo[j]
            provinsi_prabowo[j],provinsi_prabowo[j+1]=provinsi_prabowo[j+1],provinsi_prabowo[j]
print()            
print('Paslon Nomer 01')
print()
for i in range (len(provinsi_jokowi)):
    print(provinsi_jokowi[i],'=',jokowi[i])
print()
print()
print('Paslon Nomer 02')
print()
for i in range (len(provinsi_prabowo)):
    print(provinsi_prabowo[i],'=',prabowo[i])
print()
for i in range (x):
    paslon01+=jokowi[i]
    paslon02+=prabowo[i]
print ('suara paslon 01=',paslon01,'suara')
print ('suara paslon 02=',paslon02,'suara')
print()
print()
if paslon01>paslon02:
    print('CEBONG BAHAGIA')
else:
    print('KAMPRET BAHAGIA')

    
