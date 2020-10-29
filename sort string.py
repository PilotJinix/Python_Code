#k=input()
li = ["Agung","agung","fera","Chinta"]
x = len(li)
#for i in range (0,x):
    #li.append(k[i])

print("List is : ",li)


for i in range(0,x):
    for j in range(0,x):
        if li[i]<li[j]:
            temp = li[i]
            li[i]=li[j]
            li[j]=temp
j=""

nama=[]
for i in range(0,x):
    ##j = j+li[i]
    nama.append(li[i])

##print("After sorting String is : ",j)
print (nama)
