a=int(input())
if(a==1):
    d=""
    l=1
    b=int(input("Masukkan jumlah level segitiga"))
    while (l<=b):
        i=l
        while(i>0):
            d+="*"
            i-=1
        d=d+"\n"
        l+=1
    print(d)
if(a==2):
    b=int(input("Masukkan jumlah level segitiga"))
    f=""
    while (b>0):
        k=b
        while(k>0):
            f+="*"
            k-=1
        f=f+"\n"
        b-=1
    print(f)
