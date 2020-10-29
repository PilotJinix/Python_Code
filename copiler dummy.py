username=["selica","Asuna","Klein","boRuto","Anjir123","eUgeO","asaDaShan","DeathGun","Sinon","Simon","Naruto","Power Ranger","shamon","pengen beli truk","admin"]
ID=["127HDJ","a13MSA","aNSD23","gNAS12","b12DNA","HASDN12","hLGO12","lIDUP1","SUSAH1","oSDSSD","TEMPO1","12DSAS","12S34S","ADAS12","AB12NS"]
i=input()
ID.append(i)
nama=input()
username.append(nama)

for x in range (len(ID)):
    for y in range (len(ID)-1-x):
        if ID[y]>ID[y+1]:
            ID[y],ID[y+1]=ID[y+1],ID[y]
            username[y],username[y+1]=username[y+1],username[y]
for x in range (len(ID)):
    if ID[x]==(i):
        print (x)
        print (ID [x])
        print (username [x])
        
            
