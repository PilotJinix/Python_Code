print ("Muhammad Agung Santoso")
print ("182410103081")

maxlevel=int(input("Masukkan level piramida?"))
currentlevel=1

for currentlevel in range (1,maxlevel,1):
    maxspasi=maxlevel-currentlevel
    maxbintang=(2*currentlevel)-1
    printspasi=""
    printbintang=""

    for currentspasi in range(maxspasi):
        printspasi+="."
    
    for currentbintang in range(maxbintang):
        printbintang+="^"
    print(printspasi+printbintang)
    currentlevel+=1
    
    

        
        
        
