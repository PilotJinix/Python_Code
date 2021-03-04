# ===============================
# Nomer 1
# ===============================
#
# a = int(input("Masukkan Nilai A = "))
# b = int(input("Masukkan Nilai B = "))
# c = int(input("Masukkan Nilai C = "))
#
# if c**2 == (a**2 + b**2):
#     print("Benar")
# else:
#     print("Salah")
#
# Input: a
# Input: b
# Input: c
#
# if c**2 == (a**2 + b**2) return true
# else return false

# ===============================
# Nomer 2
# ===============================

n = [6, 4, 5, 1, 12, 1, 2]

for j in range(len(n)-1):
    print("ini J = ", j)
    for k in range (len(n)-1):
        print("ini K = ", k)
        if n[k] > n[k+1]:
            print("nilai n[k] {} nilai n[k+1]".format(n[k]),n[k+1])
            n[k], n[k+1] = n[k+1], n[k]


print("N paling kecil = {} - N paling besar = {}".format(n[0], n[len(n)-1]))
print(n[0])
print(n[len(n)-1])
print("Hasilnya adalah = ", n[len(n)-1]-n[0])

