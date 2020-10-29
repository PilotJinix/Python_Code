'''
mobil=["avanza","xenia","fortuner","alphard"]
motor=["ninja","aerox","nmax"]
mobil.append("lamborghini")
mobil.append("audi")
mobil.remove(mobil[0])
motor.remove(motor[0])
mobil.extend(motor)
for i in range (len(mobil)):
    print(mobil[i],end=" ")
'''

nama = ['yuda','agung','rizki']
nim = [301,21,323]
index = nama.index('yuda')
print('nimnya adalah ',nim[index])

