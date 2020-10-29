kalimat = ["apel","apel","apel","mangga","mangga",]
banyak=0
kata=input()
for i in range (len(kalimat)):
    if kata == kalimat[i]:
        banyak+=1

print(banyak)
