def kalikan_matriks(mat_a, mat_b):
    temp_row = []
    temp_mat = []
    temp_sum = 0
 
    for i in range(0, lbr_matriks(mat_a)):
        for j in range(0, pjg_matriks(mat_a)):
            for k in range(0, lbr_matriks(mat_a)):
                temp_sum += mat_a[i][k] * mat_b[j][k]
            temp_row.append(temp_sum)
            temp_sum = 0
        temp_mat.append(temp_row)
        temp_row = []
    return temp_mat
 
matriks_a = [[2, 2, 2], [2, 2, 2], [2, 2, 2]]
matriks_b = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
 
print (matriks_a)
cetak_matriks(matriks_a)
 
print (matriks_b)
cetak_matriks(matriks_b)
 
print ("\nhasil perkalian :")
hasil = kalikan_matriks(matriks_a, matriks_b)
cetak_matriks(hasil)
