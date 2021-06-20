def binaryexponentiation(konstanta, pangkat):
    if pangkat != "0":
        print("Nilai Konstanta = ", konstanta)
        print("Nilai pangkat = ", pangkat)
        product = konstanta
        # range(start,stop,step)
        for i in range(len(pangkat) - 2, -1, -1):
            print(len(pangkat) - 2)
            print("i =", i)
            print("Pangkat [i] =", pangkat[i])
            print("product sebelum dipangkat = ", product)
            product *= product
            print("product sesudah dipangkat = ", product)
            if int(pangkat[i]) == 1:
                product *= konstanta
                print("product memenuhi = ", product)
        return product
    else:
        return 1

print(binaryexponentiation(int(input("Masukkan Konstanta = ")),
bin(int(input("Masukkan Pangkat = ")))[2:][::-1]))

# index = 0
# data = "abcde"
#
# for index in range(len(data)):
#     print(index)


# for i in range (100):
#     a = bin(i)[2:][::-1]
#     print("data index ke ", i, "= ",a)


# c = 12345
# data = list(str(c))
# print(data)
# for i in range (len(c)):
#     print(i)






# def binaryexponentiation(konstanta, pangkat):
#     print("Nilai Konstanta = ",konstanta)
#     print("Nilai pangkat = ",pangkat)
#     product = konstanta
#     # range(start,stop,step)
#     for i in range(len(pangkat)-2, -1, -1):
#         print(len(pangkat)-2)
#         print("i =",i)
#         print("Pangkat [i] =", pangkat[i])
#         print("product sebelum dipangkat = ",product)
#         product *= product
#         print("product sesudah dipangkat = ", product)
#         if int(pangkat[i]) == 1:
#             product *= konstanta
#             print("product memenuhi = ", product)
#     return product
#
# print(binaryexponentiation(int(input("Masukkan Konstanta = ")),
# bin(int(input("Masukkan Pangkat = ")))[2:][::-1]))