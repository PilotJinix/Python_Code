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


# // Memeriksa 3 bilangan a, b, c merupakan panjang sisi siku siku
# // Input: integer positif a, b, c
# // Output: True jika bilangan a, b, c merupakan panjang sisi segitiga siku siku
# // Output: False jika bilangan a, b, c bukan merupakan panjang sisi segitiga siku siku
# Input: a
# Input: b
# Input: c
#
# if c**2 = (a**2 + b**2) return true
# else return false

# ===============================
# Nomer 2
# ===============================
#
inptuser = int(input("Masukkan jumlah angka yang di inginkan = "))
array = []
for i in range(inptuser):
    array.append(int(input()))

for j in range(len(array) - 1):
    print("ini J = ", j)
    for k in range (len(array) - 1):
        print("ini K = ", k)
        if array[k] > array[k + 1]:
            # print("nilai n[k] {} nilai n[k+1]".format(array[k]), array[k + 1])
            array[k], array[k + 1] = array[k + 1], array[k]

print("N paling kecil = {} - N paling besar = {}".format(array[0], array[len(array) - 1]))
print("Hasilnya adalah = ", array[len(array) - 1] - array[0])

# input: inptruser "Ask to user to input how to many number to add on the array inptuser"
# declare array[0, n-1] as array
#
# for i <- 0 to inptuser do
#   Input: append input from user to array as much intpruser
#
# for j <- 0 to n-1 do
#   for k <- 0 to n-1 do
#       if array[k] > array[k + 1] return array[k], array[k + 1] = array[k + 1], array[k]
#       else retrun false
# return array[len(array) - 1] - array[0]



# ===============================
# Nomer 3
# ===============================

# ===============================
# Nomer 4
# ===============================


