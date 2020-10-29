p=int(input("Masukkan angka ganjil lebih dari 5"))
code1=[]
code2=[]

for o in range (p):
    code1.append (int(input()))
for o in range (p):
    code2.append (int(input()))

for o in range (p):
    for i in range (p):
        if o==i and i==p-o-1:
            print (end='X')
        else:
            if o==i:
                print(code1[o],end='')
            elif i==p-o-1:
                
                print(code2[o],end='')
            else:
                print(0,end='')
    print()
    
    


