def rek(a):
    print("awal",a)
    if (a>0):
        rek(a-1)
        print(a)
    print("luar",a)

    
rek(5)
